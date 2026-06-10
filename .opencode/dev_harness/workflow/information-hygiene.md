# Information Hygiene

Use this policy when work creates, moves, renames, rewrites, supersedes, or otherwise changes information artifacts.

## Required Evidence

Information hygiene evidence must cover:

- parent context for every new or changed artifact
- replaced or superseded information
- stale references checked or fixed
- duplicate content removed or reconciled
- orphaned artifacts checked or removed
- unresolved links checked or fixed
- traceability from source context to final artifact

## Stage Responsibilities

- Planner-owned work order declares whether the task touches information artifacts and what hygiene evidence is required.
- Planner-owned work order carries the required checks and affected artifacts to implementation, using helper output when helpers were selected.
- Builder performs cleanup directly or through the builder-owned `orchestrator-cleanup` helper, then reports what changed.
- `orchestrator-cleanup` handles focused reference patching, status tracker updates, duplicate or superseded content reconciliation, orphaned artifact removal, unresolved link checks, and traceability cleanup inside the approved builder scope.
- Reviewer-coordinated verifier checks the evidence against the work order control flags.
- Review helpers fail missing, partial, or contradictory evidence.
- Reviewer gate blocks completion when required hygiene evidence is missing.

## Plans Directory Exemption

The `.opencode/dev_harness_plans/` directory stores standardized plan summaries for every implementation task as local archive records.

- It is **volatile local content**, NOT part of the implementation artifact graph.
- Information-hygiene checks do NOT require reference patching, duplicate reconciliation, or stale-link cleanup across plan files.
- The planner writes the complete plan summary file, including draft approval fields, and MUST verify the write succeeded.
- The reviewer SHOULD still check archive integrity for the current task:
  1. A plan file exists for the current task.
  2. The plan file contains all required fields from `.opencode/dev_harness/workflow/plan-summary-schema.md`.
  3. The timestamp is recent and matches the current execution session.
