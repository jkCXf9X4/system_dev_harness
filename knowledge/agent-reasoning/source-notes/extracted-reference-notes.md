# Extracted Reference Notes

These notes extract the decision-relevant meaning of each source for local agent access. They are paraphrased and intentionally not a copy of the full papers.

## SRC-001: A Survey on Large Language Model based Autonomous Agents

Canonical source: https://arxiv.org/abs/2308.11432

Primary subjects:

- agent architecture
- memory
- evaluation
- applications and open challenges

Agent-relevant extract:

- Treat LLM-based autonomous agents as systems, not isolated prompts.
- The paper frames construction, application, evaluation, and open challenges as connected design concerns.
- The construction view supports separating model reasoning, memory, tool interaction, planning, and environment feedback.
- The evaluation view supports explicit checks instead of relying on model confidence or implementation self-report.
- Memory is useful when it improves later decisions, but it must be bounded and connected to evaluation signals.

Useful for:

- deciding whether an agent workflow needs explicit construction stages
- justifying memory and evaluation as first-class workflow parts
- checking that prompt changes do not overfocus on wording while ignoring system design

Mapped claims:

- AK-001
- AK-002
- AK-004
- AK-005
- AK-008

## SRC-002: The Rise and Potential of Large Language Model Based Agents

Canonical source: https://arxiv.org/abs/2309.07864

Primary subjects:

- general LLM-agent framework
- perception, decision, and action components
- single-agent, multi-agent, and human-agent cooperation

Agent-relevant extract:

- The paper describes LLM agents through separable functional components rather than a single monolithic prompt.
- Its high-level framework supports assigning different responsibilities to different stages or roles.
- Multi-agent and human-agent settings require communication and coordination discipline.
- Agent societies and cooperation patterns add flexibility, but also increase coordination and evaluation complexity.

Useful for:

- reviewing role boundaries
- deciding whether a workflow should use one agent, multiple agents, or human review checkpoints
- grounding handoff design in a general agent framework

Mapped claims:

- AK-001
- AK-005
- AK-007

## SRC-003: Large Language Model based Multi-Agents: A Survey of Progress and Challenges

Canonical source: https://arxiv.org/abs/2402.01680

Primary subjects:

- multi-agent systems
- agent profiling
- communication
- capability growth
- benchmarks and challenges

Agent-relevant extract:

- Multi-agent LLM systems are relevant when complex work benefits from specialized profiles and communication.
- Agent profiles should be deliberate because they shape what each agent attends to, produces, and hands off.
- Communication is a central design concern, not just a formatting detail.
- Multi-agent designs need benchmarks and checks because coordination can fail even when individual agents seem competent.
- The source supports treating role design, communication protocol, and evaluation as coupled choices.

Useful for:

- designing orchestrator, planner, builder, verifier, and reviewer boundaries
- checking that handoffs preserve constraints and evidence
- identifying risks from over-fragmented agent workflows

Mapped claims:

- AK-001
- AK-004
- AK-007
- AK-008

## SRC-004: ReAct: Synergizing Reasoning and Acting in Language Models

Canonical source: https://arxiv.org/abs/2210.03629

Primary subjects:

- interleaved reasoning and action
- tool use
- environment feedback
- interpretability

Agent-relevant extract:

- Reasoning and action should inform each other during a task.
- Environment actions can gather information that changes the plan.
- Reasoning traces help track goals, exceptions, and plan updates.
- Tool interaction can reduce unsupported generation when the tool returns relevant external evidence.
- The workflow implication is that discovery, tool use, and evidence capture should be attached to reasoning steps.

Useful for:

- designing discovery and builder stages
- deciding when an agent must inspect files before planning or editing
- requiring evidence links from commands, tests, and repository reads

Mapped claims:

- AK-002
- AK-003
- AK-006

## SRC-005: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

Canonical source: https://arxiv.org/abs/2201.11903

Primary subjects:

