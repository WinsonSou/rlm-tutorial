"""
Step 15: Real-World Task -- Cross-Document Policy Analysis
===========================================================

CONCEPT
-------
Everything up to Step 14 used toy examples (haystack, 5 short docs). Now we
apply the SimpleRLM to a REAL corpus: 30 Norfolk Industries IT infrastructure
policy documents that heavily cross-reference each other (~1M chars total).

These documents are perfect for testing RLMs because:
  - They cross-reference each other (Change Mgmt -> CAB -> Incident Mgmt)
  - They share roles across docs (CISO, Head of IT Infrastructure, CAB)
  - They cite the same frameworks (ISO 27001, ITIL 4, COBIT, NIST, SOC 2)
  - Controls in one doc depend on controls in others (backup -> DR -> incident)

We run three progressively harder queries:
  1. Single-doc: find MFA requirements from the IAM policy
  2. Cross-reference: which policies reference the Change Advisory Board?
  3. Multi-hop: trace a vulnerability response across 4 policies

A direct LLM call CANNOT handle this -- the 30 docs total ~1M chars which
far exceeds our model's 20K token context window. The RLM solves this by
using code to search/filter the context and only passing small excerpts to
sub-LLM calls.

Run:  python step15_real_world_policies.py
"""

import io
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from config import API_KEY, BASE_URL, MAX_CONTEXT_TOKENS, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# =============================================================================
# Infrastructure (from Step 13 -- self-contained)
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

RLM_SYSTEM_PROMPT = """You answer queries by writing Python code in ```repl``` blocks.

## REPL tools:
- `context`: a dict mapping filenames to document text.
- `llm_query(prompt)`: call a sub-LLM to read and interpret text. Prompt MUST be under 8000 chars.
- `llm_query_batched(prompts)`: concurrent sub-LLM calls. Same 8000 char limit per prompt.
- `print()`: see code output.

## HARD ROLE CONSTRAINT (non-negotiable)
You DO NOT have permission to read, parse, summarize, interpret, or reason about ANY natural-language document content.
Treat every document string as an opaque byte array. You may ONLY:
- measure length
- search for keywords using regex / substring checks
- split into lines and select small spans by indices
- print VERY small metadata (filenames, counts, line numbers, matched keywords, short snippets <= 200 chars)

If the user asks ANY question whose answer depends on document meaning, policy, intent, or interpretation:
YOU MUST call llm_query() on a short excerpt and use ONLY its return value to answer.


## CRITICAL RULES:
1. You CANNOT read or understand document content yourself. You can only use Python code (regex, `in`, slicing) to LOCATE relevant sections.
2. To UNDERSTAND or ANSWER questions about any text, you MUST pass it to llm_query(). Always use llm_query() to interpret document excerpts. DO NOT DEVIATE FROM THIS STEP!
3. NEVER print large text to read it yourself. NEVER pass a full document to llm_query(). Always extract a short excerpt first (under 8000 chars), then call llm_query().
4. When done, call FINAL(your_answer).

## FREQUENCY RULE (maximize sub-LLM usage)
When in doubt, call llm_query.
You MUST call llm_query for each of the following steps (even if you think you “already know”):
1) Decide which documents are relevant (use small snippets / hit-lists only)
2) Decide which excerpt span best answers the question
3) Interpret the excerpt to produce the final answer
4) If multiple documents are involved, call llm_query per document/excerpt and then one extra llm_query to synthesize.

Prefer llm_query_batched when you have 2+ excerpts to interpret.

## STRICT EXCERPTING RULES
- NEVER pass full documents to llm_query.
- Each llm_query prompt MUST include:
  (a) the user question,
  (b) the excerpt,
  (c) an instruction: "Answer ONLY using the excerpt; if insufficient, say INSUFFICIENT."
- Excerpts should be 20–60 lines OR <= 6000 characters (whichever is smaller).
- If you need more context, take a second adjacent excerpt and call llm_query again.

## WORKFLOW (MANDATORY)
Step A: Explore
- list context keys
- print sizes
- keyword scan to find candidate docs + line numbers (do NOT print doc text)

Step B: Extract
- extract minimal relevant line ranges
- print only line indices + tiny snippets (<= 200 chars) to verify extraction

Step C: Delegate
- call llm_query / llm_query_batched to interpret excerpts
- if result says INSUFFICIENT, expand range and re-call

Step D: Aggregate
- if multiple sub-answers, call llm_query once more to synthesize into final response

Step E: FINAL
- print llm_query call count + justifications
- FINAL(final_answer)

## FAILURE MODE OVERRIDE
If you ever catch yourself about to “read” or “interpret” the document content directly:
STOP, and call llm_query on the excerpt instead.

EXAMPLE -- "What does the audit policy say about frequency?":
```repl
import re
for key in context:
    if 'audit' in key.lower() or 'audit' in context[key][:200].lower():
        print(f"{key}: {len(context[key])} chars")
```
Next turn:
```repl
doc = context['28_Infrastructure_Compliance_Audit...md']
lines = doc.split('\\n')
for i, line in enumerate(lines):
    if 'frequency' in line.lower() or 'annual' in line.lower():
        print(f"Line {i}: {line.strip()}")
```
Next turn (MUST use llm_query to interpret):
```repl
excerpt = '\\n'.join(lines[30:60])
answer = llm_query(f"What is the audit frequency based on this policy excerpt?\\n\\n{excerpt}")
print(answer)
```
Next turn: FINAL(answer)

Write ```repl``` code now."""


