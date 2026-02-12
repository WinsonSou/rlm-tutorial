"""
Step 10: The RLM System Prompt
===============================

CONCEPT
-------
The system prompt is how we TEACH the LLM to behave as an RLM. It explains:
  1. That a `context` variable exists in the REPL
  2. That `llm_query()` is available for sub-LLM calls
  3. How to use ```repl``` code blocks
  4. Example strategies (peek, chunk, map, aggregate)
  5. How to signal completion with FINAL() / FINAL_VAR()

The quality of the system prompt dramatically affects RLM performance. The
paper uses a single, fixed system prompt across all experiments.

From the paper:
  "The RLM system prompt is fixed for each model across all experiments
   and is not tuned for any particular benchmark."

WHY THIS MATTERS
----------------
The system prompt is the RLM's "training" -- it teaches an untrained LLM
to use the REPL environment effectively. A good prompt includes concrete
examples of strategies the LLM can employ.

Run:  python step10_system_prompt.py
"""

import io
import os
import re
import sys
import time

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# ── The RLM system prompt ──────────────────────────────────────────────────
# This is modeled after the actual prompt from the RLM paper/codebase,
# adapted for our tutorial.

RLM_SYSTEM_PROMPT = """You are tasked with answering a query using an associated context. You have access to a Python REPL environment where the context is stored as a variable. You will interact iteratively until you provide a final answer.

The REPL environment is initialized with:
1. A `context` variable containing the data you need to analyze. Check its type and content first.
2. An `llm_query(prompt)` function that calls a sub-LLM (handles ~500K chars) for semantic analysis.
3. Use `print()` to view outputs from your code.

You will only see truncated outputs from the REPL, so use llm_query() for detailed analysis of large text. Use variables as buffers to build up your final answer.

STRATEGIES you should consider:
- **Peek first**: Always start by examining the context structure (type, length, first few items).
- **Grep/filter**: Use regex or keyword search to narrow down relevant parts.
- **Chunk + Map**: Split context into chunks, run llm_query() on each, collect results.
- **Aggregate**: Combine sub-results with another llm_query() or programmatically.

Example -- finding information in a large text:
```repl
# 1. Peek at the context
print(type(context), len(context) if isinstance(context, (str, list)) else "")
print(str(context)[:500])
```

Example -- chunk and map over documents:
```repl
# Split into chunks and query each
chunk_size = len(context) // 5
results = []
for i in range(5):
    start = i * chunk_size
    end = start + chunk_size if i < 4 else len(context)
    chunk = context[start:end]
    answer = llm_query(f"Extract key facts from this text:\\n{chunk}")
    results.append(answer)
    print(f"Chunk {i}: {answer[:100]}...")
```

Example -- keyword search then targeted analysis:
```repl
import re
# Find lines containing a keyword
matches = [line for line in context.split('\\n') if 'keyword' in line.lower()]
print(f"Found {len(matches)} matches")
for m in matches[:5]:
    print(m)
```

When you have your answer, signal completion with:
  FINAL(your answer text)     -- for direct text answers
  FINAL_VAR(variable_name)    -- to return a REPL variable's value

IMPORTANT: Create variables in ```repl``` blocks FIRST, then call FINAL_VAR in a SEPARATE response.

Think step by step. Execute code immediately -- don't just describe what you'll do."""


# ── Show the prompt ────────────────────────────────────────────────────────
console.print(Panel("[bold]The RLM System Prompt[/bold]", style="cyan"))
console.print(Syntax(RLM_SYSTEM_PROMPT, "markdown", theme="monokai", word_wrap=True))
console.print()


# ── REPL and RLM classes ────────────────────────────────────────────────────
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


class SimpleREPL:
    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def inject_function(self, name: str, fn):
        self.globals[name] = fn

    def load_context(self, context):
        self.locals["context"] = context

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


def find_code_blocks(text: str) -> list[str]:
    pattern = r"```repl\s*\n(.*?)```"
    return [m.strip() for m in re.findall(pattern, text, re.DOTALL) if m.strip()]


