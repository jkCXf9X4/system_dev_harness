# Test Guidance

This test suite checks the copied OpenCode workflow payload, especially agent prompts and reusable templates.

Run the suite from the repository root:

```bash
pytest -q tests/test_opencode_workflow_probes.py
```

The fixture copies `opencode.json` and `.opencode/` into a temporary simple project, then runs `opencode run` probes against that copied payload. That means the tests are checking the runtime package as shipped, not the source docs directly.

Expect the suite to take roughly a minute or two because it exercises `opencode run` end to end.

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
- testing verifier or reviewer prompts for files that should come from the planner work order

## File Naming Assertions

It is reasonable to assert exact paths when the path is the behavior under test, for example:

- canonical backlog location: `product-breakdown/cross-cutting/06-evolution/candidates/`
- shared workflow policies: `workflow/control-policy.md`, `workflow/information-hygiene.md`, `workflow/review-output.md`
- work-order-producing stages naming required implementation inputs

It is usually not reasonable to force exact support filenames into verifier, reviewer, or gate prompts. Those stages should validate control flags and work-order-selected files rather than hard-coding every possible product-breakdown support file.

## Canonical Rule Location

Detailed rules should live in copied runtime context under `.opencode/dev_harness/`.

Use:

- `product-breakdown/` for the source documentation and traceability set, and `.opencode/dev_harness/product-breakdown/` for the copied runtime guidance used by agents
- `.opencode/dev_harness/workflow/` for workflow control, information hygiene, and review-output rules
- `.opencode/dev_harness_memories/` for repo-local workflow memory that should not be copied from the dev harness package

Tests should verify those canonical files and then verify that agents reference them.

## Extending Tests

- Add new smoke coverage in `tests/test_opencode_workflow_probes.py`.
- Prefer one assertion per behavior rather than one assertion per sentence in a prompt.
- Use exact paths only when the path is the behavior under test, such as a canonical source file or required runtime template.
- Avoid asserting full prompt text unless the whole string is the subject of the test.
