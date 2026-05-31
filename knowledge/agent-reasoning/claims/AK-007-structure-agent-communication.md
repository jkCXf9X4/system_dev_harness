# AK-007: Structure Communication Between Agents

## Claim

Multi-agent systems need explicit communication structure so constraints and evidence survive handoffs.

## Practical Interpretation

Handoff and packet prompts should preserve mission, source material, constraints, required checks, stop conditions, and unresolved gaps. Agents should not infer missing upstream decisions when the packet is incomplete.

## Applies To

- Orchestrator
- Packet
- Handoff
- Builder
- Reporter

## Evidence

- SRC-003 highlights agent profiling and communication as essential topics in LLM-based multi-agent systems.
- SRC-002 surveys multi-agent and human-agent cooperation as major LLM-agent application patterns.

## Trace Targets

- implementation packet shape
- handoff boundary
- final control report

## Limits

Structured communication should stay compact. Overly large packets can obscure the constraints they are meant to preserve.
