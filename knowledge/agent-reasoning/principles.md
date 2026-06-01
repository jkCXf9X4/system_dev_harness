# Agent Structure And Prompt Principles

These principles summarize the reusable guidance from the claim set.

| Principle | Supported by |
| --- | --- |
| Split complex work into explicit roles with narrow responsibilities. | AK-001 |
| Perform repository/context discovery before contract or implementation synthesis. | AK-002 |
| Keep reasoning, tool use, and evidence capture connected, but do not let action stages invent scope. | AK-003 |
| Use independent review and feedback loops to correct incomplete or weak outputs. | AK-004 |
| Keep persistent lessons as explicit memory, with reviewable prevention checks. | AK-005 |
| Treat retrieved memory as a hypothesis that may need freshness, provenance, scope, and live-environment verification before use. | AK-009 |
| Design software agents around the interface they use to inspect, edit, and test code. | AK-006 |
| Make inter-agent communication structured enough to preserve constraints across handoffs. | AK-007 |
| Evaluate agent output against evidence, task criteria, and failure modes rather than self-assessed confidence. | AK-008 |

## Practical Rule

When changing agent prompts or structure, cite the smallest relevant `AK-NNN` claim and explain how the change preserves or improves that claim.
