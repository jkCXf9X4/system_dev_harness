# Continuous Improvement Discovery Prompt

Use this template when the request is exploratory and should produce backlog-ready candidates instead of immediate code changes.

```text
Explore improvement opportunities around [area, module, workflow, or recurring pain].

Goal:
- Identify backlog-worthy improvements with evidence.
- Do not edit code during this task.
- If a backlog-worthy item is found, persist it to disk before returning it.

Context:
- Current pain: [slow workflow, repeated review issue, confusing ownership, flaky tests, etc.]
- Known constraints: [release timing, compatibility boundaries, team ownership, performance budget.]
- Recent evidence: [issue, PR, review comment, test failure, operator note, or file path.]

Explore:
- [Directory, module, workflow, or behavior to inspect.]
- [Adjacent area that may explain the problem.]
- [Known non-goal or area to avoid.]

Return candidates with:
- Theme.
- Evidence and source files.
- Current pain or risk.
- Proposed improvement.
- Expected benefit.
- Risk and blast radius.
- Suggested priority.
- Backlog-ready task seed.
- What must stay out of unrelated feature or bug-fix diffs.
- File path for the written candidate.
```

Best-practice notes:
- Use this for cleanup, refactoring, pattern changes, responsibility shifts, tuning, and backlog discovery.
- Keep it read-only so exploratory work does not contaminate a contained implementation.
- Ask for evidence and blast radius; improvement ideas without both are hard to schedule safely.
