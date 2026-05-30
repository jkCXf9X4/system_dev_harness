# AK-002: Ground Synthesis In Prior Discovery

## Claim

Agent outputs are more controllable when planning and synthesis are grounded in inspected context instead of broad, late-stage improvisation.

## Practical Interpretation

Repository discovery should happen before contract, architecture, and implementation packet synthesis. Downstream stages should consume the discovered context and avoid repeating broad search unless their role explicitly allows it.

## Applies To

- Planner
- Discovery
- Contract
- Architecture
- Packet

## Evidence

- SRC-001 identifies agent construction, task context, and evaluation as linked concerns for autonomous agents.
- SRC-004 shows that actions that gather environment information can update and support reasoning plans.
- SRC-007 emphasizes the importance of software-agent interfaces for repository navigation and task execution.

## Trace Targets

- discovery-first workflow policy
- context bundle design
- packet source-material requirements

## Limits

Discovery should stay narrow enough to avoid wasting context or creating an implicit implementation plan before the contract exists.
