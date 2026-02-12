"""
Step 11: Needle in a Haystack -- RLM vs Direct LLM
====================================================

CONCEPT
-------
Now we test our SimpleRLM against a direct LLM call on the classic
"needle in a haystack" task: find a hidden fact buried in a large context.

This mirrors the S-NIAH benchmark from the paper, where RLMs maintain
near-perfect performance while base LLMs degrade with context length.

From the paper:
  "RLMs demonstrate extremely strong performance even at the 10M+ token
   scale, and dramatically outperform all other approaches at long-context
   processing."

WHY THIS MATTERS
----------------
This is the first real head-to-head comparison showing that our
from-scratch RLM implementation actually works better than stuffing
everything into the LLM's prompt.

Run:  python step11_needle_haystack.py
"""

import io
import random
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


# ── Shared infrastructure (from previous steps) ──────────────────────────────
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
1. `context` -- the data to analyze (check type and length first)
2. `llm_query(prompt)` -- calls a sub-LLM for semantic analysis
3. `print()` -- to view results

Strategies: peek first, use regex/keyword search, chunk+map with llm_query if needed.

Write code in ```repl``` blocks. When done: FINAL(answer) or FINAL_VAR(var_name).
Create variables in ```repl``` first, then FINAL_VAR in your NEXT response.
Think step by step and execute immediately."""


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
    var_match = re.search(r"FINAL_VAR\(([^)]+)\)", text)
    if var_match and locals_dict:
        vn = var_match.group(1).strip().strip("\"'")
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
    def __init__(self, depth=0, max_depth=1, max_iterations=8):
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
            ctx_meta = f"\n\nContext is a {type(context).__name__} with {len(context)} items/chars."

        messages = [
            {"role": "system", "content": RLM_SYSTEM_PROMPT + ctx_meta},
            {"role": "user", "content": query},
        ]

        for _ in range(self.max_iterations):
            self.total_llm_calls += 1
            r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            text = r.choices[0].message.content
            if text is None:
                console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"    [dim]{r.choices[0]}[/dim]")
                text = ""

            final = find_final_answer(text, repl.locals)
            if final:
                return final

            blocks = find_code_blocks(text)
            messages.append({"role": "assistant", "content": text})
            if blocks:
                out = ""
                for b in blocks:
                    so, se = repl.execute(b)
                    out += format_output(so, se) + "\n"
                messages.append({"role": "user", "content": f"Output:\n{out}\nContinue. Use FINAL() when done."})
            else:
                messages.append({"role": "user", "content": "Write ```repl``` code or FINAL()."})

        return "Max iterations reached."


# ── Build haystack data ────────────────────────────────────────────────────
FILLER_PARAGRAPHS = [
    "The history of bread-making dates back thousands of years to ancient Egypt. Early breads were flatbreads made from ground grains mixed with water and baked on hot stones.",
    "Octopuses are remarkable creatures with three hearts, blue blood, and the ability to change color and texture in milliseconds.",
    "The Dead Sea is one of the saltiest bodies of water on Earth. Its salinity allows people to float effortlessly.",
    "Coffee was first cultivated in Ethiopia in the 9th century. Legend has it that a goat herder named Kaldi noticed his goats became energetic after eating certain berries.",
    "The Great Wall of China stretches over 13,000 miles across northern China. It is one of the most impressive construction projects in human history.",
    "Antarctica is the driest continent on Earth, technically classified as a desert despite being covered in ice.",
    "The Fibonacci sequence appears throughout nature, from sunflower seeds to tree branching patterns.",
    "Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still edible.",
    "The Amazon River discharges more water into the ocean than the next seven largest rivers combined.",
    "Venus rotates in the opposite direction to most planets. A day on Venus is longer than its year.",
    "The Mariana Trench reaches a maximum depth of about 36,000 feet with over 1,000 times atmospheric pressure.",
    "The human brain contains approximately 86 billion neurons connected by 100 trillion synapses.",
    "The Sahara Desert was once a lush green savanna with lakes and diverse wildlife 5,000-10,000 years ago.",
    "Lightning strikes the Earth approximately 100 times every second, reaching temperatures five times hotter than the Sun's surface.",
    "The oldest known living organism is a bristlecone pine tree over 4,850 years old in California.",
]

NEEDLE = "HIDDEN_FACT: The world's oldest known recipe is for beer, dating back to approximately 1800 BCE in ancient Sumeria."


def build_haystack(num_paragraphs: int, needle_position: str = "middle") -> str:
    random.seed(42)
    paragraphs = [random.choice(FILLER_PARAGRAPHS) for _ in range(num_paragraphs)]
    if needle_position == "start":
        idx = max(1, len(paragraphs) // 10)
    elif needle_position == "end":
        idx = len(paragraphs) - max(1, len(paragraphs) // 10)
    else:
        idx = len(paragraphs) // 2
    paragraphs.insert(idx, NEEDLE)
    return "\n\n".join(paragraphs)


# ── Direct LLM approach ───────────────────────────────────────────────────
def direct_llm(question: str, context: str) -> tuple[str, float]:
    start = time.time()
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": f"{question}\n\nContext:\n{context}"}],
        **model_kwargs(),
    )
    return r.choices[0].message.content, time.time() - start


# ── Benchmark ──────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Needle-in-a-Haystack Benchmark: RLM vs Direct LLM[/bold]\n\n"
    "We hide a HIDDEN_FACT in increasingly large context and compare\n"
    "our SimpleRLM against stuffing everything into the LLM's prompt.",
    style="cyan",
))

QUESTION = "What is the HIDDEN_FACT in the text? Quote it exactly."
ANSWER_KEY = "1800 BCE"

table = Table(title="RLM vs Direct LLM: Needle in a Haystack")
table.add_column("Paragraphs", justify="right")
table.add_column("~Chars", justify="right")
table.add_column("Position", justify="center")
table.add_column("Direct LLM", justify="center")
table.add_column("Direct Time", justify="right")
table.add_column("RLM", justify="center")
table.add_column("RLM Time", justify="right")
table.add_column("RLM Calls", justify="right")

sizes = [10, 30, 60]
positions = ["start", "middle", "end"]

for size in sizes:
    for pos in positions:
        haystack = build_haystack(size, pos)

        # Direct LLM
        direct_answer, direct_time = direct_llm(QUESTION, haystack)
        direct_found = ANSWER_KEY in direct_answer

        # RLM
        rlm = SimpleRLM(depth=0, max_depth=1, max_iterations=5)
        start = time.time()
        rlm_answer = rlm.completion(QUESTION, context=haystack)
        rlm_time = time.time() - start
        rlm_found = ANSWER_KEY in str(rlm_answer)

        d_status = "[green]FOUND[/green]" if direct_found else "[red]MISS[/red]"
        r_status = "[green]FOUND[/green]" if rlm_found else "[red]MISS[/red]"

        table.add_row(
            str(size), f"{len(haystack):,}", pos,
            d_status, f"{direct_time:.1f}s",
            r_status, f"{rlm_time:.1f}s",
            str(rlm.total_llm_calls),
        )

console.print(table)

# ── Analysis ──────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Analysis[/bold]\n\n"
    "The RLM approach:\n"
    "  1. Never sends the full context to the LLM (avoids context rot)\n"
    "  2. Uses code to search: regex, keyword matching, slicing\n"
    "  3. Only sends relevant snippets to sub-LLMs\n"
    "  4. Takes more time (multiple API calls) but more reliable\n\n"
    "The paper showed this scales to 10M+ tokens where direct LLM fails completely.\n"
    "For S-NIAH tasks, RLMs maintain near-perfect accuracy at all scales.",
    style="green",
))

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. For needle-in-haystack, both approaches often work at small scales.
# 2. At larger scales, the RLM is more robust (code-based search).
# 3. The RLM costs more API calls but avoids context rot entirely.
# 4. The paper's S-NIAH results: RLM maintains near-100% at all scales.
# 5. The real advantage shows on HARDER tasks (next step: multi-document).
#
# NEXT: Step 12 tests multi-document reasoning where the advantage is larger.
# ─────────────────────────────────────────────────────────────────────────────
