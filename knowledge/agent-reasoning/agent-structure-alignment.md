# Agent Structure Alignment

This analysis compares the current OpenCode agent structure with the research-backed claims in this knowledge base. It is a reasoning aid for prompt and workflow decisions, not an approval record for implementation changes.

## Current Structure Reviewed

Runtime prompts:

- `.opencode/agents/orchestrator.md`
- `.opencode/agents/orchestrator-planner.md`
- `.opencode/agents/orchestrator-discovery.md`
- `.opencode/agents/orchestrator-contract.md`
- `.opencode/agents/orchestrator-architecture.md`
- `.opencode/agents/orchestrator-lessons.md`
- `.opencode/agents/orchestrator-memory.md`
- `.opencode/agents/orchestrator-memory-curator.md`
- `.opencode/agents/orchestrator-builder.md`
- `.opencode/agents/orchestrator-build-error-resolver.md`
- `.opencode/agents/orchestrator-cleanup.md`
- `.opencode/agents/orchestrator-verifier.md`
- `.opencode/agents/orchestrator-review-*.md`
- `.opencode/agents/orchestrator-reviewer.md`
- `.opencode/agents/orchestrator-reflection.md`
- `.opencode/agents/orchestrator-reporter.md`
- `.opencode/agents/orchestrator-improvement.md`
- `.opencode/agents/orchestrator-improvement-evaluator.md`
- `.opencode/agents/orchestrator-researcher.md`

Policy and product context:

- `.opencode/dev_harness/workflow/control-policy.md`
- `.opencode/dev_harness/workflow/information-hygiene.md`
- `.opencode/dev_harness/workflow/review-output.md`
- `.opencode/dev_harness/product-breakdown/`
- `.opencode/dev_harness_memories/`
- `product-breakdown/02-architecture/architecture.md`
- `product-breakdown/02-architecture/decisions/AD-001-use-opencode-agent-workflow-for-orchestration.md`
- `product-breakdown/02-architecture/decisions/AD-003-use-structured-handoff-before-code-editing.md`

## Overall Assessment

The current structure is more distributed than the earlier linear stage model. The main top-level delivery path is now:

```text
orchestrator
  -> planner, with directed planning helpers
  -> builder, with directed implementation helpers
  -> reviewer, with directed verification and review helpers
  -> reflection, with memory-curation ownership
  -> reporter
```

The strongest alignment is still with:

- role specialization and multi-agent decomposition (`AK-001`)
- review feedback loops and deterministic gating (`AK-004`, `AK-008`)
- explicit memory and reusable workflow patterns (`AK-005`)
- agent-computer interface boundaries through permissions, helper ownership, and write boundaries (`AK-006`)
- structured communication through work orders, control flags, structured feedback fields, and final reports (`AK-007`)

The redistributed structure improves responsibility placement, especially around planner-owned synthesis, builder-owned cleanup, reviewer-owned verification, final reflection, focused improvement evaluation, and durable memory curation. It also introduces new failure modes:

- top-level agents can now under-delegate when a helper trigger applies
- some boundaries are policy-enforced rather than permission-enforced
- helper outputs can be lost or weakened when summarized by the owning top-level stage
- edit-capable helper agents increase the importance of strict write boundaries
- focused improvement evaluation and memory curation can duplicate each other unless their capture purposes stay distinct

The architecture is directionally research-aligned, but the previous claim of uniformly strong alignment is too broad. The updated structure deserves a more conditional assessment: strong where ownership and write boundaries are explicit, moderate where correctness depends on adaptive trigger selection and faithful carry-forward of helper evidence.

## Alignment Matrix

