# Subagent Lifecycle Policy

Use this policy when a stage considers sending follow-up work to an existing directed helper or starting a fresh helper context.

The workflow cannot force compaction, clearing, pruning, or reset of another agent's conversation context. Context freshness is therefore controlled by lifecycle choice: reuse the existing helper only when its accumulated context is still valuable, or start a fresh helper with a compact handoff when accumulated context is more likely to harm the result.

## Reuse Existing Helper

Reuse an existing helper only when all of these are true:

- the next task directly depends on the helper's current private context
- the helper stayed inside its assigned role and scope
- the task objective has not materially shifted
- the prior helper conversation is likely to improve correctness
- the stage can state why a fresh handoff would lose useful evidence

## Start Fresh

Start fresh when any of these are true:

- the task shifted materially
- the helper has received repeated corrections
- the helper repeats stale assumptions
- the helper output becomes vague, inconsistent, or over-broad
- unrelated topics have passed through the same helper context
- a compact handoff would be clearer than accumulated history

When starting fresh, do not pass prior transcripts. Pass only the current objective, relevant evidence, constraints, decisions, and deliverable. Treat the prior helper output as evidence to summarize, not as hidden memory to preserve.

## Lifecycle Decision

Before invoking a helper after earlier helper work, the owning stage should record:

```text
helper_lifecycle:
  reuse_decision: reuse_existing|start_fresh|not_applicable
  reason: <why this lifecycle choice fits the next helper task>
  prior_context_dependency: none|low|medium|high
  context_rot_risk: low|medium|high
  handoff_summary: <compact summary for a fresh helper, or not_applicable>
```

Use `not_applicable` for first-time helper calls or direct work with no helper reuse decision.

## Fresh Helper Handoff

Use this compact handoff shape when starting fresh:

```text
fresh_helper_handoff:
  objective: <current helper objective>
  relevant_files: <paths or none>
  known_state: <current evidence and status>
  decisions_made: <stable decisions already made, or none>
  constraints: <scope, permissions, non-destructive requirements, and verification limits>
  non_goals: <what the helper must not do>
  deliverable: <exact output expected>
  verification_or_review_focus: <checks, review lens, or not_applicable>
```

Important facts that must survive beyond a helper run belong in stage outputs, product-breakdown artifacts, workflow memory, or explicit handoffs. Do not rely on long-lived helper conversation history as durable state.
