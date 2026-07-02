# IMP-056: Eliminate Inline Duplication — Planner Output vs. Plan File Content

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Eliminate the duplication between the planner agent's inline output schema and the plan file content defined in plan-summary-schema.md.

## Evidence

- `.opencode/agents/orchestrator-planner.md` (lines 129–151 define inline output fields)
- `.opencode/dev_harness/workflow/plan-summary-schema.md` (defines plan file schema)
- Architecture analysis finding #3 from FRAMEWORK-REVIEW-001: "Schema duplication: Planner returns inline output that duplicates plan file content"
- Architecture analysis finding #6 from FRAMEWORK-REVIEW-001: "Output field mismatch: planner.md output fields (lines 129–151) don't exactly match plan-summary-schema required fields"

## Current Pain Or Risk

The planner agent defines its output schema inline (lines 129–151 of orchestrator-planner.md) and also writes plan files per `plan-summary-schema.md`. These two schemas overlap significantly but are maintained independently. Architecture analysis found that the inline output fields do not exactly match the plan-summary-schema required fields, creating:

- **Schema drift**: The inline schema and plan file schema can diverge over time
- **Maintenance burden**: Any schema change must be applied in two places
- **Inconsistency risk**: Downstream consumers may receive different field sets depending on whether they read the planner output or the plan file
- **Violation of KM-010**: The framework duplicates schema definitions instead of referencing a single source

## Proposed Improvement

Replace the inline output schema in the planner agent with a reference to `plan-summary-schema.md`:

1. Remove the inline output field definitions from `orchestrator-planner.md` (lines 129–151)
2. Replace with a directive: "Output must conform to `plan-summary-schema.md`"
3. Ensure `plan-summary-schema.md` covers all fields the planner needs to produce
4. Add any missing fields to `plan-summary-schema.md` if the inline schema contains fields not yet in the plan file schema

## Expected Benefit

- Single source of truth for plan file schema
- Eliminated schema drift risk
- Reduced maintenance burden
- Clearer contract between planner and downstream consumers
- Alignment with KM-010 (reference, don't duplicate)

## Risk And Blast Radius

- Medium blast radius: affects planner agent, plan-summary-schema.md, and any downstream consumers that parse planner output directly
- Risk of breaking downstream consumers if they depend on fields that are in the inline schema but not in plan-summary-schema.md
- Requires careful audit of all fields in both schemas before consolidation

## Suggested Priority

Medium

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Compare all fields in planner inline output (lines 129–151) against plan-summary-schema.md required fields
2. Identify any fields present in one but not the other
3. Add missing fields to plan-summary-schema.md
4. Replace inline schema in planner with a reference directive
5. Verify downstream consumers still receive all required fields

Do NOT implement:
- Changes to actual planner output logic or field values
- Changes to downstream consumer parsing logic
- Schema format changes (keep existing field names and types)

## Out Of Scope

- Changes to actual planner output logic or field values
- Changes to downstream consumer parsing logic
- Schema format changes
- Changes to the plan file writing logic

## Traceability

- Intent: Eliminate schema duplication and drift risk
- Product: Evolution layer — agent framework quality improvement
- Architecture: Schema consolidation; no structural changes
- Implementation: Planner agent edit, plan-summary-schema.md update
- Verification: All fields from inline schema are present in plan-summary-schema.md after consolidation

## Notes

This finding originates from FRAMEWORK-REVIEW-001 architecture analysis findings #3 and #6. The inline output fields (lines 129–151) don't exactly match plan-summary-schema required fields, confirming active schema drift. Consolidation aligns with KM-010 (reference, don't duplicate).