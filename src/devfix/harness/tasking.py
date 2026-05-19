from __future__ import annotations

import re

from devfix.harness.schemas import BacklogCandidate


def parse_backlog_candidate(path: str, content: str) -> BacklogCandidate:
    return BacklogCandidate(
        path=path,
        title=_heading(content),
        status=_field(content, "Status"),
        goal=_field(content, "Goal"),
        scope=_section_bullets(content, "Scope"),
        acceptance_criteria=_section_bullets(content, "Acceptance criteria"),
    )


def build_task_prompt(candidate: BacklogCandidate, content: str) -> str:
    header = [
        f"Selected backlog item: {candidate.title}",
        f"Path: {candidate.path}",
    ]
    if candidate.goal:
        header.append(f"Goal: {candidate.goal}")
    return "\n".join(header) + "\n\n" + content.strip()


def looks_like_backlog_meta_prompt(prompt: str) -> bool:
    normalized = prompt.lower()
    return "evaluate the backlog" in normalized or ("select" in normalized and "backlog" in normalized)


def _heading(content: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return "Backlog Item"


def _field(content: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.+)$", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def _section_bullets(content: str, heading: str) -> list[str]:
    section = _section_text(content, heading)
    results: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            results.append(stripped[2:].strip())
    return results


def _section_text(content: str, heading: str) -> str:
    pattern = rf"^(?:##?\s+{re.escape(heading)}|{re.escape(heading)}:)\s*$"
    lines = content.splitlines()
    collecting = False
    collected: list[str] = []
    for line in lines:
        if re.match(pattern, line.strip(), re.IGNORECASE):
            collecting = True
            continue
        if collecting and line.strip().startswith("#"):
            break
        if collecting:
            collected.append(line)
    return "\n".join(collected).strip()
