# Candidate Capture

Use this policy only when the planner sets `workflow_mode: candidate_capture`.

Review-only repo-state assessments use candidate capture when the user asks for findings, evaluation, recommendation, or future task seeds instead of immediate changes. The builder should persist every backlog-worthy finding to disk, or return `no_candidate` when the inspected scope does not justify a backlog artifact.

Incidental `improvement_candidates` raised during normal delivery are backlog candidates only. They do not authorize scope expansion, current-task implementation, direct approval, skipped checks, or persistence by the stage that found them.

If an incidental candidate reaches final reporting without a candidate-capture disposition, the reporter must return `user_feedback_required: true` and request a follow-up `workflow_mode: candidate_capture` run instead of treating the suggestion as persisted.

Candidate capture uses the normal guarded chain:

```text
planner -> builder -> reviewer -> reflection -> reporter
```

## Ownership

- Planner scopes the candidate-capture work order and selects directed helpers.
- Builder is the only workflow stage that persists improvement backlog artifacts, and should write backlog-worthy candidates to file before returning its disposition.
- Reviewer gates candidate artifacts as information artifacts and blocks when a backlog-worthy finding was reported but not saved to disk.
- Reflection handles durable memory triage only.
- Reporter summarizes the reviewed disposition.

## Builder Write Boundary

Builder should write backlog-worthy candidates to disk, but may write only:

- `product-breakdown/06-evolution/candidates/IMP-NNN.md`
- `product-breakdown/06-evolution/selected/IMP-NNN.md`
- `product-breakdown/06-evolution/done/IMP-NNN.md`
- `product-breakdown/06-evolution/README.md`

Do not edit implementation files during candidate capture.

## Persistence Rules

- Load `.opencode/dev_harness/product-breakdown/templates/improvement-backlog-overview-template.md`.
- Load `.opencode/dev_harness/product-breakdown/templates/improvement-candidate-template.md`.
- Create and save a candidate file when the item has concrete evidence, meaningful impact, and a scoped future task seed.
- Do not create a placeholder file when no backlog-worthy item exists; return `no_candidate` with inspected scope and rationale.
- Check duplicates across `candidates/`, `selected/`, `done/`, and existing historical `evaluations/` before choosing the next `IMP-NNN`.
- Keep candidate files proposed only; do not imply implementation approval.

## Required Evidence

- source evidence inspected
- backlog-worthiness threshold decision
- duplicate-check result
- candidate ID and file path, or `no_candidate` rationale
- product-breakdown layer placement
- information hygiene checks for overview tables, stale references, duplicate content, orphaned artifacts, unresolved links, and traceability

## Valid Dispositions

- `persisted` with candidate ID and candidate file path
- `no_candidate` with inspected scope and rationale
