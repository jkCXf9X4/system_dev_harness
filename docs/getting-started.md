# Getting Started

## Minimum Prerequisites

- `opencode` available on `PATH`
- `pytest` available if you want to run the local smoke suite

## First Run

1. Copy `opencode.json` and `.opencode/` into the target repository root.
2. Run `opencode` for interactive work.
3. Run `opencode run "your task"` for a one-shot request.
4. From this repository, run `pytest -q tests/test_opencode_workflow_probes.py` to confirm the copied payload still loads.

## What Success Looks Like

- OpenCode starts from the `orchestrator` primary agent.
- The workflow uses the copied `.opencode/` payload, not the source `product-breakdown/` tree.
- The smoke suite passes before you publish a changed payload.

If `opencode` or `pytest` is missing, install them through the tooling used in your environment before copying the payload into a target repository.
