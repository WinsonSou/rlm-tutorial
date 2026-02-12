"""
Step 13: Full RLM Implementation
=================================

CONCEPT
-------
This step brings together everything from Steps 1-12 into a polished,
feature-complete RLM implementation:

  - SimpleREPL: Sandboxed execution with output capture
  - SimpleRLM: Depth-controlled recursive model with iterative loop
  - Token tracking: Count all LLM calls and sub-calls
  - Rich console output: Visual iteration-by-iteration trace
  - Batched queries: llm_query_batched() for concurrent sub-calls
  - Configurable system prompt
  - Output truncation to prevent context explosion

This is the culmination of the tutorial -- a working RLM you built from
scratch, understanding every piece.

From the paper:
  "An RLM exposes the same external interface as an LLM: it accepts a
   string prompt of arbitrary structure and produces a string response."

Run:  python step13_full_rlm.py
"""

import io
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# =============================================================================
# Safe Builtins
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


# =============================================================================
# System Prompt
# =============================================================================

RLM_SYSTEM_PROMPT = """You are tasked with answering a query using an associated context. You have access to a Python REPL environment that stores the context as a variable and can recursively query sub-LLMs.

The REPL environment has:
1. `context` -- your data to analyze. Always check type and length first.
2. `llm_query(prompt)` -- call a sub-LLM for semantic analysis (~500K char capacity).
3. `llm_query_batched(prompts)` -- call the sub-LLM with multiple prompts concurrently. Returns a list of responses in the same order. Much faster than sequential llm_query calls.
4. `SHOW_VARS()` -- list all variables you've created.
5. `print()` -- view results (output is truncated, so be strategic).

You will only see truncated outputs, so use llm_query() for detailed analysis.

STRATEGIES:
- **Peek**: Start by checking context type, length, and first few items.
- **Grep**: Use regex or keywords to filter relevant parts.
- **Chunk + Map**: Split context, run llm_query on each chunk, collect results.
  Use llm_query_batched for concurrent processing when chunks are independent.
- **Aggregate**: Combine sub-results into a final answer.

Write code in ```repl``` blocks. Use print() to see results. Variables persist.

When done, signal your answer:
  FINAL(your answer)        -- direct text answer
  FINAL_VAR(variable_name)  -- return a REPL variable's value

IMPORTANT: Create variables in ```repl``` blocks FIRST, then FINAL_VAR in NEXT response.
Think step by step. Execute code immediately -- don't just describe what you'll do."""


# =============================================================================
# Parsing Utilities
# =============================================================================

def find_code_blocks(text: str) -> list[str]:
    """Extract code from ```repl``` fenced blocks."""
    return [m.strip() for m in re.findall(r"```repl\s*\n(.*?)```", text, re.DOTALL) if m.strip()]


def find_final_answer(text: str, repl_locals: dict | None = None) -> str | None:
    """Check for FINAL() or FINAL_VAR() in LLM output."""
    var_match = re.search(r"FINAL_VAR\(([^)]+)\)", text)
    if var_match and repl_locals is not None:
        var_name = var_match.group(1).strip().strip("\"'")
        if var_name in repl_locals:
            return str(repl_locals[var_name])
        available = [k for k in repl_locals if not k.startswith("_")]
        return f"Error: '{var_name}' not found. Available: {available}"
    final_match = re.search(r"FINAL\((.+?)\)", text, re.DOTALL)
    return final_match.group(1).strip() if final_match else None


