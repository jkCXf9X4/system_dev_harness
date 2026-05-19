# ADR-0002: Use Versioned Markdown For Traceable Context

## Status

Accepted

## Context

The solution needs a durable, reviewable chain from intent to implementation. If the context lives only in chat history, it is hard to inspect, hard to update, and hard to trace.

## Decision

Store intent, commitments, architecture, decisions, implementation mapping, and persistent lessons under `.opencode/`. Load those docs through `opencode.json` instructions so agents share the same stable context.

## Consequences

Benefits:

- context is reviewable in git
- traceability stays explicit
- lessons and architecture can evolve without losing the chain
- the current solution can be understood without replaying a chat transcript

Tradeoffs:

- the docs must be kept in sync with the workflow prompts
- additions to the chain must be intentional rather than ad hoc

## Traceability

- Product commitments: PC-003, PC-006, PC-007
- Use cases: UC-001, UC-004, UC-009
