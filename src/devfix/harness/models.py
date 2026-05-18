from __future__ import annotations

import os
import ssl
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def _prefer_system_ca_bundle() -> None:
    if os.getenv("SSL_CERT_FILE"):
        return

    candidates = [
        Path("/etc/ssl/certs/ca-certificates.crt"),
        Path("/etc/pki/tls/certs/ca-bundle.crt"),
        Path("/usr/lib/ssl/cert.pem"),
    ]
    default_paths = ssl.get_default_verify_paths()
    for value in (default_paths.cafile, default_paths.capath):
        if value:
            candidates.append(Path(value))

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            os.environ.setdefault("SSL_CERT_FILE", str(candidate))
            os.environ.setdefault("REQUESTS_CA_BUNDLE", str(candidate))
            return


def openrouter_model(model_env: str, *, temperature: float = 0.2) -> ChatOpenAI:
    """Create an OpenAI-compatible LangChain chat model backed by OpenRouter."""
    _prefer_system_ca_bundle()
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
