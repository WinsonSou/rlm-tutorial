"""
Shared configuration for all tutorial steps.
Points to your internal OpenAI-compatible endpoint.
"""

BASE_URL = "https://open.ai.compatible.endpoint.goes.here/enterpriseai/v1"
MODEL = "gpt-oss-120b"
#MODEL = "qwen3-coder-next"
API_KEY = "API_KEY_GOES_HERE"

MAX_CONTEXT_TOKENS = 20480

TEMPERATURE = 1
TOP_P = 1 #0.95 for qwen3-coder-next and 1 for gpt-oss-12b
TOP_K = 40
REASONING_EFFORT = "high"  # Set to "low", "medium", or "high" if the model supports it


def model_kwargs() -> dict:
    """Build extra kwargs for chat.completions.create().
    Omits reasoning_effort when None so it works with any model."""
    kwargs: dict = {
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        #"extra_body": {"top_k": TOP_K},
    }
    if REASONING_EFFORT is not None:
        kwargs["reasoning_effort"] = REASONING_EFFORT
    return kwargs
