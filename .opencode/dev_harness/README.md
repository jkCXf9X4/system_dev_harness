# Dev Harness

This directory holds reusable workflow context that is copied into development repos along with the active payload.

## Layout

- `prompts/` - reusable prompt templates mapped to the workflow use cases.
- `product-breakdown/` - layered product breakdown guidance split into small files for agent use.
- `workflow/` - shared workflow control, information hygiene, known-mistakes memory, and review-output policies.

## Usage

Keep this dev harness context versioned in the package repo, then copy `.opencode/` and `opencode.json` into the target development repo when you want to use the workflow.

For product breakdown work, start with `product-breakdown/README.md` and load only the specific layer, decision, naming, or traceability file needed for the task.

For guarded workflow behavior, use `workflow/control-policy.md`, `workflow/information-hygiene.md`, `workflow/known-mistakes.md`, and `workflow/review-output.md` instead of duplicating those rules in agent prompts.
