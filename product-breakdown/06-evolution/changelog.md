# Changelog

## 2026-05-20

- Implemented IMP-001 through IMP-009 improvements:
  - Renamed docs directories to match product-breakdown template numbering
  - Distributed ADR files into per-layer `decisions/` directories with prefixed IDs
  - Created verification layer (`04-verification/`) and operation layer (`05-operation/`)
  - Added root `decision-log.md` and `traceability-map.md`
  - Added revision loop to guarded workflow (blocked gate → planner re-scoping)
  - Added improvement candidate persistence under `product-breakdown/06-evolution/backlog/`
  - Established backlog infrastructure under `06-evolution/`