| Research-backed claim | Current alignment | Evidence in current solution | Critical assessment |
| --- | --- | --- | --- |
| AK-001: role specialization | Strong, with coordination risk | The orchestrator is routing-only. Planner, builder, reviewer, reflection, reporter, improvement, researcher, evaluator, memory, cleanup, verifier, and review helpers have explicit roles, permissions, non-goals, and output fields. | Responsibility is better distributed than before. The risk has shifted from monolithic prompts to helper selection, helper output preservation, and overlapping capture roles. |
| AK-002: ground synthesis in prior discovery | Moderate | `orchestrator-discovery` remains the broad repository inspection helper. Planner is instructed to use it for code changes and to produce the work order from selected helper outputs. | This is no longer a hard permission boundary. Planner has read/search/list/bash permissions, so discovery-first discipline is enforced mainly by policy and prompt text. The claim should not be described as "planner cannot inspect the repository." |
| AK-003: connect reasoning with tool and environment actions | Moderate to strong | Discovery reports searches and files read. Builder reports files changed, cleanup, and verification suggestions. Verifier reports commands, exit status, stdout/stderr excerpts, changed files, placement, cleanup, and pass/fail. | Verifier evidence is now structured enough for review. Builder and helper evidence would still benefit from a uniform command/evidence schema and explicit "evidence changed the plan" fields for revisions. |
| AK-004: review feedback loops | Strong | Reviewer coordinates verifier, architecture review, completeness review, lessons review, memory recall, memory curation, researcher, and focused improvement evaluation. Blocked outcomes route back to planner with revision context. | The loop is stronger after moving review orchestration into the reviewer. The main risk is skipped helpers or weak `helper_not_used` rationales on tasks where adaptive triggers should require independent review. |
| AK-005: explicit reviewable memory | Stronger than before | `orchestrator-memory` retrieves relevant lessons and patterns. `orchestrator-reflection` owns final memory-incorporation triage. `orchestrator-memory-curator` writes only durable lessons and patterns under `.opencode/dev_harness_memories/` with rejection rules and duplicate checks. | The earlier gap about missing promotion ownership is mostly resolved. The remaining issue is governance: reflection and curator outputs must reject one-off task state and keep memory distinct from backlog candidates. |
| AK-006: agent-computer interface design | Moderate to strong | The primary orchestrator has no file or shell permissions. Builder, cleanup, build-error resolver, improvement, improvement evaluator, and memory curator are edit-capable but have narrow write boundaries. Verifier and reviewers are read-only. | The interface is explicit, but edit authority is now distributed across more helpers. That is acceptable only if write boundaries stay precise and reviewer evidence checks cover helper edits. |
| AK-007: structured communication | Moderate to strong | The planner-owned work order replaces the old packet stage. Control flags, structured feedback fields, `handoff_required`, helper-not-used rationales, reviewer decisions, reflection results, and reporter summaries preserve state across agents. | Structured communication is still present, but the center of gravity is now the work order and control feedback, not packet and handoff agents. The risk is information loss when many helper outputs are collapsed into one work order, reflection decision, or final report. |
| AK-008: evaluate against evidence | Strong | Review output uses pass/fail/needs_waiver. The reviewer blocks on missing evidence. Verifier has explicit command and cleanup evidence fields. Waivers require named risk, scope, and follow-up or expiry. | The evidence model is strong for task-local completion. The remaining weakness is aggregate evaluation: the workflow does not yet track blocked reasons, waiver frequency, helper skip frequency, or repeated verification gaps across runs. |

## Research-To-Structure Fit

### Agent Architecture And Role Decomposition

Sources: `SRC-001`, `SRC-002`, `SRC-003`, `SRC-008`, `SRC-010`

The current agent set maps to four top-level delivery responsibilities plus specialized helpers:

- `orchestrator` routes only.
- `planner` classifies the request, selects planning helpers, applies route selection, owns test planning, owns product-breakdown placement, and emits the builder work order.
- `discovery`, `contract`, `architecture`, `lessons`, `memory`, and `researcher` are planner-directed helpers.
- `builder` implements the approved work order and may use `build-error-resolver`, `cleanup`, and `researcher`.
- `reviewer` coordinates verifier, independent review helpers, memory recall, memory curation, researcher, and the completion gate.
- `reflection` reviews completed run evidence and owns final durable-memory incorporation triage.
- `reporter` preserves the final status and selected evidence.
- `improvement` runs broad candidate discovery when the requested outcome is candidate capture.
- `improvement-evaluator` captures one focused backlog-worthy finding raised by another stage.
- `memory-curator` captures durable task-independent workflow memory when invoked by reflection or another owning stage.

This is a strong fit for multi-agent research because roles are explicit and coordination is visible in versioned prompts. It also reflects a more realistic agent system than the earlier fixed pipeline: top-level stages own judgment and call helpers when risk requires them.

The main architectural risk is role overlap:

- `orchestrator-improvement` and `orchestrator-improvement-evaluator` both write improvement candidates, but one is broad discovery and the other is focused finding evaluation.
- `orchestrator-memory`, `orchestrator-lessons`, `orchestrator-review-lessons`, `orchestrator-reflection`, and `orchestrator-memory-curator` all touch lesson concerns, but reflection owns final triage and only the curator writes durable memory.
- `orchestrator-cleanup` can fix information hygiene inside builder scope, while `orchestrator-improvement-evaluator` captures out-of-scope cleanup opportunities.

The prompts mostly separate these roles, but future changes should preserve the distinctions. Adding agents should require a clear ownership reason, a non-overlap statement, and a write boundary when the agent can edit.

### Planning, Task Decomposition, And Scope Control

Sources: `SRC-004`, `SRC-005`, `SRC-009`, `SRC-010`

