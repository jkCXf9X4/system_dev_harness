# ADR-0003: Use Structured Handoff Before Code Editing

## Status

Accepted, amended

## Context

The solution is intended to support agentic development, but the primary failure modes are shortcutting, partial implementations, architecture drift, lost requirements, and repeated mistakes.

The workflow now supports an edit-capable builder stage, but code editing still needs to start from explicit constraints. Without a structured handoff, the workspace becomes another coding agent rather than a controlled delivery workflow.

## Decision

The workflow will produce an implementation packet and a handoff brief before implementation begins. The handoff must include the requirement contract, architecture guardrails, known mistakes, required checks, completion checklist, stop conditions, and required final response shape.

Completion is not self-assessed by the builder. It is checked by independent reviewer roles against the contract and implementation evidence, then routed through a deterministic completion gate.

## Consequences

Benefits:

- task intent stays inspectable before implementation starts
- handoffs remain consistent and reviewable
- implementation works from explicit constraints
- approval remains separated from execution

Tradeoffs:

- the workflow still depends on user or agent discipline to collect evidence
- review quality depends on the completeness of the handoff and artifact set
- small-task build handoff is an explicit exception that trades ceremony for speed and must remain low-risk

## Traceability

- Product commitments: PC-001, PC-004, PC-005
- Use cases: UC-005, UC-006, UC-007, UC-008
