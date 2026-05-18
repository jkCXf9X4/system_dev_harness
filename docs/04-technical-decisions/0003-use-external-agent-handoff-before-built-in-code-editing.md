# ADR-0003: Use External Agent Handoff Before Built-In Code Editing

## Status

Accepted

## Context

The harness is intended to support agentic development, but the primary failure modes are shortcutting, partial implementations, architecture drift, lost requirements, and repeated mistakes.

Embedding code-editing tools too early would make the harness another coding agent before the control system is mature. The immediate need is to create strict, reviewable handoff packets that guide external coding agents.

## Decision

The harness will produce external coding-agent handoff packets before it performs built-in code edits. External execution is integrated through an adapter boundary rather than hard-coding one coding tool into graph logic.

The packet must include:

- requirement contract
- architecture guardrails
- known mistakes to avoid
- required tests and checks
- completion checklist
- stop conditions
- required final response shape

Completion is not self-assessed by the coding agent. It is checked by independent reviewer roles against the contract and implementation evidence, then routed through a deterministic completion gate.

Initial adapters:

- manual adapter for copy/paste handoff
- opencode adapter for `opencode run --format json`

## Consequences

Benefits:

- supports guarded coding without giving the harness write access yet
- keeps task intent inspectable before implementation starts
- makes external agent prompts consistent and reviewable
- reduces risk while preserving a path to future built-in code editing
- keeps opencode-specific process handling outside core graph logic

Tradeoffs:

- users must still run a separate coding agent
- the harness depends on supplied external evidence until direct integrations exist
- review quality depends on the completeness of changed files, diff, test output, and agent output provided to the CLI
- opencode session id parsing depends on its JSON event shape

## Traceability

- Product commitments: PC-001, PC-004, PC-005
- Use cases: UC-004, UC-006, UC-008
- Requirements: FR-006, FR-007, FR-013, FR-014, FR-017, FR-019, FR-021, FR-022, FR-023, QR-002, QR-008, QR-009, QR-010
