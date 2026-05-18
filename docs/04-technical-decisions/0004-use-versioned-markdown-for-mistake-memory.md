# ADR-0004: Use Versioned Markdown For Mistake Memory

## Status

Accepted

## Context

One of the target problems is that agents repeatedly make the same mistakes. The harness needs persistent mistake memory, but the first version should remain lightweight, transparent, and easy to review.

A database or local JSON store would be easier for automation later, but harder for humans to inspect during early design.

## Decision

Start persistent mistake memory as versioned markdown in `docs/07-lessons/known-mistakes.md`, with YAML lesson input also supported for more structured automation.

Each lesson should include:

- pattern
- why it matters
- prevention rule
- completion check

The CLI parses lesson files into structured `KnownMistake` objects before passing them into the known mistake check node.

## Consequences

Benefits:

- lessons are reviewable in pull requests
- humans and agents can both read the same source of truth
- no new storage dependency is required
- lessons can later be migrated to structured storage

Tradeoffs:

- markdown is less machine-queryable than YAML, JSON, or SQLite
- duplicate or stale lessons require human hygiene
- relevance matching is initially LLM-driven

## Traceability

- Product commitments: PC-003
- Use cases: UC-003, UC-009
- Requirements: FR-005, FR-016, C-006
