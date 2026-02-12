"""
Step 2: Experiencing Context Rot
================================

CONCEPT
-------
"Context rot" is the phenomenon where an LLM's ability to accurately recall and
reason about information degrades as the input context grows longer -- even when
the context fits within the model's window.

From the RLM paper (Zhang et al., 2025):
  "The effective context window of an LLM cannot be understood independently
   of the specific task.  More complex problems will exhibit degradation at
   even shorter lengths than simpler ones."

Anthropic defines context rot as: "[when] the number of tokens in the context
window increases, the model's ability to accurately recall information from
that context decreases."

WHY THIS MATTERS
----------------
This is THE core problem that Recursive Language Models solve.  If LLMs handled
arbitrarily long contexts perfectly, we wouldn't need RLMs.  Run this script
and watch the LLM struggle as context grows.

The key observation from the paper: on the OOLONG benchmark, even GPT-5 (with
272K token context) struggles on information-dense tasks at 132K tokens.  An
RLM using the smaller GPT-5-mini outperforms GPT-5 by >33% raw score.

WHAT WE DO
----------
1. Embed a known "SECRET_FACT" at different positions within increasingly large
   filler text.
2. Ask the LLM to retrieve it.
3. Watch accuracy degrade with context size.

Run:  python step02_context_rot.py
"""

import random
import time

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

SECRET_FACT = "The speed of light in a vacuum is exactly 299,792,458 meters per second."

FILLER_PARAGRAPHS = [
    "The history of bread-making dates back thousands of years to ancient Egypt. Early breads were flatbreads made from ground grains mixed with water and baked on hot stones. The discovery of leavening -- using yeast to make bread rise -- was likely accidental, but it transformed baking forever.",
    "Octopuses are remarkable creatures with three hearts, blue blood, and the ability to change color and texture in milliseconds. They are considered the most intelligent invertebrates, capable of solving puzzles, opening jars, and even escaping from aquariums.",
    "The Dead Sea, located between Jordan and Israel, is one of the saltiest bodies of water on Earth. Its salinity of about 34% makes it nearly ten times saltier than the ocean. This extreme salinity allows people to float effortlessly on its surface.",
    "Coffee was first cultivated in Ethiopia in the 9th century. Legend has it that a goat herder named Kaldi noticed his goats became energetic after eating berries from a certain tree. The practice of brewing coffee spread through the Arabian Peninsula and eventually to Europe.",
    "The Great Wall of China, contrary to popular belief, is not visible from space with the naked eye. However, it remains one of the most impressive construction projects in human history, stretching over 13,000 miles across northern China.",
    "Antarctica is the driest continent on Earth, technically classified as a desert. Despite being covered in ice, it receives very little precipitation. The interior of the continent is one of the driest places on the planet.",
    "The Fibonacci sequence appears throughout nature, from the spiral arrangement of sunflower seeds to the branching patterns of trees. This mathematical pattern, where each number is the sum of the two preceding ones, reflects fundamental principles of growth and efficiency.",
    "Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still perfectly edible. Honey's low moisture content and acidic pH create an inhospitable environment for bacteria and microorganisms.",
    "The Amazon River discharges more water into the ocean than the next seven largest rivers combined. During the wet season, its mouth can be over 300 miles wide, and it accounts for roughly 20% of all river water flowing into the world's oceans.",
    "Venus rotates in the opposite direction to most planets in our solar system. A day on Venus is longer than its year -- it takes 243 Earth days to rotate once on its axis but only 225 Earth days to orbit the Sun.",
    "The Mariana Trench is the deepest known part of the ocean, reaching a maximum depth of about 36,000 feet. The pressure at the bottom is over 1,000 times atmospheric pressure at sea level. Despite this extreme environment, life exists even at these depths.",
    "The human brain contains approximately 86 billion neurons, each connected to thousands of others. This creates a network of roughly 100 trillion connections. Despite representing only 2% of body weight, the brain consumes about 20% of the body's energy.",
    "The Sahara Desert was once a lush green savanna. Around 5,000-10,000 years ago, it received significantly more rainfall and was home to lakes, rivers, and diverse wildlife. Climate shifts gradually transformed it into the arid landscape we know today.",
    "Lightning strikes the Earth approximately 100 times every second, or about 8 million times per day. A single bolt can reach temperatures of 30,000 Kelvin -- five times hotter than the surface of the Sun.",
    "The oldest known living organism is a bristlecone pine tree named Methuselah, located in California's White Mountains. It is estimated to be over 4,850 years old, meaning it was already ancient when the Egyptian pyramids were being built.",
]


def build_context(num_paragraphs: int, needle_position: str = "middle") -> str:
    """Build a context block with a SECRET_FACT hidden at the specified position."""
    random.seed(42)
    paragraphs = [random.choice(FILLER_PARAGRAPHS) for _ in range(num_paragraphs)]
    if needle_position == "start":
        idx = 1
    elif needle_position == "end":
        idx = len(paragraphs) - 1
    else:
        idx = len(paragraphs) // 2
    paragraphs.insert(idx, f"SECRET_FACT: {SECRET_FACT}")
    return "\n\n".join(paragraphs)


