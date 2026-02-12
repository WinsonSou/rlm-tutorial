"""
Step 17: Async and Streaming
=============================

CONCEPT
-------
Step 13's SimpleRLM uses ThreadPoolExecutor for concurrent sub-LLM calls.
The production rlm library uses asyncio. This step shows both approaches
side-by-side, plus streaming output for real-time visibility.

Part A: Async batched calls using asyncio + AsyncOpenAI
Part B: Streaming output -- see tokens arrive in real-time
Part C: Comparison -- sync vs async vs streaming on the same task

From the paper:
  "RLMs without asynchronous LM calls are slow. We implemented all sub-LM
   queries naively as blocking / sequential calls, which caused our RLM
   experiments to be slow."

WHY THIS MATTERS
----------------
In real-world use, sub-LLM calls dominate RLM latency. Async execution can
cut wall time dramatically when you have 5-10+ independent sub-calls.
Streaming gives users real-time feedback during long RLM runs.

Run:  python step17_async_streaming.py
"""

import asyncio
import io
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from openai import AsyncOpenAI, OpenAI
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()
sync_client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
async_client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)


# =============================================================================
# Part A: Async batched calls
# =============================================================================

console.print(Panel("[bold]Part A: Async vs Sync Batched Calls[/bold]", style="cyan"))


# ── Sync approach (ThreadPoolExecutor from Step 13) ────────────────────────

def sync_llm_call(prompt: str) -> str:
    """Single synchronous LLM call."""
    r = sync_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": "Be concise."},
                  {"role": "user", "content": prompt}],
        **model_kwargs(),
    )
    return r.choices[0].message.content or ""


def sync_batched(prompts: list[str]) -> list[str]:
    """Concurrent calls using ThreadPoolExecutor."""
    results = [None] * len(prompts)
    def call(idx, prompt):
        return idx, sync_llm_call(prompt)
    with ThreadPoolExecutor(max_workers=min(len(prompts), 5)) as ex:
        futs = {ex.submit(call, i, p): i for i, p in enumerate(prompts)}
        for f in as_completed(futs):
            idx, result = f.result()
            results[idx] = result
    return results


# ── Async approach (asyncio + AsyncOpenAI) ─────────────────────────────────

async def async_llm_call(prompt: str) -> str:
    """Single async LLM call."""
    r = await async_client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": "Be concise."},
                  {"role": "user", "content": prompt}],
        **model_kwargs(),
    )
    return r.choices[0].message.content or ""


async def async_batched(prompts: list[str]) -> list[str]:
    """Concurrent calls using asyncio.gather."""
    tasks = [async_llm_call(p) for p in prompts]
    return await asyncio.gather(*tasks)


# ── Sequential baseline ──────────────────────────────────────────────────

def sequential_calls(prompts: list[str]) -> list[str]:
    """Sequential calls for baseline comparison."""
    return [sync_llm_call(p) for p in prompts]


# ── Benchmark ──────────────────────────────────────────────────────────────

PROMPTS = [
    "What year was the Eiffel Tower completed? Reply in one sentence.",
    "Who invented the telephone? Reply in one sentence.",
    "What is the chemical symbol for gold? Reply in one word.",
    "Name the largest planet in our solar system. Reply in one word.",
    "What is the boiling point of water in Celsius? Reply with just the number.",
    "Who painted the Mona Lisa? Reply in one or two words.",
    "What is the capital of Japan? Reply in one word.",
    "How many continents are there? Reply with just the number.",
    "What year did World War II end? Reply with just the year.",
    "What is the speed of light in km/s (approx)? Reply with just the number.",
]

console.print(f"  Benchmarking {len(PROMPTS)} concurrent LLM calls...\n")

# Sequential
console.print("  [dim]Running sequential...[/dim]")
start = time.time()
seq_results = sequential_calls(PROMPTS)
seq_time = time.time() - start
console.print(f"  Sequential: {seq_time:.1f}s")

# ThreadPool
console.print("  [dim]Running ThreadPoolExecutor...[/dim]")
start = time.time()
tp_results = sync_batched(PROMPTS)
tp_time = time.time() - start
console.print(f"  ThreadPool: {tp_time:.1f}s")

# Async
console.print("  [dim]Running asyncio...[/dim]")
start = time.time()
async_results = asyncio.run(async_batched(PROMPTS))
async_time = time.time() - start
console.print(f"  Asyncio:    {async_time:.1f}s\n")

bench_table = Table(title="Batched Call Benchmark (10 prompts)")
bench_table.add_column("Method", style="bold")
bench_table.add_column("Wall Time", justify="right")
bench_table.add_column("Speedup vs Sequential", justify="right")
bench_table.add_row("Sequential", f"{seq_time:.1f}s", "1.0x")
bench_table.add_row("ThreadPoolExecutor", f"{tp_time:.1f}s",
                     f"{seq_time / tp_time:.1f}x" if tp_time > 0 else "N/A")
bench_table.add_row("asyncio.gather", f"{async_time:.1f}s",
                     f"{seq_time / async_time:.1f}x" if async_time > 0 else "N/A")
console.print(bench_table)

# Show sample results
console.print(f"\n  Sample async result: [green]{async_results[0]}[/green]\n")


# =============================================================================
# Part B: Streaming output
# =============================================================================

console.print(Panel("[bold]Part B: Streaming Output[/bold]", style="cyan"))
console.print("  Watch tokens arrive in real-time as the LLM responds.\n")


