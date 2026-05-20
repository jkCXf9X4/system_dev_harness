# 02 Architecture Layer

The architecture layer describes the stable system structure that supports the product.

## Typical Artifacts



```text
quality-attributes.md - lists the properties the system must satisfy
context-view.md       - shows external actors, systems, and trust boundaries
container-view.md     - breaks the system into deployable or runtime units
component-view.md     - explains the internal structure of each container
data-view.md          - describes data ownership, flow, and storage choices
integration-view.md   - documents external integrations and protocols
deployment-view.md    - maps the runtime structure onto infrastructure
decisions/            - stores architecture-level decisions and rationale
```

## Questions Answered

- What are the major system parts?
- What are the important boundaries?
- How do components interact?
- Where is data owned?
- What quality attributes shape the design?
- How is the system deployed?

## Example Decisions

```text
AD-001-use-a-modular-monolith-for-v1.md
AD-002-project-is-the-core-bounded-context.md
AD-003-reporting-uses-a-separate-read-model.md
AD-004-background-jobs-handle-long-running-exports.md
```

Architecture decisions affect system boundaries, module ownership, runtime structure, data flow, integrations, deployment, and quality attributes.
