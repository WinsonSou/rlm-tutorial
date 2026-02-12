"""
Step 4: REPL Sandbox
====================

CONCEPT
-------
Before the LLM can write code to interact with context, we need a safe place
to execute that code.  Python's `exec()` function runs arbitrary code strings,
but we need to:

  1. Capture stdout/stderr instead of printing to the terminal
  2. Maintain a persistent namespace (variables survive across executions)
  3. Restrict dangerous operations (no `eval`, `exec`, `input`)
  4. Handle errors gracefully (return stderr, don't crash)

This is the REPL (Read-Eval-Print Loop) environment from the RLM paper.

From the paper:
  "We choose the environment to be a loop where the LM can write to and read
   the output of cells of a Python REPL Notebook... that is pre-loaded with
   the context as a variable in memory."

WHY THIS MATTERS
----------------
The REPL sandbox is the environment (E) in the RLM framework.  It's where:
- The context lives as a variable
- The LLM's code gets executed
- Sub-LLM calls happen (Step 7)
- Final answers are built up

Run:  python step04_repl_sandbox.py
"""

import io
import sys

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

console = Console()


# ── The simplest exec() ───────────────────────────────────────────────────
console.print(Panel("[bold]Experiment 1: Raw exec()[/bold]", style="cyan"))

code = "x = 2 + 2\nprint(f'x = {x}')"
console.print(Syntax(code, "python", theme="monokai"))
console.print("  Running exec()...")

namespace = {}
exec(code, namespace)
console.print(f"  namespace['x'] = {namespace['x']}")
console.print(f"  [dim]Output went to terminal (not captured). We need to fix this.[/dim]\n")


# ── Capturing stdout/stderr ───────────────────────────────────────────────
console.print(Panel("[bold]Experiment 2: Capturing Output[/bold]", style="cyan"))


def execute_simple(code: str, namespace: dict) -> tuple[str, str]:
    """Execute code and capture stdout/stderr."""
    old_stdout, old_stderr = sys.stdout, sys.stderr
    stdout_buf, stderr_buf = io.StringIO(), io.StringIO()
    try:
        sys.stdout, sys.stderr = stdout_buf, stderr_buf
        exec(code, namespace)
    except Exception as e:
        stderr_buf.write(f"{type(e).__name__}: {e}")
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr
    return stdout_buf.getvalue(), stderr_buf.getvalue()


ns = {}
stdout, stderr = execute_simple("x = 42\nprint(f'The answer is {x}')", ns)
console.print(f"  stdout: [green]{stdout!r}[/green]")
console.print(f"  stderr: [red]{stderr!r}[/red]")
console.print(f"  namespace['x'] = {ns['x']}")

# Error handling
stdout, stderr = execute_simple("y = 1 / 0", ns)
console.print(f"\n  Divide by zero:")
console.print(f"  stdout: [green]{stdout!r}[/green]")
console.print(f"  stderr: [red]{stderr!r}[/red]")
console.print(f"  namespace['x'] still = {ns['x']}  (persistent!)\n")


# ── Persistent namespace ─────────────────────────────────────────────────
console.print(Panel("[bold]Experiment 3: Persistent Namespace[/bold]", style="cyan"))
console.print("  Variables survive across multiple exec() calls.\n")

ns2 = {}
cells = [
    "total = 0",
    "total += 10\nprint(f'After +10: {total}')",
    "total += 20\nprint(f'After +20: {total}')",
    "total *= 2\nprint(f'After *2: {total}')",
]

for i, cell in enumerate(cells):
    stdout, stderr = execute_simple(cell, ns2)
    console.print(f"  Cell {i}: {cell!r}")
    if stdout:
        console.print(f"         -> [green]{stdout.strip()}[/green]")
    if stderr:
        console.print(f"         -> [red]{stderr.strip()}[/red]")

console.print(f"\n  Final namespace['total'] = {ns2['total']}")
console.print(f"  [dim]This is how the RLM builds up results across iterations![/dim]\n")


