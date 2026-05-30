# Agent Reasoning Knowledge Base

This directory stores research-backed knowledge for reasoning about agent structure and prompts.

It is intentionally separate from `product-breakdown/` and `.opencode/`:

- `product-breakdown/` remains the product traceability and decision source.
- `.opencode/` remains the copied runtime payload.
- `knowledge/agent-reasoning/` provides cited research claims that future decisions, prompt changes, or reviews can reference.

## Source Standard

Use peer-reviewed or arXiv research as the primary source material. Do not add practitioner blog posts, vendor documentation, or framework docs unless the source standard is explicitly changed later.

## How To Use

1. Start with `principles.md` for the compact design guidance.
2. Use `subject-overview.md` to browse the research by topic.
3. Use `source-notes/extracted-reference-notes.md` when an agent needs source-level context without opening the papers.
4. Use `knowledge-map.md` to connect a workflow concept to supporting claims.
5. Open the relevant `claims/AK-NNN-*.md` file for evidence, limits, and trace targets.
6. Cite the claim ID, not the full research summary, from future decisions or reviews.

## Source Text Policy

Do not vendor full paper text into this repository. Keep local reference material as metadata, paraphrased notes, topic mappings, and short trace pointers. If full text is needed, use the canonical source URLs in `source-index.md` or `source-notes/source-manifest.json`.

## ID Scheme

- `SRC-NNN` identifies a research source in `source-index.md`.
- `AK-NNN` identifies a reusable agent-knowledge claim in `claims/`.

Knowledge claims are not implementation approval. They provide reasoning evidence that must still be applied through the normal product-breakdown decision and workflow review process.
