# Verification Evidence Prompt

Use this template when the implementation is complete and the next step is proving the change is ready.

```text
Verify the completed change for [feature, fix, PR, branch, or commit range].

Change summary:
- [What changed.]
- [Primary files or modules touched.]
- [Known risky behavior.]

Required checks:
- `[unit or focused test command]`
- `[integration, build, lint, typecheck, or manual command]`
- [Manual workflow or screenshot check, if relevant.]

Acceptance criteria to confirm:
- [Criterion one.]
- [Criterion two.]
- [Regression behavior that must still work.]

Evidence to report:
- Commands run and pass/fail result.
- Any failing output that remains relevant.
- Files or behavior inspected manually.
- Residual risk, skipped checks, or environment limitations.

Do not make implementation changes unless verification exposes a blocking issue. If a blocking issue is found, stop and report the issue with the smallest suggested fix.
```

Best-practice notes:
- Verification prompts should name exact commands where possible.
- Ask for skipped checks explicitly; missing evidence should be visible.
- Separate verification from implementation to avoid unreviewed late changes.
