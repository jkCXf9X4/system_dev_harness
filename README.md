# OpenCode Workflow Package

Portable OpenCode workflow package for guarded agentic development.

Start here: [docs/README.md](docs/README.md)

Quick start:

1. Copy `opencode.json` and `.opencode/` into the target repository root.
2. Run `opencode` for interactive use or `opencode run "your task"` for one-shot work.
3. Run `pytest -q tests/test_opencode_workflow_probes.py` from this repository to verify the shipped payload.

Local sync helper:

```bash
python -m pip install -e .
system-dev-harness-sync
```
