# Building Recursive Language Models (RLMs) From First Principles

A hands-on, step-by-step tutorial that rebuilds the core ideas from
[Alex Zhang's Recursive Language Models paper](https://arxiv.org/abs/2512.24601)
by discovering each piece through experimentation. Every component is motivated
by a concrete limitation of the previous step -- nothing is introduced "just because."

**All steps use your internal OpenAI-compatible endpoint** -- no public API keys required.

## Prerequisites

- Python 3.12 (managed via `uv`)
- `uv` package manager

## Setup

```bash
cd rlm-tutorial

# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
```

For Step 14 (running the real RLM library):
```bash
uv pip install -e ".[rlm]"
```

## How to Navigate

Each step is a self-contained Python script you run from the project root:

```bash
python step01_hello_llm.py
```

Read the docstring at the top of each file first -- it explains the concept,
why it matters, and how it connects to the previous step.

## Learning Progression

```
Phase 1: Foundations -- "Why do we need RLMs?"
──────────────────────────────────────────────
Step 1:  Hello LLM
  "An LLM is a text -> text function."
         |
Step 2:  Context Rot
  "Long inputs degrade LLM quality -- we need a solution."
         |
Step 3:  Naive Fixes
  "Manual chunking, summarization, and grep all break."
  "We need the LLM to decide its own strategy + call itself."

Phase 2: Building Blocks -- "The pieces of an RLM"
───────────────────────────────────────────────────
Step 4:  REPL Sandbox
  "exec() gives us a sandbox the LLM can write code into."
         |
Step 5:  LLM Writes Code
  "The LLM writes code, we execute it, feed results back."
         |
Step 6:  Context as Variable              <-- KEY RLM INSIGHT
  "Don't feed context to the LLM -- let it interact with it."
         |
Step 7:  Sub-LLM Calls
  "Code in the REPL can call the LLM recursively."

Phase 3: Assembly -- "Building the RLM"
───────────────────────────────────────
Step 8:  Recursive Depth
  "Depth control: root LM vs sub-LM."
         |
Step 9:  Iterative Loop
  "FINAL() / FINAL_VAR() + the multi-turn loop."
         |
Step 10: System Prompt
  "The system prompt that teaches the LLM to use the REPL."
         |
Step 11: Needle in a Haystack
  "RLM vs direct LLM on finding hidden facts."
         |
Step 12: Multi-Document Reasoning
  "Cross-document QA with partition + map + reduce."
         |
Step 13: Full RLM
  "Complete implementation with batched queries, rich output, usage tracking."

Phase 4: Bridge
───────────────
Step 14: Real Library
  "Map your from-scratch code to Alex Zhang's production rlm library."
  "Actually run the real library on Norfolk Industries policies for comparison."

Phase 5: Production -- "Taking RLMs to the real world"
──────────────────────────────────────────────────────
Step 15: Real-World Policies
  "Cross-document reasoning over 30 Norfolk Industries IT infrastructure"
  "policy documents (~1M chars). Single-doc (MFA requirements),"
  "cross-reference (CAB roles), and multi-hop (vulnerability response path)."
         |
Step 16: Robustness
  "Retry with exponential backoff, execution timeout, malformed output recovery."
  "Graceful sub-LLM failure handling, structured logging."
         |
Step 17: Async & Streaming
  "asyncio vs ThreadPool benchmarks, streaming tokens in real-time."
  "Code block detection from streaming responses."
```

## The Core Idea in 30 Seconds

Traditional LLM call:
```
LLM(query + huge_context) -> answer    # context rot degrades quality
```

Recursive Language Model call:
```
RLM(query, huge_context) ->
  1. Root LLM sees only the query + metadata ("context is 2M chars")
  2. Root LLM writes code to peek at / chunk / filter the context
  3. Root LLM spawns sub-LLM calls over smaller pieces
  4. Root LLM aggregates results -> answer
```

The LLM never sees the full context at once. It decides how to decompose it.

## References

- [RLM Paper (arXiv)](https://arxiv.org/abs/2512.24601)
- [RLM Blog Post](https://alexzhang13.github.io/blog/2025/rlm/)
- [RLM GitHub Repository](https://github.com/alexzhang13/rlm)
- [RLM Minimal Implementation](https://github.com/alexzhang13/rlm-minimal)
