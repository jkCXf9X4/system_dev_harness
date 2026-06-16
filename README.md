# System Dev Harness

A portable OpenCode workflow package that adds a structured pipeline around agentic software development.

When a request comes in, the system routes it through a series of specialized agents: a planner clarifies the task into a work order, a builder implements the changes, and a reviewer checks the result against multiple criteria — completeness, architecture constraints, test coverage, and past lessons. If issues are found, the task goes back for revision. A completion gate determines the outcome: approved, blocked, or requiring a waiver.

The workflow is defined entirely within `.opencode/`, which contains agent definitions and policy documents. It ships as two artifacts — `opencode.json` and the `.opencode/` directory — that can be copied into any repository. A small Python helper handles syncing the payload into downstream repos. An explicit escape hatch allows direct use of OpenCode's native build agent for small tasks, without weakening the default guarded path.

This project is designed for teams who want more oversight and repeatability when using AI coding agents, without blocking the ability to bypass the workflow for straightforward changes.

## Quick start

1. Copy `opencode.json` and `.opencode/` into the target repository root.
2. Run `opencode` for interactive use or `opencode run "your task"` for one-shot work.
3. Run `pytest -q tests/test_opencode_workflow_probes.py` from this repository to verify the shipped payload.

## Local sync helper

```bash
python -m pip install git+https://github.com/jkCXf9X4/system_dev_harness.git
system-dev-harness-sync
```

## Further reading

- [docs/README.md](docs/README.md) — detailed documentation