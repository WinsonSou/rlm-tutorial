"""
Step 5: LLM Writes Code
========================

CONCEPT
-------
Now we connect the two pieces from Steps 1 and 4:
  - Step 1: The LLM generates text (including code)
  - Step 4: The REPL sandbox executes code and captures output

The bridge is: ask the LLM to wrap its code in ```repl``` blocks, parse those
blocks out of the response, execute them, and return the output.

This is how the RLM interacts with its environment: the model writes code
blocks, we execute them, and feed the results back.

From the paper:
  "The LM interacts by outputting code blocks, and it receives a (truncated)
   version of the output in its context."

WHY THIS MATTERS
----------------
This is the control flow of every RLM iteration:
  1. LLM generates text (may include ```repl``` code blocks)
  2. We parse out the code blocks
  3. Execute each block in the REPL sandbox
  4. Format the output (stdout/stderr) as a string
  5. Append to the conversation history
  6. Repeat

After this step you have an LLM that can write and execute code -- the core
interaction pattern of the RLM.

Run:  python step05_llm_writes_code.py
"""

import io
import re
import sys

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# ── REPL from Step 4 ────────────────────────────────────────────────────────
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
    """A minimal REPL sandbox with output capture and safe builtins."""

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

    def get_var(self, name: str):
        return self.locals.get(name)


# ── Code block parsing ──────────────────────────────────────────────────────
# The LLM wraps code in ```repl``` blocks. We need to extract them.

def find_code_blocks(text: str) -> list[str]:
    """Extract code from ```repl``` fenced blocks in LLM output."""
    pattern = r"```repl\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [m.strip() for m in matches if m.strip()]


# ── Experiment 1: Parse code blocks ─────────────────────────────────────────
console.print(Panel("[bold]Experiment 1: Parsing Code Blocks[/bold]", style="cyan"))

sample_response = """
I'll calculate the sum of squares from 1 to 10.

```repl
total = sum(x**2 for x in range(1, 11))
print(f"Sum of squares 1-10: {total}")
```

The sum of squares from 1 to 10 is 385.
"""

blocks = find_code_blocks(sample_response)
console.print(f"  Found {len(blocks)} code block(s):")
for i, block in enumerate(blocks):
    console.print(Syntax(block, "python", theme="monokai", line_numbers=True))

repl = SimpleREPL()
stdout, stderr = repl.execute(blocks[0])
console.print(f"  stdout: [green]{stdout.strip()}[/green]")
console.print(f"  stderr: [red]{stderr!r}[/red]\n")


# ── Experiment 2: LLM generates code, we execute it ────────────────────────
console.print(Panel("[bold]Experiment 2: LLM Generates Code -> We Execute It[/bold]", style="cyan"))

system_prompt = """You have access to a Python REPL environment.
When you want to run code, wrap it in triple backticks with 'repl' as the language:

```repl
# your code here
print("result")
```

Use print() to show results. Variables persist between code blocks."""

user_prompt = "Calculate the first 15 Fibonacci numbers and print them as a list."

console.print(f"  [bold]Asking LLM:[/bold] {user_prompt}\n")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    **model_kwargs(),
)

llm_output = response.choices[0].message.content
console.print(Panel(llm_output, title="LLM Response", style="dim"))

blocks = find_code_blocks(llm_output)
repl2 = SimpleREPL()

for i, block in enumerate(blocks):
    console.print(f"  [bold]Executing block {i + 1}:[/bold]")
    console.print(Syntax(block, "python", theme="monokai"))
    stdout, stderr = repl2.execute(block)
    if stdout:
        console.print(f"  [green]stdout: {stdout.strip()}[/green]")
    if stderr:
        console.print(f"  [red]stderr: {stderr.strip()}[/red]")
    console.print()


# ── Experiment 3: Multi-turn code execution ────────────────────────────────
# This simulates what the RLM loop does: ask -> code -> execute -> feed back.

