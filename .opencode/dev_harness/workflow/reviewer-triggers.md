# Reviewer Triggers

Purpose: Defines reviewer-stage helper triggers for adaptive risk-based helper selection, including validation as a reviewer-invoked parallel helper.

## Reviewer Triggers

- Repo-state review requests require `orchestrator-review-completeness`; add `orchestrator-review-architecture` when the review scope includes code structure, architecture, module boundaries, dependency shape, or responsibility fit.
- Code changes require `orchestrator-verifier` plus `orchestrator-review-completeness`; architecture review is added when architecture triggers apply.
- Behavior changes require `orchestrator-review-completeness` to check acceptance criteria, edge cases, and test adequacy.
- Product-breakdown or information-artifact changes require `orchestrator-review-completeness`; durable decision changes also require `orchestrator-review-architecture`.
- Architecture, module-boundary, dependency-shape, or responsibility changes require `orchestrator-review-architecture`.
- Known repeated mistake risk or revision input requires `orchestrator-review-lessons`.
- Durable lesson, pattern, or decision uncertainty requires `orchestrator-memory`; evidenced repeatable memory candidates are reported to `orchestrator-reflection` for final memory triage.
- External dependency, API, framework, standard, version, or documentation uncertainty requires `orchestrator-researcher`; reviewer may not approve external claims without cited researcher evidence or a waiver.

Low-risk documentation, formatting, wording, or metadata-only tasks may be planned or reviewed directly when the stage records why no risk trigger applies.

### Validation Triggers (Reviewer-Invoked Helper)

Validation (`orchestrator-validation`) is a read-only reviewer-invoked parallel helper that checks builder evidence against planner intent and acceptance criteria.

Validation is **REQUIRED** when:
- Behavior changes or user-facing changes
- Ambiguous scope at planning time
- `user_feedback_required` was true during planning

Validation is **NOT_APPLICABLE** when:
- Config changes, dependency bumps, trivial fixes, documentation-only changes
- `workflow_mode: candidate_capture`

Validation is invoked as a reviewer parallel helper, not a separate serial stage. When validation is required, the reviewer includes it among parallel helpers. When validation is not_applicable, the reviewer sets `not_applicable` for the validation helper.

Source: extracted from `adaptive-risk-triggers.md` §E Validation Triggers, §F Reviewer Triggers.