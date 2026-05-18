# Traceability Matrix

This matrix connects use cases, requirements, implementation artifacts, and design decisions.

## Current Traceability

| Source | Requirement | Implementation | Decision |
| --- | --- | --- | --- |
| UC-001 | FR-001, FR-002, FR-003 | `requirement_contract` node | ADR-0001 |
| UC-002 | FR-004 | `architecture_context` node | ADR-0001 |
| UC-003 | FR-005, FR-016 | `known_mistake_check` node, `docs/lessons/known-mistakes.md` | ADR-0004 |
| UC-004 | FR-006, FR-007 | `implementation_packet`, `external_agent_handoff` nodes | ADR-0003 |
| UC-005 | FR-008 | independent reviewer nodes | ADR-0001 |
| UC-006 | FR-013, FR-014, FR-019 | `completion_gate`, `revise_packet`, `human_interrupt` nodes | ADR-0003 |
| UC-007 | FR-009, QR-003 | `harness/models.py`, `.env.example` | ADR-0002 |
| UC-008 | FR-015 | `final_control_report` node | ADR-0001 |
| UC-009 | FR-005, FR-016 | `docs/lessons/known-mistakes.md` | ADR-0004 |
| UC-010 | FR-017, FR-018 | `evidence_intake`, Pydantic schemas, independent reviewer nodes | ADR-0001 |
| Vision: grounded architecture context | FR-020 | default context loading in `app.py` | ADR-0001 |
| Vision: guarded agentic development | QR-002, QR-008, QR-009 | no direct code-edit tools; external handoff packet | ADR-0003 |
| Vision: inspectable workflow | QR-001, QR-004, QR-005 | `docs/`, `harness/prompts.py` | ADR-0001 |

## Decision To Requirement Mapping

| Decision | Supports | Notes |
| --- | --- | --- |
| ADR-0001 LangGraph for workflow orchestration | FR-010, FR-011, QR-001 | Makes workflow states explicit and checkpointable. |
| ADR-0002 OpenRouter as model access layer | FR-009, QR-003 | Keeps model selection configurable through OpenAI-compatible access. |
| ADR-0003 External agent handoff before built-in code editing | QR-002, QR-006, QR-008, QR-009 | Enables guarded coding without embedding file mutation yet. |
| ADR-0004 Versioned markdown for mistake memory | FR-005, FR-016, C-006 | Makes repeated mistakes reviewable and reusable. |

## How To Use This File

- Add a row when adding a use case, requirement, node, prompt, or decision.
- Do not rely on implementation files alone to explain intent.
- If a code change cannot point to a requirement or decision, either document the missing rationale or reconsider the change.