def streaming_llm_call(prompt: str, system: str = "You are a helpful assistant.") -> str:
    """LLM call with streaming -- prints tokens as they arrive."""
    stream = sync_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        stream=True,
        **model_kwargs(),
    )

    full_response = ""
    console.print("  [dim]Streaming:[/dim] ", end="")
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_response += token
            console.print(f"[green]{token}[/green]", end="")
    console.print()  # newline
    return full_response


# Demo streaming
console.print("  [bold]Demo: Streaming a response[/bold]\n")
stream_result = streaming_llm_call("Explain what a Recursive Language Model is in 3 sentences.")
console.print(f"\n  Full response captured: {len(stream_result)} chars\n")


# ── Streaming with code block detection ────────────────────────────────────

console.print(Panel("[bold]Streaming + Code Block Detection[/bold]", style="cyan"))
console.print("  Parse ```repl``` blocks from a streaming response in real-time.\n")


def streaming_with_code_detection(prompt: str, system: str) -> tuple[str, list[str]]:
    """Stream response and detect code blocks as they complete."""
    stream = sync_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        stream=True,
        **model_kwargs(),
    )

    full_response = ""
    in_code_block = False
    current_block = ""
    completed_blocks = []

    for chunk in stream:
        if not chunk.choices or not chunk.choices[0].delta.content:
            continue
        token = chunk.choices[0].delta.content
        full_response += token

        # Detect code block boundaries
        if "```repl" in (full_response[-20:]) and not in_code_block:
            in_code_block = True
            current_block = ""
            console.print("  [cyan][CODE BLOCK START][/cyan]")
        elif in_code_block and "```" in token and not token.strip().startswith("```repl"):
            # Check if this is the closing ```
            after_open = full_response.split("```repl")[-1]
            if after_open.rstrip().endswith("```"):
                in_code_block = False
                # Extract the block content
                block = after_open.rsplit("```", 1)[0].strip()
                if block:
                    completed_blocks.append(block)
                    console.print(f"  [cyan][CODE BLOCK END - {len(block)} chars][/cyan]")
        elif in_code_block:
            current_block += token
            console.print(f"[yellow]{token}[/yellow]", end="")
        else:
            console.print(f"[dim]{token}[/dim]", end="")

    console.print()
    return full_response, completed_blocks


system = """You have a Python REPL. Write code in ```repl``` blocks. Use print() to show results.
Answer the question using code."""

console.print("  [bold]Demo: Stream + detect code blocks[/bold]\n")
text, blocks = streaming_with_code_detection(
    "Calculate the sum of all prime numbers less than 50. Show your work.",
    system,
)
console.print(f"\n  Detected {len(blocks)} code block(s)")
for i, b in enumerate(blocks):
    console.print(f"  Block {i}: [green]{b[:100]}...[/green]" if len(b) > 100 else f"  Block {i}: [green]{b}[/green]")
console.print()


# =============================================================================
# Part C: Comparison on a real task
# =============================================================================

console.print(Panel("[bold]Part C: Full Comparison on a Real Task[/bold]", style="cyan"))

# We compare 3 approaches to answering 5 independent sub-questions

SUB_QUESTIONS = [
    "What was the first antibiotic discovered, and who discovered it?",
    "What was the first nuclear weapon test called, and when did it happen?",
    "When was the Human Genome Project completed?",
    "Who was the first person to walk on the Moon, and when?",
    "What was the first message sent over ARPANET?",
]

console.print(f"  Task: Answer {len(SUB_QUESTIONS)} independent questions concurrently.\n")

# Sequential
console.print("  [dim]Sequential...[/dim]")
start = time.time()
seq_answers = [sync_llm_call(q) for q in SUB_QUESTIONS]
seq_t = time.time() - start

# ThreadPool
console.print("  [dim]ThreadPool...[/dim]")
start = time.time()
tp_answers = sync_batched(SUB_QUESTIONS)
tp_t = time.time() - start

# Async
console.print("  [dim]Async...[/dim]")
start = time.time()
a_answers = asyncio.run(async_batched(SUB_QUESTIONS))
a_t = time.time() - start

comp_table = Table(title="Real Task Comparison (5 sub-questions)")
comp_table.add_column("Method", style="bold")
comp_table.add_column("Wall Time", justify="right")
comp_table.add_column("Speedup", justify="right")
comp_table.add_column("Sample Answer")
comp_table.add_row("Sequential", f"{seq_t:.1f}s", "1.0x", seq_answers[0][:80])
comp_table.add_row("ThreadPool", f"{tp_t:.1f}s",
                    f"{seq_t / tp_t:.1f}x" if tp_t > 0 else "N/A", tp_answers[0][:80])
comp_table.add_row("asyncio", f"{a_t:.1f}s",
                    f"{seq_t / a_t:.1f}x" if a_t > 0 else "N/A", a_answers[0][:80])
console.print(comp_table)


# =============================================================================
# Summary
# =============================================================================

console.print(Panel(
    "[bold]Key Takeaways[/bold]\n\n"
    "1. [bold]asyncio + AsyncOpenAI[/bold] is the cleanest way to do concurrent sub-calls.\n"
    "   The real rlm library uses this pattern via acompletion().\n\n"
    "2. [bold]ThreadPoolExecutor[/bold] works well and is simpler if you don't want async.\n"
    "   Our SimpleRLM uses this approach.\n\n"
    "3. [bold]Streaming[/bold] gives real-time visibility into LLM output.\n"
    "   Useful for demos and interactive sessions.\n"
    "   Code block detection from streams requires careful boundary tracking.\n\n"
    "4. Both async methods give roughly the same speedup over sequential.\n"
    "   The bottleneck is API latency, not Python overhead.\n\n"
    "5. For an RLM with 10+ sub-calls per iteration, async can cut\n"
    "   total wall time by 3-5x or more.",
    style="green",
))
