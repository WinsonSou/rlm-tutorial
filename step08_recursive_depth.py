"""
Step 8: Recursive Depth Control
================================

CONCEPT
-------
In the RLM framework, there are two kinds of LLM calls:

  - Root LM (depth 0): Sees the query + metadata about context. Writes code
    in the REPL. Decides the strategy for interacting with context.

  - Sub-LM (depth 1): Called by llm_query() from within the REPL. Sees a
    smaller piece of context directly. Answers specific sub-questions.

The key rule: when depth >= max_depth, the call becomes a plain LLM call
(no REPL, no code execution). This prevents infinite recursion.

From the paper:
  "In our experiments we only consider a recursive depth of 1 -- i.e. the
   root LM can only call LMs, not other RLMs."

  "It is a relatively easy change to allow the REPL environment to call
   RLMs instead of LMs, but we felt that for most modern long context
   benchmarks, a recursive depth of 1 was sufficient."

WHY THIS MATTERS
----------------
Depth control is what makes the system "recursive" in a controlled way.
Without it, the root LM could spawn sub-LMs that spawn more sub-LMs
infinitely. With depth=1, the root LM gets a REPL environment while
sub-LMs are plain text-in/text-out calls.

This step introduces the class structure we build on through Step 13.

Run:  python step08_recursive_depth.py
"""

import io
import re
import sys

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.tree import Tree

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# ── Safe builtins ────────────────────────────────────────────────────────────
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


# ── Core classes ─────────────────────────────────────────────────────────────

class SimpleREPL:
    """REPL sandbox with context loading and sub-LLM support."""

    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def inject_function(self, name: str, fn):
        """Add a callable to the REPL globals."""
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


class SimpleRLM:
    """
    A Recursive Language Model with depth control.

    - depth=0 (root): Gets a REPL environment, writes code, can call sub-LLMs
    - depth>=max_depth: Falls back to a plain LLM call (no REPL)
    """

    def __init__(
        self,
        depth: int = 0,
        max_depth: int = 1,
        max_iterations: int = 5,
    ):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.total_llm_calls = 0
        self.total_sub_calls = 0

    def completion(self, prompt: str, context=None) -> str:
        """
        The main RLM entry point.

        If depth >= max_depth: plain LLM call (text in, text out).
        Otherwise: REPL loop with code execution and sub-LLM calls.
        """
        self.total_llm_calls += 1

        # At max depth, fall back to plain LLM
        if self.depth >= self.max_depth:
            console.print(f"  [dim][depth={self.depth}] Plain LLM call (no REPL)[/dim]")
            return self._plain_llm_call(prompt)

        # Below max depth: use the REPL environment
        console.print(f"  [bold][depth={self.depth}] REPL mode[/bold]")
        return self._repl_loop(prompt, context)

    def _plain_llm_call(self, prompt: str) -> str:
        """A simple LLM call with no REPL environment."""
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
        """Called by code running in the REPL. Creates a depth+1 call."""
        self.total_sub_calls += 1
        sub_rlm = SimpleRLM(
            depth=self.depth + 1,
            max_depth=self.max_depth,
            max_iterations=self.max_iterations,
        )
        result = sub_rlm.completion(prompt)
        self.total_sub_calls += sub_rlm.total_sub_calls
        return result

    def _repl_loop(self, prompt: str, context=None) -> str:
        """The REPL interaction loop for depth < max_depth."""
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_llm_query)

        if context is not None:
            repl.load_context(context)

        ctx_info = ""
        if context is not None:
            ctx_info = f"\nYou have a `context` variable ({len(str(context)):,} chars)."
            ctx_info += "\nUse `llm_query(prompt)` to ask the sub-LLM questions."

        system = (
            "You have a Python REPL environment. Write ```repl``` code blocks to "
            "execute code. Use print() to see results." + ctx_info
        )

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]

        for i in range(self.max_iterations):
            self.total_llm_calls += 1
            response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            llm_text = response.choices[0].message.content
            if llm_text is None:
                if self.verbose:
                    console.print(f"  [yellow]LLM returned None content. Full response:[/yellow]")
                    console.print(f"  [dim]{response.choices[0]}[/dim]")
                llm_text = ""

            blocks = find_code_blocks(llm_text)
            messages.append({"role": "assistant", "content": llm_text})

            if not blocks:
                return llm_text

            all_output = ""
            for block in blocks:
                stdout, stderr = repl.execute(block)
                if stdout:
                    all_output += f"stdout:\n{stdout}"
                if stderr:
                    all_output += f"stderr:\n{stderr}"

            messages.append({
                "role": "user",
                "content": f"Code output:\n{all_output}\n\nContinue your analysis."
            })

        return "Max iterations reached."


