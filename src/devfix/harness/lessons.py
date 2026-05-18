from __future__ import annotations

import re
from typing import Any

import yaml

from devfix.harness.schemas import KnownMistake


def parse_lessons(content: str) -> list[KnownMistake]:
    stripped = content.strip()
    if not stripped:
        return []

    if stripped.startswith("lessons:"):
        raw = yaml.safe_load(stripped) or {}
        return [KnownMistake.model_validate(item) for item in raw.get("lessons", [])]

    return _parse_markdown_lessons(stripped)


def _parse_markdown_lessons(content: str) -> list[KnownMistake]:
    lessons: list[KnownMistake] = []
    content = re.sub(r"```.*?```", "", content, flags=re.S)
    blocks = re.split(r"(?m)^###\s+", content)
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        if not lines:
            continue
        title_line = lines[0].strip()
        match = re.match(r"(?P<id>KM-\d+):\s*(?P<title>.+)", title_line)
        if not match:
            continue
        fields = _extract_markdown_fields("\n".join(lines[1:]))
        lessons.append(
            KnownMistake(
                id=match.group("id"),
                title=match.group("title"),
                pattern=fields.get("Pattern", ""),
                prevention_rule=fields.get("Prevention rule", ""),
                completion_check=fields.get("Completion check", ""),
                severity=_severity(fields),
                tags=[],
            )
        )
    return lessons


def _extract_markdown_fields(content: str) -> dict[str, str]:
    names = ["Pattern", "Why it matters", "Prevention rule", "Completion check"]
    fields: dict[str, str] = {}
    for index, name in enumerate(names):
        next_names = names[index + 1 :]
        next_pattern = "|".join(re.escape(f"{next_name}:") for next_name in next_names)
        if next_pattern:
            pattern = rf"{re.escape(name)}:\s*(.*?)(?=\n(?:{next_pattern})|\Z)"
        else:
            pattern = rf"{re.escape(name)}:\s*(.*)\Z"
        match = re.search(pattern, content, re.S)
        if match:
            fields[name] = match.group(1).strip()
    return fields


def _severity(fields: dict[str, Any]) -> str:
    text = " ".join(str(value).lower() for value in fields.values())
    if any(word in text for word in ["security", "data loss", "corruption", "critical"]):
        return "high"
    if any(word in text for word in ["hidden", "risk", "rework", "maintenance"]):
        return "medium"
    return "low"
