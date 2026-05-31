# ED-001: Use Evolution Backlog For Improvement Candidates

## Status

Accepted

## Context

The workflow separates contained delivery from exploratory improvement. Improvement candidates need a durable, versioned landing zone that stays out of implementation diffs until they are turned into a scoped task contract. Without a canonical backlog location, candidates are easy to scatter, duplicate, or leave implicit.

## Decision

Use `product-breakdown/06-evolution/candidates/` as the canonical location for backlog-ready improvement candidates. Keep one file per candidate under `product-breakdown/06-evolution/candidates/`. Treat these files as proposed work, not implementation approval.

## Consequences

Benefits:

- backlog candidates remain reviewable and versioned
- improvement work stays separate from implementation diffs
- grooming can happen without losing source context

Tradeoffs:

- backlog content can go stale if it is not groomed
- the directory layout must stay in sync with the improvement workflow prompts and templates

## Traceability

- Product commitments: PC-006, PC-009
- Use cases: UC-012
