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
- `.opencode/agents/orchestrator-packet.md`
- `.opencode/agents/orchestrator-handoff.md`
- `.opencode/agents/orchestrator-builder.md`
- `.opencode/agents/orchestrator-verifier.md`
- `.opencode/agents/orchestrator-review-*.md`
- `.opencode/agents/orchestrator-reviewer.md`
- `.opencode/agents/orchestrator-reporter.md`
- `.opencode/agents/orchestrator-improvement.md`
- `.opencode/agents/orchestrator-researcher.md`

Policy and product context:

- `.opencode/dev_harness/workflow/control-policy.md`
- `.opencode/dev_harness/workflow/review-output.md`
- `product-breakdown/02-architecture/architecture.md`
- `product-breakdown/02-architecture/decisions/AD-001-use-opencode-agent-workflow-for-orchestration.md`
- `product-breakdown/02-architecture/decisions/AD-003-use-structured-handoff-before-code-editing.md`

## Overall Assessment

The current structure aligns well with the research direction represented by `SRC-001` through `SRC-012`.

The strongest alignment is with:

- role specialization and multi-agent decomposition (`AK-001`)
- discovery before synthesis (`AK-002`)
- explicit reasoning/action/evidence separation (`AK-003`)
- independent review loops and deterministic gating (`AK-004`, `AK-008`)
- explicit memory through known mistakes (`AK-005`)
- agent-computer interface boundaries through permissions and stage prompts (`AK-006`)
- structured handoffs and packets (`AK-007`)

The main improvement opportunity is not the high-level architecture. The current architecture already follows the research-backed shape. The next gains are likely in stronger traceability between each prompt instruction and the knowledge claims, clearer evaluation metrics for prompt quality, and tighter handling of external research and agent-computer interface behavior.

## Alignment Matrix

| Research-backed claim | Current alignment | Evidence in current solution | Assessment |
| --- | --- | --- | --- |
| AK-001: role specialization | Strong | The orchestrator is only a dispatcher. Specialist stages own planning, discovery, contract, architecture, lessons, packet, builder, verifier, review, gate, reporting, research, and improvement. | The structure follows source guidance that complex agent systems should use explicit functional roles instead of a monolithic prompt. |
| AK-002: ground synthesis in prior discovery | Strong | Planner cannot inspect the repository. Discovery is the only broad search stage. Contract, architecture, packet, and handoff consume discovery output and avoid broad rediscovery. | This directly supports discovery-before-synthesis and reduces hallucinated contracts or implementation plans. |
| AK-003: connect reasoning with tool and environment actions | Moderate to strong | Discovery, builder, verifier, and reviewer prompts require files inspected, commands run, evidence, and changed files. | Good action/evidence capture exists, but prompts could more explicitly require "how evidence changed the plan" in discovery, verifier, and revision loops. |
| AK-004: review feedback loops | Strong | Independent requirement, architecture, completeness, lessons, and QA reviews feed a completion gate. Blocked outputs route into a revision loop. | The structure matches feedback-loop research well and avoids single-pass self-approval. |
| AK-005: explicit reviewable memory | Moderate to strong | `orchestrator-lessons` reads versioned known mistakes and turns relevant lessons into prevention rules. Review-lessons checks implementation evidence against persistent memory. | The workflow uses durable memory, but new lesson creation appears candidate-based rather than governed by an explicit promotion policy. |
| AK-006: agent-computer interface design | Moderate | Per-agent permissions separate read, search, edit, bash, task, and external access. Builder edits; verifier and reviewers are read-only. | Permission boundaries are strong. The remaining gap is that shell/tool output schemas are prose-based, not structured enough to consistently compare across runs. |
| AK-007: structured communication | Strong | Contract, architecture, lessons, packet, and handoff prompts require structured outputs. `control-policy.md` defines stage applicability, control flags, waivers, and revision flags. | The packet/handoff structure aligns closely with multi-agent communication research. |
| AK-008: evaluate against evidence | Strong | Verifier collects evidence. Review agents use a shared review-output protocol. Gate blocks on missing evidence, missing hygiene, or missing product-breakdown traceability. | The completion model is research-aligned. Further rigor would come from explicit evaluation dimensions and historical outcome tracking. |

## Research-To-Structure Fit

### Agent Architecture And Role Decomposition

Sources: `SRC-001`, `SRC-002`, `SRC-003`, `SRC-008`, `SRC-010`

The current agent set maps cleanly to specialized responsibilities:

- `orchestrator` is coordination only.
- `planner` handles request normalization.
- `discovery` handles repository inspection.
- `contract` defines verifiable obligations.
- `architecture` defines design constraints.
- `lessons` injects memory.
- `packet` packages implementation constraints.
- `builder` executes.
- `verifier` checks.
- `review-*` agents provide independent assessment.
- `reviewer` applies the gate.
- `reporter` summarizes outcome.
- `improvement` separates exploratory backlog creation from delivery work.
- `researcher` isolates external source gathering.

This is a good fit for the surveyed view of LLM agents as systems with separable components and multi-agent workflows with profiled roles. The use of a dispatcher that is explicitly forbidden from doing specialist work is especially aligned with role-boundary guidance.

Risk: the number of agents can create coordination cost. The current packet and control flags mitigate this, but future roles should be added only when they reduce ambiguity or isolate a real failure mode.

### Planning, Task Decomposition, And Scope Control

Sources: `SRC-004`, `SRC-005`, `SRC-009`, `SRC-010`