- multi-step reasoning
- task decomposition
- prompt examples

Agent-relevant extract:

- Decomposing hard tasks into intermediate reasoning steps can improve performance on complex tasks.
- The technique is most relevant when the task requires multi-step inference rather than direct recall.
- For agent prompts, the practical lesson is to make decomposition explicit where it affects correctness.
- The source does not by itself prove that longer visible reasoning is always better; reasoning structure should be paired with verification.

Useful for:

- planner and contract prompts
- deciding when a prompt needs explicit subtask decomposition
- avoiding one-shot synthesis for complex requests

Mapped claims:

- AK-002
- AK-007

## SRC-006: Reflexion: Language Agents with Verbal Reinforcement Learning

Canonical source: https://arxiv.org/abs/2303.11366

Primary subjects:

- reflection
- feedback
- episodic memory
- coding and sequential decision tasks

Agent-relevant extract:

- Agents can improve across attempts by converting task feedback into reusable verbal memory.
- Feedback can come from external results or internal critique, but it must be represented in a way that later attempts can use.
- Reflection is most useful when it is connected to observable success or failure signals.
- For this repository, the strongest design implication is to store durable lessons as reviewable memory rather than leaving them in transient conversation state.

Useful for:

- lesson-memory policy
- review feedback loops
- deciding when repeated failures should become persistent known mistakes

Mapped claims:

- AK-004
- AK-005
- AK-008

## SRC-007: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

Canonical source: https://arxiv.org/abs/2405.15793

Primary subjects:

- software-engineering agents
- agent-computer interface design
- repository navigation
- editing and testing

Agent-relevant extract:

- Software agents are users of their tooling and benefit from interfaces designed around their needs and limits.
- Repository navigation, editing, and test execution are not incidental details; they shape agent performance.
- The source supports explicit command, file, and verification interfaces for coding agents.
- The paper is especially relevant when deciding whether an agent should have broad shell access, narrowed tools, or structured repository operations.

Useful for:

- builder and verifier design
- deciding tool permissions
- specifying evidence from file reads, edits, and test commands

Mapped claims:

- AK-002
- AK-003
- AK-006
- AK-008

## SRC-008: LLM-Based Multi-Agent Systems for Software Engineering

Canonical source: https://arxiv.org/abs/2404.04834

Primary subjects:

- software-engineering multi-agent systems
- SDLC coverage
- specialization
- trustworthy automation

Agent-relevant extract:

- Multi-agent LLM systems can target multiple software-development lifecycle stages.
- Specialization and collaboration can help manage software complexity, but they introduce dependency on agent synergy.
- The source identifies robustness, trustworthiness, and scalable coordination as important open areas.
- For this repository, it supports connecting prompt/agent roles to concrete software-engineering stages rather than generic personas.

Useful for:

- mapping roles to SDLC responsibilities
- justifying specialized agents for planning, implementation, verification, and review
- documenting why review gates still matter in autonomous workflows

Mapped claims:

- AK-001
- AK-007
- AK-008

## SRC-009: Understanding the planning of LLM agents

Canonical source: https://arxiv.org/abs/2402.02716

Primary subjects:

- planning
- task decomposition
- plan selection
- external modules
- reflection and memory

Agent-relevant extract:

- LLM-agent planning can be understood through categories such as decomposition, selection, external support, reflection, and memory.
- Planning quality depends on how the agent turns an objective into actionable steps and how it revises those steps.
- External modules and memory are planning supports, not substitutes for task understanding.
- The workflow implication is to separate request interpretation, context discovery, plan construction, and plan verification.

Useful for:

- planner prompt design
- scope control
- deciding what information must exist before implementation starts

Mapped claims:

- AK-002
- AK-003
- AK-005
- AK-008

## SRC-010: A Review of Prominent Paradigms for LLM-Based Agents

Canonical source: https://arxiv.org/abs/2406.05804

Primary subjects:

