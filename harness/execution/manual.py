from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from harness.execution.base import ExecutionAdapter, ExecutionResult, SessionRef
from harness.schemas import EvidenceBundle, ExternalAgentHandoff


class ManualAdapter(ExecutionAdapter):
    name = "manual"

    def execute(self, handoff: ExternalAgentHandoff, *, title: str, workdir: Path) -> ExecutionResult:
        instruction = "\n".join(
            [
                handoff.agent_instruction,
                "",
                "Non-negotiable constraints:",
                *[f"- {item}" for item in handoff.non_negotiable_constraints],
                "",
                "Completion checklist:",
                *[f"- {item}" for item in handoff.completion_checklist],
                "",
                "Required final response:",
                *[f"- {item}" for item in handoff.required_final_response],
            ]
        )
        session = SessionRef(
            adapter=self.name,
            session_id=f"manual-{uuid4()}",
            title=title,
            attach_command="Paste the External Agent Handoff into your coding agent, then rerun with evidence flags.",
        )
        evidence = EvidenceBundle(has_evidence=False, agent_output=instruction)
        return ExecutionResult(session=session, evidence=evidence, raw_output=instruction)