The current workflow decomposes delivery into request normalization, discovery, contract, guardrails, memory, packet, execution, verification, review, and gate. This reflects planning research that separates task decomposition, plan selection, reflection, memory, and external support.

Strong points:

- Planner is prevented from inspecting the repository, keeping classification separate from evidence gathering.
- Discovery happens before contract and architecture synthesis.
- Packet generation is explicitly scoped to upstream outputs.
- Improvement discovery is separated from contained delivery, reducing scope drift.

Gap: revision planning receives blocking gaps, but the prompts could require an explicit "changed plan because of evidence" section. That would better connect blocked feedback to a revised plan.

### Tool Use, Repository Interaction, And Agent-Computer Interface

Sources: `SRC-004`, `SRC-007`, `SRC-010`

The permission model is a strong local expression of agent-computer interface design:

- Orchestrator cannot read, search, edit, or run shell commands.
- Planner cannot inspect repository files.
- Discovery can search and run shell commands, but cannot edit.
- Builder can edit.
- Verifier can run checks but cannot edit.
- Reviewers and gate are read-only.

This aligns with the SWE-agent result that software agents need interfaces designed for repository navigation, editing, and testing. It also supports ReAct-style interaction because discovery, builder, and verifier connect environment actions to later reasoning.

Gap: command evidence is requested as prose. A stricter evidence schema would improve comparability:

- command
- purpose
- exit code
- important output excerpt
- files or behavior covered
- uncovered acceptance criteria

### Prompt Design And Instruction Structure

Sources: `SRC-005`, `SRC-010`, `SRC-012`

The prompts consistently define:

- role identity
- permissions
- non-goals
- input assumptions
- output fields
- stop conditions or blocking behavior

This aligns with prompt-engineering research that task-specific instructions and structured outputs improve downstream control. The prompts also avoid relying on a generic "be helpful" instruction for critical workflow behavior.

Gap: prompts do not yet cite `AK-*` claims directly. Adding lightweight claim references to prompt comments or product decisions would improve traceability from research to runtime instruction.

### Memory, Reflection, And Lessons

Sources: `SRC-001`, `SRC-006`, `SRC-009`, `SRC-010`

The known-mistakes stage is a strong design choice because it makes memory explicit, versioned, and reviewable instead of relying on hidden conversation context. The review-lessons agent closes the loop by checking whether relevant lessons were actually applied.

Gap: the system distinguishes "lesson candidates" from existing memory, but the promotion path for turning repeated findings into durable lessons should be explicit. Without that, memory can become either stale or underused.

### Review, Verification, And Evaluation

Sources: `SRC-001`, `SRC-003`, `SRC-006`, `SRC-011`

The evaluation model is one of the strongest parts of the current solution:

- verifier gathers local evidence
- reviewers independently evaluate against different criteria
- shared review output protocol standardizes pass/fail/waiver status
- completion gate blocks missing evidence
- waiver policy requires named risk, scope, and follow-up or expiry condition
- revision loop preserves findings and prevents infinite repetition

This aligns well with agent-evaluation research, especially the need for realistic evidence, robustness checks, and explicit treatment of missing or incomplete evidence.

Gap: the current evaluation is task-local. The system does not yet track aggregate workflow quality, such as repeated blocked reasons, prompt-stage failure rates, waiver frequency, or verification gaps over time.

### Multi-Agent Communication And Handoff

Sources: `SRC-002`, `SRC-003`, `SRC-008`, `SRC-010`

The packet and handoff stages are strong communication controls. They preserve:

- mission
- source material
- control flags
- implementation behavior
- architecture constraints
- known mistakes
- checks
- definition of done
- stop conditions
- missing upstream context
- deferred improvement candidates

This matches research concerns around communication and coordination in multi-agent systems.

Gap: the packet is the central coordination artifact, but the prompt does not explicitly require source-to-requirement trace rows. Adding a compact trace table could make downstream review easier.

## Recommended Improvements

1. Add research trace references to product decisions and prompt-change decisions.

Use `AK-*` IDs in future architecture or implementation decisions when changing agent responsibilities, prompt output fields, or gate behavior.

2. Add a structured evidence schema to verifier and builder outputs.

This would strengthen `AK-003`, `AK-006`, and `AK-008` by making environment evidence easier for reviewers and gates to consume consistently.

3. Add an explicit revision delta field.

Planner or packet revisions should state:

- blocking finding addressed
- changed scope or plan
- evidence that justifies the change
- unchanged constraints

4. Define a lesson promotion policy.

The workflow should say when a new lesson candidate becomes durable known-mistake memory, who approves it, and when stale lessons should be retired.

5. Track aggregate evaluation outcomes.

Add an optional improvement-backlog or operations artifact that records recurring blocked findings, waiver reasons, missing evidence categories, and prompt-stage friction. This would turn task-local reviews into system-level learning.

6. Add compact source-to-contract trace rows in implementation packets.

For research-backed or product-breakdown-sensitive work, the packet could include a table mapping source material to requirements, checks, and review focus.

## Bottom Line

The current agent structure is well aligned with the research results. It already implements the major design patterns supported by the source set: specialized roles, discovery before synthesis, explicit tool/action boundaries, persistent memory, structured handoffs, independent review, evidence-based gating, and controlled revision loops.

The next improvements should focus on measurable rigor rather than structural expansion: better evidence schemas, direct `AK-*` trace links, revision deltas, lesson promotion rules, and aggregate evaluation metrics.
