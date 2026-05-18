# Known Mistakes

This file is persistent mistake memory for the harness. Add project-specific repeated failures here so future tasks can check against them.

Each lesson should be concrete enough to become a review check.

## Template

```text
### KM-000: Short title

Pattern:
What mistake tends to happen?

Why it matters:
What risk or rework does it cause?

Prevention rule:
What must future agents do differently?

Completion check:
How should reviewers verify this did not happen again?
```

## Current Lessons

### KM-001: Do Not Implement Plausible Partial Solutions

Pattern:
Agents may satisfy the most visible part of a task while leaving edge cases, integration points, documentation, or tests unfinished.

Why it matters:
The result looks complete but creates hidden follow-up work and repeated review cycles.

Prevention rule:
Every implementation packet must include a completion checklist tied to the requirement contract.

Completion check:
Reviewers must verify each contract item is complete, explicitly waived, or blocking.

### KM-002: Do Not Ignore Architecture Constraints

Pattern:
Agents may choose the fastest local implementation even when it conflicts with existing architecture, patterns, or boundaries.

Why it matters:
Short-term progress creates long-term inconsistency and maintenance risk.

Prevention rule:
Every task must identify architecture constraints and forbidden shortcuts before coding handoff.

Completion check:
Architecture reviewer must confirm the implementation plan preserves integration boundaries and existing patterns.

### KM-003: Do Not Lose Track During Long Tasks

Pattern:
Agents may start aligned with the task but drift after several steps or corrections.

Why it matters:
The final output may no longer satisfy the original task contract.

Prevention rule:
External coding-agent handoff must require the agent to re-check the contract before final response.

Completion check:
Completeness reviewer must compare final work against the original contract, not only the latest local change.
