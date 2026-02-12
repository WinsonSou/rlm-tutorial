"""
Step 6: Context as a Variable -- The Key RLM Insight
=====================================================

CONCEPT
-------
This is the single most important idea in the entire RLM paper:

  **Don't feed the context to the LLM. Put it in the REPL as a variable
  and let the LLM interact with it through code.**

Traditional approach:
  LLM(query + huge_context) -> answer     # context rot!

RLM approach:
  REPL.locals["context"] = huge_context   # context lives in code environment
  LLM(query + "context is 2M chars")      # LLM only sees metadata
  LLM writes: print(context[:1000])       # LLM peeks at the data
  LLM writes: len(context)                # LLM checks the size
  LLM writes: re.findall(r'\\d+', context) # LLM searches programmatically

The LLM never sees the full context in its prompt. It decides how to
interact with it through code.

From the paper:
  "The key insight is that long prompts should not be fed into the neural
   network directly but should instead be treated as part of the environment
   that the LLM can symbolically interact with."

WHY THIS MATTERS
----------------
This is what makes RLMs fundamentally different from other long-context
approaches. The context is an OBJECT in the environment, not part of the
prompt. The LLM can peek, slice, grep, chunk, and transform it at will.

Run:  python step06_context_as_variable.py
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


# ── REPL and helpers from previous steps ─────────────────────────────────────
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
        """Load context as a variable in the REPL -- THE KEY RLM OPERATION."""
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


# ── Load the haystack context ───────────────────────────────────────────────
haystack_path = os.path.join(os.path.dirname(__file__), "sample_data", "haystack.txt")
with open(haystack_path) as f:
    haystack = f.read()

console.print(Panel(
    f"[bold]The Key Insight: Context as a Variable[/bold]\n\n"
    f"Loaded haystack.txt: {len(haystack):,} characters\n"
    f"The LLM will NOT see this text. It only knows it exists as 'context'.",
    style="cyan",
))


# ── Experiment 1: Traditional vs RLM approach ──────────────────────────────
console.print(Panel("[bold]Experiment 1: Traditional vs RLM Approach[/bold]", style="cyan"))

question = "What is the secret fact mentioned in the text?"

# Traditional: stuff context into the prompt
console.print("  [bold]Traditional:[/bold] Feed entire context to LLM")
trad_response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": f"{question}\n\nContext:\n{haystack}"}],
    **model_kwargs(),
)
console.print(f"  Response: [green]{trad_response.choices[0].message.content[:200]}[/green]\n")

# RLM: context is a variable, LLM only sees metadata
console.print("  [bold]RLM approach:[/bold] Context is a variable in the REPL")
console.print(f"  LLM sees: 'You have a context variable with {len(haystack):,} characters'")
console.print(f"  LLM does NOT see the actual text!\n")


# ── Experiment 2: LLM interacts with context through code ──────────────────
console.print(Panel("[bold]Experiment 2: LLM Interacts With Context Via Code[/bold]", style="cyan"))

repl = SimpleREPL()
repl.load_context(haystack)

system_prompt = """You have access to a Python REPL environment with a variable called `context` that contains text data.
You do NOT see the context directly -- you must use code to interact with it.
The context has {ctx_len} characters.

To run code, use ```repl``` blocks:
```repl
print(context[:500])  # peek at the first 500 chars
```