class SimpleREPL:
    def __init__(self):
        self.globals: dict = {"__builtins__": SAFE_BUILTINS.copy(), "__name__": "__main__"}
        self.locals: dict = {}

    def inject_function(self, name, fn):
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

def format_output(stdout, stderr, max_chars=2000):
    parts = []
    if stdout:
        parts.append(f"stdout:\n{stdout[:max_chars]}{'...' if len(stdout) > max_chars else ''}")
    if stderr:
        parts.append(f"stderr:\n{stderr}")
    return "\n".join(parts) if parts else "(no output)"


class SimpleRLM:
    def __init__(self, depth=0, max_depth=1, max_iterations=10, verbose=True):
        self.depth = depth
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.root_llm_calls = 0
        self.sub_llm_calls = 0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    SUB_LLM_SYSTEM = (
        "Answer concisely based only on the provided text. "
        "Your context window is ~20,000 tokens. If the input seems large, "
        "focus on the most relevant parts to the question asked. "
        "Do not make up information not present in the text."
    )

    def completion(self, query, context=None):
        if self.depth >= self.max_depth:
            return self._plain_call(query)
        return self._repl_loop(query, context)

    def _plain_call(self, prompt):
        self.root_llm_calls += 1
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": self.SUB_LLM_SYSTEM},
                      {"role": "user", "content": prompt}],
            **model_kwargs(),
        )
        self._track(r)
        return r.choices[0].message.content

    def _sub_query(self, prompt):
        self.sub_llm_calls += 1
        if self.verbose:
            console.print(f"      [magenta]>> sub-LLM call ({len(prompt):,} chars)[/magenta]")
            console.print(f"      [dim]{prompt[:200]}{'...' if len(prompt) > 200 else ''}[/dim]")
        sub = SimpleRLM(self.depth + 1, self.max_depth, verbose=False)
        result = sub.completion(prompt)
        self.sub_llm_calls += sub.sub_llm_calls
        self.total_input_tokens += sub.total_input_tokens
        self.total_output_tokens += sub.total_output_tokens
        if self.verbose:
            console.print(f"      [magenta]<< sub-LLM response ({len(str(result)):,} chars)[/magenta]")
            console.print(f"      [dim]{str(result)[:200]}{'...' if len(str(result)) > 200 else ''}[/dim]")
        return result

    def _sub_query_batched(self, prompts):
        results = [None] * len(prompts)
        def call_one(idx, prompt):
            return idx, self._sub_query(prompt)
        with ThreadPoolExecutor(max_workers=min(len(prompts), 5)) as ex:
            futs = {ex.submit(call_one, i, p): i for i, p in enumerate(prompts)}
            for f in as_completed(futs):
                idx, result = f.result()
                results[idx] = result
        return results

    def _track(self, response):
        usage = getattr(response, "usage", None)
        if usage:
            self.total_input_tokens += usage.prompt_tokens
            self.total_output_tokens += usage.completion_tokens

    def _repl_loop(self, query, context):
        repl = SimpleREPL()
        repl.inject_function("llm_query", self._sub_query)
        repl.inject_function("llm_query_batched", self._sub_query_batched)
        repl.inject_function("SHOW_VARS", repl.show_vars)
        if context is not None:
            repl.load_context(context)

        ctx_meta = ""
        if context is not None:
            if isinstance(context, list):
                total = sum(len(str(i)) for i in context)
                ctx_meta = (f"\n\nContext is a list of {len(context)} items ({total:,} total chars)."
                            f"\nWARNING: Too large for one LLM call. Use code to search/filter.")
            elif isinstance(context, dict):
                total = sum(len(str(v)) for v in context.values())
                key_sizes = ", ".join(f"'{k}' ({len(str(v)):,} chars)" for k, v in list(context.items())[:8])
                if len(context) > 8:
                    key_sizes += f", ... and {len(context) - 8} more"
                ctx_meta = (f"\n\nContext is a dict with {len(context)} keys ({total:,} total chars)."
                            f"\nKeys: [{key_sizes}]"
                            f"\nWARNING: Too large for one LLM call. Search/filter with code, "
                            f"then pass only short excerpts (<8000 chars) to llm_query().")
            else:
                ctx_meta = f"\n\nContext is a string with {len(context):,} characters."
                if len(context) > 40000:
                    ctx_meta += "\nWARNING: Too large for one LLM call. Slice/grep first."

        messages = [
            {"role": "system", "content": RLM_SYSTEM_PROMPT + ctx_meta},
            {"role": "user", "content": query},
        ]

        for iteration in range(self.max_iterations):
            self.root_llm_calls += 1
            r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
            self._track(r)
            text = r.choices[0].message.content
            if text is None:
                if self.verbose:
                    console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
                    console.print(f"    [dim]{r.choices[0]}[/dim]")
                text = ""

            if self.verbose:
                console.print(Panel(
                    f"[bold]Iteration {iteration + 1}[/bold]",
                    style="cyan", expand=False,
                ))
                console.print(f"  [bold]LLM response:[/bold]")
                console.print(f"  {text[:1000]}{'...' if len(text) > 1000 else ''}\n")

            final = find_final_answer(text, repl.locals)
            if final:
                if self.verbose:
                    console.print(f"    [bold green]FINAL answer found![/bold green]")
                return final

            blocks = find_code_blocks(text)
            messages.append({"role": "assistant", "content": text})
            if blocks:
                out = ""
                for i, b in enumerate(blocks):
                    if self.verbose:
                        console.print(f"  [bold yellow]Code block {i + 1}:[/bold yellow]")
                        console.print(Syntax(b, "python", theme="monokai", line_numbers=True))
                    so, se = repl.execute(b)
                    out += format_output(so, se) + "\n"
                    if self.verbose:
                        if so:
                            console.print(f"  [green]stdout: {so.strip()[:500]}[/green]")
                        if se:
                            console.print(f"  [red]stderr: {se.strip()[:300]}[/red]")
                messages.append({"role": "user", "content": f"Output:\n{out}\nContinue. FINAL() when done."})
            else:
                if self.verbose:
                    console.print(f"  [yellow]No code blocks found in response.[/yellow]")
                messages.append({"role": "user", "content": "You must write ```repl``` code or call FINAL(answer)."})

        self.root_llm_calls += 1
        messages.append({"role": "user", "content": "Max iterations. FINAL() now."})
        r = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
        self._track(r)
        t = r.choices[0].message.content
        if t is None:
            if self.verbose:
                console.print(f"    [yellow]LLM returned None content. Full response:[/yellow]")
                console.print(f"    [dim]{r.choices[0]}[/dim]")
            t = ""
        f = find_final_answer(t, repl.locals)
        return f if f else t

    def print_summary(self, elapsed):
        t = Table(title="Run Summary", style="bold")
        t.add_column("Metric", style="bold")
        t.add_column("Value", justify="right")
        t.add_row("Root LLM calls", str(self.root_llm_calls))
        t.add_row("Sub-LLM calls", str(self.sub_llm_calls))
        t.add_row("Total calls", str(self.root_llm_calls + self.sub_llm_calls))
        t.add_row("Input tokens", f"{self.total_input_tokens:,}")
        t.add_row("Output tokens", f"{self.total_output_tokens:,}")
        t.add_row("Wall time", f"{elapsed:.1f}s")
        console.print(t)


