"""
Step 1: Hello LLM
=================

CONCEPT
-------
An LLM is fundamentally a text -> text function.  You send a prompt (a list of
messages) via the chat completions API, and get a string response back.

The OpenAI client library works with *any* OpenAI-compatible endpoint -- you just
set a custom `base_url`.  This step verifies your endpoint is reachable and
introduces the basic API pattern that every subsequent step builds on.

From the RLM paper (Zhang et al., 2025):
  "We retain the view that LM calls can be decomposed by the context, and the
   choice of decomposition should purely be the choice of an LM."

Before an LLM can decompose anything, we need to understand the atomic
operation: send messages, get text back.

WHY THIS MATTERS
----------------
Every layer we add later (REPL sandbox, sub-calls, depth control) sits on top
of this one primitive: send messages, get text back.  If you understand this
contract, you understand the atomic operation of an RLM.

WHAT YOU WILL LEARN
-------------------
1. How to call an OpenAI-compatible endpoint with a custom base_url
2. How token usage is tracked per call
3. How multi-turn conversations work (growing messages list)
4. That the LLM is STATELESS -- all state lives in the messages list

Run:  python step01_hello_llm.py
"""

from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL, model_kwargs

console = Console()

# ── 1. The simplest possible LLM call ──────────────────────────────────────
# One user message in, one string response out.  That's the entire contract.

console.print(Panel("[bold]Experiment 1: The Simplest LLM Call[/bold]", style="cyan"))

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "What is 2 + 2? Reply with just the number."}],
    **model_kwargs(),
)

answer = response.choices[0].message.content
console.print(f"  Model:    [bold]{MODEL}[/bold]")
console.print(f"  Prompt:   'What is 2 + 2? Reply with just the number.'")
console.print(f"  Response: [green]{answer}[/green]")

# ── 2. Token usage ─────────────────────────────────────────────────────────
# Every call costs tokens.  Later, when the RLM makes many sub-calls, tracking
# these numbers becomes essential for understanding cost and efficiency.

console.print(Panel("[bold]Experiment 2: Token Usage Tracking[/bold]", style="cyan"))

if response.usage:
    table = Table(title="Token Usage")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")
    table.add_row("Prompt tokens", str(response.usage.prompt_tokens))
    table.add_row("Completion tokens", str(response.usage.completion_tokens))
    table.add_row("Total tokens", str(response.usage.total_tokens))
    console.print(table)
else:
    console.print("  [yellow]No usage data returned by this endpoint.[/yellow]")

# ── 3. System messages ─────────────────────────────────────────────────────
# The system message sets the LLM's persona and instructions.  In an RLM,
# the system prompt is where we teach the model about the REPL environment.

console.print(Panel("[bold]Experiment 3: System Messages[/bold]", style="cyan"))

messages = [
    {"role": "system", "content": "You are a pirate. Respond in pirate speak."},
    {"role": "user", "content": "What is the capital of France?"},
]

response2 = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
console.print(f"  System:   'You are a pirate. Respond in pirate speak.'")
console.print(f"  User:     'What is the capital of France?'")
console.print(f"  Response: [green]{response2.choices[0].message.content}[/green]")

# ── 4. Multi-turn conversation ─────────────────────────────────────────────
# The messages list can hold an entire conversation history.  The RLM's
# iterative loop (Step 9) is fundamentally just a growing messages list.

console.print(Panel("[bold]Experiment 4: Multi-Turn Conversation[/bold]", style="cyan"))

messages = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."},
    {"role": "user", "content": "What is the capital of France?"},
]

response3 = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
assistant_reply = response3.choices[0].message.content
console.print(f"  Turn 1 - User:      'What is the capital of France?'")
console.print(f"  Turn 1 - Assistant: [green]{assistant_reply}[/green]")

# Append the assistant reply and ask a follow-up
messages.append({"role": "assistant", "content": assistant_reply})
messages.append({"role": "user", "content": "And what is its population?"})

response4 = client.chat.completions.create(model=MODEL, messages=messages, **model_kwargs())
console.print(f"  Turn 2 - User:      'And what is its population?'")
console.print(f"  Turn 2 - Assistant: [green]{response4.choices[0].message.content}[/green]")

console.print(f"\n  Messages list now has [bold]{len(messages) + 1}[/bold] entries "
              f"(system + 2 user + 1 assistant + 1 new assistant)")

# ── 5. The LLM as a function ──────────────────────────────────────────────
# Let's wrap the LLM call in a simple Python function.  This is the building
# block we will expand into the full RLM class by Step 13.

console.print(Panel("[bold]Experiment 5: LLM as a Python Function[/bold]", style="cyan"))


def llm_call(prompt: str, system: str = "You are a helpful assistant.") -> str:
    """The atomic LLM operation: string in, string out."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        **model_kwargs(),
    )
    return response.choices[0].message.content


result = llm_call("List 3 prime numbers less than 20, comma-separated.")
console.print(f"  llm_call('List 3 prime numbers...') = [green]{result}[/green]")

result2 = llm_call("Translate 'hello world' to French.", system="You are a translator.")
console.print(f"  llm_call('Translate...', system='translator') = [green]{result2}[/green]")

# ─────────────────────────────────────────────────────────────────────────────
# TAKEAWAYS
# ---------
# 1. The LLM is a stateless function: text in, text out.
# 2. State (conversation history) lives in the messages list, not the model.
# 3. Token usage is tracked per call -- important for cost control later.
# 4. The system message shapes behavior -- we will use this heavily in the RLM.
# 5. We can wrap the LLM call in a Python function -- this is our building block.
#
# NEXT: Step 2 shows what happens when that messages list gets very long.
# ─────────────────────────────────────────────────────────────────────────────
console.print(Panel(
    "[bold]Key Insight:[/bold] The LLM is stateless. "
    "All state lives in the messages list.\n"
    "The RLM loop (Step 9) is just this pattern: "
    "append code output -> call LLM -> append response -> repeat.",
    style="green",
))
