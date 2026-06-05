# Architecture Guidance

Use this guidance when a task needs architecture guardrails, boundary checks, or durable design review.

## Shared Architecture Rules

- Prefer simple, readable, modular solutions that fit existing responsibilities before adding new abstractions.
- Treat unknown architecture as risk, not permission to improvise.
- Check module responsibility fit, coupling risk, boundary fit, and readability together rather than independently.
- When a task introduces a durable choice, apply `.opencode/dev_harness/product-breakdown/decision-placement.md`, `.opencode/dev_harness/product-breakdown/templates/decision-template.md`, and `.opencode/dev_harness/product-breakdown/templates/decision-log-entry-template.md` when an index is maintained.
- When architecture depends on product-breakdown artifacts, load only the exact `.opencode/dev_harness/product-breakdown/` files named by the caller.
- Return `not_applicable` when the caller's context shows no architecture, module-boundary, dependency, or durable-decision impact.

## Context Expectations

- The caller must provide the relevant discovery bundle, implementation evidence, or review evidence.
- Do not do broad repository search unless the caller's bundle is insufficient and the architecture risk cannot be assessed from the provided context.
