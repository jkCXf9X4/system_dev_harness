# Revision Loop Policy

Purpose: Governs the revision loop when the completion gate returns `blocked`.

When the completion gate returns `blocked`, the guarded workflow enters a revision loop:

1. **Iteration cap.** Default maximum of 3 revision attempts. The router may override this cap per-task by setting `max_revision_attempts` in the control flags.
2. **No-improvement detection.** If the same blocking gap IDs appear in consecutive iterations, escalate to the human operator immediately instead of looping again.
3. **Revision control flag.** When a revision is active, the `revision` control flag is set to `true` with the current iteration count (e.g., `revision: true, revision_count: 2`). This flag is carried from the gate through the planner to downstream stages so that selected helpers know the revision context.
4. **Evidence preservation.** All review findings from every iteration must be preserved and attached to the final report, regardless of whether the workflow completes, loops, or escalates.
5. **Escalation.** When the iteration cap is exceeded or no-improvement detection triggers, the workflow produces a `blocked_max_reached` status with full iteration history. A human operator decides the next action.

