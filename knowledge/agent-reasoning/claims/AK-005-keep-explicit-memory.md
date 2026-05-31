# AK-005: Keep Lessons As Explicit Reviewable Memory

## Claim

Persistent, inspectable memory helps agents reuse feedback and avoid repeated failures better than relying on transient conversation context.

## Practical Interpretation

Known mistakes should be stored as versioned artifacts with stable IDs, prevention rules, and completion checks. Prompt stages should load only task-relevant lessons to avoid noisy context.

## Applies To

- Lessons stage
- Lessons review
- Known-mistakes memory
- Improvement workflow

## Evidence

- SRC-006 uses verbal feedback as memory for later attempts by language agents.
- SRC-001 discusses memory as a core part of autonomous-agent construction.
- SRC-002 frames LLM agents as systems that can incorporate internal state and external context.

## Trace Targets

- known-mistakes policy
- lessons prompt
- lessons review prompt

## Limits

Persistent memory can become stale. It needs pruning and should not be treated as permanent truth.
