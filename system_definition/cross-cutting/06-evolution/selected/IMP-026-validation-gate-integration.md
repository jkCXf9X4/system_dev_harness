# IMP-026: Validation Gate Integration

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

In Progress

## Layer

Evolution

## Theme

Add a validation gate between contract and builder stages to close the verification-only gap.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (lines 5-15: Required Stages list shows orchestrator-planner, orchestrator-builder, orchestrator-reviewer, orchestrator-reflection, orchestrator-reporter — no validation stage)
- `.opencode/dev_harness/workflow/stage-output-schema.md` (entire file: all fields are verification-oriented — no validation acceptance criteria, no "did we build the right thing?" check)
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` (entire file: triggers select helpers for verification, architecture, completeness — no validation trigger)
- `.opencode/dev_harness/workflow/agent-boundaries.md` (lines 12-16: Read-Only Agents list includes reviewer but no validation agent)
- `.opencode/dev_harness/agents/orchestrator-reviewer.md` (lines 70-74: gate returns approved|blocked|waiver_required — verification gate, not validation)
- ISO/IEC 15288 §6.4 — Validation Process: per ISO 15288, validation confirms that the system meets stakeholder requirements and satisfies stakeholder needs in the intended operational environment, distinct from verification which checks conformance to a technical specification.
- V-Model: explicit distinction between verification (are we building it right?) and validation (are we building the right thing?)

## Current Pain Or Risk

The current stage-gate model only checks whether implementation matches the contract (verification). There is no systematic check of whether the delivered work actually satisfies the user's original intent, solves the real problem, or meets acceptance criteria in the target environment. This creates a risk of delivering technically correct solutions that miss the user's actual need, especially for complex or ambiguous tasks.

Workflow lessons memory documents this pattern as KM-001 (Do Not Implement Plausible Partial Solutions), where agents satisfy the most visible part of a task but leave edge cases and intent gaps. A validation gate would catch these before the completion gate.

## Proposed Improvement

Add a lightweight validation stage (`orchestrator-validation`) between the builder and reviewer stages in the guarded chain. The validation stage would:

1. Accept the builder's implementation evidence and the planner's original work order (including intent, acceptance criteria, and user context)
2. Check that the delivered change satisfies the original user intent, not just the technical contract
3. Identify gaps between what was built and what was actually needed
4. Return a validation pass/fail with blocking gaps, or `not_applicable` for purely technical/internal tasks

The validation stage should be:
- **Optional for low-risk, purely technical tasks** (config changes, dependency bumps, trivial fixes)
- **Required for feature work, behavior changes, user-facing changes, and ambiguous tasks**
- Triggered by a new risk trigger in `adaptive-risk-triggers.md`

## Expected Benefit

- Catches intent-to-implementation gaps before the completion gate, reducing revision loops
- Closes the V-Model validation gap in the workflow architecture
- Provides a formal "did we build the right thing?" check alongside the existing "did we build it right?" review
- Reduces the risk of KM-001 (partial solutions) type failures
- Creates traceable validation evidence for each task

## Risk And Blast Radius

- Adds one more stage to the guarded chain, increasing workflow latency for tasks that require it
- Risk of validation over-scope if not correctly bounded: must validate the current task only, not the whole product
- Low blast radius: changes are confined to `control-policy.md` (required stages), `adaptive-risk-triggers.md` (new trigger), agent definitions, and a new `orchestrator-validation.md` agent file
- Does not affect builder, reviewer, reflection, or reporter unless the new stage blocks

## Suggested Priority

Medium

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

2026-06-30

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Create `.opencode/dev_harness/agents/orchestrator-validation.md` as a read-only agent that receives builder evidence and planner intent, and returns a validation pass/fail with blocking gaps
2. Add `orchestrator-validation` to the Required Stages list in `control-policy.md` (between builder and reviewer)
3. Add validation trigger rules to `adaptive-risk-triggers.md` (required when: behavior changes, user-facing changes, ambiguous scope, or `user_feedback_required` was true during planning)
4. Add `validation_status` field to `stage-output-schema.md` common fields
5. Update `agent-boundaries.md` Read-Only Agents list to include orchestrator-validation
6. Add `not_applicable` path for purely technical tasks (config changes, dependency bumps)

Do NOT implement these scoped extensions:
- A separate validation report format (reuse stage-output-schema.md common fields)
- Integration with external validation tools or user acceptance testing
- Historical validation evidence storage

## Out Of Scope

- User acceptance testing integration or external validation tooling
- Historical validation evidence database
- Product-level validation outside individual task scope
- Replacement of the existing reviewer gate

## Traceability

- Intent: ISO/IEC 15288 §6.4 Validation Process; V-Model verification/validation distinction
- Product: Evolution layer — workflow process improvement
- Architecture: Maintains existing stage-gate pattern; adds one new stage between builder and reviewer
- Implementation: New agent file, updated control-policy, updated adaptive-risk-triggers, updated stage-output-schema
- Verification: Reviewer gate checks validation stage exists and its output is not missing for applicable tasks

## Notes

This gap is confirmed in the work-systems engineering evaluation (2026-06-29) as Discovery Gap #1: No validation gate. The current system has verification only. The V-Model explicitly requires both verification AND validation as separate concerns. Per ISO/IEC 15288 §6.4.2.3.1, the validation process must confirm that the actual system element meets the stakeholder requirements and satisfies the stakeholder needs — a check the current workflow does not perform.