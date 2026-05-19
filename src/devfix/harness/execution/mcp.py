from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from devfix.harness.execution.policy import MCPPolicy


class MCPToolCall(BaseModel):
    tool: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    outcome: str
    details: str = ""


class MCPToolResult(BaseModel):
    payload: Any = None
    trace: MCPToolCall


class MCPClient(ABC):
    def __init__(self, *, workdir: Path, policy: MCPPolicy) -> None:
        self.workdir = workdir.resolve()
        self.policy = policy

    @abstractmethod
    def list_files(self, roots: list[str]) -> MCPToolResult:
        """Return repo-relative file paths within allowed roots."""

    @abstractmethod
    def read_file(self, path: str) -> MCPToolResult:
        """Return file text for an allowed path."""

    @abstractmethod
    def search_text(self, pattern: str, roots: list[str]) -> MCPToolResult:
        """Search text within allowed roots."""

    @abstractmethod
    def apply_patch(self, patch: str) -> MCPToolResult:
        """Apply a unified diff patch within allowed roots."""

    @abstractmethod
    def run_test(self, command: str) -> MCPToolResult:
        """Run an allowed verification command."""
