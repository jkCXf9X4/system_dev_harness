# Sequence Diagrams & Parametric Constraints

> **Runtime reference copy for agent context.** Canonical source: `product-breakdown/pbs/02-architecture/sequence-parametric.md`.

Message-sequence tables for the two guarded workflow paths and parametric constraint definitions.

Current as of IMP-032 (2026-06-29).

## Notation

Sequence tables follow lifeline/message conventions adapted from SysML Sequence Diagrams. Each row is one message exchange between lifelines (agents or stages). Messages are ordered by sequence number.

Parametric constraints define bounds and invariant conditions adapted from SysML Parametric Diagrams.

---

## Guarded Delivery Path

### Message-Sequence Table

| Seq | Source Lifeline | Target Lifeline | Message / Action | References |
|---|---|---|---|---|
| 1 | Operator | Orchestrator | Task request (intent, scope, subject) | — |
| 2 | Orchestrator | Planner | Invoke planner with task request | State: idle → active (planner) |
| 3 | Planner | Self | Normalize request, select workflow mode (delivery), resolve uncertainty | State: active → active (helper planning) |
| 4 | Planner | [Planning helpers] | Invoke helpers per adaptive risk triggers (parallel-safe packets) | Contract: H10–H14 |
| 5 | [Planning helpers] | Planner | Return analysis outputs | State: waiting_for_input → active |
| 6 | Planner | Self | Synthesize work order, persist plan summary | State: active → completed |
| 7 | Planner | Builder | Hand off work order | Contract: H01 |
| 8 | Builder | Self | Implement changes per work order | State: idle → active |
| 9 | Builder | [Build helpers] | Invoke build-error-resolver / cleanup if needed | — |
| 10 | [Build helpers] | Builder | Return results | State: waiting_for_input → active |
| 11 | Builder | Self | Optionally run builder-owned review pass | State: active (review pass) |
| 12 | Builder | Reviewer | Hand off implementation evidence | Contract: H02 |
| 13 | Reviewer | [Review helpers] | Invoke verifier, review-architecture, review-completeness, review-lessons (parallel-safe packets) | State: active → waiting_for_input |
| 14 | [Review helpers] | Reviewer | Return verification/review findings | — |
| 15 | Reviewer | Self | Compute gate decision (approved | blocked | waiver_required) | State: active → completed |
| 16 | Reviewer | Reflection | Hand off gate result and memory candidates | Contract: H03 |
| 17 | Reflection | Self | Perform memory triage | State: idle → active → completed |
| 18 | Reflection | Memory curator | Invoke if durable memory candidate accepted | — |
| 19 | Memory curator | Reflection | Return curation result | — |
| 20 | Reflection | Reporter | Hand off memory triage result | Contract: H04 |
| 21 | Reporter | Operator | Output final control report | — |

### Revision Loop

| Seq | Source | Target | Message | Condition |
|---|---|---|---|---|
| R1 | Reviewer | Planner | Gate=blocked, return findings with iteration count | Blocking gaps exist, iteration ≤ max |
| R2 | Planner | Builder | Revised work order addressing specific findings | Iteration count incremented |
| R3 | Builder | Reviewer | Updated implementation evidence | Per normal delivery path |

---

## Candidate-Capture Path

### Message-Sequence Table

