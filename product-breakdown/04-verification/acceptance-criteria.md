# Acceptance Criteria

The workflow package must satisfy these high-level acceptance criteria:

- Every guarded workflow run produces a planner-owned work order with verifiable checks.
- Every change is independently reviewed before completion.
- Every completed guarded workflow run performs final reflection before reporting so durable memory incorporation is explicitly accepted, rejected, deferred, or marked not applicable.
- Workflow memory includes trust metadata, revalidation cues, and an explicit boundary between durable memory, task-local evidence, run history, and improvement backlog items.
- Memory curation reports a concrete decision taxonomy, and review/report outputs surface memory hygiene whenever memory influenced the task.
- Reviewer findings are actionable (blocked findings route back to planner per the revision loop).
- Stale references, status trackers, duplicates, superseded content, unresolved links, traceability, and orphaned artifacts are reconciled before completion.
- Improvement candidates are persisted to `product-breakdown/06-evolution/candidates/` by the improvement workflow or focused evaluator without changing implementation files.
- Bug, fix, regression, feature, and documentation subjects route to improvement when the user asks for proposal, evaluation, candidate, future-task-seed, or backlog capture instead of implementation.
- Working agents can trigger focused improvement evaluation, while the primary orchestrator cannot invoke the focused evaluator directly.
- Product source information, scope, stable decisions, and traceability remain in `product-breakdown/`.
- Runnable guidance, examples, install/deploy instructions, verification commands, and contributor workflow remain in `docs/` without duplicating product text.
