# Task: Add Output Artifact Directory

Status: todo

Goal:
Write run artifacts to a dedicated directory so completed work is inspectable outside console output.

Current state:
- The CLI prints the final report to stdout.
- Artifacts remain in graph state and are not exported to the filesystem.
- There is no `--output-dir` option.

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

