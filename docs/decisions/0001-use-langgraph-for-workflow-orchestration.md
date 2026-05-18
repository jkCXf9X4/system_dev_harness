# ADR-0001: Use LangGraph For Workflow Orchestration

## Status

Accepted

## Context

The harness needs explicit workflow states, role-specific nodes, controlled transitions, and future support for checkpointing, human approval, replay, and durable execution.

A generic chat loop would hide too much process logic inside prompts. The project needs the process itself to be inspectable.

## Decision

Use LangGraph as the initial workflow orchestration framework.

Represent guarded development roles as graph nodes:

- requirement contract
- architecture context
- known mistake check
- implementation packet
- external agent handoff
- reviewer council
- completion decision
- final control report

## Consequences

Benefits:

- workflow state is explicit
- graph steps can be checkpointed
- future human-in-the-loop interrupts fit the model
- node outputs can become traceable artifacts

Tradeoffs:

- slightly more setup than a direct one-shot LLM call
- graph state schema must be maintained as the workflow evolves
- team needs basic familiarity with LangGraph concepts

## Traceability

- Vision: governed contract loop, inspectable workflow
- Use cases: UC-001 through UC-008
- Requirements: FR-001 through FR-012, QR-001, QR-004
- Implementation: `harness/graph.py`, `harness/state.py`, `harness/prompts.py`
