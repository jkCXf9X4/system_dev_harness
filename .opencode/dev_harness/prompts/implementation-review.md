# Implementation Review Prompt

Use this template when reviewing an existing diff, branch, PR, or completed planner work order.

```text
Review [branch, PR number, commit range, or changed files] for correctness and regressions.

Review focus:
- [Primary behavior or requirement.]
- [Risk area such as data migration, concurrency, security, API compatibility, UI state, or error handling.]
- [Test coverage expectations.]

Known context:
- Requirement: [Link or summary.]
- Non-goals: [What should not be evaluated as part of this review.]
- Relevant commands: `[test or verification command]`

Please prioritize findings in this order:
- Bugs or behavioral regressions.
- Requirement gaps.
- Missing or weak tests for changed behavior.
- Maintainability issues only when they create concrete risk.

For each finding, include:
- File and line reference.
- Why it is a problem.
- A concrete suggested fix or verification step.

If no issues are found, say that clearly and list any residual risk or test gap.
```

Best-practice notes:
- Define the review focus up front so feedback stays tied to risk.
- Ask for file and line references to make findings actionable.
- Keep style feedback secondary unless it affects behavior, maintenance, or tests.
