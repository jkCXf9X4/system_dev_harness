# Acceptance Criteria

The workflow package must satisfy these high-level acceptance criteria:

- Every guarded workflow run produces a planner-owned work order with verifiable checks.
- Every change is independently reviewed before completion.
- Reviewer findings are actionable (blocked findings route back to planner per the revision loop).
- Stale references, duplicates, and orphaned artifacts are reconciled before completion.
- Improvement candidates are persisted to `product-breakdown/06-evolution/backlog/` by the improvement workflow without changing implementation files.
- The `docs/` tree remains aligned with the operator-facing documentation hierarchy and the product-breakdown source tree.
