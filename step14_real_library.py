"""
Step 14: Running the Real RLM Library
=======================================

CONCEPT
-------
Now that you've built an RLM from scratch and understand every piece, let's
use Alex Zhang's production `rlm` library on the same policy documents.

This step shows:
1. How your SimpleRLM components map to the real library's classes
2. The architectural differences (socket-based LM handler)
3. Actually running the real library on Norfolk Industries policy docs

MAPPING
-------
  Your code                    ->  Real library
  ────────────────────────────────────────────────
  SimpleREPL                   ->  rlm.environments.local_repl.LocalREPL
  SimpleRLM                    ->  rlm.core.rlm.RLM
  llm_query()                  ->  Socket-based LMHandler + send_lm_request()
  find_code_blocks()           ->  rlm.utils.parsing.find_code_blocks()
  find_final_answer()          ->  rlm.utils.parsing.find_final_answer()
  RLM_SYSTEM_PROMPT            ->  rlm.utils.prompts.RLM_SYSTEM_PROMPT
  config.py (BASE_URL, etc.)   ->  OpenAIClient(base_url=..., api_key=...)

PREREQUISITE
------------
Install the real library from the repo root:
  uv pip install -e .

Run:  python step14_real_library.py
"""

import os
import time

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from config import API_KEY, BASE_URL, MODEL

console = Console()


# =============================================================================
# Part 1: Mapping your code to the real library
# =============================================================================

console.print(Panel("[bold]Part 1: How Your Code Maps to the Real Library[/bold]", style="cyan"))

mapping_table = Table(title="SimpleRLM -> rlm Library Mapping")
mapping_table.add_column("Your Code (Steps 1-13)", style="bold")
mapping_table.add_column("Real Library", style="bold cyan")
mapping_table.add_column("Key Difference")

mapping_table.add_row(
    "SimpleREPL",
    "LocalREPL",
    "Real version uses temp dirs, threading locks, file-based context loading"
)
mapping_table.add_row(
    "SimpleRLM",
    "RLM",
    "Real version supports multiple backends, environments, persistence"
)
mapping_table.add_row(
    "llm_query() direct call",
    "Socket-based LMHandler",
    "Real version uses TCP sockets (4-byte length prefix + JSON)"
)
mapping_table.add_row(
    "find_code_blocks()",
    "rlm.utils.parsing.find_code_blocks()",
    "Nearly identical regex-based extraction"
)
mapping_table.add_row(
    "find_final_answer()",
    "rlm.utils.parsing.find_final_answer()",
    "Real version also checks REPL environment object"
)
mapping_table.add_row(
    "RLM_SYSTEM_PROMPT",
    "rlm.utils.prompts.RLM_SYSTEM_PROMPT",
    "Real prompt is more detailed with chunking examples"
)
mapping_table.add_row(
    "config.py",
    "OpenAIClient(base_url=..., api_key=...)",
    "Real version uses BaseLM + client registry"
)
mapping_table.add_row(
    "ThreadPoolExecutor (batched)",
    "asyncio + acompletion()",
    "Real version uses async for concurrent sub-calls"
)

console.print(mapping_table)
console.print()


# =============================================================================
# Part 2: Architecture comparison
# =============================================================================

console.print(Panel("[bold]Part 2: Architecture Differences[/bold]", style="cyan"))

console.print("""
  [bold]Your SimpleRLM (Steps 1-13):[/bold]
  ┌──────────────┐
  │  SimpleRLM   │──── llm_query() ──── direct OpenAI call
  │  (depth=0)   │
  │  ┌────────┐  │
  │  │  REPL  │  │
  │  └────────┘  │
  └──────────────┘

  [bold]Real RLM library:[/bold]
  ┌──────────────┐       TCP Socket        ┌──────────────┐
  │     RLM      │◄────────────────────────►│  LMHandler   │
  │  (main)      │                          │  (TCP server) │
  └──────────────┘                          └──────────────┘
         │                                         ▲
         ▼                                         │
  ┌──────────────┐       TCP Socket                │
  │  LocalREPL   │────────────────────────────────┘
  │  (exec code) │  llm_query() -> socket request
  └──────────────┘

  The real library uses a TCP socket server (LMHandler) so that:
  - Isolated environments (Modal, Docker, E2B) can reach the LLM
  - Multiple concurrent requests are handled via threading
  - The protocol is: 4-byte big-endian length + JSON payload
""")


# =============================================================================
# Part 3: Running the real library on Norfolk Industries policies
# =============================================================================

