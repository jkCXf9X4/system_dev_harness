# IMP-027: Quantitative Workflow Metrics

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Add a measurement and metrics framework for quantitative evaluation of workflow effectiveness.

## Evidence

- `.opencode/dev_harness/workflow/control-policy.md` (entire file: no reference to metrics, measurement, instrumentation, or quantitative gates)
- `.opencode/dev_harness/workflow/stage-output-schema.md` (entire file: all fields are qualitative — user_feedback_required, improvement_candidates, research_requests, helper_lifecycle — no quantitative fields like cycle_time, defect_count, revision_count)
- `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` (entire file: triggers are qualitative heuristics — code changes, behavior changes, architecture changes — no quantitative thresholds like "more than X revision loops in Y tasks")
- `.opencode/dev_harness/workflow/stage-gate.md` (file does not exist — referenced but absent, no metrics gate is possible)
- ISO/IEC 15288 §6.3.7 — Measurement Process: "The measurement process shall collect, analyze, and report data relating to the products and processes"
- CMMI Maturity Level 3 — Process Definition: requires defined, measured processes; Level 4 — Quantitative Management: requires statistical process control
- CMMI Measurement and Analysis process area: "Develop and sustain a measurement capability used to support management information needs"

## Current Pain Or Risk

The workflow has no quantitative data to support process improvement decisions. There is no way to:
- Measure cycle time per task type
- Track defect rate or revision frequency
- Identify process bottlenecks (which stages repeatedly block)
- Quantify the impact of process changes
- Set quantitative improvement targets

All process governance is heuristic — based on lessons memory and qualitative observation. This makes it impossible to detect gradual process degradation, compare the effectiveness of workflow versions, or provide CMMI-relevant evidence of quantitative process management.

Revision governance exists (iteration cap of 3, no-improvement detection) but relies on the same heuristic observation without metrics.

## Proposed Improvement

Add a lightweight measurement framework that instruments the guarded workflow with quantitative checkpoints:

1. **Instrumentation points**: Each stage output field in `stage-output-schema.md` gains optional `workflow_metrics` fields:
   - `stage_start_time` / `stage_end_time` (ISO-8601)
   - `helper_count` (number of helpers invoked)
   - `revision_iteration` (current revision loop count)
   - `blocking_finding_count` (for reviewer stage)
   - `files_changed_count` (for builder stage)

2. **Metrics accumulation**: A new file under `.opencode/dev_harness/workflow/workflow-metrics-schema.md` defines which metrics are accumulated across stages and how they fold into the final report.

3. **Metrics report section**: The reporter stage includes a metrics summary block in its output (minimum: cycle_time, revision_count, helper_count, gate_result).

4. **No database or permanent storage**: Metrics are task-local and reported in the final report only. No historical database, dashboard, or trending required for the initial implementation.

## Expected Benefit

- Enables quantitative assessment of workflow effectiveness per task
- Provides data for future process improvement decisions
- Creates CMMI-aligned measurement evidence
- Allows detection of systemic bottlenecks (e.g., "80% of blocking findings occur at the same stage")
- Low overhead: instrumentation is passive, requires no external infrastructure

## Risk And Blast Radius

- Adding timestamps and counters to stage output could create schema drift if existing consumers parse exact fields
- Low blast radius: changes are confined to `stage-output-schema.md`, reporter agent, and an optional new schema file
- No external dependencies, no data persistence, no dashboard
- Zero impact on existing stage logic — metrics are passive annotations, not decision inputs

## Suggested Priority

Low (non-blocking enhancement; the workflow works without it)

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Create `.opencode/dev_harness/workflow/workflow-metrics-schema.md` defining: `cycle_time_ms`, `stage_durations_ms` (map), `helper_invocation_count`, `revision_iteration_count`, `blocking_finding_count`, `files_changed_count`
2. Add optional `workflow_metrics` field group to `stage-output-schema.md` common fields (all fields prefixed with `metrics_`)
3. Update reporter agent to accumulate metrics from all stages and include a metrics summary block in its output
4. Add a `metrics` section to `control-policy.md` referencing the new schema

Do NOT implement these scoped extensions:
- Historical metrics database or dashboard
- Automated trend analysis or alerts
- Metrics-driven gating decisions (metrics are informational only)
- Cross-task aggregation or reporting

## Out Of Scope

- Historical metrics database or dashboard
- Trend analysis, alerts, or automated process adjustment based on metrics
- Cross-task aggregation in reporter output
- External monitoring or observability integration

## Traceability

- Intent: ISO/IEC 15288 §6.3.7 Measurement Process; CMMI Measurement and Analysis
- Product: Evolution layer — workflow process maturity improvement
- Architecture: Additive to existing schema; no structural changes
- Implementation: New schema file, updated stage-output-schema, updated reporter, updated control-policy
- Verification: Reporter test verifies metrics block is present and populated for each implemented stage

## Notes

This gap is confirmed in the work-systems engineering evaluation (2026-06-29) as Discovery Gap #2: No quantitative measurement/metrics. The workflow currently has zero instrumentation. ISO/IEC 15288 §6.3.7 requires a systematic measurement process. CMMI Level 3+ requires defined and measured processes. The minimal implementation described here (task-local, passive, no persistence) provides the measurement foundation without over-engineering.