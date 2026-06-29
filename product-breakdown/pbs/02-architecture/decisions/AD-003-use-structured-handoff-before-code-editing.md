# AD-003: Use Structured Handoff Before Code Editing

## Status

Accepted, amended

## Context

The solution is intended to support agentic development, but the primary failure modes are shortcutting, partial implementations, architecture drift, lost requirements, and repeated mistakes.

The workflow supports an edit-capable builder stage, but code editing still needs to start from explicit constraints. Without a structured planner-owned work order or handoff, the workspace becomes another coding agent rather than a controlled delivery workflow.

## Decision

The workflow will always produce a planner-owned builder work order before implementation begins. It will produce a handoff brief only when external or manual implementation is requested, or when the orchestrator will use the handoff as builder-stage input.

When produced, the handoff must include the requirement contract, architecture guardrails, known mistakes, required checks, completion checklist, stop conditions, and required final response shape. It is non-executing guidance and cannot authorize skipped checks, direct approval, waived failures, or scope expansion.

Completion is not self-assessed by the builder. It is checked by the reviewer stage and independent review helpers against the work order and implementation evidence, then routed through a deterministic completion gate.

## Consequences

Benefits:

- task intent stays inspectable before implementation starts
- handoffs remain consistent and reviewable when external or manual implementation is needed
- implementation works from explicit constraints
- approval remains separated from execution

Tradeoffs:

- the workflow still depends on user or agent discipline to collect evidence
- review quality depends on the completeness of the work order, handoff when used, and artifact set
- direct build-agent use remains an explicit operator choice outside the orchestrator path and must not become a shortcut that omits contract, architecture, or review requirements

## Traceability

- Product commitments: PC-001, PC-004, PC-005
- Use cases: UC-005, UC-006, UC-007, UC-008
