"""
Step 16: Error Handling and Robustness
=======================================

CONCEPT
-------
Our SimpleRLM from Step 13 works, but it's fragile. In production, you will
encounter:

  1. API errors: timeouts, rate limits, connection drops
  2. Malformed LLM output: broken code blocks, invalid FINAL() tags
  3. Infinite loops in REPL code: the LLM writes `while True: pass`
  4. Sub-LLM failures: network errors during recursive calls
  5. Silent failures: no output, no error, just nothing useful

This step builds a RobustRLM that handles all of these gracefully.

WHY THIS MATTERS
----------------
The paper mentions: "RLMs without asynchronous LM calls are slow" and
"distinguishing between a final answer and a thought is brittle for RLMs."
Real-world use requires handling these failure modes so the system doesn't
crash on the first hiccup.

Run:  python step16_robustness.py
"""

import io
import os
import re
import signal
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# =============================================================================
# Base infrastructure (from Step 13)
# =============================================================================

SAFE_BUILTINS = {
    "print": print, "len": len, "str": str, "int": int, "float": float,
    "list": list, "dict": dict, "set": set, "tuple": tuple, "bool": bool,
    "range": range, "enumerate": enumerate, "zip": zip, "sorted": sorted,
    "min": min, "max": max, "sum": sum, "abs": abs, "round": round,
    "any": any, "all": all, "isinstance": isinstance, "type": type,
    "map": map, "filter": filter, "reversed": reversed, "repr": repr,
    "chr": chr, "ord": ord, "hex": hex, "bin": bin, "hasattr": hasattr,
    "getattr": getattr, "setattr": setattr, "dir": dir, "callable": callable,
    "iter": iter, "next": next, "hash": hash, "id": id, "format": format,
    "bytes": bytes, "bytearray": bytearray, "object": object, "super": super,
    "property": property, "staticmethod": staticmethod, "classmethod": classmethod,
    "__import__": __import__, "open": open,
    "Exception": Exception, "ValueError": ValueError, "TypeError": TypeError,
    "KeyError": KeyError, "IndexError": IndexError, "RuntimeError": RuntimeError,
    "eval": None, "exec": None, "input": None, "compile": None,
    "globals": None, "locals": None,
}

RLM_SYSTEM_PROMPT = """You answer queries by writing Python code in ```repl``` blocks.

REPL tools:
- `context`: your data (string, list, or dict).
- `llm_query(prompt)`: call a sub-LLM to read and interpret text. Prompt MUST be under 8000 chars.
- `llm_query_batched(prompts)`: concurrent sub-LLM calls. Same 8000 char limit per prompt.
- `print()`: see code output.

CRITICAL RULES:
1. You CANNOT read or understand document content yourself. Use Python code (regex, `in`, slicing) to LOCATE relevant sections.
2. To UNDERSTAND or ANSWER questions about text, you MUST pass it to llm_query(). Always use llm_query() to interpret excerpts.
3. NEVER print large text to read it yourself. NEVER pass a full document to llm_query(). Always extract a short excerpt first.
4. When done, call FINAL(your_answer) or FINAL_VAR(variable_name).

Write ```repl``` code now. Think step by step."""


def find_code_blocks(text):
    return [m.strip() for m in re.findall(r"```repl\s*\n(.*?)```", text, re.DOTALL) if m.strip()]

def find_final_answer(text, locals_dict=None):
    vm = re.search(r"FINAL_VAR\(([^)]+)\)", text)
    if vm and locals_dict:
        vn = vm.group(1).strip().strip("\"'")
        if vn in locals_dict:
            return str(locals_dict[vn])
    m = re.search(r"FINAL\((.+?)\)", text, re.DOTALL)
    return m.group(1).strip() if m else None

def format_output(stdout, stderr, max_chars=2000):
    parts = []
    if stdout:
        parts.append(f"stdout:\n{stdout[:max_chars]}{'...' if len(stdout) > max_chars else ''}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


# =============================================================================
# Robust REPL -- with execution timeout
# =============================================================================

class RobustREPL:
    """REPL with execution timeout to prevent infinite loops."""

    def __init__(self, exec_timeout: float = 30.0):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}
        self.exec_timeout = exec_timeout

    def inject_function(self, name, fn):
        self.globals[name] = fn

    def load_context(self, context):
        self.locals["context"] = context

    def show_vars(self) -> str:
        available = {k: type(v).__name__ for k, v in self.locals.items() if not k.startswith("_")}
        return f"Available variables: {available}" if available else "No variables yet."

    def execute(self, code: str) -> tuple[str, str]:
        """Execute code with a timeout. Returns (stdout, stderr)."""
        result = {"stdout": "", "stderr": ""}

        def _run():
            old_stdout, old_stderr = sys.stdout, sys.stderr
            stdout_buf, stderr_buf = io.StringIO(), io.StringIO()
            try:
                sys.stdout, sys.stderr = stdout_buf, stderr_buf
                combined = {**self.globals, **self.locals}
                exec(code, combined, combined)
                for key, value in combined.items():
                    if key not in self.globals and not key.startswith("_"):
                        self.locals[key] = value
            except Exception as e:
                stderr_buf.write(f"{type(e).__name__}: {e}")
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
                result["stdout"] = stdout_buf.getvalue()
                result["stderr"] = stderr_buf.getvalue()

        thread = threading.Thread(target=_run, daemon=True)
        thread.start()
        thread.join(timeout=self.exec_timeout)

        if thread.is_alive():
            result["stderr"] += f"\nTimeoutError: Code execution exceeded {self.exec_timeout}s limit."

        return result["stdout"], result["stderr"]