The current workflow decomposes delivery into request normalization, adaptive helper selection, work-order synthesis, scoped implementation, focused verification, independent review, gate routing, and final reporting.

Strong points:

- Route selection separates issue subject from requested outcome.
- Planner owns the work order instead of delegating final synthesis to a separate packet stage.
- Discovery, contract, architecture, lessons, memory, and researcher helpers are available when risk requires them.
- Product-breakdown placement, traceability, test obligations, and durable behavior impact are planner-owned work-order sections.
- Revision input carries blocking finding IDs, iteration count, and original task normalization back to planner.

Gaps:

- Discovery-first behavior is no longer permission-enforced. Planner can inspect files directly, so the workflow relies on the planner following helper triggers and providing `helper_not_used` rationales.
- Revision planning says it must address blocking findings, but it does not require a dedicated revision delta that maps each blocking finding to a changed scope, changed check, or preserved constraint.
- Low-risk direct planning is useful, but it increases review dependence on clear trigger detection.

This assessment treats AK-002 as moderate rather than strong until the prompt or permissions make discovery-first behavior more mechanically enforceable.

### Tool Use, Repository Interaction, And Agent-Computer Interface

Sources: `SRC-004`, `SRC-007`, `SRC-010`

The current permission model is nuanced:

- The primary orchestrator has no read, search, list, edit, or shell permission.
- Planner can read, search, list, and run shell commands, but cannot edit.
- Discovery, contract, architecture, lessons, memory, verifier, reviewer, review helpers, reflection, reporter, and researcher cannot edit.
- Builder, build-error resolver, cleanup, improvement, improvement evaluator, and memory curator can edit within narrower write boundaries.
- External research is isolated in `orchestrator-researcher`.

This reflects agent-computer interface research well because each role has an interface matched to its job. The newest improvement is the focused cleanup helper: information hygiene is now a builder-owned implementation responsibility instead of a vague review expectation.

Risks:

- More edit-capable agents means more places where scope control can fail.
- The cleanup helper can safely reduce stale references only if it stays tied to the approved builder work order.
- The improvement evaluator and memory curator can write durable artifacts during normal work, so reviewer, reflection, and reporter evidence must make those side effects visible.
- Bash-enabled planning and review agents can gather evidence, but prompts should continue to prefer narrow, project-local checks.

### Prompt Design And Instruction Structure

Sources: `SRC-005`, `SRC-010`, `SRC-012`

The prompts consistently define:

- role identity
- permissions
- directed helpers
- write boundaries or non-editing constraints
- non-goals
- route or trigger rules
- output fields
- structured feedback fields
- stop conditions and waiver behavior

The current structure is better than the earlier version in one important way: it avoids forcing every task through every helper. Adaptive risk triggers let low-risk documentation, wording, and metadata-only tasks stay lightweight while still requiring helper use for code, behavior, architecture, product-breakdown, external-research, and memory risks.

The tradeoff is that prompt quality now depends heavily on trigger clarity. If `helper_not_used` rationales are weak, the system can appear compliant while skipping useful independent judgment.

Future prompt changes should include lightweight `AK-*` trace references in product decisions or prompt-change rationale. The runtime prompts themselves do not need to be full research documents, but durable changes to agent responsibilities should cite the relevant claim IDs.

### Memory, Reflection, And Lessons

Sources: `SRC-001`, `SRC-006`, `SRC-009`, `SRC-010`

The current memory model is substantially stronger than the earlier alignment document described:

- `orchestrator-memory` retrieves task-relevant lessons, patterns, and decision pointers without editing them.
- `orchestrator-lessons` turns persistent lesson memory into prevention checks for planning.
- `orchestrator-review-lessons` independently checks implementation evidence against relevant lessons.
- `orchestrator-reflection` reviews completed run evidence and owns the final decision about whether memory candidates should be curated, rejected, deferred, or marked not applicable.
- `orchestrator-memory-curator` evaluates durable memory candidates and writes only lessons or patterns when the finding is repeatable, task-independent, and useful for future planning or review.

This addresses the earlier gap about lesson promotion ownership. The remaining risk is evidence quality. A one-off task note should not become memory, and a repeated workflow failure should not be left only as a backlog candidate.

The boundary between memory and improvement backlog is important:

- memory captures durable prevention rules, reusable patterns, and decision pointers
- improvement candidates capture future work
- implementation evidence and current task state belong in neither

### Review, Verification, And Evaluation

Sources: `SRC-001`, `SRC-003`, `SRC-006`, `SRC-011`

The review model remains one of the strongest parts of the system:

