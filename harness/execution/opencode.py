from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from uuid import uuid4

from harness.execution.base import ExecutionAdapter, ExecutionResult, SessionRef
from harness.schemas import EvidenceBundle, ExternalAgentHandoff


class OpenCodeAdapter(ExecutionAdapter):
    name = "opencode"

    def __init__(
        self,
        *,
        mode: str = "headless",
        attach_url: str = "",
        model: str = "",
        agent: str = "",
        timeout_seconds: int = 1800,
    ) -> None:
        self.mode = mode
        self.attach_url = attach_url
        self.model = model
        self.agent = agent
        self.timeout_seconds = timeout_seconds

    def execute(self, handoff: ExternalAgentHandoff, *, title: str, workdir: Path) -> ExecutionResult:
        if shutil.which("opencode") is None:
            raise RuntimeError("opencode executable not found on PATH.")

        prompt = self._format_prompt(handoff)
        session_id = f"opencode-{uuid4()}"
        command = self._build_command(prompt, title)
        completed = subprocess.run(
            command,
            cwd=workdir,
            text=True,
            capture_output=True,
            timeout=self.timeout_seconds,
            check=False,
        )
        raw_output = "\n".join(part for part in [completed.stdout, completed.stderr] if part)
        parsed_session = self._extract_session_id(raw_output) or session_id
        session = SessionRef(
            adapter=self.name,
            session_id=parsed_session,
            title=title,
            attach_command=self._attach_command(parsed_session),
            export_command=f"opencode export {parsed_session}",
        )
        evidence = EvidenceBundle(
            has_evidence=bool(raw_output.strip()),
            agent_output=raw_output.strip(),
        )
        if completed.returncode != 0:
            evidence.agent_output = f"opencode exited with {completed.returncode}\n\n{evidence.agent_output}"
        return ExecutionResult(session=session, evidence=evidence, raw_output=raw_output)

    def _build_command(self, prompt: str, title: str) -> list[str]:
        command = ["opencode", "run", "--format", "json", "--title", title]
        if self.attach_url:
            command.extend(["--attach", self.attach_url])
        if self.model:
            command.extend(["--model", self.model])
        if self.agent:
            command.extend(["--agent", self.agent])
        if self.mode == "interactive":
            command.append(prompt)
            return command
        command.append(prompt)
        return command

    def _attach_command(self, session_id: str) -> str:
        if self.attach_url:
            return f"opencode attach {self.attach_url} --session {session_id}"
        return f"opencode --session {session_id}"

    def _format_prompt(self, handoff: ExternalAgentHandoff) -> str:
        return "\n".join(
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

    def _extract_session_id(self, output: str) -> str:
        for line in output.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            try:
                event = json.loads(stripped)
            except json.JSONDecodeError:
                continue
            for key in ("sessionID", "sessionId", "session_id", "id"):
                value = event.get(key)
                if isinstance(value, str) and value:
                    return value
            session = event.get("session")
            if isinstance(session, dict):
                for key in ("id", "sessionID", "sessionId", "session_id"):
                    value = session.get(key)
                    if isinstance(value, str) and value:
                        return value
        return ""