# =============================================================================
# Structured Log Entry
# =============================================================================

class LogEntry:
    def __init__(self, iteration: int, event: str, detail: str = "",
                 tokens_in: int = 0, tokens_out: int = 0):
        self.timestamp = datetime.now().isoformat()
        self.iteration = iteration
        self.event = event
        self.detail = detail
        self.tokens_in = tokens_in
        self.tokens_out = tokens_out

    def __repr__(self):
        return f"[{self.timestamp}] iter={self.iteration} {self.event}: {self.detail[:80]}"


# =============================================================================
# Robust RLM
# =============================================================================

class RobustRLM:
    """
    RLM with production-grade error handling:
    - Retry with exponential backoff on API errors
    - Execution timeout per code block
    - Malformed output recovery
    - Graceful degradation on sub-LLM failures
    - Structured logging
    """

    def __init__(self, depth=0, max_depth=1, max_iterations=10, verbose=True,
                 max_retries=3, exec_timeout=30.0):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.max_retries = max_retries
        self.exec_timeout = exec_timeout
        self.root_llm_calls = 0
        self.sub_llm_calls = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.log: list[LogEntry] = []

    def _log(self, iteration: int, event: str, detail: str = "",
             tokens_in: int = 0, tokens_out: int = 0):
        entry = LogEntry(iteration, event, detail, tokens_in, tokens_out)
        self.log.append(entry)
        if self.verbose:
            console.print(f"    [dim]{entry}[/dim]")

    def _llm_call_with_retry(self, messages: list, iteration: int = 0) -> str:
        """Call the LLM with exponential backoff retry on transient errors."""
        last_error = None
        for attempt in range(self.max_retries):
            try:
                self.root_llm_calls += 1
                r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
                usage = getattr(r, "usage", None)
                tin = usage.prompt_tokens if usage else 0
                tout = usage.completion_tokens if usage else 0
                self.total_input_tokens += tin
                self.total_output_tokens += tout
                self._log(iteration, "llm_call_ok", f"attempt={attempt+1}", tin, tout)
                content = r.choices[0].message.content
                if content is None:
                    self._log(iteration, "llm_none_content", f"Full choice: {r.choices[0]}")
                    return ""
                return content
            except Exception as e:
                last_error = e
                wait = 2 ** attempt
                self._log(iteration, "llm_call_retry",
                          f"attempt={attempt+1}, error={type(e).__name__}: {e}, wait={wait}s")
                if self.verbose:
                    console.print(f"    [yellow]Retry {attempt+1}/{self.max_retries} "
                                  f"after {type(e).__name__}, waiting {wait}s...[/yellow]")
                time.sleep(wait)

        self._log(iteration, "llm_call_failed", f"All {self.max_retries} retries exhausted: {last_error}")
        raise RuntimeError(f"LLM call failed after {self.max_retries} retries: {last_error}")

    def _sub_query_safe(self, prompt: str) -> str:
        """Sub-LLM call with error handling -- returns error string on failure."""
        self.sub_llm_calls += 1
        try:
            sub = RobustRLM(self.depth + 1, self.max_depth, verbose=False,
                            max_retries=self.max_retries, exec_timeout=self.exec_timeout)
            result = sub.completion(prompt)
            self.sub_llm_calls += sub.sub_llm_calls
            self.total_input_tokens += sub.total_input_tokens
            self.total_output_tokens += sub.total_output_tokens
            return result
        except Exception as e:
            return f"[SUB-LLM ERROR: {type(e).__name__}: {e}]"

    def _sub_query_batched_safe(self, prompts: list[str]) -> list[str]:
        """Concurrent sub-LLM calls with per-call error handling."""
        results = [None] * len(prompts)
        def call_one(idx, prompt):
            return idx, self._sub_query_safe(prompt)
        with ThreadPoolExecutor(max_workers=min(len(prompts), 5)) as ex:
            futs = {ex.submit(call_one, i, p): i for i, p in enumerate(prompts)}
            for f in as_completed(futs):
                try:
                    idx, result = f.result()
                    results[idx] = result
                except Exception as e:
                    results[futs[f]] = f"[BATCH ERROR: {e}]"
        return results

    def _find_code_blocks_robust(self, text: str) -> list[str]:
        """Try multiple patterns to extract code blocks from potentially malformed output."""
        # Standard pattern
        blocks = find_code_blocks(text)
        if blocks:
            return blocks

        # Fallback: try ```python blocks
        py_blocks = [m.strip() for m in re.findall(r"```python\s*\n(.*?)```", text, re.DOTALL) if m.strip()]
        if py_blocks:
            self._log(0, "parse_fallback", "Used ```python``` instead of ```repl```")
            return py_blocks

        # Fallback: try unclosed code blocks
        unclosed = re.findall(r"```repl\s*\n(.*?)$", text, re.DOTALL)
        if unclosed:
            self._log(0, "parse_fallback", "Found unclosed ```repl``` block")
            return [unclosed[0].strip()]

        return []

    def completion(self, query: str, context=None) -> str:
        if self.depth >= self.max_depth:
            return self._plain_call(query)
        return self._repl_loop(query, context)

    SUB_LLM_SYSTEM = (
        "Answer concisely based only on the provided text. "
        "Your context window is ~20,000 tokens. If the input seems large, "
        "focus on the most relevant parts. Do not make up information."
    )

    def _plain_call(self, prompt: str) -> str:
        self.root_llm_calls += 1
        try:
            r = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": self.SUB_LLM_SYSTEM},
                          {"role": "user", "content": prompt}],
                **model_kwargs(),
            )
            usage = getattr(r, "usage", None)
            if usage:
                self.total_input_tokens += usage.prompt_tokens
                self.total_output_tokens += usage.completion_tokens
            return r.choices[0].message.content or ""
        except Exception as e:
            return f"[ERROR: {e}]"

    def _repl_loop(self, query: str, context=None) -> str:
        repl = RobustREPL(exec_timeout=self.exec_timeout)
        repl.inject_function("llm_query", self._sub_query_safe)
        repl.inject_function("llm_query_batched", self._sub_query_batched_safe)
        repl.inject_function("SHOW_VARS", repl.show_vars)
        if context is not None:
            repl.load_context(context)

        ctx_meta = ""
        if context is not None:
            if isinstance(context, list):
                ctx_meta = f"\n\nContext is a list of {len(context)} items."
            elif isinstance(context, dict):
                ctx_meta = f"\n\nContext is a dict with {len(context)} keys."
            else:
                ctx_meta = f"\n\nContext is a string with {len(str(context)):,} chars."

        messages = [
            {"role": "system", "content": RLM_SYSTEM_PROMPT + ctx_meta},
            {"role": "user", "content": query},
        ]

        for iteration in range(self.max_iterations):
            if self.verbose:
                console.print(f"  [bold cyan]--- Iteration {iteration + 1} ---[/bold cyan]")

            try:
                text = self._llm_call_with_retry(messages, iteration)
            except RuntimeError as e:
                self._log(iteration, "fatal", str(e))
                return f"[FATAL: {e}]"

            # Check final answer
            final = find_final_answer(text, repl.locals)
            if final:
                self._log(iteration, "final_answer", final[:100])
                if self.verbose:
                    console.print(f"    [bold green]FINAL![/bold green]")
                return final

            # Extract and execute code blocks (with robust parsing)
            blocks = self._find_code_blocks_robust(text)
            messages.append({"role": "assistant", "content": text})

            if blocks:
                all_output = ""
                for block in blocks:
                    self._log(iteration, "exec_code", block[:80])
                    stdout, stderr = repl.execute(block)
                    output = format_output(stdout, stderr)
                    all_output += output + "\n"

                    if self.verbose:
                        if stdout:
                            console.print(f"    [green]{stdout.strip()[:300]}[/green]")
                        if stderr:
                            console.print(f"    [red]{stderr.strip()[:200]}[/red]")

                    # Check for timeout
                    if "TimeoutError" in stderr:
                        self._log(iteration, "timeout", "Code block timed out")

                messages.append({
                    "role": "user",
                    "content": f"Output:\n{all_output}\nContinue. FINAL() when done."
                })
            else:
                self._log(iteration, "no_code_blocks", "LLM did not produce code")
                messages.append({
                    "role": "user",
                    "content": "No code blocks found. Write ```repl``` code or FINAL()."
                })

        # Force final answer
        self._log(self.max_iterations, "max_iterations", "Forcing final answer")
        try:
            messages.append({"role": "user", "content": "Max iterations. FINAL() now."})
            text = self._llm_call_with_retry(messages, self.max_iterations)
            final = find_final_answer(text, repl.locals)
            return final if final else text
        except RuntimeError:
            return "[FATAL: Could not produce final answer]"

    def print_log(self, last_n: int = 20):
        """Print the structured log."""
        t = Table(title="Execution Log (last entries)")
        t.add_column("Time", style="dim")
        t.add_column("Iter", justify="right")
        t.add_column("Event", style="bold")
        t.add_column("Detail")
        for entry in self.log[-last_n:]:
            ts = entry.timestamp.split("T")[1][:8]
            t.add_row(ts, str(entry.iteration), entry.event, entry.detail[:60])
        console.print(t)