- tool use
- retrieval-augmented generation
- planning
- feedback learning
- policy, evaluator, and dynamic model roles

Agent-relevant extract:

- Tool use, planning, and feedback learning are reusable paradigms across LLM-agent frameworks.
- The source provides a unified way to compare agent workflows through roles, tasks, environments, and evaluators.
- Evaluation and feedback are not add-ons; they shape how agent behavior improves and how workflow quality is judged.
- For prompt work, this supports distinguishing task policy, evaluator behavior, and environment interaction in separate instructions.

Useful for:

- role and prompt taxonomy
- deciding where evaluator logic belongs
- reviewing whether a workflow has planning, action, and feedback paths

Mapped claims:

- AK-001
- AK-003
- AK-004
- AK-007

## SRC-011: Survey on Evaluation of LLM-based Agents

Canonical source: https://arxiv.org/abs/2503.16416

Primary subjects:

- agent evaluation
- benchmarks
- software-engineering agents
- robustness, safety, cost, and scalability

Agent-relevant extract:

- Agent evaluation should cover capabilities, application-specific benchmarks, generalist agents, benchmark dimensions, and developer evaluation tools.
- Planning, reasoning, and tool use need evaluation in realistic environments, not only isolated language tasks.
- The source identifies open gaps around cost-efficiency, safety, robustness, fine-grained assessment, and scalable evaluation.
- For this repository, it supports completion gates that require evidence and explicit residual risk handling.

Useful for:

- verifier and reviewer prompts
- acceptance criteria
- deciding when a task should be blocked for missing evidence
- documenting evaluation gaps in decisions

Mapped claims:

- AK-004
- AK-008

## SRC-012: A Systematic Survey of Prompt Engineering in Large Language Models

Canonical source: https://arxiv.org/abs/2402.07927

Primary subjects:

- prompt engineering
- task-specific instructions
- prompt taxonomy
- strengths, limits, and applications

Agent-relevant extract:

- Prompt engineering uses task-specific instructions or learned prompt representations to shape model behavior without changing model weights.
- Prompt techniques vary by application and have different strengths and limitations.
- The source supports making prompt structure explicit: role, context, task, constraints, output format, and evaluation expectations should not be left implicit.
- It also supports avoiding universal prompt claims; prompt choices should be tied to task type and measured behavior.

Useful for:

- prompt audits
- output contract design
- deciding which instruction fields belong in each agent role
- documenting prompt limitations

Mapped claims:

- AK-001
- AK-002
- AK-007
- AK-008

## SRC-013: From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

Canonical source: https://arxiv.org/abs/2605.26112

Primary subjects:

- agent harness design
- context governance
- trustworthy memory
- dynamic skill routing
- verification and governance
- safe agent evolution

Agent-relevant extract:

- The paper argues that agent performance emerges from the interaction between the foundation model and the surrounding harness: memory, context construction, skill routing, orchestration, and verification/governance.
- It frames trustworthy memory as a systems bottleneck, not just a storage problem.
- Memory quality is described through precision, durability, retrievability, and verifiability.
- The key memory failure mode is stale-but-confident use: a relevant memory entry can remain retrievable while its target has drifted after environment changes.
- The proposed system move is to re-establish trust at retrieval time and periodically verify memory against the live environment.
- The paper separates prompt, skill, and memory as temporal layers: prompt controls the current task, skill controls reusable procedures, and memory controls what should survive over time.
- Harness-level evaluation should include process and longitudinal measures such as memory hygiene, context efficiency, communication fidelity, verification cost, and safe evolution.

Useful for:

- memory-curator rules
- deciding when memory-derived assumptions require live verification
- separating durable memory, procedural patterns, and improvement candidates
- evaluating workflow memory quality across repeated runs
- reviewing whether prompt changes treat memory as evidence rather than permanent truth

Mapped claims:

- AK-005
- AK-006
- AK-007
- AK-008
- AK-009
