# Task: Add Output Artifact Directory

Status: done

Goal:
Write run artifacts to a dedicated directory so completed work is inspectable outside console output.

Implemented:
- `--output-dir` exports a stable run manifest, final control report, execution session metadata, and numbered artifact files.
- Failed runs also export a failure manifest and the captured prompt for inspection.

Verification:
- `src/devfix/output.py` writes `run.json`, `final-control-report.md`, `execution-session.json`, and `artifacts/*.md`.
- Smoke-tested with synthetic data.
- The harness still prints the console summary.

Scope:
- Add a configurable output directory for each run.
- Write the final control report to a file.
- Write rendered artifacts and execution session metadata to files.
- Keep stdout output intact for interactive use.

Out of scope:
- Durable database persistence.
- Human approval interrupts.
- Built-in code editing.

Acceptance criteria:
- A run can be configured with an output directory.
- The run produces a stable file structure for report and artifact output.
- The written files preserve the execution session reference and final control decision.
- The existing console summary still works.
