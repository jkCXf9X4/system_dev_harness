from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel

from harness.schemas import EvidenceBundle, ExternalAgentHandoff


class SessionRef(BaseModel):
    adapter: str
    session_id: str = ""
    title: str = ""
    attach_command: str = ""
    export_command: str = ""
    transcript_path: str = ""


class ExecutionResult(BaseModel):
    session: SessionRef
    evidence: EvidenceBundle
    raw_output: str = ""


class ExecutionAdapter(ABC):
    name: str

    @abstractmethod
    def execute(self, handoff: ExternalAgentHandoff, *, title: str, workdir: Path) -> ExecutionResult:
        """Execute or prepare execution for an external coding agent."""
