# Operation

## Running the Workflow

Run the workflow in the target repository root:

```bash
opencode run "your task"
```

Or start an interactive session:

```bash
opencode
```

## Handling a Blocked Task

1. Read the gate output for blocking gaps and the next required action.
2. Let the revision loop route blocked results back to the planner.
3. After the revision cap or a no-improvement signal, review the iteration history and decide whether to rescope or stop.

## Handling Stage Feedback

Every top-level stage can return `user_feedback_required`. When it does, answer the specific `user_feedback_request` before the chain continues. Treat `improvement_candidates` as backlog candidates only; they are not approval to expand the current task.

## Approving a Waiver

When the gate returns `waiver_required`:

1. Review the named risk, waiver scope, and follow-up or expiry condition.
2. Accept or reject the waiver in the conversation.
3. If accepted, the workflow completes with the waiver attached to the final report.
4. If rejected, the workflow routes as `blocked`.

## Re-running a Stage

If a stage fails or produces unexpected output, rerun the full workflow from the beginning. Individual stage reruns are not supported.
