# Task: Add Human Approval Gates

Status: todo

Goal:
Introduce explicit pause and resume checkpoints so a human can inspect and edit state before the workflow continues.

Current state:
- The graph uses in-memory checkpointing.
- The workflow has a `human_interrupt` schema, but there is no user-facing pause/resume flow.
- Completion routing is deterministic, but it is not interactive.

Scope:
- Add explicit approval checkpoints in the workflow.
- Support pause and resume behavior across those checkpoints.
- Allow the user to inspect and adjust state before continuing.
- Make the approval points obvious in the final report and run artifacts.

Out of scope:
- Durable persistence across process restarts.
- Built-in code editing.

Acceptance criteria:
- The workflow can pause at a named approval point.
- A human can resume the workflow after inspection or edits.
- The run preserves enough state to continue without recomputing the entire flow.
- The approval points are visible in the output artifacts.

