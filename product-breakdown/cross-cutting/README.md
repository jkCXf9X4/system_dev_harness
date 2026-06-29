# Cross-Cutting Artifacts

This directory groups artifacts that span both the Functional Breakdown Structure (FBS) and the Product Breakdown Structure (PBS). These transversal layers verify, operate, and evolve the system without belonging exclusively to the functional or physical decomposition.

## Contents

| Layer | Description |
| --- | --- |
| `04-verification/` | Acceptance criteria, test strategy, and traceability matrix — verification is a per-level horizontal view |
| `05-operation/` | Operational requirements, deployment constraints, and runbook requirements |
| `06-evolution/` | Improvement lifecycle: candidates, selected, done, roadmap, risks, and changelog |

## Relationship to FBS and PBS

Cross-cutting layers connect functional requirements (FBS) to physical implementation (PBS):

- **Verification** criteria are per-PBS-layer horizontal views while the overall strategy is cross-cutting.
- **Operation** requirements respond to functional needs for availability, reliability, and maintainability.
- **Evolution** candidates derive from functional gaps and manage the physical improvement lifecycle.

## Links

- [FBS directory](../fbs/README.md) — functional architecture
- [PBS directory](../pbs/README.md) — physical architecture
- [Breakdown structures](../breakdown-structures.md) — FBS/PBS/WBS relationship model