console.print(Panel("[bold]Part 3: Running the Real RLM Library[/bold]", style="cyan"))

# Load the Norfolk Industries policy documents
policies_dir = os.path.join(os.path.dirname(__file__), "sample_data", "policies")
policies = {}
for fname in sorted(os.listdir(policies_dir)):
    if fname.endswith(".md"):
        with open(os.path.join(policies_dir, fname)) as f:
            policies[fname] = f.read()

total_chars = sum(len(v) for v in policies.values())
console.print(f"  Loaded {len(policies)} policy documents ({total_chars:,} chars)\n")

# The query -- same as Step 15 Q1 for comparison
QUERY = ("What are Norfolk Industries' requirements for multi-factor authentication (MFA)? "
         "Which systems require it and what exceptions exist?")

try:
    from rlm import RLM

    console.print("  [green]rlm library is installed![/green]\n")

    rlm = RLM(
        backend="openai",
        backend_kwargs={
            "model_name": MODEL,
            "api_key": API_KEY,
            "base_url": BASE_URL,
        },
        environment="local",
        max_depth=1,
        max_iterations=15,
        verbose=True,
    )

    console.print(f"  [bold]Query:[/bold] {QUERY}\n")
    console.print("  [bold]Running the real RLM library...[/bold]\n")

    start = time.time()
    result = rlm.completion(policies, root_prompt=QUERY)
    elapsed = time.time() - start

    console.print(f"\n  [bold]Answer:[/bold]")
    console.print(f"  [green]{result.response}[/green]\n")
    console.print(f"  [dim]Execution time: {elapsed:.1f}s[/dim]")

    if result.usage_summary:
        usage_dict = result.usage_summary.to_dict()
        usage_table = Table(title="Real RLM Usage Summary")
        usage_table.add_column("Metric", style="bold")
        usage_table.add_column("Value", justify="right")
        for model_name, model_usage in usage_dict.get("model_usage_summaries", {}).items():
            usage_table.add_row(f"{model_name} - calls", str(model_usage.get("total_calls", 0)))
            usage_table.add_row(f"{model_name} - input tokens", f"{model_usage.get('total_input_tokens', 0):,}")
            usage_table.add_row(f"{model_name} - output tokens", f"{model_usage.get('total_output_tokens', 0):,}")
        console.print(usage_table)

except ImportError:
    console.print("  [yellow]The rlm library is not installed.[/yellow]")
    console.print("  Install it from the repo root: [bold]uv pip install -e .[/bold]\n")

    console.print("  [bold]Here's what the code would look like:[/bold]\n")
    code = f'''from rlm import RLM

# Load your policy documents as a dict
policies = {{...}}  # filename -> content

rlm = RLM(
    backend="openai",
    backend_kwargs={{
        "model_name": "{MODEL}",
        "api_key": "your-api-key",
        "base_url": "{BASE_URL}",
    }},
    environment="local",
    max_depth=1,
    max_iterations=15,
    verbose=True,
)

# The real library accepts context as the first arg, query as root_prompt
result = rlm.completion(
    policies,
    root_prompt="What are the MFA requirements?",
)
print(result.response)
print(result.usage_summary.to_dict())
'''
    console.print(Syntax(code.strip(), "python", theme="monokai"))

except Exception as e:
    console.print(f"  [red]Error running the real RLM library: {e}[/red]")
    import traceback
    traceback.print_exc()


# =============================================================================
# Part 4: Comparison
# =============================================================================

console.print(Panel(
    "[bold]SimpleRLM vs Real RLM Library[/bold]\n\n"
    "Both implementations use the same core algorithm:\n"
    "  1. Root LLM sees metadata, not raw context\n"
    "  2. Root LLM writes code to search/filter context\n"
    "  3. Sub-LLM calls interpret excerpts\n"
    "  4. Iterative loop until FINAL()\n\n"
    "[bold]What the real library adds:[/bold]\n"
    "  - Socket-based LMHandler for isolated environments\n"
    "  - Docker, Modal, E2B, Daytona, Prime sandbox support\n"
    "  - Async sub-LLM calls via acompletion()\n"
    "  - RLMLogger for trajectory inspection\n"
    "  - Persistent multi-turn conversations\n"
    "  - Multiple backend support (OpenAI, Anthropic, Gemini, etc.)\n\n"
    "Your SimpleRLM from Steps 1-13 is the same core algorithm.\n"
    "The real library wraps it with production infrastructure.",
    style="green",
))
