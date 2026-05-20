# IMD-001: Use Versioned Markdown For Mistake Memory

## Status

Accepted

## Context

The solution needs project-specific repeated failures to be visible to future tasks. If lessons only live in memory, they are easy to lose and easy to repeat.

## Decision

Keep persistent mistake memory in `.opencode/dev_harness/workflow/known-mistakes.md` and load it through the dev harness workflow context. Use stable lesson ids, prevention rules, and completion checks so reviewers can refer to them consistently.

## Consequences

Benefits:

- lessons are versioned and reviewable
- review checks can reference stable ids
- the lesson memory can grow with the project

Tradeoffs:

- the lesson file must be maintained as the solution evolves
- stale lessons need pruning when they stop being relevant

## Traceability

- Product commitments: PC-003, PC-006
- Use cases: UC-004, UC-009
