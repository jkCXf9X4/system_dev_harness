# Product Commitments

Product commitments translate the product vision into durable promises the workspace should preserve across implementation changes.

They are more stable than implementation plans and more concrete than vision statements. They should not describe package names, function names, or execution details.

## Commitments

| ID | Commitment | Trace |
| --- | --- | --- |
| PC-001 | The workspace shall keep development anchored to an explicit task contract. | Vision, UC-001, UC-002 |
| PC-002 | The workspace shall make architecture and requirement drift visible before work is considered complete. | Vision, UC-003, UC-007, UC-008 |
| PC-003 | The workspace shall use persistent mistake memory to reduce repeated correction loops. | Vision, UC-004, UC-009 |
| PC-004 | The workspace shall separate execution from approval so coding output is reviewed against evidence. | Vision, UC-006, UC-007, UC-008 |
| PC-005 | The workspace shall require incomplete work to be blocked or explicitly waived rather than silently accepted. | Vision, UC-008 |
| PC-006 | The workspace shall keep design rationale and touched artifacts traceable through Intent -> Product Commitments -> System Architecture -> Technical Decisions -> Implementation -> Verification, and shall reconcile stale, duplicate, superseded, or orphaned information before completion. | Vision, UC-010 |
| PC-007 | The workspace shall express workflow behavior through repository-local OpenCode agents and config rather than hidden runtime code. | Vision, UC-001, UC-005, UC-006 |
| PC-008 | The workspace shall require architecture work to evaluate modularity, simplicity, readability, and module responsibility fit. | Vision, UC-003, UC-011 |
| PC-009 | The workspace shall run continuous improvement as a separate exploratory workflow that feeds backlog candidates without expanding contained feature diffs. | Vision, UC-009, UC-012 |
| PC-010 | The workspace shall allow direct operator-chosen build execution outside the orchestrator path without letting the orchestrator omit guarded workflow stages. | Vision, UC-001, UC-013 |

## Trace Links

- PC-001 satisfies the governed contract loop in the vision.
- PC-002 satisfies architecture preservation and visible drift detection.
- PC-003 satisfies persistent lesson memory.
- PC-004 satisfies reviewer approval over self-assessed completion.
- PC-005 satisfies explicit waivers over silent requirement loss.
- PC-006 satisfies KM-005 traceability, artifact lineage, and information hygiene.
- PC-007 satisfies OpenCode-native workflow definitions.
- PC-008 satisfies active design quality stewardship during architecture work.
- PC-009 satisfies deliberate codebase improvement from current delivery pressure while preserving scoped implementation and verification.
- PC-010 satisfies explicit direct build use while preserving orchestrator guardrails.
