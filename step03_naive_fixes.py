"""
Step 3: Naive Fixes -- Why We Need RLMs
=======================================

CONCEPT
-------
Before inventing something new, let's try the obvious solutions to context rot:

  1. CHUNKING: Split the context into pieces, ask the LLM about each chunk.
     Problem: The answer might span chunk boundaries.

  2. SUMMARIZATION: Summarize the context, then ask questions about the summary.
     Problem: Summaries lose detail. Fine-grained info is discarded.

  3. KEYWORD SEARCH (grep): Search for relevant keywords, extract matching lines.
     Problem: Can't handle SEMANTIC queries (e.g., "which items are about animals?").

Each approach partially works but has a fundamental blind spot.  We need a system
where the LLM itself decides HOW to decompose and interact with the context.

From the RLM paper:
  "Unlike prior agentic methods that rigidly define these workflow patterns,
   RLMs defer these decisions entirely to the language model."

WHY THIS MATTERS
----------------
This step makes the case for RLMs by showing that static, pre-determined
strategies for handling long context all fail in different ways.  The insight
is that the LLM should decide its own strategy at runtime.

Run:  python step03_naive_fixes.py
"""

import re

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def llm_call(prompt: str, system: str = "You are a helpful assistant. Be concise.") -> str:
    """The atomic LLM operation from Step 1."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        **model_kwargs(),
    )
    return response.choices[0].message.content


# ── Sample data: a multi-section article ────────────────────────────────────
# The answer to our question requires combining info from TWO sections.

ARTICLE = """
### Section 1: Early Career
Dr. Elena Vasquez began her career at the University of Buenos Aires in 1987,
where she studied molecular biology. She published her first paper on protein
folding in 1990, which was largely ignored by the scientific community.

### Section 2: The Breakthrough
In 1995, while working at a small lab in Zurich, Vasquez discovered a novel
enzyme she named "Catalase-7". This enzyme could break down certain toxins
200 times faster than any known biological catalyst. She published these
findings in Nature, catapulting her to scientific fame.

### Section 3: Awards and Recognition
Vasquez received the Lasker Award in 2001 for her work on Catalase-7. She was
also shortlisted for the Nobel Prize in Chemistry in 2003 but did not win.
She joined MIT as a full professor in 2004.

### Section 4: Later Work
At MIT, Vasquez shifted her focus to applications of Catalase-7 in
environmental cleanup. Her team demonstrated that the enzyme could neutralize
industrial pollutants in water supplies. By 2010, three water treatment plants
in South America were using her technology.

