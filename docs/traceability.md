# Traceability Matrix

This file records backward traceability between documentation layers and implementation evidence.

## Documentation Chain

The documentation chain moves from intent to proof:

```text
Intent -> Product Commitments -> System Architecture -> Technical Decisions -> Implementation -> Verification
```

Trace links point backward to the layer being satisfied. Higher layers describe intent and constraints without linking down into lower-level implementation details.

## Layer Responsibilities

| Layer | Artifact | Responsibility | Links Back To |
| --- | --- | --- | --- |
| Intent | `docs/vision.md` | Captures why the harness exists, the problems it solves, desired outcomes, non-goals, and guiding principles. | None |
| Product Commitments | `docs/product-commitments.md` | Translates intent into durable product promises. | Intent |
| System Architecture | `docs/architecture.md` | Describes stable guarantees, concepts, boundaries, and control flow. | Product Commitments and requirements |
| Technical Decisions | `docs/decisions/` | Bridges architecture to material build choices and tradeoffs. | Architecture, requirements, and constraints |
| Implementation | `docs/implementation.md`, `devfix/`, `docs/execution-adapters.md` | Implements the selected decisions and exposes operational behavior. | Technical decisions, requirements, and architecture |
| Verification | Tests, execution evidence, reviewer verdicts, final control reports | Proves whether implementation satisfies the documented contract. | Implementation, requirements, and acceptance criteria |

## Traceability Rules

- Higher-level artifacts should not link down into lower-level implementation details.
- Lower-level artifacts should identify the higher-level promise, requirement, decision, or boundary they satisfy.
- Requirements should be stable anchors; if meaning changes, create a new ID.
- Architecture should describe stable concepts and boundaries, not transient module layouts.
- Technical decisions should explain why a build choice satisfies architecture and constraints.
- Implementation evidence should trace backward to requirements, decisions, or acceptance criteria.

## Requirement To Product Commitment Mapping

| Requirement | Satisfies |
| --- | --- |
| FR-001, FR-002, FR-003 | PC-001 |
| FR-004, FR-020 | PC-002 |
| FR-005, FR-016 | PC-003 |
| FR-006, FR-007, FR-017, FR-021, FR-022, FR-023 | PC-004 |
| FR-013, FR-014, FR-019, QR-008, QR-009, QR-010 | PC-005 |
| QR-001, QR-004, QR-005 | PC-006 |

## Implementation Traceability

| Implementation Artifact | Satisfies | Decision | Upstream Rationale |
| --- | --- | --- | --- |
| `requirement_contract` node | FR-001, FR-002, FR-003 | ADR-0001 | UC-001, PC-001 |
| `architecture_context` node | FR-004, FR-020 | ADR-0001 | UC-002, PC-002 |
| `known_mistake_check` node, `docs/lessons/known-mistakes.md` | FR-005, FR-016 | ADR-0004 | UC-003, UC-009, PC-003 |
| `implementation_packet`, `external_agent_handoff` nodes | FR-006, FR-007 | ADR-0003 | UC-004, PC-004 |
| independent reviewer nodes | FR-008, FR-017, FR-018 | ADR-0001 | UC-005, UC-010, PC-004 |
| `completion_gate`, `revise_packet`, `human_interrupt` nodes | FR-013, FR-014, FR-019 | ADR-0003 | UC-006, PC-005 |
| `devfix/harness/models.py`, `.env.example` | FR-009, QR-003 | ADR-0002 | UC-007 |
| `final_control_report` node | FR-015 | ADR-0001 | UC-008 |
| `devfix/runner.py` default context loading | FR-020 | ADR-0001 | PC-002 |
| `devfix/harness/execution/`, `--executor`, opencode adapter | FR-021, FR-022, FR-023 | ADR-0003 | PC-004 |
| external handoff packet with no direct code-edit tools | QR-002, QR-008, QR-009 | ADR-0003 | PC-004, PC-005 |
| `docs/`, `devfix/harness/prompts.py` | QR-001, QR-004, QR-005 | ADR-0001 | PC-006 |

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