# ── Safe builtins ────────────────────────────────────────────────────────
console.print(Panel("[bold]Experiment 4: Safe Builtins[/bold]", style="cyan"))
console.print("  Restrict dangerous functions like eval(), exec(), input().\n")

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
    # Blocked -- these are dangerous
    "eval": None, "exec": None, "input": None, "compile": None,
    "globals": None, "locals": None,
}


def execute_safe(code: str, namespace: dict) -> tuple[str, str]:
    """Execute code in a sandboxed namespace with restricted builtins."""
    namespace.setdefault("__builtins__", SAFE_BUILTINS)
    old_stdout, old_stderr = sys.stdout, sys.stderr
    stdout_buf, stderr_buf = io.StringIO(), io.StringIO()
    try:
        sys.stdout, sys.stderr = stdout_buf, stderr_buf
        exec(code, namespace)
    except Exception as e:
        stderr_buf.write(f"{type(e).__name__}: {e}")
    finally:
        sys.stdout, sys.stderr = old_stdout, old_stderr
    return stdout_buf.getvalue(), stderr_buf.getvalue()


safe_ns = {"__builtins__": SAFE_BUILTINS.copy()}

# Safe operation
stdout, stderr = execute_safe("print(sum(range(10)))", safe_ns)
console.print(f"  sum(range(10)): stdout={stdout.strip()!r}  stderr={stderr!r}")

# Blocked operation
stdout, stderr = execute_safe("eval('2+2')", safe_ns)
console.print(f"  eval('2+2'):    stdout={stdout!r}  stderr={stderr!r}")

# Import still works (needed for regex, json, etc.)
stdout, stderr = execute_safe("import re\nprint(re.findall(r'\\d+', 'abc 123 def 456'))", safe_ns)
console.print(f"  import re:      stdout={stdout.strip()!r}  stderr={stderr!r}\n")


# ── The complete REPL class ──────────────────────────────────────────────
console.print(Panel("[bold]Experiment 5: The SimpleREPL Class[/bold]", style="cyan"))
console.print("  Putting it all together into a reusable class.\n")


class SimpleREPL:
    """A minimal REPL sandbox with output capture and safe builtins."""

    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def execute(self, code: str) -> tuple[str, str]:
        """Execute code, return (stdout, stderr)."""
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
        """Retrieve a variable from the REPL namespace."""
        return self.locals.get(name)


repl = SimpleREPL()

# Multi-cell session
cells = [
    ("Define data", "data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]"),
    ("Sort it", "sorted_data = sorted(data)\nprint(f'Sorted: {sorted_data}')"),
    ("Stats", "avg = sum(data) / len(data)\nprint(f'Mean: {avg:.2f}, Max: {max(data)}, Min: {min(data)}')"),
    ("Filter", "big = [x for x in data if x > avg]\nprint(f'Above mean: {big}')"),
]

result_table = Table(title="SimpleREPL Session")
result_table.add_column("Cell", style="bold")
result_table.add_column("Code")
result_table.add_column("stdout", style="green")
result_table.add_column("stderr", style="red")

for label, code in cells:
    stdout, stderr = repl.execute(code)
    result_table.add_row(label, code[:60], stdout.strip(), stderr.strip())

console.print(result_table)
console.print(f"\n  Variables in REPL: {list(repl.locals.keys())}")
console.print(f"  repl.get_var('avg') = {repl.get_var('avg')}")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. exec() runs code strings and stores results in a namespace dict.
# 2. Capturing stdout/stderr lets us control what the LLM sees as output.
# 3. The namespace persists -- variables accumulate across calls.
# 4. Restricting builtins prevents dangerous operations.
# 5. SimpleREPL is the foundation of the RLM's environment.
#
# NEXT: Step 5 has the LLM *generate* the code that runs in this REPL.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] The REPL is a persistent, sandboxed Python environment.\n"
    "Variables accumulate across cells. Output is captured as strings.\n"
    "This is the 'environment' (E) in the RLM framework.",
    style="green",
))
