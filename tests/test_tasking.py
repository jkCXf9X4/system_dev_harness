from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from devfix.harness.tasking import build_task_prompt, looks_like_backlog_meta_prompt, parse_backlog_candidate


class TaskingTests(unittest.TestCase):
    def test_parse_backlog_candidate(self) -> None:
        content = """# Task: Add Durable Runs

Status: todo

Goal:
Persist workflow runs beyond a single process lifetime.

Scope:
- Add a durable checkpointer.
- Preserve run state across restarts.

Acceptance criteria:
- A run can be resumed after process restart.
"""
        candidate = parse_backlog_candidate("plans/backlog/003-add-durable-runs.md", content)
        self.assertEqual(candidate.title, "Task: Add Durable Runs")
        self.assertEqual(candidate.status, "todo")
        self.assertIn("Add a durable checkpointer.", candidate.scope)
        self.assertIn("A run can be resumed after process restart.", candidate.acceptance_criteria)

    def test_build_task_prompt(self) -> None:
        content = "# Task: Sample\n\nGoal:\nDo work."
        candidate = parse_backlog_candidate("plans/backlog/sample.md", content)
        prompt = build_task_prompt(candidate, content)
        self.assertIn("Selected backlog item: Task: Sample", prompt)
        self.assertIn("Path: plans/backlog/sample.md", prompt)

    def test_meta_prompt_detection(self) -> None:
        self.assertTrue(looks_like_backlog_meta_prompt("Evaluate the backlog, select most value item, implement the item"))
        self.assertFalse(looks_like_backlog_meta_prompt("Implement durable runs using sqlite"))


if __name__ == "__main__":
    unittest.main()