def find_code_blocks(text: str) -> list[str]:
    pattern = r"```repl\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [m.strip() for m in matches if m.strip()]


# ── Visualize the depth concept ─────────────────────────────────────────────
console.print(Panel("[bold]The Depth Concept[/bold]", style="cyan"))

tree = Tree("[bold]RLM Call (depth=0, root)")
tree.add("[bold cyan]REPL Environment")
code_node = tree.add("[bold yellow]LLM writes code")
sub = code_node.add("[bold]llm_query() -> depth=1")
sub.add("[dim]Plain LLM call (no REPL)")
sub.add("[dim]Returns text directly")
code_node.add("[bold yellow]More code...")
tree.add("[bold green]FINAL answer")

console.print(tree)
console.print()


# ── Experiment 1: Depth 0 vs Depth 1 ──────────────────────────────────────
console.print(Panel("[bold]Experiment 1: Root LLM (depth=0) vs Sub-LLM (depth=1)[/bold]", style="cyan"))

console.print("  [bold]Root call (depth=0):[/bold] Gets REPL, can execute code")
root_rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=2)
result = root_rlm.completion("Calculate 2^10 using code. Print the result.")
console.print(f"  Result: [green]{result[:200]}[/green]")
console.print(f"  Total LLM calls: {root_rlm.total_llm_calls}\n")

console.print("  [bold]Sub call (depth=1):[/bold] Plain LLM, no REPL")
sub_rlm = SimpleRLM(depth=1, max_depth=1, max_iterations=2)
result = sub_rlm.completion("What is 2^10? Reply with just the number.")
console.print(f"  Result: [green]{result[:200]}[/green]")
console.print(f"  Total LLM calls: {sub_rlm.total_llm_calls}\n")


# ── Experiment 2: Root LLM calling sub-LLMs ──────────────────────────────
console.print(Panel("[bold]Experiment 2: Root LLM Spawns Sub-LLM Calls[/bold]", style="cyan"))

context_text = """
Document 1: The Eiffel Tower was completed in 1889 for the World's Fair in Paris.
It stands 330 meters tall and was the tallest man-made structure in the world until 1930.

Document 2: The Great Pyramid of Giza was built around 2560 BCE for Pharaoh Khufu.
It was the tallest man-made structure for over 3,800 years.

Document 3: The Burj Khalifa in Dubai is currently the tallest building in the world
at 828 meters. It was completed in 2010.
"""

rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=50)
result = rlm.completion(
    "Which structure was the tallest for the longest period of time? "
    "Use the context and llm_query to analyze each document.",
    context=context_text,
)
console.print(f"  [green]{result[:500]}[/green]")
console.print(f"  Root LLM calls: {rlm.total_llm_calls}")
console.print(f"  Sub-LLM calls:  {rlm.total_sub_calls}\n")


# ── Experiment 3: What deeper recursion would look like ───────────────────
console.print(Panel("[bold]Experiment 3: Deeper Recursion (Conceptual)[/bold]", style="cyan"))

console.print("  With max_depth=2, the call tree would look like:\n")
tree2 = Tree("[bold]RLM depth=0 (root)")
t2_repl = tree2.add("[bold cyan]REPL: writes code")
t2_sub = t2_repl.add("[bold]llm_query() -> RLM depth=1")
t2_sub_repl = t2_sub.add("[bold cyan]REPL: writes code")
t2_sub_sub = t2_sub_repl.add("[bold]llm_query() -> depth=2")
t2_sub_sub.add("[dim]Plain LLM call (max_depth reached)")
tree2.add("[bold green]FINAL answer")
console.print(tree2)

console.print(
    "\n  The paper uses max_depth=1 for all experiments.\n"
    "  Deeper recursion is possible but not yet needed for current benchmarks.\n"
)

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. depth=0 (root): REPL environment with code execution + sub-LLM calls.
# 2. depth>=max_depth: Plain LLM call (text in, text out). No REPL.
# 3. This prevents infinite recursion while allowing controlled nesting.
# 4. The paper uses max_depth=1 (root calls LLMs, not other RLMs).
# 5. The SimpleRLM class encapsulates this logic.
#
# NEXT: Step 9 adds the iterative loop with FINAL() / FINAL_VAR() parsing
# so the RLM knows when it has found its answer.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] Depth control makes recursion safe and bounded.\n"
    "Root LM (depth=0) gets the full REPL with sub-calls.\n"
    "Sub-LMs (depth>=max) are plain text-in/text-out calls.\n"
    "This two-tier structure is the backbone of the RLM class.",
    style="green",
))
