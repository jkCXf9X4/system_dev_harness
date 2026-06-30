# 05 Operation Layer

The operation layer describes durable operational behavior, support constraints, deployment constraints, monitoring expectations, and recovery expectations.

Runnable procedures, command examples, install steps, usage walkthroughs, and contributor workflow belong in `docs/`. Operation-layer artifacts may link to those guides, but should not copy their step-by-step instructions.

## Typical Artifacts



```text
runbook.md           - captures operational requirements and recovery constraints
monitoring.md        - captures metrics, alerts, and observability expectations
deployment-process.md - captures release and deployment product constraints
incident-response.md  - captures incident handling and escalation expectations
support-model.md      - captures support responsibilities and expectations
decisions/           - stores operational decisions and rationale
```

## Questions Answered

- What deployment constraints must the product satisfy?
- What monitoring and recovery expectations exist?
- What incident handling behavior is required?
- What operational responsibilities exist?
- What support processes are product requirements rather than guide steps?
- How are releases controlled?

## Example Decisions

```text
OD-001-use-feature-flags-for-risky-releases.md
OD-002-alert-on-failed-background-jobs.md
OD-003-keep-audit-logs-for-permission-changes.md
OD-004-deploy-through-controlled-weekly-releases.md
```

Operational decisions affect reliability, supportability, observability, deployment, incident response, and runtime cost.
