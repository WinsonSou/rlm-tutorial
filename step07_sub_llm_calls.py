"""
Step 7: Sub-LLM Calls -- Recursion from Within the REPL
========================================================

CONCEPT
-------
In Steps 5-6, the LLM writes code that interacts with the context through
Python operations (slicing, regex, etc.). But what about SEMANTIC tasks?

  "Which of these paragraphs discuss scientific discoveries?"
  "Classify each line as a question about a person, place, or thing."

These require understanding meaning, not just pattern matching. The solution:
inject an `llm_query()` function into the REPL globals so that code running
in the REPL can call the LLM itself.

This is the "recursive" in Recursive Language Models. The root LLM (depth 0)
writes code that calls a sub-LLM (depth 1) to answer questions about chunks
of context.

From the paper:
  "The REPL environment also loads in a module that allows it to query a
   sub-LM inside the environment."

  "RLMs encourage the LLM, in the code it produces, to programmatically
   construct sub-tasks on which they can invoke themselves recursively."

WHY THIS MATTERS
----------------
This completes the core pieces of an RLM:
  1. REPL sandbox (Step 4)
  2. LLM writes code (Step 5)
  3. Context as variable (Step 6)
  4. Sub-LLM calls from code (this step)

The root LLM can now: peek at context -> chunk it -> call sub-LLMs on
each chunk -> aggregate results. All through code it writes itself.

Run:  python step07_sub_llm_calls.py
"""

import io
import os
import re
import sys

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# ── REPL with llm_query injected ────────────────────────────────────────────
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
    def __init__(self, llm_fn=None):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}
        self.sub_call_count = 0
        if llm_fn:
            self.globals["llm_query"] = self._make_tracked_llm_query(llm_fn)

    def _make_tracked_llm_query(self, llm_fn):
        """Wrap the LLM function to track call count."""
        def tracked_llm_query(prompt: str) -> str:
            self.sub_call_count += 1
            return llm_fn(prompt)
        return tracked_llm_query

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

    def load_context(self, context):
        self.locals["context"] = context

    def get_var(self, name: str):
        return self.locals.get(name)


def find_code_blocks(text: str) -> list[str]:
    pattern = r"```repl\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [m.strip() for m in matches if m.strip()]


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


# ── The sub-LLM function ───────────────────────────────────────────────────
def llm_query(prompt: str) -> str:
    """Call the LLM from within the REPL. This is the 'recursive' part."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise and precise."},
            {"role": "user", "content": prompt},
        ],
        **model_kwargs(),
    )
    return response.choices[0].message.content


# ── Experiment 1: llm_query from the REPL ──────────────────────────────────
console.print(Panel("[bold]Experiment 1: Calling the LLM From Inside the REPL[/bold]", style="cyan"))
console.print("  We inject llm_query() into the REPL globals.\n")

repl = SimpleREPL(llm_fn=llm_query)

code = '''
answer = llm_query("What is the chemical formula for water? Reply with just the formula.")
print(f"Sub-LLM says: {answer}")
'''
console.print(Syntax(code.strip(), "python", theme="monokai"))
stdout, stderr = repl.execute(code)
console.print(f"  [green]{stdout.strip()}[/green]")
console.print(f"  Sub-LLM calls so far: {repl.sub_call_count}\n")


# ── Experiment 2: Semantic analysis via sub-LLM ───────────────────────────
console.print(Panel("[bold]Experiment 2: Semantic Analysis via Sub-LLM[/bold]", style="cyan"))
console.print("  The sub-LLM can answer questions that code alone cannot.\n")

# Load multi-document context
docs_dir = os.path.join(os.path.dirname(__file__), "sample_data", "documents")
documents = []
for fname in sorted(os.listdir(docs_dir)):
    if fname.endswith(".txt"):
        with open(os.path.join(docs_dir, fname)) as f:
            documents.append(f.read())

repl2 = SimpleREPL(llm_fn=llm_query)
repl2.load_context(documents)

code = '''
# The root LLM writes this code to classify each document
for i, doc in enumerate(context):
    first_line = doc.split("\\n")[0]
    # Use the sub-LLM for SEMANTIC classification
    category = llm_query(
        f"Classify this document in one word (science/history/technology): {first_line}"
    )
    print(f"Doc {i}: {first_line[:50]}... -> {category.strip()}")
'''
console.print(Syntax(code.strip(), "python", theme="monokai"))
stdout, stderr = repl2.execute(code)
console.print(f"  [green]{stdout}[/green]")
console.print(f"  Sub-LLM calls made: {repl2.sub_call_count}\n")


# ── Experiment 3: Chunk + Map pattern ──────────────────────────────────────
# This is the most common RLM strategy: chunk the context, run sub-LLM
# calls on each chunk, aggregate results.

console.print(Panel("[bold]Experiment 3: Chunk + Map + Reduce[/bold]", style="cyan"))
console.print("  The most powerful RLM pattern: chunk -> sub-LLM each -> aggregate.\n")

# Load the haystack as context
haystack_path = os.path.join(os.path.dirname(__file__), "sample_data", "haystack.txt")
with open(haystack_path) as f:
    haystack = f.read()

repl3 = SimpleREPL(llm_fn=llm_query)
repl3.load_context(haystack)

code = '''
# Split context into paragraphs
paragraphs = [p.strip() for p in context.split("\\n\\n") if p.strip()]
print(f"Total paragraphs: {len(paragraphs)}")

# Map: ask the sub-LLM about each chunk
summaries = []
for i, para in enumerate(paragraphs):
    summary = llm_query(
        f"In one sentence, what is this paragraph about? "
        f"If it contains a SECRET_FACT, say 'SECRET: <the fact>'.\\n\\n{para}"
    )
    summaries.append(summary.strip())
    print(f"Para {i}: {summary.strip()[:500]}")

# Reduce: aggregate findings
all_summaries = "\\n".join(f"{i}: {s}" for i, s in enumerate(summaries))
final = llm_query(
    f"Based on these paragraph summaries, what is the SECRET_FACT?\\n\\n{all_summaries}"
)
print(f"\\nFINAL ANSWER: {final}")
'''
console.print(Syntax(code.strip(), "python", theme="monokai"))
stdout, stderr = repl3.execute(code)
console.print(f"  [green]{stdout}[/green]")
if stderr:
    console.print(f"  [red]{stderr}[/red]")
console.print(f"  Total sub-LLM calls: {repl3.sub_call_count}\n")


# ── Experiment 4: The LLM decides its own strategy ────────────────────────
console.print(Panel(
    "[bold]Experiment 4: The LLM Decides the Strategy[/bold]",
    style="cyan",
))
console.print("  Now let the ROOT LLM choose how to interact with context.\n")

repl4 = SimpleREPL(llm_fn=llm_query)
with open(haystack_path) as f:
    repl4.load_context(f.read())

system_prompt = """You have a Python REPL with:
- `context`: a string variable with {ctx_len} characters of text
- `llm_query(prompt)`: calls an LLM and returns its response as a string

