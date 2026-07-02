# Tailoring

Purpose: Defines workflow tailoring profiles and selection rules.

The workflow must be tailored to the task and project context instead of applying the same process depth to every request. The planner must choose the lightest workflow profile that still covers the task's risk, uncertainty, and traceability needs, then record that choice in `tailoring_record`.

Use these baseline profiles:

- `standard` for routine contained delivery tasks that need the full guarded chain but no exceptional escalation.
- `high_assurance` for behavior changes, cross-module changes, architecture or boundary changes, external uncertainty, revision-heavy work, large jobs, or other high-blast-radius tasks.

Tailoring may change helper depth, review emphasis, or whether optional helpers are invoked. Tailoring does not remove required stages, waive evidence requirements, or bypass review and gate rules. When a task uses a narrower or broader process than the default, the planner must explain why in the work order and plan summary.

