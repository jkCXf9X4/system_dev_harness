from __future__ import annotations

from pydantic import BaseModel


def render_model(title: str, model: BaseModel) -> str:
    return f"## {title}\n\n```json\n{model.model_dump_json(indent=2)}\n```"


def render_text(title: str, content: str) -> str:
    return f"## {title}\n\n{content}"
