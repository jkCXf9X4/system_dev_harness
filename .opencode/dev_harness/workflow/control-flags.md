# Control Flags

Purpose: Defines planner-owned control flags carried forward into builder and reviewer evidence.

Planner-owned planning output must carry these flags forward into builder and reviewer evidence:

```text
touches_information_artifacts: true|false
touches_product_breakdown: true|false
requires_decision_record: true|false
requires_external_research: true|false
```

Planner-directed helpers may correct initial flags when discovery or specialist planning proves them wrong. Reviewer and gate checks use the final planner work order as the source of truth for required evidence.

Source: extracted from `control-policy.md` §12 Control Flags.