# ADR-0002: Use OpenRouter As Initial Model Access Layer

## Status

Accepted

## Context

The harness will likely need different model characteristics for different roles:

- stronger reasoning for planning
- careful review for architecture and risk
- faster cheaper models for summaries and QA drafts

Hard-coding direct provider clients into the graph would make experimentation and provider changes harder.

## Decision

Use OpenRouter as the initial model access layer through an OpenAI-compatible client.

Keep model choices in environment variables:

- `PLANNER_MODEL`
- `REVIEWER_MODEL`
- `FAST_MODEL`

## Consequences

Benefits:

- one API shape for many model providers
- model IDs can change without graph code changes
- role-specific model assignment is straightforward
- future fallback and routing experiments are easier

Tradeoffs:

- OpenRouter becomes an operational dependency
- model availability and behavior can change over time
- provider-specific features may not map cleanly through the unified API

## Traceability

- Vision: configurable model access over provider lock-in
- Use cases: UC-007
- Requirements: FR-009, QR-003, C-003
- Implementation: `devfix/harness/models.py`, `.env.example`
