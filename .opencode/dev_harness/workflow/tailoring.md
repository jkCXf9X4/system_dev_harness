# Tailoring

Purpose: Defines workflow tailoring profiles and selection rules.

The workflow must be tailored to the task and project context instead of applying the same process depth to every request. The planner must choose the lightest workflow profile that still covers the task's risk, uncertainty, and traceability needs, then record that choice in `tailoring_record`.

Use these baseline profiles:

- `lightweight` for low-risk documentation, metadata-only, or narrow no-code tasks with no architecture, external dependency, or major verification risk. When all concrete thresholds from `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` are met, stages may be skipped per the Lightweight Skip Rules defined there.
- `standard` for routine contained delivery tasks that need the full guarded chain but no exceptional escalation.
- `high_assurance` for behavior changes, cross-module changes, architecture or boundary changes, external uncertainty, revision-heavy work, large jobs, or other high-blast-radius tasks.

Tailoring may change helper depth, review emphasis, or whether optional helpers are invoked. Tailoring does not remove required stages, waive evidence requirements, or bypass review and gate rules. When a task uses a narrower or broader process than the default, the planner must explain why in the work order and plan summary. When `lightweight` profile is selected and all concrete thresholds from `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` are met, the planner work order must record which stages are skipped and why in the `tailoring_record`.

Source: extracted from `control-policy.md` §3 Tailoring.