console.print(Panel("[bold]Experiment 3: Multi-Turn Code Execution[/bold]", style="cyan"))
console.print("  Simulating the RLM loop: LLM writes code -> execute -> feed output back.\n")

repl3 = SimpleREPL()
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "I want to analyze some data. First, create a list of 20 random "
                                 "numbers between 1 and 100 (use seed 42 for reproducibility)."},
]

for turn in range(3):
    console.print(f"  [bold cyan]--- Turn {turn + 1} ---[/bold cyan]")

    response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
    llm_text = response.choices[0].message.content
    if llm_text is None:
        console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
        console.print(f"  [dim]{response.choices[0]}[/dim]")
        llm_text = ""
    console.print(f"  LLM says: {llm_text[:200]}{'...' if len(llm_text) > 200 else ''}\n")

    blocks = find_code_blocks(llm_text)
    messages.append({"role": "assistant", "content": llm_text})

    if blocks:
        all_output = ""
        for block in blocks:
            console.print(Syntax(block, "python", theme="monokai"))
            stdout, stderr = repl3.execute(block)
            output = ""
            if stdout:
                output += f"stdout:\n{stdout}"
            if stderr:
                output += f"stderr:\n{stderr}"
            all_output += output
            if stdout:
                console.print(f"  [green]{stdout.strip()}[/green]")
            if stderr:
                console.print(f"  [red]{stderr.strip()}[/red]")

        # Feed the execution result back to the LLM
        messages.append({
            "role": "user",
            "content": f"Code output:\n{all_output}\n\nNow calculate the mean, median, and "
                       f"standard deviation of the data." if turn == 0 else
                       f"Code output:\n{all_output}\n\nNow find the top 3 largest values and "
                       f"their positions in the original list." if turn == 1 else
                       f"Code output:\n{all_output}\n\nGreat, summarize your findings."
        })
    else:
        console.print("  [dim]No code blocks in this response.[/dim]")
        break

    console.print()

console.print(f"  [dim]Variables in REPL after 3 turns: {list(repl3.locals.keys())}[/dim]\n")


# ── Format output for the LLM ──────────────────────────────────────────────
console.print(Panel("[bold]Experiment 4: Output Truncation[/bold]", style="cyan"))
console.print("  In a real RLM, we truncate long outputs so the LLM's context doesn't explode.\n")


def format_repl_output(stdout: str, stderr: str, max_chars: int = 2000) -> str:
    """Format REPL output for feeding back to the LLM, with truncation."""
    parts = []
    if stdout:
        if len(stdout) > max_chars:
            parts.append(f"stdout (truncated to {max_chars} chars):\n{stdout[:max_chars]}...")
        else:
            parts.append(f"stdout:\n{stdout}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


# Demo truncation
repl4 = SimpleREPL()
stdout, stderr = repl4.execute("for i in range(500): print(f'Line {i}: ' + 'x' * 50)")
formatted = format_repl_output(stdout, stderr, max_chars=200)
console.print(f"  Raw stdout length: {len(stdout)} chars")
console.print(f"  Truncated output:\n  [dim]{formatted}[/dim]\n")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. The LLM wraps code in ```repl``` blocks; we parse them with regex.
# 2. We execute each block in our REPL sandbox and capture output.
# 3. The output is formatted (and truncated) and fed back to the LLM.
# 4. This create a multi-turn loop: LLM -> code -> execute -> output -> LLM.
# 5. Variables persist across turns -- the REPL accumulates state.
#
# But notice: we're still feeding the context directly to the LLM!
#
# NEXT: Step 6 introduces the KEY RLM insight -- putting the context
# in the REPL as a variable instead of in the LLM's prompt.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] The LLM -> code -> execute -> output loop is the\n"
    "core interaction pattern of an RLM. But we haven't yet put the CONTEXT\n"
    "into the REPL. That's the key insight in Step 6.",
    style="green",
))
