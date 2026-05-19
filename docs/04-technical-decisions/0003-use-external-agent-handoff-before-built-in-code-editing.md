# ADR-0003: Use External Agent Handoff Before Built-In Code Editing

## Status

Accepted

## Context

The solution is intended to support agentic development, but the primary failure modes are shortcutting, partial implementations, architecture drift, lost requirements, and repeated mistakes.

Embedding code-editing behavior too early would make the workspace another coding agent without the control system being mature. The immediate need is to create strict, reviewable handoff packets that guide implementation.

## Decision

The workflow will produce an implementation packet and a handoff brief before the builder agent edits files. The handoff must include the requirement contract, architecture guardrails, known mistakes, required checks, completion checklist, stop conditions, and required final response shape.

Completion is not self-assessed by the builder. It is checked by independent reviewer roles against the contract and implementation evidence, then routed through a deterministic completion gate.

## Consequences

Benefits:

- task intent stays inspectable before implementation starts
- handoffs remain consistent and reviewable
- the builder stage works from explicit constraints
- approval remains separated from execution

Tradeoffs:

- the workflow still depends on user or agent discipline to collect evidence
- review quality depends on the completeness of the handoff and artifact set

## Traceability

- Product commitments: PC-001, PC-004, PC-005
- Use cases: UC-005, UC-006, UC-007, UC-008
