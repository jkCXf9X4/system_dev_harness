from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from devfix.harness.execution import FilesystemMCPClient, MCPPolicy


class MCPPolicyTests(unittest.TestCase):
    def test_list_and_read_files_within_allowed_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            docs = workdir / "docs"
            docs.mkdir()
            target = docs / "note.md"
            target.write_text("hello", encoding="utf-8")

            client = FilesystemMCPClient(workdir=workdir, policy=MCPPolicy(allowed_roots=["docs"]))
            listed = client.list_files(["docs"])
            self.assertEqual(listed.payload, ["docs/note.md"])
            content = client.read_file("docs/note.md")
            self.assertEqual(content.payload, "hello")

    def test_read_denied_outside_allowed_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            docs = workdir / "docs"
            docs.mkdir()
            blocked = workdir / "blocked.txt"
            blocked.write_text("secret", encoding="utf-8")

            client = FilesystemMCPClient(workdir=workdir, policy=MCPPolicy(allowed_roots=["docs"]))
            with self.assertRaises(RuntimeError):
                client.read_file("blocked.txt")

    def test_validate_command(self) -> None:
        policy = MCPPolicy(allowed_roots=["src"])
        self.assertTrue(policy.validate_command("python3 -m compileall src"))
        self.assertFalse(policy.validate_command("bash -lc rm -rf /"))


if __name__ == "__main__":
    unittest.main()
