# Decision Log Entry Template

Use this template for a compact global decision-log entry. It points to the full decision record and should not duplicate the complete rationale.

```markdown
| <ID> | <Title> | <Layer> | <Status> | `<path/to/decision.md>` | `<related-artifact.md>`, `<related-directory/>` |
```

## Fields

| Field | Purpose |
| --- | --- |
| ID | Stable decision ID, such as `PD-001`, `AD-001`, or `IMD-001`. |
| Title | Short decision title. |
| Layer | Owning layer: Intent, Product, Architecture, Implementation, Verification, Operation, or Evolution. |
| Status | Proposed, Accepted, Superseded, Rejected, or Deprecated. |
| Location | Path to the full decision file. |
| Related artifacts | Short list of directly affected artifacts. |

## Maintenance

- Keep the entry short and stable.
- Update it when status, file path, or primary affected artifacts change.
- Do not use it as a substitute for the full decision file.