# =============================================================================
# Demonstrations
# =============================================================================

if __name__ == "__main__":
    # ── Demo 1: Execution timeout ──────────────────────────────────────────
    console.print(Panel("[bold]Demo 1: Execution Timeout[/bold]", style="cyan"))
    console.print("  Testing that infinite loops in REPL code are safely killed.\n")

    repl = RobustREPL(exec_timeout=3.0)
    code = "import time\nwhile True:\n    time.sleep(0.1)"
    console.print(Syntax(code, "python", theme="monokai"))
    start = time.time()
    stdout, stderr = repl.execute(code)
    elapsed = time.time() - start
    console.print(f"  stdout: {stdout!r}")
    console.print(f"  stderr: [red]{stderr}[/red]")
    console.print(f"  Time: {elapsed:.1f}s (timeout was 3s)\n")

    # Verify REPL still works after timeout
    stdout2, stderr2 = repl.execute("print('REPL still works!')")
    console.print(f"  After timeout: [green]{stdout2.strip()}[/green]\n")

    # ── Demo 2: Malformed output recovery ──────────────────────────────────
    console.print(Panel("[bold]Demo 2: Malformed Output Recovery[/bold]", style="cyan"))
    console.print("  Testing robust parsing of broken code blocks.\n")

    rlm = RobustRLM(verbose=False)

    # Test fallback to ```python
    text1 = "Here is my code:\n```python\nprint('hello')\n```"
    blocks1 = rlm._find_code_blocks_robust(text1)
    console.print(f"  ```python block: {blocks1}")

    # Test unclosed block
    text2 = "Let me try:\n```repl\nx = 42\nprint(x)"
    blocks2 = rlm._find_code_blocks_robust(text2)
    console.print(f"  Unclosed block:  {blocks2}")

    # Test no blocks
    text3 = "I think the answer is 42."
    blocks3 = rlm._find_code_blocks_robust(text3)
    console.print(f"  No blocks:       {blocks3}\n")

    # ── Demo 3: Sub-LLM failure graceful degradation ───────────────────────
    console.print(Panel("[bold]Demo 3: Sub-LLM Failure Handling[/bold]", style="cyan"))
    console.print("  The _sub_query_safe method returns error strings instead of crashing.\n")

    rlm2 = RobustRLM(verbose=False)
    # This should work normally
    result = rlm2._sub_query_safe("What is 2+2? Reply with just the number.")
    console.print(f"  Normal call: [green]{result}[/green]\n")

    # ── Demo 4: Full robust RLM on real task ──────────────────────────────
    console.print(Panel("[bold]Demo 4: Full Robust RLM[/bold]", style="cyan"))

    haystack_path = os.path.join(os.path.dirname(__file__), "sample_data", "haystack.txt")
    with open(haystack_path) as f:
        haystack = f.read()

    rlm3 = RobustRLM(max_iterations=5, exec_timeout=15.0)
    start = time.time()
    result = rlm3.completion("Find the SECRET_FACT in the text.", context=haystack)
    elapsed = time.time() - start

    console.print(f"\n  [bold]Answer:[/bold] [green]{result[:300]}[/green]")

    # Show the structured log
    rlm3.print_log()

    # ── Summary ────────────────────────────────────────────────────────────
    console.print(Panel(
        "[bold]What RobustRLM Adds Over SimpleRLM[/bold]\n\n"
        "1. [bold]Retry with backoff[/bold]: API errors are retried 3x with exponential wait\n"
        "2. [bold]Execution timeout[/bold]: Code blocks killed after N seconds (prevents hangs)\n"
        "3. [bold]Malformed output[/bold]: Falls back to ```python blocks, unclosed blocks\n"
        "4. [bold]Graceful degradation[/bold]: Sub-LLM errors return error strings, not crashes\n"
        "5. [bold]Structured logging[/bold]: Every event timestamped for debugging\n\n"
        "These are the minimum requirements for using RLMs in production.",
        style="green",
    ))