# =============================================================================
# Load policy documents
# =============================================================================

def load_policies() -> dict[str, str]:
    """Load all Norfolk Industries policy .md files as a dict of {filename: content}."""
    policies_dir = os.path.join(os.path.dirname(__file__), "sample_data", "policies")
    policies = {}
    for fname in sorted(os.listdir(policies_dir)):
        if fname.endswith(".md"):
            with open(os.path.join(policies_dir, fname)) as f:
                policies[fname] = f.read()
    return policies


policies = load_policies()
total_chars = sum(len(v) for v in policies.values())

console.print(Panel(
    f"[bold]Step 15: Real-World Cross-Document Policy Analysis[/bold]\n\n"
    f"Loaded {len(policies)} Norfolk Industries IT infrastructure policy documents\n"
    f"({total_chars:,} total chars, ~{total_chars // 4:,} tokens).\n\n"
    f"These policies cross-reference each other through shared governance bodies\n"
    f"(CAB, ISMS), shared roles (CISO, Head of IT Infrastructure Services),\n"
    f"and shared frameworks (ISO 27001, ITIL 4, NIST CSF, SOC 2, SOX).",
    style="cyan",
))

# Show document inventory
inv_table = Table(title="Document Inventory")
inv_table.add_column("#", justify="right")
inv_table.add_column("Filename")
inv_table.add_column("Chars", justify="right")
inv_table.add_column("Title")