def find_final_answer(text: str, repl_locals: dict | None = None) -> str | None:
    var_match = re.search(r"FINAL_VAR\(([^)]+)\)", text)
    if var_match and repl_locals is not None:
        var_name = var_match.group(1).strip().strip("\"'")
        if var_name in repl_locals:
            return str(repl_locals[var_name])
    final_match = re.search(r"FINAL\((.+?)\)", text, re.DOTALL)
    if final_match:
        return final_match.group(1).strip()
    return None


def format_output(stdout: str, stderr: str, max_chars: int = 3000) -> str:
    parts = []
    if stdout:
        if len(stdout) > max_chars:
            parts.append(f"stdout (truncated to {max_chars} chars):\n{stdout[:max_chars]}...")
        else:
            parts.append(f"stdout:\n{stdout}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


class SimpleRLM:
    """RLM with the full system prompt."""

    def __init__(self, depth: int = 0, max_depth: int = 1, max_iterations: int = 10,
                 system_prompt: str = RLM_SYSTEM_PROMPT):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.system_prompt = system_prompt
        self.total_llm_calls = 0
        self.total_sub_calls = 0

    def completion(self, query: str, context=None) -> str:
        if self.depth >= self.max_depth:
            return self._plain_llm_call(query)
        return self._repl_loop(query, context)

    def _plain_llm_call(self, prompt: str) -> str:
        self.total_llm_calls += 1
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Be concise."},
                {"role": "user", "content": prompt},
            ],
            **model_kwargs(),
        )
        return response.choices[0].message.content

    def _sub_llm_query(self, prompt: str) -> str:
        self.total_sub_calls += 1
        sub = SimpleRLM(depth=self.depth + 1, max_depth=self.max_depth)
        return sub.completion(prompt)

    def _repl_loop(self, query: str, context=None) -> str:
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_llm_query)

        if context is not None:
            repl.load_context(context)

        # Build metadata about the context for the system prompt
        ctx_meta = ""
        if context is not None:
            ctx_type = type(context).__name__
            ctx_len = len(context) if hasattr(context, "__len__") else "unknown"
            ctx_meta = f"\n\nYour context is a {ctx_type} with {ctx_len} total items/characters."

        messages = [
            {"role": "system", "content": self.system_prompt + ctx_meta},
            {"role": "user", "content": query},
        ]

        for iteration in range(self.max_iterations):
            self.total_llm_calls += 1
            response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            llm_text = response.choices[0].message.content
            if llm_text is None:
                console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"  [dim]{response.choices[0]}[/dim]")
                llm_text = ""

            console.print(f"  [dim]--- Iteration {iteration + 1} ---[/dim]")

            # Check for final answer
            final = find_final_answer(llm_text, repl.locals)
            if final is not None:
                console.print(f"  [bold green]FINAL answer found![/bold green]")
                return final

            # Execute code blocks
            blocks = find_code_blocks(llm_text)
            messages.append({"role": "assistant", "content": llm_text})

            if blocks:
                all_output = ""
                for block in blocks:
                    stdout, stderr = repl.execute(block)
                    output = format_output(stdout, stderr)
                    all_output += output + "\n"
                    if stdout:
                        console.print(f"  [green]{stdout.strip()[:300]}[/green]")
                    if stderr:
                        console.print(f"  [red]{stderr.strip()[:200]}[/red]")

                messages.append({
                    "role": "user",
                    "content": f"Code output:\n{all_output}\n\n"
                               "Continue. When done, use FINAL() or FINAL_VAR()."
                })
            else:
                messages.append({
                    "role": "user",
                    "content": "No code blocks found. Please write ```repl``` code "
                               "or provide FINAL()."
                })

        self.total_llm_calls += 1
        messages.append({"role": "user", "content": "Max iterations reached. FINAL() now."})
        resp = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
        text = resp.choices[0].message.content
        if text is None:
            console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
            console.print(f"  [dim]{resp.choices[0]}[/dim]")
            text = ""
        final = find_final_answer(text, repl.locals)
        return final if final else text


