# Acceptance Criteria

The workflow package must satisfy these high-level acceptance criteria:

- Every guarded workflow run produces a planner-owned work order with verifiable checks.
- Planner and reviewer stages identify parallel-safe helper packets for independent helper work and preserve dependencies, expected outputs, and file write sets.
- Every change is independently reviewed before completion.
- Every completed guarded workflow run performs final reflection before reporting so durable memory incorporation is explicitly accepted, rejected, deferred, or marked not applicable.
- Workflow memory includes trust metadata, revalidation cues, and an explicit boundary between durable memory, task-local evidence, run history, and improvement backlog items.
- Memory curation reports a concrete decision taxonomy, and review/report outputs surface memory hygiene whenever memory influenced the task.
- Product-breakdown source docs define the canonical storage mechanism for product rationale, runtime prompts, dev harness context, workflow memory, improvement backlog items, task-local evidence, skills/plugins, and external research.
- Reviewer findings are actionable (blocked findings route back to planner per the revision loop).
- Stale references, status trackers, duplicates, superseded content, unresolved links, traceability, and orphaned artifacts are reconciled before completion.
- Repo-state review tasks either produce trace-preserving updates or a reviewed no-change/backlog result that records stale, duplicated, conflicting, or orphaned findings.
- Backlog-worthy improvement candidates are persisted to `product-breakdown/cross-cutting/06-evolution/candidates/` by builder candidate-capture mode before the builder returns, without changing implementation files.
- Every deliberate candidate-capture run receives a reviewed disposition before final reporting: accepted candidate or no candidate.
- Bug, fix, regression, feature, and documentation subjects use `workflow_mode: candidate_capture` when the user asks for proposal, evaluation, candidate, future-task-seed, or backlog capture instead of implementation.
- Working agents can surface incidental improvement candidates without persisting them; deliberate persistence requires a candidate-capture work order.
- Product source information, scope, stable decisions, and traceability remain in `product-breakdown/`.
- Runnable guidance, examples, install/deploy instructions, verification commands, and contributor workflow remain in `docs/` without duplicating product text.
- Review-only repo-state assessment requests use `workflow_mode: candidate_capture`; review-and-change requests use `workflow_mode: delivery`.
