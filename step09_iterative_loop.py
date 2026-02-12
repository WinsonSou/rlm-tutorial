"""
Step 9: The Iterative Loop -- FINAL() / FINAL_VAR()
====================================================

CONCEPT
-------
The RLM runs in a loop:
  1. Send messages to the LLM
  2. Parse code blocks from the response
  3. Execute code in the REPL
  4. Append output to messages
  5. Check if the LLM produced a FINAL answer
  6. If not, repeat from step 1

The LLM signals it's done in two ways:
  - FINAL(answer text here): Directly provide the answer as text.
  - FINAL_VAR(variable_name): Return the value of a REPL variable.

FINAL_VAR is powerful because the LLM can build up a complex answer in
the REPL (e.g., a list of results from sub-LLM calls) and return it as
a variable. This enables unbounded output length.

From the paper:
  "When the root LM is confident it has an answer, it can either directly
   output the answer as FINAL(answer), or it can build up an answer using
   the variables in its REPL environment, and return the string inside
   that answer as FINAL_VAR(final_ans_var)."

WHY THIS MATTERS
----------------
The iterative loop is the control flow of the entire RLM. Without it,
the system would be a single-shot code generation. The loop allows the
LLM to iteratively refine its approach based on execution feedback.

Run:  python step09_iterative_loop.py
"""

import io
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


# ── Parsing functions ────────────────────────────────────────────────────────

def find_code_blocks(text: str) -> list[str]:
    """Extract code from ```repl``` fenced blocks."""
    pattern = r"```repl\s*\n(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    return [m.strip() for m in matches if m.strip()]


def find_final_answer(text: str, repl_locals: dict | None = None) -> str | None:
    """
    Check if the LLM has provided a final answer.

    Two formats:
      FINAL(answer text)     -> returns "answer text"
      FINAL_VAR(var_name)    -> returns str(repl_locals[var_name])
    """
    # Check for FINAL_VAR first (more specific)
    var_match = re.search(r"FINAL_VAR\(([^)]+)\)", text)
    if var_match and repl_locals is not None:
        var_name = var_match.group(1).strip().strip("\"'")
        if var_name in repl_locals:
            return str(repl_locals[var_name])
        return f"Error: Variable '{var_name}' not found. Available: {list(repl_locals.keys())}"

    # Check for FINAL(...)
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


# ── Experiment 1: Parsing FINAL() and FINAL_VAR() ──────────────────────────
console.print(Panel("[bold]Experiment 1: Parsing Final Answers[/bold]", style="cyan"))

test_cases = [
    ("FINAL(The answer is 42)", None, "Direct answer"),
    ("Based on my analysis, FINAL(Paris is the capital of France)", None, "Embedded in text"),
    ("FINAL_VAR(result)", {"result": "Hello World", "tmp": 123}, "Variable reference"),
    ("FINAL_VAR(my_list)", {"my_list": [1, 2, 3]}, "List variable"),
    ("No final answer here, just thinking...", None, "No answer yet"),
]

for text, locals_dict, label in test_cases:
    answer = find_final_answer(text, locals_dict)
    if answer is not None:
        console.print(f"  {label}: [green]{answer}[/green]")
    else:
        console.print(f"  {label}: [dim](no final answer)[/dim]")
console.print()


# ── REPL class ──────────────────────────────────────────────────────────────
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


# ── The iterative RLM loop ──────────────────────────────────────────────────

class SimpleRLM:
    """RLM with depth control and iterative FINAL() loop."""

    def __init__(self, depth: int = 0, max_depth: int = 1, max_iterations: int = 10):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.total_llm_calls = 0
        self.total_sub_calls = 0

    def completion(self, prompt: str, context=None) -> str:
        if self.depth >= self.max_depth:
            return self._plain_llm_call(prompt)
        return self._repl_loop(prompt, context)

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

    def _repl_loop(self, prompt: str, context=None) -> str:
        """The core iterative loop with FINAL() detection."""
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_llm_query)

        if context is not None:
            repl.load_context(context)

        ctx_info = ""
        if context is not None:
            ctx_info = f"\n\nYou have a `context` variable ({len(str(context)):,} chars)."
            ctx_info += "\nUse `llm_query(prompt)` to call a sub-LLM for semantic analysis."

        system = (
            "You have a Python REPL environment. Write ```repl``` code blocks.\n"
            "Use print() to see results. Variables persist across blocks.\n"
            + ctx_info + "\n\n"
            "When done, signal your answer with:\n"
            "  FINAL(your answer here)  -- for direct text answers\n"
            "  FINAL_VAR(variable_name) -- to return a REPL variable's value\n"
            "\n"
            "IMPORTANT: Create and assign variables in a ```repl``` block FIRST, "
            "then call FINAL_VAR in your NEXT response (not in code)."
        )

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ]

        for iteration in range(self.max_iterations):
            self.total_llm_calls += 1
            response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            llm_text = response.choices[0].message.content
            if llm_text is None:
                console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"    [dim]{response.choices[0]}[/dim]")
                llm_text = ""

            console.print(f"    [dim]Iteration {iteration + 1}[/dim]")

            # Check for final answer BEFORE executing code
            final = find_final_answer(llm_text, repl.locals)
            if final is not None:
                console.print(f"    [bold green]FINAL answer found![/bold green]")
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
                        console.print(f"    [green]{stdout.strip()[:200]}[/green]")
                    if stderr:
                        console.print(f"    [red]{stderr.strip()[:200]}[/red]")

                messages.append({
                    "role": "user",
                    "content": f"Code output:\n{all_output}\n\nContinue your analysis. "
                               "When you have the answer, use FINAL() or FINAL_VAR()."
                })
            else:
                # No code, no FINAL -- ask the LLM to conclude
                messages.append({
                    "role": "user",
                    "content": "Please provide your final answer using FINAL()."
                })

        # Ran out of iterations -- force an answer
        return self._force_final_answer(messages)

    def _force_final_answer(self, messages: list) -> str:
        """Ask the LLM to produce a final answer when iterations run out."""
        self.total_llm_calls += 1
        messages.append({
            "role": "user",
            "content": "You've run out of iterations. Please provide your best answer now with FINAL()."
        })
        response = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
        text = response.choices[0].message.content
        if text is None:
            console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
            console.print(f"    [dim]{response.choices[0]}[/dim]")
            text = ""
        final = find_final_answer(text)
        return final if final else text