def format_output(stdout: str, stderr: str, max_chars: int = 3000) -> str:
    """Format REPL output with truncation."""
    parts = []
    if stdout:
        if len(stdout) > max_chars:
            parts.append(f"stdout (truncated to {max_chars} chars):\n{stdout[:max_chars]}...")
        else:
            parts.append(f"stdout:\n{stdout}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


# =============================================================================
# SimpleREPL
# =============================================================================

class SimpleREPL:
    """Sandboxed Python REPL with output capture, context loading, and LLM injection."""

    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def inject_function(self, name: str, fn):
        self.globals[name] = fn

    def load_context(self, context):
        self.locals["context"] = context

    def show_vars(self) -> str:
        available = {k: type(v).__name__ for k, v in self.locals.items() if not k.startswith("_")}
        return f"Available variables: {available}" if available else "No variables yet."

    def execute(self, code: str) -> tuple[str, str]:
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
        return stdout_buf.getvalue(), stderr_buf.getvalue()

    def get_var(self, name: str):
        return self.locals.get(name)


# =============================================================================
# SimpleRLM -- The Complete Implementation
# =============================================================================

class SimpleRLM:
    """
    A complete Recursive Language Model built from scratch.

    Architecture:
      - depth=0 (root): REPL environment + code execution + sub-LLM calls
      - depth>=max_depth: Plain LLM call (no REPL, no recursion)

    Usage:
      rlm = SimpleRLM()
      result = rlm.completion("What is X?", context=large_text)
    """

    def __init__(
        self,
        depth: int = 0,
        max_depth: int = 1,
        max_iterations: int = 10,
        system_prompt: str = RLM_SYSTEM_PROMPT,
        verbose: bool = True,
    ):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.system_prompt = system_prompt
        self.verbose = verbose

        # Usage tracking
        self.root_llm_calls = 0
        self.sub_llm_calls = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def completion(self, query: str, context=None) -> str:
        """
        The main entry point -- a drop-in replacement for an LLM call.

        Args:
            query: The user's question or instruction.
            context: Optional data (str, list, dict) to load into the REPL.

        Returns:
            The final answer as a string.
        """
        if self.depth >= self.max_depth:
            return self._plain_call(query)
        return self._repl_loop(query, context)

    def _plain_call(self, prompt: str) -> str:
        """Plain LLM call at max depth (no REPL)."""
        self.root_llm_calls += 1
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Be concise and precise."},
                {"role": "user", "content": prompt},
            ],
            **model_kwargs(),
        )
        self._track_usage(response)
        return response.choices[0].message.content

    def _sub_llm_query(self, prompt: str) -> str:
        """Called from REPL code via llm_query(). Creates a depth+1 call."""
        self.sub_llm_calls += 1
        sub = SimpleRLM(
            depth=self.depth + 1,
            max_depth=self.max_depth,
            verbose=False,
        )
        result = sub.completion(prompt)
        self.sub_llm_calls += sub.sub_llm_calls
        self.total_input_tokens += sub.total_input_tokens
        self.total_output_tokens += sub.total_output_tokens
        return result

    def _sub_llm_query_batched(self, prompts: list[str]) -> list[str]:
        """Concurrent sub-LLM calls via llm_query_batched()."""
        results = [None] * len(prompts)

        def call_one(idx, prompt):
            return idx, self._sub_llm_query(prompt)

        with ThreadPoolExecutor(max_workers=min(len(prompts), 5)) as executor:
            futures = {executor.submit(call_one, i, p): i for i, p in enumerate(prompts)}
            for future in as_completed(futures):
                idx, result = future.result()
                results[idx] = result

        return results

    def _track_usage(self, response):
        """Track token usage from an API response."""
        usage = getattr(response, "usage", None)
        if usage:
            self.total_input_tokens += usage.prompt_tokens
            self.total_output_tokens += usage.completion_tokens

    def _repl_loop(self, query: str, context=None) -> str:
        """The core iterative REPL loop."""
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_llm_query)
        repl.inject_function("llm_query_batched", self._sub_llm_query_batched)
        repl.inject_function("SHOW_VARS", repl.show_vars)

        if context is not None:
            repl.load_context(context)

        # Build context metadata
        ctx_meta = self._build_context_metadata(context)

        messages = [
            {"role": "system", "content": self.system_prompt + ctx_meta},
            {"role": "user", "content": query},
        ]

        start_time = time.time()

        for iteration in range(self.max_iterations):
            self.root_llm_calls += 1
            response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            self._track_usage(response)
            llm_text = response.choices[0].message.content
            if llm_text is None:
                if self.verbose:
                    console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
                    console.print(f"  [dim]{response.choices[0]}[/dim]")
                llm_text = ""

            if self.verbose:
                console.print(f"  [bold cyan]--- Iteration {iteration + 1} ---[/bold cyan]")

            # Check for final answer
            final = find_final_answer(llm_text, repl.locals)
            if final is not None:
                elapsed = time.time() - start_time
                if self.verbose:
                    console.print(f"  [bold green]FINAL answer found![/bold green]")
                    self._print_summary(iteration + 1, elapsed)
                return final

            # Execute code blocks
            blocks = find_code_blocks(llm_text)
            messages.append({"role": "assistant", "content": llm_text})

            if blocks:
                all_output = ""
                for block in blocks:
                    if self.verbose:
                        console.print(Syntax(block, "python", theme="monokai"))
                    stdout, stderr = repl.execute(block)
                    output = format_output(stdout, stderr)
                    all_output += output + "\n"
                    if self.verbose:
                        if stdout:
                            console.print(f"  [green]{stdout.strip()[:300]}[/green]")
                        if stderr:
                            console.print(f"  [red]{stderr.strip()[:200]}[/red]")

                messages.append({
                    "role": "user",
                    "content": f"Code output:\n{all_output}\n\nContinue. FINAL() or FINAL_VAR() when done."
                })
            else:
                if self.verbose:
                    console.print("  [dim](No code blocks)[/dim]")
                messages.append({
                    "role": "user",
                    "content": "Write ```repl``` code or provide FINAL()."
                })

        # Force final answer
        elapsed = time.time() - start_time
        if self.verbose:
            console.print("  [yellow]Max iterations reached. Forcing answer.[/yellow]")
            self._print_summary(self.max_iterations, elapsed)
        return self._force_final(messages, repl.locals)

    def _build_context_metadata(self, context) -> str:
        """Build metadata string about the context for the system prompt."""
        if context is None:
            return ""
        ctx_type = type(context).__name__
        if isinstance(context, str):
            return f"\n\nYour context is a string with {len(context):,} characters."
        elif isinstance(context, list):
            total_chars = sum(len(str(item)) for item in context)
            return f"\n\nYour context is a list with {len(context)} items ({total_chars:,} total chars)."
        elif isinstance(context, dict):
            return f"\n\nYour context is a dict with {len(context)} keys."
        return f"\n\nYour context is a {ctx_type}."

    def _force_final(self, messages: list, locals_dict: dict) -> str:
        """Force a final answer when max iterations are reached."""
        self.root_llm_calls += 1
        messages.append({
            "role": "user",
            "content": "Max iterations reached. Provide your best answer with FINAL() now."
        })
        r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
        self._track_usage(r)
        text = r.choices[0].message.content
        if text is None:
            if self.verbose:
                console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"  [dim]{r.choices[0]}[/dim]")
            text = ""
        final = find_final_answer(text, locals_dict)
        return final if final else text

    def _print_summary(self, iterations: int, elapsed: float):
        """Print a summary of the RLM run."""
        table = Table(title="RLM Run Summary", style="bold")
        table.add_column("Metric", style="bold")
        table.add_column("Value", justify="right")
        table.add_row("Iterations", str(iterations))
        table.add_row("Root LLM calls", str(self.root_llm_calls))
        table.add_row("Sub-LLM calls", str(self.sub_llm_calls))
        table.add_row("Total LLM calls", str(self.root_llm_calls + self.sub_llm_calls))
        table.add_row("Input tokens", f"{self.total_input_tokens:,}")
        table.add_row("Output tokens", f"{self.total_output_tokens:,}")
        table.add_row("Wall time", f"{elapsed:.1f}s")
        console.print(table)

    def get_usage(self) -> dict:
        """Return usage statistics."""
        return {
            "root_llm_calls": self.root_llm_calls,
            "sub_llm_calls": self.sub_llm_calls,
            "total_llm_calls": self.root_llm_calls + self.sub_llm_calls,
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
        }


