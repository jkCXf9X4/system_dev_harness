# Decision Log Guidance

The root-level `decision-log.md` is a global index of decisions.

It should answer:

- Which decisions exist?
- What layer owns each decision?
- What status does each decision have?
- Where is the full decision record?
- Which artifacts are related?

It should not duplicate decision context, alternatives, consequences, or verification detail.

## Suggested Table

```markdown
# Decision Log

| ID | Title | Layer | Status | Location | Related artifacts |
| --- | --- | --- | --- | --- | --- |
| PD-001 | Projects are the primary organizing unit | Product | Accepted | `01-product/decisions/PD-001-projects-are-the-primary-organizing-unit.md` | `capabilities.md`, `use-cases/create-project.md` |
| AD-001 | Use a modular monolith for v1 | Architecture | Accepted | `02-architecture/decisions/AD-001-use-a-modular-monolith-for-v1.md` | `component-view.md`, `deployment-view.md` |
```

## Maintenance Rule

When a decision file is added, renamed, superseded, or deprecated, update the index in the same change.

Use `templates/decision-log-entry-template.md` for compact register entries.
