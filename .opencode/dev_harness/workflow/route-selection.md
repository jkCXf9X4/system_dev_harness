# Route Selection

Purpose: Separates the subject from the requested outcome for guarded workflow routing.

Planner output separates the subject from the requested outcome:

```text
issue_kind: bug|fix|regression|feature|docs|cleanup|refactor|tuning|architecture|workflow|review|other
requested_outcome: implement_now|capture_candidate
workflow_mode: delivery|candidate_capture
route: guarded_chain
```

Use `workflow_mode: delivery` when the user asks for actual changes now. Use `workflow_mode: candidate_capture` when the user asks for a proposal, recommendation, evaluation, discovery, review-only assessment, documented candidate, future task seed, or backlog item.

Bug, fix, regression, feature, documentation, cleanup, and refactoring subjects can all use `workflow_mode: candidate_capture` when the requested outcome is candidate capture. Do not use the subject alone to block candidate capture.

Repo-state review requests use the same split: review-and-change requests are delivery, while review-only assessment requests are candidate capture with either persisted candidates or a reviewed `no_candidate` result.

Both workflow modes use the same guarded chain: planner, builder, reviewer, reflection, and reporter. Validation runs as a reviewer-invoked parallel helper, not a separate serial stage. In `candidate_capture` mode, load `.opencode/dev_harness/workflow/candidate-capture.md` for detailed ownership, write-boundary, disposition, and review rules.

