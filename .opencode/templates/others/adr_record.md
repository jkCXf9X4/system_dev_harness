# ADR Record Template

Use this template to keep a lightweight register entry for an architecture decision record.
It complements the full ADR template when the repository also wants a compact index or log entry.

```text
ADR ID: [ADR-000]
Title: [Short descriptive title]
Status: [proposed | accepted | superseded | rejected]
File: [Path to the full ADR]
Context summary: [One or two sentences.]
Decision summary: [One or two sentences.]
Traceability: [Intent, Product Commitments, System Architecture, Technical Decisions, Implementation, Verification]
Follow-up actions: [Any cleanup, documentation, or backlog items.]
```

Best-practice notes:
- Keep the record entry short and stable.
- Use it to point to the full ADR, not to duplicate the whole decision discussion.
- Update the record when the ADR status or file path changes.
- one ADR per file
