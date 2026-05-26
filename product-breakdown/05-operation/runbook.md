# Operational Product Requirements

This artifact captures durable operational behavior for the workflow package. Runnable operator steps live in [docs/operation.md](../../docs/operation.md).

## Requirements

- Operators must be able to run the workflow from a target repository after copying the runtime payload.
- Blocked work must preserve gate findings, stable gap identifiers, and the next required action for planner re-scoping.
- Revision loops must stop at the configured cap or no-improvement signal and return the decision to the human operator.
- Waiver handling must expose the named risk, waiver scope, follow-up or expiry condition, and user decision before completion.
- Stage feedback must be explicit when user input is required before continuing.
- Stage failures or unexpected output must have a conservative recovery path that preserves the guarded workflow contract.

## Product Boundaries

- The product does not support arbitrary individual stage reruns as an approved completion path.
- Improvement candidates reported during operation are backlog candidates only; they do not authorize current-task scope expansion.
- Operator escape hatches must not weaken the default planner-builder-reviewer-reporter path.

## Trace Links

- Operator-facing runbook: [docs/operation.md](../../docs/operation.md)
- Workflow control policy: [.opencode/dev_harness/workflow/control-policy.md](../../.opencode/dev_harness/workflow/control-policy.md)
- Architecture completion model: [product-breakdown/02-architecture/architecture.md](../02-architecture/architecture.md)
