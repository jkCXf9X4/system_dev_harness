# 04 Verification Layer — Cross-Cutting

This layer belongs to the **cross-cutting** decomposition. It describes how the product and system are proven to work.

## Contents

- `acceptance-criteria.md` — Verification strategy overview, 18 centralized acceptance criteria, and 5 validation criteria (VAL-001 through VAL-005) for user-need satisfaction
- `decisions/` — Verification-level decision records (VD-001 through VD-003)
- `test-strategy.md` — Overall verification approach
- `traceability-matrix.md` — Requirement-to-verification mapping

## Key Decisions

| ID | Title | Status |
|---|---|---|
| VD-001 | Verification Strategy Dual Pattern | Accepted |
| VD-002 | Acceptance Criteria As Verification Index | Accepted |
| VD-003 | Independent Review Requirement | Accepted |

## Related Artifacts

- Per-layer verification files: `fbs/00-intent/verification.md`, `fbs/01-product/verification.md`, `pbs/02-architecture/verification.md`, `pbs/03-implementation/verification.md`, `cross-cutting/05-operation/verification.md`, `cross-cutting/06-evolution/verification.md`
- Decision index: `system_definition/decision-log.md`
- Product tree: `system_definition/product-tree.md`