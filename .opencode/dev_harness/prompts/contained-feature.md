# Contained Feature Prompt

Use this template when the desired change has a known user-facing outcome and should stay inside the current architecture.

```text
Implement [feature name] for [user or workflow].

Objective:
- [Describe the observable behavior the user needs.]
- [Name the entry point, command, screen, API, or workflow affected.]

In scope:
- [Specific behavior to add.]
- [Specific files, modules, or boundaries that are expected to change, if known.]
- [Data, configuration, or UI states that must be handled.]

Out of scope:
- Broad refactors, pattern switches, unrelated cleanup, or responsibility changes.
- Changes to [module/API/schema] unless required to satisfy the objective.

Acceptance criteria:
- [Concrete outcome that can be checked.]
- [Important edge case.]
- [Compatibility or regression requirement.]

Verification:
- Run [test command or manual check].
- Report the changed files and evidence from verification.
```

Best-practice notes:
- Lead with the outcome, not the preferred implementation.
- Put constraints in `Out of scope` so the workflow can reject diff drift.
- Make acceptance criteria observable and testable.
