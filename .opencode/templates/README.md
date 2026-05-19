# Templates

This directory holds reusable workflow templates that are copied into development repos along with the active payload.

## Layout

- `prompts/` - reusable prompt templates mapped to the workflow use cases.
- `others/` - supporting templates that are not prompts, such as the improvement backlog template.

## Usage

Keep these templates versioned in the package repo, then copy `.opencode/` and `opencode.json` into the target development repo when you want to use the workflow.