for i, (fname, content) in enumerate(policies.items()):
    first_line = content.split("\n")[0].replace("#", "").strip()
    inv_table.add_row(str(i + 1), fname[:55], f"{len(content):,}", first_line[:55])

console.print(inv_table)
console.print()

console.print(Panel(
    f"[bold yellow]Note: Direct LLM comparison skipped[/bold yellow]\n\n"
    f"The 30 policy documents total {total_chars:,} chars (~{total_chars // 4:,} tokens).\n"
    f"Our model's context window is only {MAX_CONTEXT_TOKENS:,} tokens.\n"
    f"A direct LLM call would fail with a context-too-long error.\n"
    f"This is exactly why RLMs exist -- the RLM never sees all the context at once.",
    style="yellow",
))


# =============================================================================
# Query 1: Single-document retrieval
# =============================================================================

console.print(Panel("[bold]Query 1: Single-Document -- MFA Requirements[/bold]", style="yellow"))

Q1 = ("What are Norfolk Industries' requirements for multi-factor authentication (MFA)? "
      "Which systems require it, what types of authentication are mandated, "
      "and what exceptions exist?")

console.print(f"  [bold]Q:[/bold] {Q1}\n")

rlm1 = SimpleRLM(max_iterations=15)
start = time.time()
r_answer = rlm1.completion(Q1, context=policies)
r_time = time.time() - start
console.print(f"\n  [green]{str(r_answer)}[/green]")
rlm1.print_summary(r_time)
console.print()


# =============================================================================
# Query 2: Cross-reference query
# =============================================================================

console.print(Panel("[bold]Query 2: Cross-Reference -- Change Advisory Board (CAB)[/bold]", style="yellow"))

Q2 = ("Which Norfolk Industries policies reference the Change Advisory Board (CAB)? "
      "For each policy that references the CAB, explain what specific role or "
      "responsibility the CAB has in that policy's processes.")

console.print(f"  [bold]Q:[/bold] {Q2}\n")

rlm2 = SimpleRLM(max_iterations=20)
start = time.time()
r_answer2 = rlm2.completion(Q2, context=policies)
r_time2 = time.time() - start
console.print(f"\n  [green]{str(r_answer2)}[/green]")
rlm2.print_summary(r_time2)
console.print()


# =============================================================================
# Query 3: Multi-hop reasoning
# =============================================================================

console.print(Panel("[bold]Query 3: Multi-Hop -- Vulnerability Response Path[/bold]", style="yellow"))

Q3 = ("Scenario: A critical vulnerability (CVE with CVSS 9.8) is discovered on a "
      "production server in Norfolk Industries' Azure cloud environment. Trace the "
      "full response path by answering:\n"
      "1. Which policy governs vulnerability scanning and patching, and what are "
      "the required timelines for critical vulnerabilities?\n"
      "2. Which policy governs the emergency change needed to deploy the patch, "
      "and what approvals are required?\n"
      "3. If the vulnerability was actively exploited, which policy governs the "
      "incident response, and what is the severity classification?\n"
      "4. After resolution, which policy covers the post-incident review and "
      "root cause analysis?\n"
      "For each, cite the specific policy name and relevant section.")

console.print(f"  [bold]Q:[/bold] {Q3[:200]}...\n")

