# AK-006: Design The Agent-Computer Interface Deliberately

## Claim

Software-engineering agents depend heavily on the interface they use to inspect repositories, edit files, and run tests.

## Practical Interpretation

Agent prompts should make allowed tools, file boundaries, verification commands, and evidence outputs explicit. Edit-capable stages should be separated from read-only review stages.

## Applies To

- Builder
- Verifier
- Direct build path
- Review agents

## Evidence

- SRC-007 reports that a custom agent-computer interface improves an agent's ability to navigate repositories, edit code, and execute tests.
- SRC-004 supports connecting environment actions to reasoning and plan updates.

## Trace Targets

- permission blocks
- builder write boundary
- verifier read-only evidence collection

## Limits

Interface design does not remove the need for task contracts, architecture constraints, or human oversight.
