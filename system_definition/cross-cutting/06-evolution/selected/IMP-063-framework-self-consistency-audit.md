# IMP-063: Framework Self-Consistency Audit — Verify Framework Follows Its Own Rules

Use this template for one backlog-ready improvement candidate.

An improvement candidate is not implementation approval. It needs a scoped task contract before code or documentation changes begin.

## Lifecycle Stage

Candidate

## Status

Proposed

## Layer

Evolution

## Theme

Audit the agent framework to verify it follows its own rules, patterns, and quality standards — particularly KM-010 (reference, don't duplicate), KM-004 (minimize parallel solutions), and KM-005 (abstraction separation).

## Evidence

- Memory findings #1–4 from FRAMEWORK-REVIEW-001:
  - Finding #1: KM-010 (reference don't duplicate) — framework should verify its own prompts follow the rule
  - Finding #2: KM-004 (minimize parallel solutions) — check for duplicate entrypoints
  - Finding #3: KM-005 (abstraction separation) — check framework's own documentation chain
  - Finding #4: Memory coverage gaps: no lesson on review protocol structure, dependency/version drift, or framework self-testability
- `.opencode/dev_harness_memories/lessons.md` (KM-010, KM-004, KM-005 definitions)
- `.opencode/dev_harness_memories/patterns.md` (framework patterns)
- `.opencode/agents/` (all 20 agent definitions — potential violations)
- `.opencode/dev_harness/workflow/` (all 28 workflow policies — potential violations)

## Current Pain Or Risk

The framework defines quality rules (KM-010, KM-004, KM-005) but does not verify its own compliance with them. Known or suspected violations include:

- **KM-010 violations**: 
  - Planner inline output duplicates plan file schema (IMP-056)
  - Helper triggers split across two files (IMP-055)
  - Acceptance criteria exist in two locations (IMP-062 finding #5)
- **KM-004 violations**: 
  - Potential duplicate entrypoints for helper selection (planner-triggers.md vs adaptive-risk-triggers.md)
- **KM-005 violations**: 
  - God planner owns 8+ responsibilities (IMP-054)
  - Documentation chain may mix abstraction levels

Additionally, memory coverage has gaps: no lessons on review protocol structure, dependency/version drift, or framework self-testability.

## Proposed Improvement

create an audit agent that can be executed on demand that stores the accumulated knowledge of how to best audit the agent frameworks

Conduct a systematic self-consistency audit of the agent framework:

1. **KM-010 audit**: Scan all agent prompts and workflow policies for duplicated content that should be a single reference
2. **KM-004 audit**: Identify all entrypoints and verify each concern has exactly one entrypoint
3. **KM-005 audit**: Verify the documentation chain maintains clear abstraction separation
4. **Memory gap fill**: Add lessons for review protocol structure, dependency/version drift, and framework self-testability
5. **Remediation plan**: For each violation found, create a remediation candidate or add to existing candidates

## Expected Benefit

- Framework follows its own rules (credibility and consistency)
- Identified violations can be systematically remediated
- Memory coverage gaps are filled
- Improved framework quality and maintainability
- Sets a precedent for self-verification

## Risk And Blast Radius

- Medium blast radius: audit touches all agent definitions and workflow policies
- Risk of finding many violations (scope creep)
- Requires careful triage to distinguish critical violations from minor ones
- Remediation may span multiple tasks

## Suggested Priority

Medium

## Selected Date

<!-- Date when this candidate was selected for implementation, or N/A -->

## Completed Date

<!-- Date when implementation was verified complete, or N/A -->

## Implementation Reference

<!-- Link to task contract, PR, or changelog entry when moved to done -->

## Task Contract Seed

The smallest scoped task would:
1. Create a self-consistency audit checklist based on KM-010, KM-004, and KM-005
2. Scan all agent definitions in `.opencode/agents/` for KM-010 violations (duplicated content)
3. Document each violation with file path, line numbers, and suggested fix
4. Add findings to existing candidates or create new ones as needed

Do NOT implement:
- Remediation of found violations (document only)
- Changes to agent prompts or workflow policies
- Changes to memory entries

## Out Of Scope

- Remediation of found violations (document only)
- Changes to agent prompts or workflow policies
- Changes to memory entries
- Full audit of all 20 agents and 28 policies in one task (start with KM-010 scan of agents)

## Traceability

- Intent: Verify framework follows its own quality rules
- Product: Evolution layer — framework quality assurance
- Architecture: Audit-only; no structural changes
- Implementation: Audit checklist, scan results, candidate updates
- Verification: Audit checklist is complete; all violations are documented

## Notes

This finding originates from FRAMEWORK-REVIEW-001 memory findings #1–4. The framework defines quality rules (KM-010, KM-004, KM-005) but does not verify its own compliance. Several known violations are already captured by other candidates (IMP-054, IMP-055, IMP-056, IMP-062), but a systematic audit may reveal additional violations.