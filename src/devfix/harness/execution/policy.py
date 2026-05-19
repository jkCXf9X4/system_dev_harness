from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class MCPPolicy(BaseModel):
    allowed_roots: list[str]
    max_list_files: int = 400
    max_read_bytes: int = 24_000
    max_search_results: int = 80
    max_discovery_files: int = 12
    patch_only_writes: bool = True
    allowed_test_commands: list[str] = Field(
        default_factory=lambda: [
            "pytest",
            "python -m pytest",
            "python3 -m pytest",
            "python -m unittest",
            "python3 -m unittest",
            "python -m compileall src",
            "python3 -m compileall src",
        ]
    )

    @field_validator("allowed_roots")
    @classmethod
    def require_roots(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("allowed_roots must not be empty")
        return value

    def resolve_roots(self, workdir: Path) -> list[Path]:
        return [(workdir / root).resolve() for root in self.allowed_roots]

    def is_allowed_path(self, workdir: Path, candidate: Path) -> bool:
        resolved = candidate.resolve()
        return any(_is_relative_to(resolved, root) for root in self.resolve_roots(workdir))

    def validate_command(self, command: str) -> bool:
        normalized = " ".join(command.strip().split())
        return any(normalized == prefix or normalized.startswith(f"{prefix} ") for prefix in self.allowed_test_commands)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False