| Seq | Source Lifeline | Target Lifeline | Message / Action | References |
|---|---|---|---|---|
| 1 | Operator | Orchestrator | Candidate-capture request | — |
| 2 | Orchestrator | Planner | Invoke planner with discovery objective | State: idle → active (planner) |
| 3 | Planner | Self | Normalize request, select workflow_mode=candidate_capture | — |
| 4 | Planner | [Planning helpers] | Invoke helpers for broad inspection (per adaptive risk triggers) | Contract: H10–H14 |
| 5 | [Planning helpers] | Planner | Return analysis and gap evidence | — |
| 6 | Planner | Builder | Hand off candidate-capture work order | Contract: H05 |
| 7 | Builder | Self | Inspect target area, persist candidate files to candidates/ | State: idle → active |
| 8 | Builder | Reviewer | Hand off persistence evidence (files written, no_candidate, or both) | Contract: H02 |
| 9 | Reviewer | Self | Validate persisted artifacts or no_candidate rationale | State: active → completed |
| 10 | Reviewer | Reflection | Hand off gate result | Contract: H03 |
| 11 | Reflection | Self | Perform memory triage | — |
| 12 | Reflection | Reporter | Hand off memory triage result | Contract: H04 |
| 13 | Reporter | Operator | Output final report with candidate disposition | — |

---

## Parametric Constraints

These constraints define invariant bounds for workflow execution. Values marked as TBD require empirical calibration.

### C01: Revision Loop Cap

```
constraint RevisionLoopCap {
  max_iterations: Integer = 3
  guard: iteration <= max_iterations
  invariant: iteration = iteration@pre + 1
  effect: if iteration > max_iterations then escalate_to_operator
}
```

| Parameter | Value | Source |
|---|---|---|
| `max_iterations` | 3 | control-policy.md — revision loop policy |
| Escalation behavior | Output `blocked_max_reached` | control-policy.md — escalation |

### C02: Context Window Utilization

```
constraint ContextWindowUtilization {
  max_tokens_per_stage: Integer  // TBD — placeholder
  guard: estimated_tokens <= max_tokens_per_stage
  invariant: stage_context_usage <= max_tokens_per_stage
}
```

| Parameter | Value | Notes |
|---|---|---|
| `max_tokens_per_stage` | TBD (placeholder: max 128K tokens per stage) | Depends on LLM provider context window. Calibrate empirically. |
| Estimation method | TBD | Not currently instrumented. |

### C03: Parallel-Safe Concurrency Bounds

```
constraint ParallelSafeConcurrency {
  max_concurrent_helpers: Integer = 3
  guard: concurrent_helper_count <= max_concurrent_helpers
  invariant: parallel_safe_packets are independent
}
```

| Parameter | Value | Source |
|---|---|---|
| `max_concurrent_helpers` | 3 | Runtime capability — OpenCode task invocation limit |
| Independence check | Each packet's dependencies are resolved before parallel dispatch | `.opencode/dev_harness/workflow/adaptive-risk-triggers.md`, `.opencode/dev_harness/workflow/parallel-helper-execution.md` |

### C04: Review Gate Invariant

```
constraint ReviewGateInvariant {
  state: gate_result in {approved, blocked, waiver_required}
  guard: if code_changes then verifier_must_have_run
  guard: if information_artifacts_touched then hygiene_evidence_must_exist
  guard: if blocking_gaps then each_gap_has_id_and_next_action
}
```

This constraint ensures the reviewer gate always produces a valid, evidence-supported outcome.

### C05: Stage Order Invariant

```
constraint StageOrderInvariant {
  ordering: planner -> builder -> reviewer -> reflection -> reporter
  guard: skip_stage only when not_applicable or waiver_granted
}
```

The stage order must follow the guarded chain. Stages may be skipped only with explicit not_applicable rationale or a granted waiver.

---

## Trace Links

- Sequence tables reference states from `agent-state-machines.md` (planner, builder, reviewer, reflection state transitions)
- Sequence tables reference interface contracts from `interface-contracts.md` (H01–H14 handoff references)
- Parametric constraints C01, C04, C05 are derived from `product-breakdown/pbs/02-architecture/architecture.md` (completion model, control flow)
- Parametric constraint C03 references `.opencode/dev_harness/workflow/adaptive-risk-triggers.md` and `.opencode/dev_harness/workflow/parallel-helper-execution.md` concurrency rules
- Satisfies SysML Sequence Diagram and Parametric Diagram adaptation requirement (IMP-032 Seed 7)