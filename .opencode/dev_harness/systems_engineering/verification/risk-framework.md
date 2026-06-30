# Risk Framework

> **Lightweight analytical framework for the orchestrator-systems-engineering agent.** This is not a formal risk management process. It provides vocabulary and structure for risk-aware analysis within the workflow.

## Risk Categories

| Category | Description |
|----------|-------------|
| Technical | Risk to system correctness, completeness, or quality |
| Schedule | Risk to timeline, sequencing, or delivery cadence |
| Integration | Risk to component compatibility or assembly |
| Interface | Risk to agent-to-agent handoff correctness |
| Resource | Risk to context window, concurrency, or tool availability |

## Likelihood Scale

| Level | Description |
|-------|-------------|
| Low | Unlikely to occur — no known precedent |
| Medium | May occur — some conditions present |
| High | Likely to occur — conditions are present or precedent exists |

## Impact Scale

| Level | Description |
|-------|-------------|
| Low | Minor effect — recoverable within normal workflow |
| Medium | Moderate effect — requires workflow adaptation |
| High | Major effect — blocks delivery or requires redesign |

## Risk Register Template

| ID | Category | Description | Likelihood | Impact | Mitigation | Residual Risk | Status |
|----|----------|-------------|------------|--------|------------|---------------|--------|
| R-001 | | | | | | | Open / Mitigated / Closed |

## Trace Links

- Used by: `orchestrator-systems-engineering` agent for risk-aware analysis
- Related artifacts: `architecture/interface-contracts.md` (interface risk), `architecture/agent-state-machines.md` (state-based risk), `verification/acceptance-criteria.md` (verification risk)