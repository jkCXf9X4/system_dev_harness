# Bugfix Regression Prompt

Use this template when something is broken, especially when there is a failing command, log, or reproduction path.

```text
Fix the regression where [actual behavior] happens when [trigger].

Observed behavior:
- [What happens now.]
- [Error message, log excerpt, screenshot path, or failing assertion.]

Expected behavior:
- [What should happen instead.]
- [Any compatibility behavior that must remain unchanged.]

Reproduction:
- Environment: [OS, runtime, relevant config, branch, commit, or fixture.]
- Steps:
  1. [Step one.]
  2. [Step two.]
  3. [Step three.]
- Failing command: `[exact command]`

Constraints:
- Keep the fix limited to the regression path unless root cause evidence requires a wider change.
- Do not rewrite neighboring code only for style.
- Preserve public APIs and persisted data formats unless explicitly called out.

Acceptance criteria:
- The reproduction no longer fails.
- A focused regression test or equivalent verification covers the fixed behavior.
- Existing nearby behavior still passes relevant checks.

Please identify the root cause before editing, implement the smallest durable fix, and report verification evidence.
```

Best-practice notes:
- Include the exact failing command when available.
- Separate observed and expected behavior to avoid ambiguity.
- Ask for root cause before editing so the fix is not just symptom masking.
