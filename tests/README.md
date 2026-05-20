# Test Guidance

This test suite checks the copied OpenCode workflow payload, especially agent prompts and reusable templates.

## Prompt Probe Assertions

Prefer behavior-level assertions over exact prompt wording.

Good assertions:

- canonical policy files exist and contain the detailed rule
- agents reference the relevant canonical policy or template family
- stages that must choose concrete files name those files
- stale or forbidden paths do not reappear

Avoid brittle assertions:

- requiring every downstream agent to repeat a specific support filename
- requiring all agents to use the same word for a concept, such as `layer`
- duplicating long policy text in prompt assertions
- testing verifier or reviewer prompts for files that should come from the packet

## File Naming Assertions

It is reasonable to assert exact paths when the path is the behavior under test, for example:

- canonical backlog location: `product-breakdown/06-evolution/backlog/`
- shared workflow policies: `workflow/control-policy.md`, `workflow/information-hygiene.md`, `workflow/review-output.md`
- packet-producing stages naming required implementation inputs

It is usually not reasonable to force exact support filenames into verifier, reviewer, or gate prompts. Those stages should validate control flags and packet-selected files rather than hard-coding every possible product-breakdown support file.

## Canonical Rule Location

Detailed rules should live in copied runtime context under `.opencode/templates/`.

Use:

- `.opencode/templates/product-breakdown/` for product-breakdown structure, decisions, and traceability
- `.opencode/templates/workflow/` for workflow control, information hygiene, and review-output rules

Tests should verify those canonical files and then verify that agents reference them.
