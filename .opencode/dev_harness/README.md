# Dev Harness

This directory holds reusable workflow context that is copied into development repos along with the active payload.

## Layout

- `prompts/` - reusable prompt templates mapped to the workflow use cases.
- `systems_engineering/` - layered systems-engineering guidance split into small files for agent use.
- `workflow/` - shared workflow control, information hygiene, and review-protocol.md policies.
- `dev_harness_memories/` - repo-local workflow memory that should not be copied from the dev harness package.

## Usage

Keep this dev harness context versioned in the package repo, then copy `.opencode/` and `opencode.json` into the target development repo when you want to use the workflow.

For systems-engineering work, start with `systems_engineering/README.md` and load only the specific layer, decision, naming, or traceability file needed for the task.

For guarded workflow behavior, use `workflow/control-policy.md`, `workflow/information-hygiene.md`, `workflow/subagent-lifecycle.md`, and `workflow/review-protocol.md` instead of duplicating those rules in agent prompts. The canonical memory files live under `dev_harness_memories/`.
