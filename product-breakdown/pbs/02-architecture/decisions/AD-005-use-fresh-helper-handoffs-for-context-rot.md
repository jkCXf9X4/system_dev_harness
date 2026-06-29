# AD-005: Use Fresh Helper Handoffs For Context Rot

## Status

Accepted

## Context

Long-running helper or subagent sessions can accumulate stale assumptions, unrelated details, and corrective turns. The runtime does not expose a parent-controlled mechanism to compact, clear, prune, or reset another agent's conversation context.

## Decision

Manage context freshness at the workflow-policy layer. Owning stages should reuse an existing helper only when its prior context is still directly useful. When accumulated context is suspect, the owning stage starts a fresh helper context and passes a compact handoff containing only the current objective, relevant evidence, decisions, constraints, non-goals, and requested deliverable.

## Consequences

- Positive: The workflow does not depend on unavailable runtime context-control APIs.
- Positive: Important state is promoted into visible stage outputs, product-breakdown artifacts, workflow memory, or explicit handoffs instead of hidden helper history.
- Negative: Some helper context may need to be summarized again when starting fresh.

## Traceability

- Dev-harness workflow - `.opencode/dev_harness/workflow/subagent-lifecycle.md` defines helper reuse, fresh-helper triggers, and compact handoff fields.
- Stage prompts - planner, builder, reviewer, and reflection reference the lifecycle policy before helper follow-up work.