### Section 5: Legacy
Vasquez retired in 2018 but continues to advise graduate students. Her total
publication count stands at 147 papers, with over 12,000 citations. The
Catalase-7 enzyme is now used in 15 countries for water treatment.
""".strip()

QUESTION = ("How many years passed between Vasquez's first paper and the "
            "Lasker Award, and what was the award for?")

# The answer requires Section 1 (first paper in 1990) + Section 3 (Lasker in 2001)
# = 11 years, for her work on Catalase-7.

console.print(Panel(
    f"[bold]Question:[/bold] {QUESTION}\n\n"
    f"[dim]The answer requires combining Section 1 (first paper: 1990) with\n"
    f"Section 3 (Lasker Award: 2001, for Catalase-7). Answer: 11 years.[/dim]",
    style="cyan",
))


# ── Approach 1: Chunking ───────────────────────────────────────────────────
console.print(Panel("[bold]Approach 1: Manual Chunking[/bold]", style="yellow"))
console.print("  Split the article into chunks, ask each chunk about the question.\n")

sections = re.split(r"### ", ARTICLE)
sections = [s.strip() for s in sections if s.strip()]

chunk_table = Table(title="Chunking Results")
chunk_table.add_column("Chunk", style="bold")
chunk_table.add_column("LLM Response")

chunk_answers = []
for i, section in enumerate(sections):
    answer = llm_call(
        f"Based ONLY on this text, answer: {QUESTION}\n\nText:\n{section}\n\n"
        f"If the text doesn't contain enough info, say 'insufficient information'."
    )
    chunk_answers.append(answer)
    chunk_table.add_row(f"Section {i + 1}", answer[:120] + "..." if len(answer) > 120 else answer)

console.print(chunk_table)
console.print(
    "  [red]Problem:[/red] No single chunk has BOTH pieces of information.\n"
    "  The answer spans chunk boundaries. We'd need to combine results.\n"
)


# ── Approach 2: Summarize then ask ─────────────────────────────────────────
console.print(Panel("[bold]Approach 2: Summarize-Then-Ask[/bold]", style="yellow"))
console.print("  Summarize the article first, then ask the question.\n")

summary = llm_call(
    f"Summarize the following article in 3-4 sentences:\n\n{ARTICLE}"
)
console.print(f"  [dim]Summary:[/dim] {summary}\n")

answer_from_summary = llm_call(
    f"Based on this summary, answer: {QUESTION}\n\nSummary:\n{summary}"
)
console.print(f"  [bold]Answer:[/bold] {answer_from_summary}\n")
console.print(
    "  [red]Problem:[/red] Summaries lose fine-grained detail.\n"
    "  If the summary didn't mention '1990' or '2001' specifically,\n"
    "  the LLM can't compute '11 years'. Information is lossy.\n"
)


# ── Approach 3: Keyword Search (grep) ──────────────────────────────────────
console.print(Panel("[bold]Approach 3: Keyword Search (Grep)[/bold]", style="yellow"))
console.print("  Search for keywords from the question, extract matching lines.\n")

keywords = ["first paper", "Lasker", "award"]
matched_lines = []
for line in ARTICLE.split("\n"):
    if any(kw.lower() in line.lower() for kw in keywords):
        matched_lines.append(line.strip())

console.print(f"  Keywords searched: {keywords}")
console.print(f"  Matched {len(matched_lines)} lines:")
for line in matched_lines:
    console.print(f"    [dim]{line}[/dim]")

if matched_lines:
    grep_context = "\n".join(matched_lines)
    answer_from_grep = llm_call(
        f"Based on these lines, answer: {QUESTION}\n\nLines:\n{grep_context}"
    )
    console.print(f"\n  [bold]Answer:[/bold] {answer_from_grep}\n")
else:
    console.print("  No lines matched!")

console.print(
    "  [red]Problem:[/red] Grep can't handle SEMANTIC queries.\n"
    "  'Which sections discuss applications?' has no keyword to grep for.\n"
    "  Also, grep misses context surrounding matched lines.\n"
)


# ── Approach 4: The RLM intuition ─────────────────────────────────────────
console.print(Panel("[bold]The RLM Intuition[/bold]", style="green"))
console.print(
    "  What if the LLM itself could decide HOW to interact with the context?\n"
    "  \n"
    "  Instead of us picking a strategy (chunk/summarize/grep),\n"
    "  we give the LLM a CODE ENVIRONMENT with the context as a variable,\n"
    "  and let it:\n"
    "    1. Peek at the context to understand its structure\n"
    "    2. Write code to extract relevant parts\n"
    "    3. Call itself recursively on smaller pieces\n"
    "    4. Aggregate results and return a final answer\n"
    "  \n"
    "  This is the core idea behind Recursive Language Models.\n"
    "  \n"
    "  From the paper:\n"
    '    "RLMs defer the choice of context management to the LM / REPL\n'
    '     environment... the LLM has full control to view and transform\n'
    '     this data, as well as ask sub-queries to a recursive LM."\n'
)

# ── Quick demo: what an RLM *would* do ────────────────────────────────────
console.print(Panel("[bold]Preview: What an RLM Would Do[/bold]", style="green"))
console.print("  If the LLM had access to code + recursive calls, it might:\n")
console.print('  [dim]```python')
console.print('  # 1. Peek at the context')
console.print('  print(context[:500])')
console.print('  # -> sees it\'s a multi-section article')
console.print('  ')
console.print('  # 2. Split by section headers')
console.print("  sections = re.split(r'### ', context)")
console.print('  ')
console.print('  # 3. Ask a sub-LLM about each section')
console.print('  for section in sections:')
console.print('      info = llm_query(f"Extract dates and awards from: {section}")')
console.print('      results.append(info)')
console.print('  ')
console.print('  # 4. Aggregate and answer')
console.print('  final = llm_query(f"Using {results}, answer: {question}")')
console.print('  ```[/dim]\n')
console.print("  This is exactly what we build in Steps 4-13.\n")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. Chunking breaks at boundaries -- answers that span chunks are missed.
# 2. Summarization is lossy -- fine-grained details are discarded.
# 3. Grep can't handle semantic queries -- only literal keyword matching.
# 4. The LLM should decide its OWN decomposition strategy at runtime.
# 5. This requires: a code environment + the context as a variable +
#    the ability to recursively call the LLM from code.
#
# NEXT: Step 4 builds the first piece: a safe Python exec() sandbox.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] Static strategies (chunk/summarize/grep) each fail.\n"
    "The LLM should decide its own strategy. This requires:\n"
    "  1. A code execution environment (Step 4)\n"
    "  2. The LLM writing code to interact with context (Steps 5-6)\n"
    "  3. Recursive self-calls from within code (Step 7)",
    style="green",
))
