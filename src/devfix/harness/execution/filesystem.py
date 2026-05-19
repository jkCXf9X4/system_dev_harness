from __future__ import annotations

import subprocess

from devfix.harness.execution.mcp import MCPClient, MCPToolCall, MCPToolResult


class FilesystemMCPClient(MCPClient):
    def list_files(self, roots: list[str]) -> MCPToolResult:
        files: list[str] = []
        for root in roots:
            root_path = (self.workdir / root).resolve()
            if not self.policy.is_allowed_path(self.workdir, root_path) or not root_path.exists():
                continue
            for path in sorted(candidate for candidate in root_path.rglob("*") if candidate.is_file()):
                files.append(path.relative_to(self.workdir).as_posix())
                if len(files) >= self.policy.max_list_files:
                    break
            if len(files) >= self.policy.max_list_files:
                break
        return MCPToolResult(
            payload=files,
            trace=MCPToolCall(
                tool="list_files",
                arguments={"roots": roots},
                outcome="ok",
                details=f"returned {len(files)} file(s)",
            ),
        )

    def read_file(self, path: str) -> MCPToolResult:
        file_path = (self.workdir / path).resolve()
        if not self.policy.is_allowed_path(self.workdir, file_path) or not file_path.is_file():
            raise RuntimeError(f"read_file denied for path: {path}")
        content = file_path.read_text(encoding="utf-8")
        truncated = content[: self.policy.max_read_bytes]
        return MCPToolResult(
            payload=truncated,
            trace=MCPToolCall(
                tool="read_file",
                arguments={"path": path},
                outcome="ok",
                details=f"read {min(len(content), len(truncated))} byte(s)",
            ),
        )

    def search_text(self, pattern: str, roots: list[str]) -> MCPToolResult:
        completed = subprocess.run(
            ["rg", "-n", "--no-heading", pattern, *roots],
            cwd=self.workdir,
            text=True,
            capture_output=True,
            check=False,
        )
        lines = [line for line in completed.stdout.splitlines() if line.strip()]
        payload = lines[: self.policy.max_search_results]
        outcome = "ok" if completed.returncode in (0, 1) else "error"
        details = completed.stderr.strip()
        return MCPToolResult(
            payload=payload,
            trace=MCPToolCall(
                tool="search_text",
                arguments={"pattern": pattern, "roots": roots},
                outcome=outcome,
                details=details or f"returned {len(payload)} match line(s)",
            ),
        )

    def apply_patch(self, patch: str) -> MCPToolResult:
        completed = subprocess.run(
            ["git", "apply", "--whitespace=nowarn", "-"],
            cwd=self.workdir,
            text=True,
            input=patch,
            capture_output=True,
            check=False,
        )
        outcome = "ok" if completed.returncode == 0 else "error"
        details = completed.stderr.strip() or completed.stdout.strip() or "patch applied"
        return MCPToolResult(
            payload={"applied": completed.returncode == 0},
            trace=MCPToolCall(
                tool="apply_patch",
                arguments={"patch_bytes": len(patch.encode("utf-8"))},
                outcome=outcome,
                details=details,
            ),
        )

    def run_test(self, command: str) -> MCPToolResult:
        if not self.policy.validate_command(command):
            raise RuntimeError(f"run_test denied for command: {command}")
        completed = subprocess.run(
            command.split(),
            cwd=self.workdir,
            text=True,
            capture_output=True,
            check=False,
        )
        payload = {
            "command": command,
            "exit_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }
        outcome = "ok" if completed.returncode == 0 else "error"
        return MCPToolResult(
            payload=payload,
            trace=MCPToolCall(
                tool="run_test",
                arguments={"command": command},
                outcome=outcome,
                details=f"exit_code={completed.returncode}",
            ),
        )
