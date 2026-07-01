# Stage Output Schema

Use this schema for every top-level stage and directed helper. Role prompts may add role-specific fields, but they should not redefine these common fields.

## Emit-By-Exception Rule

Optional fields are silent when they carry no meaningful value. Replace `none`/`not_applicable` with omission. Only emit a field when it has substantive content.

## Common Fields

```text
user_feedback_required: true|false    # only emit when true
user_feedback_request: <specific question, waiver request>  # omit when none
validation_status: pass|fail|not_applicable  # only emit when set by orchestrator-validation; other stages omit
improvement_candidates: <out-of-scope candidates>  # omit when none
research_requests: <research already performed or needed>  # omit when none
helper_lifecycle: <reuse/start-fresh decision>  # only emit when reusing a helper
```

Any stage may set `user_feedback_required: true` when it needs user input, approval, or a waiver.

When `user_feedback_required` is true, the orchestrator pauses and requests the user decision before continuing. The unresolved `user_feedback_request` must be relayed unchanged to downstream stages after the user responds so every agent sees the same active feedback context.

Improvement candidates are backlog candidates only. They do not authorize scope expansion in the current task. Incidental candidate handling and persistence ownership live in `.opencode/dev_harness/workflow/candidate-capture.md`.

Research requests are handled by `orchestrator-researcher` when source material is needed for the current stage.

Helper lifecycle decisions use `.opencode/dev_harness/workflow/subagent-lifecycle.md`. They make helper reuse explicit because the workflow cannot force compaction, clearing, pruning, or reset of another agent's context.

When a stage reuses a helper after previous helper work, include:

```text
helper_lifecycle:
  reuse_decision: reuse_existing|start_fresh
  reason: <why reuse or a fresh helper is appropriate>
```

Omit the entire `helper_lifecycle` block for first-call helpers or when no reuse decision is needed.

## Compact Output Format Example

For low-risk tasks, stages may use a compact output format:

```
status: <pass|fail|approved|blocked|...>
key_evidence: <brief summary>
findings: <stable item IDs or none>
```

All other fields are emitted only when they carry meaningful content. The compact format does not waive required evidence — it only reduces token overhead for fields that would otherwise be `none` or `not_applicable`.

## Output Mode

Stages use an `output_mode` field to control verbosity:

```text
output_mode: compact|full  # compact for lightweight/standard, full for high_assurance
```

**Compact mode** collapses helper disposition blocks to a single summary line:

```text
helpers_used: [discovery, contract] | helpers_waived: [architecture, lessons, memory, researcher, systems-engineering]
```

Move detailed rationales to an optional `helper_details` block, emitted only when `high_assurance` profile is active or when a waiver rationale is non-obvious.

**Full mode** retains verbose per-helper disposition blocks with individual `helper_not_used` rationales.

The planner sets `output_mode` in the work order based on the selected tailoring profile:
- `lightweight` → `compact`
- `standard` → `compact`
- `high_assurance` → `full`

## Helper Output Compression

Directed helpers (e.g., `orchestrator-researcher`, `orchestrator-discovery`) return compressed output to reduce token overhead in parent stage context:

```text
compressed_output: <compact summary, ≤500 tokens, all decisions and constraints included>
full_output_path: <path to file on disk containing the full helper output>
```

**Compression rules:**
- `compressed_output` must include all decisions, constraints, and action items. Raw search results, verbose logs, and intermediate reasoning may be omitted.
- `full_output_path` points to a file on disk that preserves the complete helper output for on-demand loading.
- Parent stages load the full output from `full_output_path` only when they need details beyond the compressed summary.

**Profile behavior:**
- `lightweight` / `standard` profiles → helpers MUST use `compressed_output` + `full_output_path`.
- `high_assurance` profile → helpers MAY keep full output inline instead of compressing.

**Planner synthesis:**
The planner synthesizes helper outputs into the work order, keeping only decisions, constraints, and action items. Raw search results and verbose intermediate output are not passed through. See `stage-output-schema.md` "Helper Output Compression."

## Role-Specific Return Fields (Planner and Reviewer)

Stages that own helper invocation planning (planner, reviewer) include these fields in their return block:
- `helper_agents_used`: list and rationale, or `none`
- `helper_agents_waived`: list and rationale, or `none` — include `helper_not_used` rationales for applicable-but-waived helpers
- `parallel_helper_plan`: packet IDs, helpers, dependencies, reason, expected outputs, or `none`
- `helper_dispositions`: `parallel_safe`, `dependencies`, `file_write_set`, `helper_lifecycle`

## Not Applicable

If a stage is not applicable, it must return:

```text
not_applicable
reason: <brief rationale>
evidence_inputs_inspected: <inputs reviewed before declaring not applicable>
```

Missing stage output or unjustified `not_applicable` blocks completion.

## Clarification Fields

Planner clarification output uses:

```text
clarification_status: not_needed|required
blocking_uncertainty: <decision that cannot be made safely, or none>
clarification_questions: <one to three specific questions, or none>
assumption_rationale: <why assumptions are safe, or not_applicable>
```