# Task: Add Durable Runs

Status: todo

Goal:
Persist workflow runs beyond a single process lifetime so they can be resumed and reviewed later.

Current state:
- The graph uses `InMemorySaver`.
- Runs require a thread id, but the state is lost when the process exits.
- There is no run history view.

Scope:
- Add a durable checkpointer, with SQLite as the local baseline.
- Preserve run state across process restarts.
- Record inspectable run history.
- Support restart and resume from a previous run.
- Allow comparison with prior runs.

Out of scope:
- External issue tracker integration.
- Built-in code editing.

Acceptance criteria:
- A run can be resumed after process restart.
- Prior runs are discoverable and inspectable.
- The persisted state is sufficient to continue workflow execution without reconstructing the run manually.

