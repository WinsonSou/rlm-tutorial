"""
Step 12: Multi-Document Reasoning
===================================

CONCEPT
-------
This step tests the RLM on a harder task: answering questions that require
combining information from MULTIPLE documents. This is closer to the
BrowseComp-Plus benchmark from the paper.

The direct LLM approach struggles because:
  1. The combined document context may exceed comfortable context lengths
  2. Cross-document reasoning is information-dense (every doc matters)
  3. The answer requires ASSOCIATING facts across documents

The RLM excels because it can:
  1. Peek at each document individually
  2. Use sub-LLM calls to extract relevant info per document
  3. Aggregate findings programmatically
  4. Only send relevant pieces to the sub-LLM

From the paper:
  "RLM(GPT-5) is the only model/agent able to achieve and maintain perfect
   performance at the 1000 document scale."

Run:  python step12_multi_doc_reasoning.py
"""

import io
import os
import re
import sys
import time

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# ── Infrastructure (from previous steps) ──────────────────────────────────
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

RLM_SYSTEM_PROMPT = """You are tasked with answering a query using an associated context. You have access to a Python REPL environment where the context is stored as a variable.

The REPL has:
1. `context` -- the data to analyze. It may be a string or a list. Check its type and structure first.
2. `llm_query(prompt)` -- calls a sub-LLM for semantic analysis (handles ~500K chars).
3. `print()` -- to view results.

Strategies:
- **Peek first**: Check type(context), len(context), and examine the first few items.
- **Grep/filter**: Use regex or keywords to narrow down relevant parts.
- **Chunk + Map**: For each document/chunk, call llm_query() to extract relevant info.
- **Aggregate**: Combine results and answer the original question.

Write code in ```repl``` blocks. When done: FINAL(answer) or FINAL_VAR(var_name).
Think step by step and execute immediately. Don't just describe -- write code."""


class SimpleREPL:
    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def inject_function(self, name, fn):
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

def format_output(stdout, stderr, max_chars=3000):
    parts = []
    if stdout:
        parts.append(f"stdout:\n{stdout[:max_chars]}{'...' if len(stdout) > max_chars else ''}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


class SimpleRLM:
    def __init__(self, depth=0, max_depth=1, max_iterations=10):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.total_llm_calls = 0
        self.total_sub_calls = 0

    def completion(self, query, context=None):
        if self.depth >= self.max_depth:
            return self._plain_call(query)
        return self._repl_loop(query, context)

    def _plain_call(self, prompt):
        self.total_llm_calls += 1
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": "Be concise."}, {"role": "user", "content": prompt}],
            **model_kwargs(),
        )
        return r.choices[0].message.content

    def _sub_query(self, prompt):
        self.total_sub_calls += 1
        return SimpleRLM(self.depth + 1, self.max_depth).completion(prompt)

    def _repl_loop(self, query, context):
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_query)
        if context is not None:
            repl.load_context(context)

        ctx_meta = ""
        if context is not None:
            ctx_type = type(context).__name__
            if isinstance(context, list):
                ctx_meta = f"\n\nContext is a list with {len(context)} documents."
            else:
                ctx_meta = f"\n\nContext is a {ctx_type} with {len(context)} characters."

        messages = [
            {"role": "system", "content": RLM_SYSTEM_PROMPT + ctx_meta},
            {"role": "user", "content": query},
        ]

        for iteration in range(self.max_iterations):
            self.total_llm_calls += 1
            r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            text = r.choices[0].message.content
            if text is None:
                console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"    [dim]{r.choices[0]}[/dim]")
                text = ""

            console.print(f"    [dim]Iteration {iteration + 1}[/dim]")

            final = find_final_answer(text, repl.locals)
            if final:
                console.print(f"    [bold green]FINAL![/bold green]")
                return final

            blocks = find_code_blocks(text)
            messages.append({"role": "assistant", "content": text})
            if blocks:
                out = ""
                for b in blocks:
                    so, se = repl.execute(b)
                    out += format_output(so, se) + "\n"
                    if so:
                        console.print(f"    [green]{so.strip()[:200]}[/green]")
                    if se:
                        console.print(f"    [red]{se.strip()[:200]}[/red]")
                messages.append({"role": "user", "content": f"Output:\n{out}\nContinue. FINAL() when done."})
            else:
                messages.append({"role": "user", "content": "Write ```repl``` code or FINAL()."})

        return "Max iterations reached."


# ── Load documents ──────────────────────────────────────────────────────────
docs_dir = os.path.join(os.path.dirname(__file__), "sample_data", "documents")
documents = []
for fname in sorted(os.listdir(docs_dir)):
    if fname.endswith(".txt"):
        with open(os.path.join(docs_dir, fname)) as f:
            documents.append(f.read())

all_text = "\n\n===DOCUMENT SEPARATOR===\n\n".join(documents)

console.print(Panel(
    f"[bold]Multi-Document Reasoning Test[/bold]\n\n"
    f"Loaded {len(documents)} documents, total {len(all_text):,} chars.\n"
    f"Questions require combining information across documents.",
    style="cyan",
))


