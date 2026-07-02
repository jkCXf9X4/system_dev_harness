# IMP-060: Plan File Archive Hygiene — Write Failure Handling and Archive Integrity

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Add error handling for plan file write failures and improve plan file archive integrity.

## Evidence

- `.opencode/dev_harness_plans/` (plan file archive directory)
- `.opencode/dev_harness/workflow/plan-summary-schema.md` (plan file schema)
- `.opencode/agents/orchestrator-planner.md` (plan file writing logic)
- Systems engineering finding #3 from FRAMEWORK-REVIEW-001: "Plan file single point of failure: All downstream stages depend on plan file; no error-handling path for write failure"
- Risk R1 from FRAMEWORK-REVIEW-001: "Plan file write failure would silence all downstream stages (low likelihood, critical impact)"

## Current Pain Or Risk

The plan file is a single point of failure in the guarded workflow:
- All downstream stages (builder, reviewer, reporter) depend on the plan file
- There is no error-handling path for plan file write failure
- If the planner fails to write the plan file, downstream stages either fail silently or start with no work order
- There is no validation that the written plan file is complete and valid before downstream stages begin
- The plan file archive has no integrity checks (no checksums, no validation, no backup)

Risk R1 identifies this as "low likelihood, critical impact" — the likelihood is low but the impact is total workflow failure.

## Proposed Improvement

Add plan file write failure handling and archive integrity:

1. **Write verification**: After writing the plan file, verify it exists, is non-empty, and is valid per `plan-summary-schema.md`
2. **Write failure handling**: If write or verification fails, retry once, then escalate per error recovery path (see IMP-058)
3. **Archive integrity**: Add a lightweight integrity check (file existence, non-empty, valid schema) before downstream stages consume the plan file
4. **Backup**: Optionally keep the previous plan file version as a backup before overwriting

## Expected Benefit

- Eliminated single point of failure for plan file writes
- Early detection of write failures before downstream stages start
- Clear error messages when plan file write fails
- Improved archive integrity and debuggability
- Reduced risk of silent workflow failure

## Risk And Blast Radius

- Low blast radius: changes are confined to planner agent and plan file writing logic
- Risk of false positives if verification criteria are too strict
- Minimal performance impact (file existence and schema validation are fast)
- Requires coordination with error recovery path (IMP-058)

## Suggested Priority

Medium

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

2026-07-02

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

2026-07-02

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

Implemented as part of combined task IMP-055-056-057-060-062-063. See `.opencode/dev_harness_plans/2026-07-02_000000-IMP-055-056-057-060-062-063.md`.

## Task Contract Seed

The smallest scoped task would:
1. Add write verification step to planner agent (verify file exists, non-empty, valid per schema after write)
2. Add retry-on-failure logic (retry once, then escalate)
3. Add pre-consumption integrity check to builder agent (verify plan file before starting)
4. Update `control-policy.md` to document the verification and failure handling

Do NOT implement:
- Full error recovery path (covered by IMP-058)
- Plan file backup or versioning
- Changes to plan file schema
- Changes to downstream stage logic beyond the pre-consumption check

## Out Of Scope

- Full error recovery path (covered by IMP-058)
- Plan file backup or versioning
- Changes to plan file schema
- Changes to downstream stage logic beyond the pre-consumption check

## Traceability

- Intent: Eliminate single point of failure for plan file writes
- Product: Evolution layer — workflow process robustness
- Architecture: Additive verification steps; no structural changes
- Implementation: Planner agent, builder agent, control-policy.md updates
- Verification: Planner correctly detects and reports write failures; builder correctly rejects invalid plan files

## Notes

This finding originates from FRAMEWORK-REVIEW-001 systems engineering finding #3 and risk R1. The plan file is a critical single point of failure with no error handling. This candidate is related to IMP-058 (error recovery path) and IMP-059 (pre-stage readiness verification) but focuses specifically on plan file write integrity.