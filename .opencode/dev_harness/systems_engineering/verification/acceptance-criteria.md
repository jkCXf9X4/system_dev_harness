# Verification Strategy

> **Runtime reference copy for agent context.** Canonical source: `system_definition/cross-cutting/04-verification/acceptance-criteria.md`.
> **External references:** This file adapts concepts from ISO/IEC 15288 (System life cycle processes) and the INCOSE Systems Engineering Handbook for verification/validation analysis within this workflow. Descriptions are original summaries; for authoritative definitions, consult the standards directly.

This document serves as the authoritative index for all verification criteria across the system. It defines the overall verification approach and cross-cutting concerns.

Per IMP-021, verification uses a dual INCOSE-aligned pattern:
- **Centralized strategy (this document):** Defines the overall verification approach, methods, and cross-cutting concerns. This preamble and the criteria index below form the strategy overview.
- **Per-layer verification artifacts:** Each PBS/FBS layer has a local `verification.md` that extracts and scopes the criteria relevant to that element. These per-layer artifacts are authoritative for their element.

The following per-layer verification artifacts exist:

| Layer | Path | Scope |
|---|---|---|
| Intent | `system_definition/fbs/00-intent/verification.md` | Vision, use cases |
| Product | `system_definition/fbs/01-product/verification.md` | Product commitments |
| Architecture | `system_definition/pbs/02-architecture/verification.md` | Architecture boundaries, control flow, mechanisms |
| Implementation | `system_definition/pbs/03-implementation/verification.md` | Implementation artifacts |
| Operation | `system_definition/cross-cutting/05-operation/verification.md` | Runbook, deployment process |
| Evolution | `system_definition/cross-cutting/06-evolution/verification.md` | Roadmap, changelog, risks, gap analysis, WBS |

All 18 centralized acceptance criteria are listed below. Each criterion is extracted into one or more per-layer verification artifacts as indicated by its cross-reference.

---

# Acceptance Criteria

The workflow package must satisfy these high-level acceptance criteria:

- Every guarded workflow run produces a planner-owned work order with verifiable checks.
- Planner and reviewer stages identify parallel-safe helper packets for independent helper work and preserve dependencies, expected outputs, and file write sets.
- Every change is independently reviewed before completion.
- Every completed guarded workflow run performs final reflection before reporting so durable memory incorporation is explicitly accepted, rejected, deferred, or marked not applicable.
- Workflow memory includes trust metadata, revalidation cues, and an explicit boundary between durable memory, task-local evidence, run history, and improvement backlog items.
- Memory curation reports a concrete decision taxonomy, and review/report outputs surface memory hygiene whenever memory influenced the task.
- Product-breakdown source docs define the canonical storage mechanism for product rationale, runtime prompts, dev harness context, workflow memory, improvement backlog items, task-local evidence, skills/plugins, and external research.
- Reviewer findings are actionable (blocked findings route back to planner per the revision loop).
- Stale references, status trackers, duplicates, superseded content, unresolved links, traceability, and orphaned artifacts are reconciled before completion.
- Repo-state review tasks either produce trace-preserving updates or a reviewed no-change/backlog result that records stale, duplicated, conflicting, or orphaned findings.
- Backlog-worthy improvement candidates are persisted to `system_definition/cross-cutting/06-evolution/candidates/` by builder candidate-capture mode before the builder returns, without changing implementation files.
- Every deliberate candidate-capture run receives a reviewed disposition before final reporting: accepted candidate or no candidate.
- Bug, fix, regression, feature, and documentation subjects use `workflow_mode: candidate_capture` when the user asks for proposal, evaluation, candidate, future-task-seed, or backlog capture instead of implementation.
- Working agents can surface incidental improvement candidates without persisting them; deliberate persistence requires a candidate-capture work order.
- Product source information, scope, stable decisions, and traceability remain in `system_definition/`.
- Runnable guidance, examples, install/deploy instructions, verification commands, and contributor workflow remain in `docs/` without duplicating product text.
- Review-only repo-state assessment requests use `workflow_mode: candidate_capture`; review-and-change requests use `workflow_mode: delivery`.
- Planner work orders and final reports preserve a task-tailoring record with the selected workflow profile, applied triggers, helper/stage deviations, and rationale.

---

# Validation Criteria

Validation assesses whether the delivered work satisfies the user's actual needs, per ISO 15288 §6.4 — as distinct from verification (checking conformance to a technical contract). These criteria are additive to the acceptance criteria above.

- **VAL-001**: The delivered change demonstrably addresses the user-stated problem or request, not only the technical contract wording. If the work order recorded user intent or original need, the implementation must be traceable back to that intent.
- **VAL-002**: When the task involved user-facing behavior, operational context, or stakeholder requirements, the builder evidence or reviewer findings must include an explicit "does this satisfy the original need?" assessment. Purely technical/internal tasks may mark this criterion as not_applicable.
- **VAL-003**: If the planner recorded an assumption about user intent (see `assumption_rationale` in the work order), the implementation should validate that assumption — i.e., confirm that the work remains correct under the assumed interpretation. Assumptions that turn out to be incorrect should be surfaced as blocking findings.
- **VAL-004**: Changes affecting product commitments, capability descriptions, or use-case documentation must be reviewed against the product's stated purpose and user audience defined in `fbs/00-intent/vision.md` and `fbs/01-product/product-commitments.md`. A purely internal or technical implementation with no product-behavior impact may mark this as not_applicable.
- **VAL-005**: When waiver_required is the gate result, the waiver rationale must explain not only why the technical contract deviation is acceptable but also why the deviation does not invalidate the user need or intended outcome.