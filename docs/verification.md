# Verification

## Smoke Suite

Run the repository smoke suite from the repository root:

```bash
pytest -q tests/test_opencode_workflow_probes.py
```

Run the sync helper tests:

```bash
pytest -q tests/test_sync_package.py
```

## What It Checks

- The copied `opencode.json` and `.opencode/` payload still loads in a temporary fixture project.
- The orchestrator routes the cleaner planner-builder-reviewer-reporter flow and improvement probes.
- Prompt references still point at the intended canonical template and policy files.
- The sync helper copies only payload files, writes a manifest, and prunes previously synced files that disappeared upstream.

## What To Expect

- The suite verifies the runtime package as shipped, not the source docs directly.
- On this repository it takes roughly a minute and a half.
- If you are changing prompt text or template references, read `tests/README.md` before adding exact string assertions.