# ── Experiment 1: Full RLM with system prompt ──────────────────────────────
console.print(Panel("[bold]Experiment 1: RLM With Full System Prompt[/bold]", style="cyan"))

haystack_path = os.path.join(os.path.dirname(__file__), "sample_data", "haystack.txt")
with open(haystack_path) as f:
    haystack = f.read()

rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=5)
start = time.time()
result = rlm.completion(
    "What is the SECRET_FACT mentioned in the text?",
    context=haystack,
)
elapsed = time.time() - start
console.print(f"\n  [bold]Answer:[/bold] [green]{result}[/green]")
console.print(f"  LLM calls: {rlm.total_llm_calls}, Sub calls: {rlm.total_sub_calls}")
console.print(f"  Time: {elapsed:.1f}s\n")


# ── Experiment 2: Multi-document with system prompt ────────────────────────
console.print(Panel("[bold]Experiment 2: Multi-Document Analysis[/bold]", style="cyan"))

docs_dir = os.path.join(os.path.dirname(__file__), "sample_data", "documents")
documents = []
for fname in sorted(os.listdir(docs_dir)):
    if fname.endswith(".txt"):
        with open(os.path.join(docs_dir, fname)) as f:
            documents.append(f.read())

all_docs = "\n\n---\n\n".join(documents)

rlm2 = SimpleRLM(depth=0, max_depth=1, max_iterations=6)
start = time.time()
result = rlm2.completion(
    "What KEY_DETAIL from each document is about a WARNING or PREDICTION "
    "about future consequences? List the document title and the detail.",
    context=all_docs,
)
elapsed = time.time() - start
console.print(f"\n  [bold]Answer:[/bold] [green]{result[:500]}[/green]")
console.print(f"  LLM calls: {rlm2.total_llm_calls}, Sub calls: {rlm2.total_sub_calls}")
console.print(f"  Time: {elapsed:.1f}s\n")


# ── Comparing prompts ──────────────────────────────────────────────────────
console.print(Panel("[bold]Experiment 3: Prompt Quality Matters[/bold]", style="cyan"))
console.print("  Compare a minimal prompt vs our full RLM prompt.\n")

MINIMAL_PROMPT = "You have a REPL. Write code in ```repl``` blocks. Use FINAL() when done."

rlm_minimal = SimpleRLM(depth=0, max_depth=1, max_iterations=5, system_prompt=MINIMAL_PROMPT)
start = time.time()
result_min = rlm_minimal.completion(
    "What is the SECRET_FACT?",
    context=haystack,
)
elapsed_min = time.time() - start

rlm_full = SimpleRLM(depth=0, max_depth=1, max_iterations=5)
start = time.time()
result_full = rlm_full.completion(
    "What is the SECRET_FACT?",
    context=haystack,
)
elapsed_full = time.time() - start

console.print(f"  Minimal prompt -> {result_min[:200]}")
console.print(f"    ({rlm_minimal.total_llm_calls} LLM calls, {elapsed_min:.1f}s)\n")
console.print(f"  Full RLM prompt -> {result_full[:200]}")
console.print(f"    ({rlm_full.total_llm_calls} LLM calls, {elapsed_full:.1f}s)\n")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. The system prompt teaches the LLM: context variable, llm_query(),
#    code blocks, strategies, and FINAL/FINAL_VAR.
# 2. Example strategies in the prompt (peek, grep, chunk+map) guide behavior.
# 3. Context metadata (type, length) helps the LLM choose a strategy.
# 4. The paper uses one fixed prompt for all tasks (not tuned per benchmark).
# 5. Prompt quality significantly affects performance.
#
# NEXT: Step 11 tests our RLM on a needle-in-haystack benchmark.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] The system prompt is the 'training' of an untrained RLM.\n"
    "It teaches strategies (peek, grep, chunk+map) and usage patterns\n"
    "(```repl```, llm_query, FINAL). The paper uses one prompt for all tasks.",
    style="green",
))
