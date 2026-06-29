# IMP-028: Workflow Process Decision Records

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Introduce structured process decision records (PDRs) for workflow governance decisions: waivers, risk acceptances, tailoring choices, and process deviations.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (lines 139-149: Waivers section requires named risk, waiver scope, follow-up/expiry — but no structured record format, no archive, no traceability)
- `.opencode/dev_harness/workflow/control-policy.md` (lines 151-159: Revision Loop Policy requires evidence preservation — but no structured record format for decisions made during the loop)
- `.opencode/dev_harness/product-breakdown/decision-log.md` (entire file: describes product-level decision index only — ID, Title, Layer, Status, Location, Related artifacts — no workflow governance decisions)
- `.opencode/dev_harness/product-breakdown/decision-placement.md` (entire file: placement rules for product decisions — no placement for workflow process decisions)
- ISO/IEC 15288 §6.3.4 — Decision Management Process: "The decision management process shall select a course of action from among alternatives"
- CMMI Decision Analysis and Resolution (DAR): requires formal evaluation of alternatives for selected decisions
- Work System Theory (Alter 2013): "Work systems need explicit decision records to maintain process integrity across changes in participants, technology, and context"

## Current Pain Or Risk

When the workflow makes decisions during execution — granting waivers, accepting risks, tailoring the process, or deviating from standard procedures — these decisions are:
- Not captured in a structured, persistent format
- Not archived for future reference
- Not traceable back to the original rationale
- Impossible to audit or review after the task completes

The existing waiver mechanism in `control-policy.md` requires named risk, scope, and expiry, but provides no template for recording this as a durable artifact. Decision records exist for product-level decisions (decision-log.md) but not for workflow process governance.

This creates a risk of:
- Inconsistent waiver application across tasks
- Lost rationale for process deviations
- Inability to learn from past governance decisions
- Audit gaps for compliance-sensitive workflows

## Proposed Improvement

Add a lightweight Process Decision Record (PDR) schema and archive:

1. **PDR Schema**: Define in a new file `.opencode/dev_harness/workflow/process-decision-record-schema.md` with fields:
   - `pdr_id`: unique identifier (PDR-001, PDR-002...)
   - `type`: waiver | risk_acceptance | tailoring | process_deviation | revision_override
   - `title`: short description
   - `task_id`: referencing the planner task
   - `rationale`: why the decision was made
   - `alternatives_considered`: what other options were evaluated
   - `risk_assessment`: blast radius and impact
   - `expiry_or_follow_up`: when to revisit or what to check
   - `approved_by`: which role/stage authorized it
   - `timestamp`: ISO-8601
   - `affected_artifacts`: paths or file references

2. **Trigger points in existing stages**:
   - Planner: when a waiver is requested or tailoring is applied, include a `pdr_required: true` flag
   - Reviewer: when granting a waiver or accepting a risk, write a PDR to `.opencode/dev_harness_plans/pdr-PDR-001.md`
   - Reporter: summarize PDRs created during the workflow in the final report

3. **No global index initially**: PDRs are task-local files under `.opencode/dev_harness_plans/`. A global index can be added later if auditing requirements emerge.

## Expected Benefit

- Every process governance decision is captured with rationale and alternatives
- Waivers, risk acceptances, and tailoring choices become auditable
- Future planners and reviewers can reference past PDRs for consistent decision-making
- Closes the CMMI Decision Analysis and Resolution gap
- Provides traceability for process-level governance, parallel to existing product-level decision records

## Risk And Blast Radius

- Adds one new schema file and minor instrumentation in existing stage agents
- Low blast radius: changes are confined to new schema file, minor updates to control-policy (add PDR reference), reporter agent
- No impact on existing stage logic or product breakdown structure
- Risk of PDR proliferation if every routine decision gets a record — mitigated by the trigger rule (only waivers, risk acceptances, tailoring, process deviations)

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
1. Create `.opencode/dev_harness/workflow/process-decision-record-schema.md` with the PDR fields listed above
2. Update `control-policy.md` to reference PDRs in the Waivers section (add "Write a PDR for each granted waiver with rationale and alternatives evaluated")
3. Add `pdr_created` and `pdr_refs` fields to `stage-output-schema.md` common fields
4. Update reporter agent to include a PDR summary in its output

Do NOT implement these scoped extensions:
- A global PDR index or decision log (deferred)
- Cross-task PDR analysis or pattern detection
- Automated PDR enforcement or validation
- PDR template file creation (inline in the schema is sufficient)

## Out Of Scope

- Global PDR index or cross-task analysis tooling
- Automated PDR validation or enforcement
- PDR integration with external governance tools
- Historical migration of prior informal waivers

## Traceability

- Intent: ISO/IEC 15288 §6.3.4 Decision Management Process; CMMI Decision Analysis and Resolution
- Product: Evolution layer — workflow governance improvement
- Architecture: Additive schema; no structural changes to existing stages
- Implementation: New schema file, updated control-policy waiver section, updated reporter
- Verification: Reporter output includes PDR section with count and reference when PDRs were created

## Notes

This gap is confirmed in the work-systems engineering evaluation (2026-06-29) as Discovery Gap #4: No structured decision records — with refinement. The system HAS product-level decision records (decision-log.md, decision-placement.md) but DOES NOT have workflow process decision records. These are a distinct concern that should be addressed separately from the product decision system. The refined finding acknowledges that product decisions are well-structured, but process governance decisions (waivers, tailoring, risk acceptance) lack any structured capture mechanism.