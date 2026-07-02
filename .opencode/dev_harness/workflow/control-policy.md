# Workflow Control Policy — Master Index

Use this index for guarded workflow control, stage applicability, control flags, and waivers. Each section below either contains inline rules or points to the dedicated file for that topic.

## Required Stages

Every listed top-level guarded workflow stage must run:

```text
orchestrator-router
orchestrator-planner
orchestrator-builder
orchestrator-reviewer
orchestrator-reflection
orchestrator-reporter
```

Directed helper stages run when their owning top-level stage determines they are needed from task risk. Missing required top-level output blocks completion. Missing helper output blocks completion only when the owning stage declared that helper required or when the helper is mandatory under `.opencode/dev_harness/workflow/planner-triggers.md` (planner context) or `.opencode/dev_harness/workflow/reviewer-triggers.md` (reviewer context).

If a stage is not applicable, it must use the `not_applicable` fields from `.opencode/dev_harness/workflow/stage-output-schema.md`. Missing stage output or unjustified `not_applicable` blocks completion.

## Plan File Writing

The planner delegates plan file writing to `orchestrator-plan-file-writer` (see `.opencode/agents/orchestrator-plan-file-writer.md`). The planner has `edit/write: deny` and must not write plan files directly.

Plan file write verification (existence + non-empty) is performed by the plan-file-writer after each write. The builder performs a pre-consumption integrity check before loading the plan file.

## Route Selection → See `route-selection.md`

## Tailoring → See `tailoring.md`

## Stage Output Schema

Every top-level stage and directed helper returns the common fields from `.opencode/dev_harness/workflow/stage-output-schema.md`.

## Plan Draft Approval → See `plan-draft-approval.md`

## Initial Clarification Gate → See `clarification-gate.md`

## Candidate Capture Disposition

Any working stage or directed helper may return incidental `improvement_candidates` under `.opencode/dev_harness/workflow/stage-output-schema.md`. Detailed incidental candidate handling, candidate-capture criteria, and valid dispositions live in `.opencode/dev_harness/workflow/candidate-capture.md`.

Candidate capture uses the normal guarded chain:

```text
router -> planner -> builder -> reviewer -> reflection -> reporter
```

> **Note:** Validation runs as a reviewer-invoked parallel helper, not a separate serial stage. See `.opencode/agents/orchestrator-validation.md`.

Ownership:
- Planner scopes the candidate-capture work order and selects directed helpers.
- Builder is the only workflow stage that persists improvement backlog artifacts, and should write backlog-worthy candidates to file before returning its disposition.
- Reviewer gates candidate artifacts as information artifacts. For `persisted`, reviewer blocks when the candidate file is missing or not saved to disk. For `no_candidate`, reviewer checks the inspected scope, threshold rationale, and duplicate/backlog-worthiness evidence instead of requiring a file.
- Reflection handles durable memory triage only.
- Reporter summarizes the reviewed disposition.

## Workflow Memory

Load `.opencode/dev_harness/workflow/memory-and-lessons.md` when a stage needs task-relevant memory, memory curation, memory hygiene evidence, or final reflection memory-incorporation rules.

## Final Reflection

Every completed guarded workflow, including candidate capture, must run `orchestrator-reflection` before `orchestrator-reporter`. Detailed reflection and memory-incorporation rules live in `.opencode/dev_harness/workflow/memory-and-lessons.md`.

## Adaptive Risk Triggers

Load `.opencode/dev_harness/workflow/planner-triggers.md` when planner, builder, or reviewer decides which helpers are required, optional, or waived.

## Parallel Helper Execution

Load `.opencode/dev_harness/workflow/parallel-helper-execution.md` when planner or reviewer groups independent helpers into parallel-safe packets.

## Control Flags → See `control-flags.md`

## Handoff Boundary → See `handoff-boundary.md`

## Waivers → See `waivers.md`

## Revision Loop Policy → See `revision-loop.md`

## Task Tracking

Every task processed by the guarded workflow must have a task tracking file under `.opencode/dev_harness_tasks/`. The task tracking file provides continuous, stage-by-stage traceability across the full lifecycle.

### Required Task Tracking Stages

Every stage must update the task tracking file after completing its work:

```text
orchestrator-router     → creates the task tracking file
orchestrator-planner    → appends planner stage record
orchestrator-builder    → appends builder stage record
orchestrator-reviewer   → appends reviewer stage record
orchestrator-reflection → appends reflection stage record
orchestrator-reporter   → finalizes the task tracking file
```

### Task Tracking File Writing

The router delegates task tracking file creation to `orchestrator-task-tracker`. Each stage delegates task tracking file updates to `orchestrator-task-tracker`. The router has `edit/write: deny` and must not write task tracking files directly.

Task tracking file write verification (existence + non-empty) is performed by the task-tracker after each write.

### Schema → See `task-summary-schema.md`