def ask_with_context(context: str) -> tuple[str, bool, float]:
    """Ask the LLM to find the secret fact within the context."""
    start = time.time()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": (
                f"The following text contains a SECRET_FACT. "
                f"What is the secret fact? Quote it exactly.\n\n{context}"
            ),
        }],
        **model_kwargs(),
    )
    elapsed = time.time() - start
    answer = response.choices[0].message.content or ""
    found = "299,792,458" in answer
    return answer, found, elapsed


# ── Experiment 1: Needle position at different context sizes ────────────────
console.print(Panel(
    "[bold]Experiment 1: Needle-in-a-Haystack at Increasing Context Sizes[/bold]\n\n"
    "We embed SECRET_FACT at the start, middle, or end of increasingly\n"
    "large filler text, then ask the LLM to retrieve it.",
    style="cyan",
))

table = Table(title="Context Rot Experiment")
table.add_column("Paragraphs", justify="right")
table.add_column("~Chars", justify="right")
table.add_column("Position", justify="center")
table.add_column("Found?", justify="center")
table.add_column("Time (s)", justify="right")

sizes = [5, 15, 30, 60]
positions = ["start", "middle", "end"]

for size in sizes:
    for pos in positions:
        ctx = build_context(size, pos)
        answer, found, elapsed = ask_with_context(ctx)
        status = "[green]YES[/green]" if found else "[red]NO[/red]"
        table.add_row(str(size), f"{len(ctx):,}", pos, status, f"{elapsed:.1f}")

console.print(table)

# ── Experiment 2: Information density matters ──────────────────────────────
# The paper highlights that context rot depends on TASK COMPLEXITY, not just
# context length.  Simple retrieval (needle-in-haystack) is easier than
# tasks requiring reasoning over many pieces of information.

console.print(Panel(
    "[bold]Experiment 2: Task Complexity Matters[/bold]\n\n"
    "The paper found that simpler tasks (find one needle) degrade slowly,\n"
    "while information-dense tasks (reason over ALL lines) degrade fast.\n"
    "Let's test a slightly harder task: counting specific items in context.",
    style="cyan",
))

ITEMS = [
    "The red fox jumped over the lazy dog.",
    "A blue whale surfaced near the coast.",
    "The red cardinal perched on the fence.",
    "Green parrots flew over the marketplace.",
    "The red sunset painted the sky beautifully.",
    "A yellow taxi sped through the intersection.",
    "The blue jay sang from the oak tree.",
    "Red roses bloomed in the garden path.",
    "The green frog sat on a lily pad.",
    "A red fire truck raced down the street.",
]


def build_counting_context(num_items: int) -> tuple[str, int]:
    """Build a context where the LLM must count 'red' items among filler."""
    random.seed(42)
    all_items = [random.choice(ITEMS) for _ in range(num_items)]
    red_count = sum(1 for item in all_items if "red" in item.lower())
    return "\n".join(all_items), red_count


count_table = Table(title="Counting Task (information-dense)")
count_table.add_column("Items", justify="right")
count_table.add_column("Actual Red", justify="right")
count_table.add_column("LLM Answer", justify="center")
count_table.add_column("Correct?", justify="center")

for num_items in [10, 30, 60, 100]:
    ctx, actual_red = build_counting_context(num_items)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role": "user",
            "content": (
                f"Count exactly how many of the following items contain the word 'red'. "
                f"Reply with just the number.\n\n{ctx}"
            ),
        }],
        **model_kwargs(),
    )
    llm_answer = response.choices[0].message.content.strip()
    try:
        llm_num = int("".join(c for c in llm_answer if c.isdigit()))
        correct = llm_num == actual_red
    except ValueError:
        correct = False
    status = "[green]YES[/green]" if correct else "[red]NO[/red]"
    count_table.add_row(str(num_items), str(actual_red), llm_answer, status)

console.print(count_table)

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. Even when context fits in the model's window, accuracy degrades with size.
# 2. Needle-in-haystack (simple retrieval) is relatively easy for modern LLMs.
# 3. Information-DENSE tasks (counting, aggregation) degrade much faster.
# 4. This is exactly what the RLM paper observed on OOLONG:
#    - GPT-5 struggles on information-dense tasks at 132K tokens
#    - RLM(GPT-5-mini) outperforms GPT-5 by 2x on those same tasks
#
# The question: how do we fix this?
#
# NEXT: Step 3 tries three naive approaches.  Spoiler: they all have
# fundamental limitations that lead us to the RLM architecture.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] Context rot is real and depends on task complexity.\n"
    "Simple retrieval holds up longer; information-dense tasks degrade fast.\n\n"
    "The RLM paper showed this on OOLONG: GPT-5 with 272K context window\n"
    "scores ~30 on information-dense tasks, while RLM(GPT-5-mini) scores ~64.",
    style="green",
))
