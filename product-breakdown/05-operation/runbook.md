# Runbook

## Common Operational Tasks

### Running the Workflow

OpenCode in the target repository root:

```
opencode run "your task"
```

Or run interactively:

```
opencode
```

### Handling a Blocked Task

1. Read the gate output for blocking gaps and next required action.
2. The revision loop routes blocked results back to the planner automatically (up to 3 iterations).
3. After 3 iterations (or no-improvement detection), the human operator reviews the iteration history and decides next steps.

### Approving a Waiver

When the gate returns `waiver_required`:

1. Review the waiver request: named risk, waiver scope, follow-up/expiry condition.
2. Accept or reject the waiver in the conversation.
3. If accepted, the workflow completes with the waiver attached to the final report.
4. If rejected, the workflow routes as `blocked`.

### Re-running a Stage

If a stage fails or produces unexpected output, re-run the full workflow from the beginning. Individual stage re-runs are not supported — the workflow is designed to run end-to-end.