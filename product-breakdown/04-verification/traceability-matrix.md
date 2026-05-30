# Traceability Matrix

This matrix maps the current product commitments to the verification evidence used to prove them.

## Coverage

| Concern | Source artifacts | Verification evidence | Status |
| --- | --- | --- | --- |
| Task contract and scope discipline | `product-breakdown/00-intent/use-cases.md`, `product-breakdown/01-product/product-commitments.md` | `orchestrator-contract.md`, `orchestrator-packet.md`, `tests/test_opencode_workflow_probes.py::test_contract_stage_smoke` | Covered |
| Architecture guardrails and no-shortcut routing | `product-breakdown/02-architecture/architecture.md`, AD-001 through AD-003 | `orchestrator-architecture.md`, `orchestrator-review-architecture.md`, `tests/test_opencode_workflow_probes.py::test_decision_templates_are_generic_and_referenced`, `tests/test_opencode_workflow_probes.py::test_orchestrator_does_not_route_shortcut_build` | Covered |
| Review gating and completion decision | PC-004, PC-005, UC-007, UC-008 | `orchestrator-reviewer.md`, independent review outputs, revision loop policy, gate decision | Covered |
| Information hygiene and traceability | PC-006, AD-002, IMD-001, `.opencode/dev_harness/workflow/information-hygiene.md` | `orchestrator-builder.md`, `orchestrator-verifier.md`, `tests/test_opencode_workflow_probes.py::test_information_hygiene_is_workflow_gated` | Covered |
| Continuous improvement and backlog persistence | PC-009, UC-012, ED-001, IMD-002 | `orchestrator-improvement.md`, `product-breakdown/06-evolution/backlog/`, `tests/test_opencode_workflow_probes.py::test_improvement_stage_smoke` | Covered when improvement workflow runs |
| Final reporting and research support | `orchestrator-reporter.md`, `orchestrator-researcher.md` | final control report, external documentation or dependency context when needed | Covered |

## Maintenance

Refresh this matrix when a new commitment, decision, agent stage, or verification artifact changes the evidence chain.
