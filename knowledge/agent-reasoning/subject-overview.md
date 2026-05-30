# Subject Overview

This overview groups the knowledge base by research subject so prompt and agent-structure work can start from the right evidence area.

## 1. Agent Architecture And Role Decomposition

Core question: when should work be split into multiple agents or stages?

Relevant sources:

- SRC-001: autonomous-agent construction and evaluation from a broad systems view.
- SRC-002: LLM-agent framework with agent components and single-agent, multi-agent, and human-agent settings.
- SRC-003: multi-agent profiling, communication, capacity growth, benchmarks, and challenges.
- SRC-008: multi-agent software-engineering systems across SDLC tasks.

Relevant claims:

- AK-001: role specialization.
- AK-007: structured agent communication.

Use for:

- deciding whether a new agent role is justified
- reviewing whether an existing prompt has too many responsibilities
- explaining why orchestration should route rather than perform specialist work

## 2. Planning, Task Decomposition, And Scope Control

Core question: how should agents transform a rough request into bounded work?

Relevant sources:

- SRC-004: reasoning and acting can update plans through environment interaction.
- SRC-005: decomposed reasoning can help large models solve multi-step tasks.
- SRC-009: planning taxonomy: task decomposition, plan selection, external modules, reflection, and memory.
- SRC-010: planning as one of the central LLM-agent paradigms.

Relevant claims:

- AK-002: ground synthesis in prior discovery.
- AK-003: connect reasoning with tool and environment actions.
- AK-008: evaluate against evidence.

Use for:

- planner, discovery, contract, and packet prompt changes
- controlling scope drift before implementation
- deciding what context must exist before an agent can synthesize a plan

## 3. Tool Use, Repository Interaction, And Agent-Computer Interfaces

Core question: how should agents inspect, edit, test, and report work in a repository?

Relevant sources:

- SRC-004: interleaving reasoning with task-specific actions.
- SRC-007: software-engineering agents depend on repository navigation, editing, and testing interfaces.
- SRC-010: tool use and RAG as central LLM-agent paradigms.

Relevant claims:

- AK-003: connect reasoning with actions.
- AK-006: design the agent-computer interface deliberately.
- AK-008: evaluate against evidence.

Use for:

- permission design
- builder/verifier boundaries
- command evidence requirements
- decisions about what tool access an agent role should have

## 4. Prompt Design And Instruction Structure

Core question: what should prompts specify to make agent behavior reliable and reviewable?

Relevant sources:

- SRC-005: decomposed reasoning for multi-step tasks.
- SRC-012: prompt-engineering taxonomy and task-specific instruction design.
- SRC-010: workflow roles, evaluators, and policy models across agent paradigms.

Relevant claims:

- AK-001: role specialization.
- AK-002: ground synthesis in prior discovery.
- AK-007: structured communication.
- AK-008: evidence-based evaluation.

Use for:

- prompt audits
- deciding required return fields
- reducing ambiguous agent instructions
- separating task behavior from output protocol

## 5. Memory, Reflection, And Lessons

Core question: how should agent systems preserve useful feedback without accumulating stale context?

Relevant sources:

- SRC-001: memory as part of autonomous-agent construction.
- SRC-006: verbal feedback and reflection as reusable memory.
- SRC-009: reflection and memory as planning-support categories.
- SRC-010: feedback learning as a central LLM-agent paradigm.

Relevant claims:

- AK-004: review feedback loops.
- AK-005: explicit reviewable memory.

Use for:

- known-mistakes policy
- lesson review prompts
- improvement backlog reasoning
- deciding when feedback becomes persistent memory

## 6. Review, Verification, And Evaluation

Core question: how should the workflow decide whether agent output is acceptable?

Relevant sources:

- SRC-001: evaluation strategies for autonomous agents.
- SRC-003: benchmarks and challenges for multi-agent systems.
- SRC-006: feedback-driven improvement.
- SRC-011: agent evaluation across capabilities, benchmarks, robustness, safety, and cost-efficiency.

Relevant claims:

- AK-004: review feedback loops.
- AK-008: evaluate against evidence.

Use for:

- reviewer prompt design
- completion gate rules
- acceptance criteria
- deciding when missing evidence should block completion

## 7. Multi-Agent Communication And Handoff

Core question: how should information move between agents without losing constraints?

Relevant sources:

- SRC-002: multi-agent and human-agent cooperation.
- SRC-003: agent communication as a central multi-agent concern.
- SRC-008: software-engineering multi-agent systems and collaboration across SDLC stages.
- SRC-010: common workflow roles and evaluators across agent paradigms.

Relevant claims:

- AK-001: role specialization.
- AK-007: structured communication.
- AK-008: evidence-based evaluation.

Use for:

- packet and handoff structure
- final reporting requirements
- preserving source material, constraints, checks, and unresolved gaps across stages

## 8. Software-Engineering Agent Systems

Core question: what makes coding agents different from general task agents?

Relevant sources:

- SRC-007: agent-computer interface for automated software engineering.
- SRC-008: LLM-based multi-agent systems for software engineering across SDLC stages.
- SRC-011: software-engineering benchmarks as part of agent evaluation.

Relevant claims:

- AK-006: agent-computer interface design.
- AK-007: structured communication.
- AK-008: evidence-based evaluation.

Use for:

- code-editing boundaries
- verification command strategy
- direct build path reasoning
- distinguishing implementation evidence from review approval

## 9. Risks, Limits, And Research Gaps

Core question: what should the workflow not overclaim?

Relevant sources:

- SRC-003: multi-agent systems still face coordination and evaluation challenges.
- SRC-008: trustworthy software-engineering automation remains an open research direction.
- SRC-011: agent evaluation still has gaps around robustness, safety, cost-efficiency, and scalability.
- SRC-012: prompt-engineering methods have context-specific strengths and limits.

Relevant claims:

- AK-004: feedback loops need stable findings.
- AK-005: memory can become stale.
- AK-008: weak checks do not prove completion.

Use for:

- preventing over-broad claims in decisions
- documenting why human review, waivers, and gates still matter
- choosing when to defer a prompt or agent-structure change to the improvement backlog
