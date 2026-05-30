# Source Notes

This directory gives agents local access to source-level research context without storing full paper text.

Files:

- `extracted-reference-notes.md`: paraphrased source extracts grouped by source ID.
- `source-manifest.json`: machine-readable source metadata, canonical links, topic tags, and claim mappings.

Use these notes for prompt and agent-structure reasoning. Use the canonical source URLs when deeper source inspection is required.

## Local Extraction Rules

- Prefer paraphrased notes over verbatim text.
- Preserve source IDs exactly as defined in `../source-index.md`.
- Keep source mappings traceable to subjects and claim IDs.
- Do not treat a note as implementation approval; route product or prompt changes through the normal decision process.
