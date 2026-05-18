# ADR-0003: Use External Agent Handoff Before Built-In Code Editing

## Status

Accepted

## Context

The harness is intended to support agentic development, but the primary failure modes are shortcutting, partial implementations, architecture drift, lost requirements, and repeated mistakes.

Embedding code-editing tools too early would make the harness another coding agent before the control system is mature. The immediate need is to create strict, reviewable handoff packets that guide external coding agents.

## Decision

The harness will produce external coding-agent handoff packets before it performs built-in code edits.

The packet must include:

- requirement contract
- architecture guardrails
- known mistakes to avoid
- required tests and checks
- completion checklist
- stop conditions
- required final response shape

Completion is not self-assessed by the coding agent. It is checked by reviewer roles against the contract.

## Consequences

Benefits:

- supports guarded coding without giving the harness write access yet
- keeps task intent inspectable before implementation starts
- makes external agent prompts consistent and reviewable
- reduces risk while preserving a path to future built-in code editing

Tradeoffs:

- users must still run a separate coding agent
- the harness cannot directly verify changed files yet
- review is initially focused on the handoff packet rather than actual code diffs

## Traceability

- Vision: external coding-agent handoff before built-in code editing
- Use cases: UC-004, UC-006, UC-008
- Requirements: FR-006, FR-007, FR-013, FR-014, QR-002, QR-008, QR-009
- Implementation: `implementation_packet`, `external_agent_handoff`, `completion_decision`