rlm3 = SimpleRLM(max_iterations=25)
start = time.time()
r_answer3 = rlm3.completion(Q3, context=policies)
r_time3 = time.time() - start
console.print(f"\n  [green]{str(r_answer3)}[/green]")
rlm3.print_summary(r_time3)
console.print()


# =============================================================================
# Bonus: Synthetic scale test
# =============================================================================

console.print(Panel("[bold]Bonus: Synthetic Scale Test (1000 policy excerpts)[/bold]", style="yellow"))
console.print("  Generating 1000 synthetic Norfolk Industries policy excerpts...\n")

TEMPLATES = [
    "Policy {pid}: All {role} must comply with {ref_policy} Section {sec} regarding {topic}.",
    "Policy {pid}: {role} must review {ref_policy} annually per {framework} requirements.",
    "Policy {pid}: Incidents related to {topic} must be escalated to the {role} within {hours} hours per SLO targets.",
    "Policy {pid}: Assets classified under {tier} in {ref_policy} must meet RPO of {rpo} and RTO of {rto}.",
    "Policy {pid}: {role} must ensure {topic} changes are approved by the CAB per {ref_policy} Section {sec}.",
    "Policy {pid}: OT/IT integration for {topic} must follow {ref_policy} segmentation controls.",
]
ROLES = ["CISO", "Head of IT Infrastructure Services", "IT Governance Manager",
         "Service Owner", "Platform Owner", "IT Operations Manager", "ITSM Process Owner"]
TOPICS = ["backup immutability", "privileged access", "endpoint hardening", "vulnerability scanning",
          "change enablement", "incident response", "disaster recovery", "capacity management",
          "network segmentation", "encryption key rotation", "audit evidence", "asset disposal"]
TIERS = ["Tier 1 (Mission Critical)", "Tier 2 (Business Critical)", "Tier 3 (Standard)", "Tier 4 (Non-Critical)"]
FRAMEWORKS = ["ISO 27001", "ITIL 4", "NIST CSF", "SOC 2", "COBIT 2019", "SOX"]

random.seed(42)
synthetic_policies = []
for i in range(1000):
    tmpl = random.choice(TEMPLATES)
    excerpt = tmpl.format(
        pid=f"NI-POL-{i:04d}",
        role=random.choice(ROLES),
        ref_policy=f"NI-POL-{random.randint(0, 999):04d}",
        sec=f"{random.randint(1, 12)}.{random.randint(1, 8)}",
        topic=random.choice(TOPICS),
        framework=random.choice(FRAMEWORKS),
        hours=random.choice([1, 2, 4, 8]),
        tier=random.choice(TIERS),
        rpo=random.choice(["15 min", "1 hour", "4 hours", "24 hours"]),
        rto=random.choice(["1 hour", "4 hours", "8 hours", "24 hours"]),
    )
    synthetic_policies.append(excerpt)

synthetic_text = "\n".join(synthetic_policies)
console.print(f"  Generated {len(synthetic_policies)} excerpts ({len(synthetic_text):,} chars)")
console.print(f"  Sample: [dim]{synthetic_policies[0]}[/dim]\n")

SQ = ("How many policies require CAB approval? List the first 5 policy IDs. "
      "Also, which policy ID is referenced the most by other policies?")

rlm_scale = SimpleRLM(max_iterations=10)
start = time.time()
scale_answer = rlm_scale.completion(SQ, context=synthetic_text)
scale_time = time.time() - start
console.print(f"  [green]{str(scale_answer)}[/green]")
rlm_scale.print_summary(scale_time)


# =============================================================================
# Summary
# =============================================================================

console.print(Panel(
    "[bold]Key Takeaways[/bold]\n\n"
    "1. A direct LLM call CANNOT process 30 policy docs (~1M chars) -- it far\n"
    "   exceeds the 20K token context window. The RLM handles it by never\n"
    "   seeing all context at once.\n"
    "2. The RLM uses code (regex, keyword search) to find relevant documents,\n"
    "   then passes only short excerpts to sub-LLM calls for interpretation.\n"
    "3. Multi-hop reasoning (Query 3) requires tracing across 4+ policies --\n"
    "   the RLM systematically searches and delegates to sub-LLMs.\n"
    "4. The synthetic scale test shows the RLM handles 1000+ entries by\n"
    "   using code (regex, counting) instead of reading everything.\n\n"
    "Next: Step 14 shows how the real rlm library does the same thing.",
    style="green",
))
