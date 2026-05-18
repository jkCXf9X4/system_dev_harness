from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def openrouter_model(model_env: str, *, temperature: float = 0.2) -> ChatOpenAI:
    """Create an OpenAI-compatible LangChain chat model backed by OpenRouter."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set. Copy .env.example to .env and add a key.")

    model = os.getenv(model_env)
    if not model:
        raise RuntimeError(f"{model_env} is not set.")

    default_headers = {
        "HTTP-Referer": os.getenv("OPENROUTER_SITE_URL", "http://localhost"),
        "X-OpenRouter-Title": os.getenv("OPENROUTER_APP_NAME", "system-dev-harness"),
    }

    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        default_headers=default_headers,
        temperature=temperature,
    )
