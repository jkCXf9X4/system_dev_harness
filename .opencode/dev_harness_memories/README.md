# Dev Harness Memories

This directory stores repo-local workflow memory that should not be copied from the dev harness package.

Keep durable lessons, reusable patterns, and decision pointers here so updates to the copied `.opencode/dev_harness/` tree do not overwrite local memory.

## Memory Schema

Every memory entry should carry lightweight trust metadata so future agents can tell whether the entry is still applicable:

- `scope`: the narrow context where the entry applies
- `source`: the evidence, decision, or run that produced it
- `last_verified`: the most recent date or evidence reference that confirmed it
- `confidence`: a short confidence or applicability note
- `revalidation_trigger`: what should cause a future agent to re-check it
- `environment_notes`: paths, commands, versions, or other environment-specific details when relevant

Treat memory as durable guidance, not as a substitute for checking current files or commands when the task is sensitive to drift.

## Destination Matrix

| Knowledge type | Home | Notes |
| --- | --- | --- |
| Stable fact or decision pointer | `lessons.md` | Keep it concise and reviewable. |
| Repeated failure or prevention rule | `lessons.md` | Include a completion check and revalidation trigger. |
| Reusable operating procedure | `patterns.md` | Prefer this over storing large procedural notes as lessons. |
| Durable decision pointer | `lessons.md` or `patterns.md` | Attach the pointer to the closest relevant entry instead of creating a separate history note. |
| Broad future work | Improvement backlog | Do not store backlog candidates as memory. |
| One-off task evidence or run summary | Final report or task history | Keep task-local evidence out of durable memory. |
