# Decision Log

| ID | Title | Layer | Status | Location | Related artifacts |
| --- | --- | --- | --- | --- | --- |
| AD-001 | Use OpenCode Agent Workflow For Orchestration | Architecture | Accepted | `system_definition/pbs/02-architecture/decisions/AD-001-use-opencode-agent-workflow-for-orchestration.md` | Product commitments PC-001 through PC-010, Use cases UC-001 through UC-014 |
| AD-002 | Use Versioned Markdown For Traceable Context | Architecture | Accepted | `system_definition/pbs/02-architecture/decisions/AD-002-use-versioned-markdown-for-traceable-context.md` | PC-003, PC-006, PC-007, UC-001, UC-004, UC-009 |
| AD-003 | Use Structured Handoff Before Code Editing | Architecture | Accepted | `system_definition/pbs/02-architecture/decisions/AD-003-use-structured-handoff-before-code-editing.md` | PC-001, PC-004, PC-005, UC-005, UC-006, UC-007, UC-008 |
| AD-004 | Decline Adding Agent SKILLS To Primary Agents | Architecture | Declined | `system_definition/pbs/02-architecture/decisions/AD-004-decline-adding-agent-skills-to-primary-agents.md` | KM-004, UC-001 through UC-014 |
| AD-005 | Use Fresh Helper Handoffs For Context Rot | Architecture | Accepted | `system_definition/pbs/02-architecture/decisions/AD-005-use-fresh-helper-handoffs-for-context-rot.md` | PC-003, PC-006, PC-007, UC-004, UC-009 |
| IMD-001 | Use Versioned Markdown For Mistake Memory | Implementation | Accepted | `system_definition/pbs/03-implementation/decisions/IMD-001-use-versioned-markdown-for-mistake-memory.md` | PC-003, PC-006, UC-004, UC-009 |
| IMD-002 | Copy System Definition Guidance Into Agent Payload | Implementation | Accepted | `system_definition/pbs/03-implementation/decisions/IMD-002-copy-product-breakdown-guidance-into-agent-payload.md` | PC-006, PC-007 |
| IMD-003 | Use Repo-Local Workflow Memory For Durable Lessons | Implementation | Accepted | `system_definition/pbs/03-implementation/decisions/IMD-003-use-repo-local-workflow-memory.md` | PC-003, PC-006, PC-007, UC-004, UC-009 |
| IMD-004 | Copy Architecture Artifacts Into Agent Payload | Implementation | Accepted | `system_definition/pbs/03-implementation/decisions/IMD-004-copy-architecture-artifacts-into-agent-payload.md` | PC-006, PC-007, AD-001, AD-002, AD-005 |
| IMD-005 | Rename product-breakdown/ to system_definition/ | Implementation | Accepted | `system_definition/pbs/03-implementation/decisions/IMD-005-rename-product-breakdown-to-system-definition.md` | PC-006, PC-007, IMP-033, PD-001, IMD-002, IMD-004 |
| ED-001 | Use Evolution Backlog For Improvement Candidates | Evolution | Accepted | `system_definition/cross-cutting/06-evolution/decisions/ED-001-use-evolution-backlog-for-improvement-candidates.md` | PC-006, PC-009, UC-012, `system_definition/cross-cutting/06-evolution/candidates/`, `system_definition/cross-cutting/06-evolution/roadmap.md`, `system_definition/cross-cutting/06-evolution/risks.md` |
| PD-001 | System Definition Structure Rationale | Product | Accepted | `system_definition/fbs/01-product/decisions/PD-001-product-breakdown-structure-rationale.md` | `system_definition/README.md`, `system_definition/breakdown-structures.md`, `system_definition/product-tree.md`, `system_definition/decision-placement.md` |
| PD-002 | Guided Workflow As Product Boundary | Product | Accepted | `system_definition/fbs/01-product/decisions/PD-002-guided-workflow-as-product-boundary.md` | `system_definition/README.md`, `architecture.md`, `implementation.md` |
| PD-003 | Verification Before Completion Gating | Product | Accepted | `system_definition/fbs/01-product/decisions/PD-003-verification-before-completion-gating.md` | `architecture.md`, `implementation.md`, `orchestrator-reviewer.md`, `control-policy.md`, `adaptive-risk-triggers.md` |
| VD-001 | Verification Strategy Dual Pattern | Verification | Accepted | `system_definition/cross-cutting/04-verification/decisions/VD-001-verification-strategy-dual-pattern.md` | `acceptance-criteria.md`, per-layer `verification.md` files |
| VD-002 | Acceptance Criteria As Verification Index | Verification | Accepted | `system_definition/cross-cutting/04-verification/decisions/VD-002-acceptance-criteria-as-verification-index.md` | `acceptance-criteria.md`, `test-strategy.md`, `traceability-matrix.md` |
| VD-003 | Independent Review Requirement | Verification | Accepted | `system_definition/cross-cutting/04-verification/decisions/VD-003-independent-review-requirement.md` | `orchestrator-reviewer.md`, `control-policy.md`, `agent-boundaries.md`, `architecture.md`, `adaptive-risk-triggers.md` |
| OD-001 | Dev Harness As Portable Payload | Operation | Accepted | `system_definition/cross-cutting/05-operation/decisions/OD-001-dev-harness-as-portable-payload.md` | `pyproject.toml`, `implementation.md`, `deployment-process.md`, package `README.md` |
| OD-002 | Repo-Local Workflow Memory | Operation | Accepted | `system_definition/cross-cutting/05-operation/decisions/OD-002-repo-local-workflow-memory.md` | `.opencode/dev_harness_memories/`, `orchestrator-memory.md`, `orchestrator-memory-curator.md`, `implementation.md` |
| OD-003 | No External Build Tooling | Operation | Accepted | `system_definition/cross-cutting/05-operation/decisions/OD-003-no-external-build-tooling.md` | `pyproject.toml`, `architecture.md`, `implementation.md`, `deployment-process.md` |

## Maintenance

Update this index when a decision file is added, renamed, superseded, or deprecated.