# =============================================================================
# Demo: Run the full RLM
# =============================================================================

if __name__ == "__main__":
    console.print(Panel(
        "[bold]Step 13: The Complete SimpleRLM[/bold]\n\n"
        "Everything from Steps 1-12, assembled into a clean implementation.\n"
        "This is a working Recursive Language Model built from scratch.",
        style="cyan",
    ))

    # ── Test 1: Simple computation ──────────────────────────────────────────
    console.print(Panel("[bold]Test 1: Computation (no context)[/bold]", style="yellow"))
    rlm = SimpleRLM(max_iterations=5)
    result = rlm.completion("What are the first 10 prime numbers? Calculate them in code.")
    console.print(f"\n  [bold]Answer:[/bold] [green]{result}[/green]\n")

    # ── Test 2: Needle in haystack ──────────────────────────────────────────
    console.print(Panel("[bold]Test 2: Needle in Haystack[/bold]", style="yellow"))
    haystack_path = os.path.join(os.path.dirname(__file__), "sample_data", "haystack.txt")
    with open(haystack_path) as f:
        haystack = f.read()

    rlm2 = SimpleRLM(max_iterations=5)
    result2 = rlm2.completion("Find the SECRET_FACT in the text. Quote it exactly.", context=haystack)
    console.print(f"\n  [bold]Answer:[/bold] [green]{result2}[/green]\n")

    # ── Test 3: Multi-document with batched queries ────────────────────────
    console.print(Panel("[bold]Test 3: Multi-Document with Batched Queries[/bold]", style="yellow"))
    docs_dir = os.path.join(os.path.dirname(__file__), "sample_data", "documents")
    documents = []
    for fname in sorted(os.listdir(docs_dir)):
        if fname.endswith(".txt"):
            with open(os.path.join(docs_dir, fname)) as f:
                documents.append(f.read())

    rlm3 = SimpleRLM(max_iterations=8)
    result3 = rlm3.completion(
        "Extract the KEY_DETAIL from each document. Use llm_query_batched for efficiency. "
        "Then determine which KEY_DETAIL is about a cost/expense.",
        context=documents,
    )
    console.print(f"\n  [bold]Answer:[/bold] [green]{str(result3)[:500]}[/green]\n")

    # ── Architecture summary ────────────────────────────────────────────────
    console.print(Panel(
        "[bold]What You Built[/bold]\n\n"
        "SimpleRLM is a complete Recursive Language Model with:\n"
        "  - Sandboxed REPL with safe builtins (Step 4)\n"
        "  - LLM code generation + parsing (Step 5)\n"
        "  - Context as a variable, not in the prompt (Step 6)\n"
        "  - Sub-LLM calls from within code (Step 7)\n"
        "  - Depth control for safe recursion (Step 8)\n"
        "  - Iterative loop with FINAL/FINAL_VAR (Step 9)\n"
        "  - Rich system prompt with strategy examples (Step 10)\n"
        "  - Batched queries for concurrent sub-calls\n"
        "  - Token tracking and usage reporting\n"
        "  - Rich console visualization\n\n"
        "This mirrors the architecture of the production rlm library.\n"
        "Step 14 shows how to map this to the real library.",
        style="green",
    ))
