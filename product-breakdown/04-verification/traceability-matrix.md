# Traceability Matrix

This matrix maps high-level requirements to the verification artifacts that currently cover them.

## Coverage

| Layer | Verification artifact | Status |
| --- | --- | --- |
| Intent | Acceptance criteria review | Checked by `orchestrator-review-completeness` against the planner work order |
| Product | Commitment trace check | Checked by `orchestrator-review-completeness` and product-breakdown evidence when relevant |
| Architecture | Architecture guardrail review | `orchestrator-review-architecture` |
| Implementation | Implementation evidence | Reviewer-coordinated verifier helper |
| Workflow memory | Memory layer probe coverage | `tests/test_opencode_workflow_probes.py` plus reviewer/helper routing checks |
| Verification | Traceability matrix review | This file and per-file trace links |
| Operation | Runbook verification | Manual |
