# Traceability Matrix

This matrix maps high-level requirements to the verification artifacts that currently cover them.

## Coverage

| Layer | Verification artifact | Status |
| --- | --- | --- |
| Intent | Acceptance criteria review | Checked by `orchestrator-review-completeness` against the planner work order |
| Product | Commitment trace check | Checked by `orchestrator-review-completeness` and product-breakdown evidence when relevant |
| Architecture | Architecture guardrail review | `orchestrator-review-architecture` |
| Implementation | Implementation evidence | Reviewer-coordinated verifier helper |
| Workflow memory | Memory schema, decision taxonomy, and ownership probes | `tests/test_opencode_workflow_probes.py::test_workflow_memory_layer_is_versioned_and_scoped` plus reviewer, reflection, curator, and reporter routing checks |
| Verification | Traceability matrix review | This file and per-file trace links |
| Operation | Runbook verification | Manual |