Write ```repl``` code blocks to explore the context and answer the question.
Use llm_query() for any semantic analysis. Use print() to see results.""".format(
    ctx_len=len(haystack)
)

question = "What is the secret fact in the text, and what broader topic is the text about?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question},
]

for turn in range(3):
    console.print(f"  [bold cyan]--- Turn {turn + 1} ---[/bold cyan]")
    response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
    llm_text = response.choices[0].message.content
    if llm_text is None:
        console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
        console.print(f"  [dim]{response.choices[0]}[/dim]")
        llm_text = ""
    console.print(f"  LLM: {llm_text[:300]}{'...' if len(llm_text) > 300 else ''}\n")

    blocks = find_code_blocks(llm_text)
    messages.append({"role": "assistant", "content": llm_text})

    if blocks:
        all_output = ""
        for block in blocks:
            console.print(Syntax(block, "python", theme="monokai"))
            stdout, stderr = repl4.execute(block)
            output = format_output(stdout, stderr)
            all_output += output + "\n"
            if stdout:
                console.print(f"  [green]{stdout.strip()[:500]}[/green]")
            if stderr:
                console.print(f"  [red]{stderr.strip()}[/red]")
        messages.append({"role": "user", "content": f"Code output:\n{all_output}\n\nContinue."})
    else:
        break
    console.print()

console.print(f"  Total sub-LLM calls: {repl4.sub_call_count}\n")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. llm_query() injected into the REPL lets code call the LLM.
# 2. This enables SEMANTIC operations: classify, summarize, extract meaning.
# 3. The Chunk + Map + Reduce pattern is the workhorse of RLMs:
#    - Chunk: split context into pieces
#    - Map: run llm_query() on each piece
#    - Reduce: aggregate results with another llm_query()
# 4. The root LLM decides the strategy -- we don't hardcode it.
# 5. Sub-LLM calls are tracked for cost analysis.
#
# We now have ALL the building blocks of an RLM:
#   REPL sandbox + LLM writes code + context as variable + sub-LLM calls
#
# NEXT: Steps 8-13 assemble these pieces into a complete RLM class.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] Sub-LLM calls from within the REPL complete the picture.\n"
    "The root LLM can now:\n"
    "  1. Peek at context (code)\n"
    "  2. Chunk it programmatically (code)\n"
    "  3. Ask semantic questions about each chunk (llm_query)\n"
    "  4. Aggregate results (code + llm_query)\n\n"
    "We have all the pieces. Steps 8-13 assemble them into a full RLM.",
    style="green",
))
