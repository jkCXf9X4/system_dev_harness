# AK-001: Use Role Specialization For Complex Agent Workflows

## Claim

Complex LLM-agent workflows are easier to reason about when responsibilities are split into explicit roles instead of collapsed into one unconstrained agent.

## Practical Interpretation

Agent prompts should define narrow responsibilities, permissions, inputs, outputs, and non-goals. A coordinator should route work and preserve state without doing each specialist stage's job.

## Applies To

- Orchestrator
- Planner
- Discovery
- Contract
- Architecture
- Builder
- Verifier
- Review agents

## Evidence

- SRC-002 presents LLM-based agents as configurable systems with separable components for decision-making, perception, and action.
- SRC-003 surveys multi-agent systems in which agents are profiled, communicate, and collaborate to solve complex tasks.
- SRC-001 surveys autonomous-agent construction and evaluation as a system design problem, not just a prompt-writing problem.

## Trace Targets

- `orchestrator`
- `orchestrator-*` role prompts
- workflow stage boundaries

## Limits

Role specialization adds overhead. It should be used when coordination, traceability, review, or permission boundaries matter.