# ── Experiment 2: The full iterative loop ──────────────────────────────────
console.print(Panel("[bold]Experiment 2: The Full Iterative Loop[/bold]", style="cyan"))

context = """
Employee records for Q4 2024:
Name: Alice Chen | Department: Engineering | Salary: $145,000 | Start: 2019-03-15
Name: Bob Kumar | Department: Marketing | Salary: $98,000 | Start: 2021-07-01
Name: Carol White | Department: Engineering | Salary: $155,000 | Start: 2017-11-20
Name: David Park | Department: Sales | Salary: $87,000 | Start: 2023-01-10
Name: Eve Martinez | Department: Engineering | Salary: $168,000 | Start: 2016-06-05
Name: Frank Jones | Department: Marketing | Salary: $92,000 | Start: 2022-09-12
Name: Grace Liu | Department: Sales | Salary: $95,000 | Start: 2020-04-22
Name: Henry Brown | Department: Engineering | Salary: $142,000 | Start: 2018-08-30
"""

rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=5)
console.print("  [bold]Query:[/bold] What is the average salary in Engineering? "
              "Who earns the most?\n")

start = time.time()
result = rlm.completion(
    "What is the average salary in the Engineering department? "
    "Who is the highest paid engineer? Use code to calculate precisely.",
    context=context,
)
elapsed = time.time() - start

console.print(f"\n  [bold green]Answer:[/bold green] {result}")
console.print(f"  LLM calls: {rlm.total_llm_calls}, Sub-LLM calls: {rlm.total_sub_calls}")
console.print(f"  Time: {elapsed:.1f}s\n")


# ── Experiment 3: FINAL_VAR with built-up results ────────────────────────
console.print(Panel("[bold]Experiment 3: Using FINAL_VAR for Complex Results[/bold]", style="cyan"))

rlm2 = SimpleRLM(depth=0, max_depth=1, max_iterations=6)
result = rlm2.completion(
    "Parse the employee data and create a summary dict with: department names "
    "as keys, and for each dept the count, average salary, and list of names. "
    "Store in a variable called `summary` then use FINAL_VAR(summary).",
    context=context,
)
console.print(f"  [green]{result[:600]}[/green]")
console.print(f"  LLM calls: {rlm2.total_llm_calls}\n")


# ── Experiment 4: Error recovery ─────────────────────────────────────────
console.print(Panel("[bold]Experiment 4: Error Recovery[/bold]", style="cyan"))
console.print("  The LLM can recover from code errors thanks to the iterative loop.\n")

rlm3 = SimpleRLM(depth=0, max_depth=1, max_iterations=5)
result = rlm3.completion(
    "Calculate the factorial of 20 using a recursive function. "
    "Be careful with the implementation.",
    context=None,
)
console.print(f"  [green]{result[:300]}[/green]")
console.print(f"  Iterations used: {rlm3.total_llm_calls}\n")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. The RLM loop: prompt -> code -> execute -> check FINAL -> repeat.
# 2. FINAL(text) returns a direct text answer.
# 3. FINAL_VAR(name) returns the value of a REPL variable (unbounded output).
# 4. The loop lets the LLM iteratively refine based on execution feedback.
# 5. Error recovery is natural: errors appear in stderr, LLM fixes code.
# 6. Max iterations prevent infinite loops.
#
# NEXT: Step 10 crafts the system prompt that teaches the LLM these patterns.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] The iterative loop with FINAL/FINAL_VAR gives the RLM:\n"
    "  1. Multi-step reasoning (not single-shot)\n"
    "  2. Error recovery (stderr -> fix code -> retry)\n"
    "  3. Unbounded output via FINAL_VAR (return complex variables)\n"
    "  4. Natural stopping criterion (FINAL means done)",
    style="green",
))