# ── Test 1: Cross-document question ──────────────────────────────────────
console.print(Panel("[bold]Test 1: Cross-Document Factual Question[/bold]", style="yellow"))

QUESTION1 = (
    "Which KEY_DETAIL from the documents is about a prediction or warning "
    "about future negative consequences? Give the specific detail and which "
    "document it comes from."
)

console.print(f"  [bold]Question:[/bold] {QUESTION1}\n")

# Direct LLM
console.print("  [bold]Direct LLM:[/bold]")
start = time.time()
direct = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": f"{QUESTION1}\n\n{all_text}"}],
    **model_kwargs(),
)
direct_time = time.time() - start
direct_answer = direct.choices[0].message.content
console.print(f"  {direct_answer[:300]}")
console.print(f"  [dim]Time: {direct_time:.1f}s[/dim]\n")

# RLM
console.print("  [bold]RLM:[/bold]")
rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=8)
start = time.time()
rlm_answer = rlm.completion(QUESTION1, context=all_text)
rlm_time = time.time() - start
console.print(f"\n  [green]{str(rlm_answer)[:300]}[/green]")
console.print(f"  [dim]Time: {rlm_time:.1f}s, LLM calls: {rlm.total_llm_calls}, "
              f"Sub calls: {rlm.total_sub_calls}[/dim]\n")


# ── Test 2: Aggregation question ────────────────────────────────────────
console.print(Panel("[bold]Test 2: Aggregation Across All Documents[/bold]", style="yellow"))

QUESTION2 = (
    "For each document, extract the KEY_DETAIL. Then determine: which two "
    "KEY_DETAILs are most related to each other and why?"
)

console.print(f"  [bold]Question:[/bold] {QUESTION2}\n")

# Direct LLM
console.print("  [bold]Direct LLM:[/bold]")
start = time.time()
direct2 = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": f"{QUESTION2}\n\n{all_text}"}],
    **model_kwargs(),
)
direct_time2 = time.time() - start
console.print(f"  {direct2.choices[0].message.content[:300]}")
console.print(f"  [dim]Time: {direct_time2:.1f}s[/dim]\n")

# RLM
console.print("  [bold]RLM:[/bold]")
rlm2 = SimpleRLM(depth=0, max_depth=1, max_iterations=8)
start = time.time()
rlm_answer2 = rlm2.completion(QUESTION2, context=all_text)
rlm_time2 = time.time() - start
console.print(f"\n  [green]{str(rlm_answer2)[:500]}[/green]")
console.print(f"  [dim]Time: {rlm_time2:.1f}s, LLM calls: {rlm2.total_llm_calls}, "
              f"Sub calls: {rlm2.total_sub_calls}[/dim]\n")


# ── Test 3: List-based context ──────────────────────────────────────────
console.print(Panel("[bold]Test 3: List Context (RLM Can Iterate)[/bold]", style="yellow"))

QUESTION3 = (
    "Which document discusses a project that cost approximately $2 billion? "
    "What was the project and what year did it complete?"
)

console.print(f"  [bold]Question:[/bold] {QUESTION3}\n")

# RLM with list context
console.print("  [bold]RLM with list context:[/bold]")
rlm3 = SimpleRLM(depth=0, max_depth=1, max_iterations=6)
start = time.time()
rlm_answer3 = rlm3.completion(QUESTION3, context=documents)
rlm_time3 = time.time() - start
console.print(f"\n  [green]{str(rlm_answer3)[:400]}[/green]")
console.print(f"  [dim]Time: {rlm_time3:.1f}s, LLM calls: {rlm3.total_llm_calls}, "
              f"Sub calls: {rlm3.total_sub_calls}[/dim]\n")


# ── Summary ──────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Why RLMs Excel at Multi-Document Reasoning[/bold]\n\n"
    "From the paper (BrowseComp-Plus with 1000 documents):\n"
    "  - GPT-5 direct: 0% (can't fit in context)\n"
    "  - GPT-5 + BM25: 51%\n"
    "  - Summary agent: 70%\n"
    "  - RLM(GPT-5):   91% <-- best by far\n\n"
    "The RLM's advantage:\n"
    "  1. Peek at documents to understand structure\n"
    "  2. Use regex/keywords to narrow candidates\n"
    "  3. Send relevant docs to sub-LLMs for deep analysis\n"
    "  4. Aggregate findings programmatically\n"
    "  5. Verify answers with targeted follow-up queries\n\n"
    "No single document needs to fit in the LLM's full context.",
    style="green",
))

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. Multi-document reasoning is where RLMs really shine.
# 2. The RLM can iterate over documents individually (no context rot).
# 3. Sub-LLM calls provide semantic analysis per document.
# 4. The root LLM aggregates findings across documents.
# 5. This pattern scales to 1000+ documents in the paper.
#
# NEXT: Step 13 polishes our SimpleRLM into a complete implementation with
# batched queries, token tracking, and rich console output.
# ─────────────────────────────────────────────────────────────────────────────