- verifier gathers focused command and file evidence
- completeness review checks contract satisfaction, acceptance criteria, tests, edge cases, information hygiene, stale references, duplicates, and orphaned artifacts
- architecture review checks boundaries, coupling, durable design choices, maintainability, readability, and product-breakdown fit
- lessons review checks persistent mistake memory
- reviewer applies the deterministic gate
- waivers require explicit risk, scope, and follow-up or expiry
- blocked runs route back to planner with revision context

The model is stronger after the redistribution because the reviewer owns helper selection and gate routing in one place. However, the reviewer must not become a single point of weak synthesis. The strongest future improvement would be explicit gate evidence rows that show:

- which helper was required by which trigger
- whether the helper ran or was waived
- what evidence satisfied each acceptance criterion
- which cleanup or traceability checks passed
- which findings were persisted as backlog or memory side effects

The current evidence model is task-local. It does not yet support aggregate workflow evaluation across runs.

### Multi-Agent Communication And Handoff

Sources: `SRC-002`, `SRC-003`, `SRC-008`, `SRC-010`

The old packet and handoff stages are no longer the center of communication. Current structured communication is carried by:

- planner-owned builder work order
- control flags
- structured stage feedback fields
- helper-used and helper-not-used fields
- focused verification evidence
- review-output protocol
- revision input with blocking finding IDs
- optional `handoff_required` section for external or manual implementation
- reflection result with memory incorporation status
- reporter final control report

This still aligns with AK-007, but the mechanism has changed. The work order is now the main handoff between planning and building. The optional handoff section is for external or manual implementation, not a mandatory runtime stage.

The main communication risk is compression loss. Many helpers can produce evidence, but the owning top-level stage may summarize away details needed by downstream reviewers. To reduce this risk, top-level stages should preserve stable IDs, command evidence, files inspected, files changed, helper decisions, and unresolved gaps rather than only summarizing conclusions.

### Continuous Improvement And Focused Capture

Sources: `SRC-006`, `SRC-009`, `SRC-010`, `SRC-011`

The current structure separates three related capture mechanisms:

- broad improvement discovery via `orchestrator-improvement`
- focused backlog evaluation via `orchestrator-improvement-evaluator`
- final memory-incorporation triage via `orchestrator-reflection`
- durable workflow memory writes via `orchestrator-memory-curator`

This is a useful design: exploratory improvement work is kept out of contained delivery, while focused findings from normal work can still be captured without expanding scope.

Risks:

- `orchestrator-improvement-evaluator` is available to many stages, so duplicate candidate checks must remain strict.
- Memory curation and improvement evaluation can call each other only for separate findings; otherwise they can create circular capture or double-record the same issue.
- Candidate persistence is governance, not implementation approval. Reviews and reports must keep that distinction visible.

## Recommended Improvements

1. Update research claim trace targets for the new structure.

`AK-002` and `AK-007` still mention packet/handoff targets. They should be broadened to include planner-owned work orders, control flags, structured feedback fields, helper evidence, and optional handoff sections.

2. Add explicit revision delta fields to planner output.

Revision planning should map each blocking finding ID to:

- changed scope or plan
- added or changed checks
- evidence that justifies the change
- unchanged constraints

3. Strengthen helper selection auditability.

Top-level planner and reviewer outputs should preserve a compact trigger matrix:

- trigger detected
- helper required
- helper used or waived
- `helper_not_used` rationale when waived
- evidence source

4. Keep improving evidence schema consistency.

Verifier evidence is already structured. Builder, cleanup, build-error resolver, improvement evaluator, and memory curator outputs should preserve comparable fields for command evidence, inspected files, written files, duplicate checks, and unresolved risks.

5. Track aggregate evaluation outcomes.

Add an optional operations or evolution artifact that records recurring blocked reasons, waiver frequency, helper skip frequency, repeated cleanup failures, memory candidates, and verification gaps. This would turn task-local feedback into system-level learning.

6. Add side-effect reporting for capture helpers.

Reflection and reporter outputs should clearly list improvement candidates and memory entries written, rejected, or needing more evidence. This keeps focused evaluation and memory curation visible rather than hidden as helper side effects.

7. Preserve strict write boundaries for edit-capable helpers.

Future prompt changes should review edit-capable agents as a separate risk class. Builder-owned helpers, improvement capture, and memory curation should never become general-purpose editing paths.

## Bottom Line

The current agent structure is more mature than the older linear stage model. It better distributes responsibility to subagents and aligns well with role specialization, evidence-based review, workflow memory, and scoped improvement capture.

The alignment is no longer accurately described as a packet/handoff-centered pipeline. It is now a coordinator-and-directed-helper system. That is a stronger architecture in several ways, but it depends on adaptive trigger quality, faithful helper evidence preservation, strict write boundaries, and clear separation between implementation, backlog capture, and memory curation.