Use print() to view results. Find the SECRET_FACT in the context.""".format(ctx_len=len(haystack))

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question},
]

console.print(f"  [dim]System prompt tells LLM about 'context' variable ({len(haystack):,} chars)[/dim]")
console.print(f"  [dim]LLM must write code to interact with it.[/dim]\n")

# Run 3 turns of the loop
for turn in range(10):
    console.print(f"  [bold cyan]--- Turn {turn + 1} ---[/bold cyan]")

    response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
    llm_text = response.choices[0].message.content
    if llm_text is None:
        console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
        console.print(f"  [dim]{response.choices[0]}[/dim]")
        llm_text = ""

    # Show the LLM's reasoning (truncated)
    reasoning = llm_text[:300] + "..." if len(llm_text) > 300 else llm_text
    console.print(f"  LLM: {reasoning}\n")

    blocks = find_code_blocks(llm_text)
    messages.append({"role": "assistant", "content": llm_text})

    if blocks:
        all_output = ""
        for block in blocks:
            console.print(Syntax(block, "python", theme="monokai"))
            stdout, stderr = repl.execute(block)
            output = format_output(stdout, stderr)
            all_output += output + "\n"
            if stdout:
                console.print(f"  [green]{stdout.strip()[:500]}[/green]")
            if stderr:
                console.print(f"  [red]{stderr.strip()}[/red]")

        messages.append({"role": "user", "content": f"Code output:\n{all_output}\n\nContinue."})
    else:
        console.print("  [dim](No code blocks -- LLM provided answer directly)[/dim]")
        break

    console.print()


# ── Experiment 3: Strategies the LLM can use ──────────────────────────────
console.print(Panel("[bold]Experiment 3: Strategies Available to the LLM[/bold]", style="cyan"))
console.print("  Because context is a variable, the LLM can use ANY Python operation:\n")

repl2 = SimpleREPL()
repl2.load_context(haystack)

strategies = [
    ("Peeking", "print(context[:200])"),
    ("Size check", "print(f'Total length: {len(context)} chars')"),
    ("Line count", "lines = context.split('\\n')\nprint(f'Total lines: {len(lines)}')"),
    ("Grep", "import re\nmatches = re.findall(r'SECRET.*', context)\nprint(matches)"),
    ("Keyword search", "for i, line in enumerate(context.split('\\n')):\n    if 'SECRET' in line:\n        print(f'Line {i}: {line}')"),
    ("Slicing", "print(context[len(context)//2 : len(context)//2 + 200])"),
]

for name, code in strategies:
    console.print(f"  [bold]{name}:[/bold]")
    console.print(Syntax(code, "python", theme="monokai"))
    stdout, stderr = repl2.execute(code)
    if stdout:
        console.print(f"  -> [green]{stdout.strip()[:200]}[/green]")
    if stderr:
        console.print(f"  -> [red]{stderr.strip()}[/red]")
    console.print()

# ── Experiment 4: Multi-document context ──────────────────────────────────
console.print(Panel("[bold]Experiment 4: Multi-Document Context[/bold]", style="cyan"))
console.print("  Context can be ANY Python object -- not just a string.\n")

docs_dir = os.path.join(os.path.dirname(__file__), "sample_data", "documents")
documents = []
for fname in sorted(os.listdir(docs_dir)):
    if fname.endswith(".txt"):
        with open(os.path.join(docs_dir, fname)) as f:
            documents.append({"filename": fname, "content": f.read()})

repl3 = SimpleREPL()
repl3.load_context(documents)

demo_code = """
print(f"Number of documents: {len(context)}")
print(f"Type of context: {type(context)}")
for i, doc in enumerate(context):
    print(f"  Doc {i}: {doc['filename']} ({len(doc['content'])} chars)")
    # Show first line of content
    first_line = doc['content'].split('\\n')[0]
    print(f"         {first_line}")
"""
console.print(Syntax(demo_code.strip(), "python", theme="monokai"))
stdout, stderr = repl3.execute(demo_code)
console.print(f"  [green]{stdout}[/green]")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. THE KEY INSIGHT: context lives in the REPL, not in the LLM's prompt.
# 2. The LLM only sees metadata (e.g., "context has 2M chars").
# 3. The LLM writes code to peek, slice, grep, and transform the context.
# 4. Context can be any Python object: str, list, dict, etc.
# 5. This avoids context rot because the LLM's actual prompt stays small.
#
# But what if the LLM needs to REASON about parts of the context?
# Grep and slicing aren't enough for semantic questions.
#
# NEXT: Step 7 adds the ability for code in the REPL to call the LLM itself.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] Context as a variable is the foundation of RLMs.\n"
    "The LLM's prompt stays small (no context rot). The LLM uses CODE to\n"
    "interact with the context: peek, slice, grep, transform.\n\n"
    "But code alone can't answer SEMANTIC questions about the text.\n"
    "For that, the code needs to be able to call the LLM itself (Step 7).",
    style="green",
))
