# Prompt Policy Extraction Tasks

## Objective

Reduce duplicated agent prompt responsibilities by moving shared workflow rules into focused policy files that agents load only when relevant.

## Tasks

1. Extract common stage return fields into `.opencode/dev_harness/workflow/stage-output-schema.md`.
2. Extract read/write, scope, and no-edit boundaries into `.opencode/dev_harness/workflow/agent-boundaries.md`.
3. Extract system-definition loading, placement, traceability, and decision-record rules into `.opencode/dev_harness/workflow/product-breakdown-work.md`.
4. Move incidental improvement candidate handling into `.opencode/dev_harness/workflow/candidate-capture.md`.
5. Trim agent prompts to reference shared policy files instead of duplicating policy text.
6. Update workflow probes so future prompt changes preserve the extracted boundaries.

## Completion Criteria

- Agents keep role-specific responsibilities locally.
- Shared policy language has one canonical owner.
- Candidate capture, memory, helper selection, parallel helper execution, output schema, boundaries, and system-definition rules are separately loadable.
- Workflow probes pass.
