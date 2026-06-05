# Use Cases

## Actors

- Requester: provides the task, bug report, or improvement idea.
- Orchestrator: coordinates the workflow and routes work to specialist agents.
- Planner: normalizes the request, resolves uncertainty, coordinates planning helpers, and defines the work order.
- Planning helpers: find relevant files, create checklistable requirements, and extract architecture guardrails when needed. The planner records test strategy and product-breakdown placement directly in the work order.
- Software architect: protects modularity, simple solutions, readability, and coherent module responsibilities.
- Test architect: defines focused verification strategy and expected evidence.
- Product architect: protects product behavior, product-breakdown placement, durable decisions, and traceability.
- Candidate-capture mode: uses the guarded planner, builder, reviewer, reflection, and reporter chain to turn improvement opportunities into backlog candidates.
- Builder: makes the approved changes and coordinates build-error, cleanup, documentation, and research helpers when needed.
- OpenCode build agent: handles direct operator-chosen implementation work when invoked explicitly outside the orchestrator path.
- Reviewer: coordinates verification, independent review helpers, and the completion gate.
- Review helpers: independently review contract completeness, verification adequacy, code quality, architecture, cleanliness, information hygiene, and lessons learned.
- Completion gate: computes approved, blocked, or waiver-required outcomes inside reviewer.
- Reflection agent: reviews completed runs for durable memory candidates before final reporting.
- Reporter: produces the final control report.
- Researcher: gathers external documentation or dependency context when needed.
- Human operator: approves waivers or re-runs tasks when the gate blocks completion.

## Guarded Delivery

## UC-001: Normalize A Request

Goal: turn a rough instruction into a concrete task shape and work order.

Input:

- stakeholder note
- rough feature request
- bug report
- technical improvement idea

Output:

- normalized task summary
- execution order
- likely follow-up agents

Primary value:

- prevents ambiguity at the start of the workflow

## UC-002: Create A Planner-Owned Work Order

Goal: turn the task into a binding, checklistable work order.

Input:

- normalized task
- project context
- relevant repository files

Output:

- task objective
- in scope and out of scope
- functional requirements
- acceptance criteria
- completion checklist
- waiver rules
- structured user-feedback and improvement-candidate fields

Primary value:

- prevents lost requirements and vague completion

## UC-003: Preserve Architecture During Agentic Development

Goal: keep work adapted to the current solution.

Input:

- task contract
- architecture notes
- project constraints
- existing patterns

Output:

- architectural constraints
- integration boundaries
- forbidden shortcuts
- coupling risks
- architecture review checklist

Primary value:

- prevents locally convenient implementations that damage the broader system

## UC-004: Check Persistent Known Mistakes

Goal: prevent the same project-specific mistakes from repeating.

Input:

- task contract
- architecture context
- versioned known mistakes

Output:

- relevant known mistakes
- task-specific prevention rules
- checks to run before completion
- new lesson candidates

Primary value:

- reduces repeated correction loops

## UC-005: Produce A Builder Work Order

Goal: generate strict builder instructions that a coding agent can implement from.

Input:

- requirement contract
- architecture context
- known mistake checks
- test obligations and product-breakdown guidance

Output:

- mission
- implementation behavior
- step-by-step guidance
- required tests and checks
- definition of done
- stop conditions

Primary value:

- improves coding-agent reliability without embedding code editing in the control docs

## UC-006: Implement Changes

Goal: carry out the approved changes and collect implementation evidence.

Input:

- builder work order
- handoff section when external or manual implementation is requested
- relevant files

Output:

- changed files
- cleanup of created, moved, renamed, rewritten, replaced, or superseded information
- traceability path for new information artifacts
- implementation evidence
- deferred improvement candidates

Primary value:

- keeps execution and evidence collection separate from approval

## UC-007: Review Implementation Evidence

Goal: get independent support-agent feedback before treating work as complete.

Input:

- builder work order
- requirement contract
- architecture constraints
- known mistake checks
- implementation evidence
- cleanup evidence for created, moved, renamed, rewritten, replaced, or superseded information

Output:

- focused verification output
- contract and acceptance review
- test adequacy review
- architecture review
- code quality review
- cleanliness review
- completeness review
- known mistake review
- stale-reference, duplicate-content, orphaned-artifact, and traceability findings
- blocking findings

Primary value:

- catches partial solutions and drift before completion

## UC-008: Enforce Completion Decision

Goal: decide whether a task is approved, blocked, or requires waivers.

Input:

- contract checklist
- independent reviewer findings
- waiver requests
- implementation evidence

Output:

- status
- contract checklist status
- reviewer approval status
- required waivers
- blocking gaps
- next required action

Primary value:

- prevents reviewer approval from silently overriding incomplete requirements

## UC-009: Capture New Lessons

Goal: update persistent mistake memory after a failed, corrected, or completed task exposes durable learning.

Input:

- reviewer findings
- failed tests
- human feedback
- repeated correction pattern
- final reflection output

Output:

- new known mistake candidate
- prevention rule
- future check wording
- trust metadata or revalidation cue when the lesson is sensitive to drift
- accepted, rejected, deferred, or no-action memory decision

Primary value:

- turns mistakes and reusable workflow learning into future guardrails without storing task-local state as memory

## UC-010: Produce A Final Control Report

Goal: summarize the run in a concise, reviewable report.

Input:

- structured artifacts
- gate decision
- final reflection result
- evidence bundle

Output:

- final status
- key evidence
- reflection and memory-incorporation result
- blocking items or waivers
- next required action

Primary value:

- makes the completion state explicit and auditable

## UC-011: Guard Design Quality During Architecture Work

Goal: make the architecture stage actively prefer modularity, simple solutions, and readable codebase evolution.

Input:

- task contract
- existing module boundaries
- current code organization
- relevant implementation patterns
- architecture constraints

Output:

- modularity expectations
- simplicity constraints
- readability checks
- module responsibility risks
- design quality review checklist

Primary value:

- prevents architecture review from focusing only on drift while missing unnecessary complexity, poor readability, or weak module boundaries

## Continuous Improvement

## UC-012: Drive Continuous Codebase Improvement

Goal: run the guarded workflow in candidate-capture mode to identify improvement work and feed a backlog without polluting contained feature implementation.

Input:

- bug, fix, regression, feature, documentation, cleanup, refactoring, pattern, module, or workflow subject
- explicit request for proposal, recommendation, evaluation, discovery, documented candidate, future task seed, or backlog item
- current feature set
- current requirements
- implementation evidence
- reviewer findings
- known module and pattern friction
- repository structure and change history

Output:

- cleanup candidates
- refactoring candidates
- pattern switch candidates
- module responsibility switch candidates
- tuning opportunities
- improvement rationale and priority
- follow-up contract seeds
- backlog-ready improvement entries
- no-candidate rationale when deliberate candidate capture finds no backlog-worthy item

Primary value:

- turns delivery evidence and requirement pressure into deliberate codebase improvement while keeping feature diffs scoped and verifiable

Workflow boundary:

- candidate-capture mode may persist backlog entries, but must not edit implementation files
- every deliberate candidate-capture run must receive a reviewed disposition: accepted candidate or reviewed no-candidate result
- route selection is based on requested outcome, so a bug/fix/regression subject still uses candidate-capture mode when the user asks for candidate capture rather than implementation
- candidates must not be implemented inside a contained feature task unless they are explicitly part of that task contract
- accepted candidates become backlog entries or future task contracts before code changes begin

## Direct Execution

## UC-013: Use Direct Build Execution Outside The Guarded Orchestrator

Goal: allow an operator to deliberately invoke OpenCode's build agent directly without weakening the default guarded orchestrator path.

Input:

- explicit operator-selected build invocation
- task prompt
- repository files

Output:

- direct build-agent execution
- no change to the default orchestrator entrypoint
- no inherited orchestrator prompt when the normal build agent is explicitly selected
- no permission for the orchestrator to skip planner, builder, reviewer, reflection, or reporter stages

Primary value:

- preserves operator escape hatches while keeping the default workflow governed

## UC-014: Review Current Repository State

Goal: assess the repository's current state for freshness, completeness, consistency, traceability, and alignment with the current product and workflow contract.

Input:

- repo files that need review, including code, documentation, config, prompts, and metadata
- product-breakdown source docs when the review needs product context
- runtime prompts and workflow policy when the review needs workflow context
- recent repository changes relevant to the review scope
- user-specified review scope

Output:

- review gap list
- stale, duplicated, conflicting, or orphaned references
- missing trace links or broken relationships between repo artifacts
- recommended updates or backlog candidates
- no-change rationale when the repo state is already aligned

Primary value:

- keeps repository artifacts aligned before stale code, docs, config, or metadata spreads

Workflow fit:

- the planner treats review work as a first-class task, not an informal side note
- if the user wants changes now, the task runs in delivery mode and the builder may edit the relevant repo artifacts while preserving traceability
- if the user wants only an assessment, proposal, future-task seed, or backlog capture, the task runs in candidate-capture mode and persists only backlog-ready review candidates
- in candidate-capture mode, the builder returns a reviewed `no_candidate` result when the inspected scope does not justify a backlog artifact
- reviewer still checks evidence, traceability, and stale-reference cleanup before completion
- external dependency, API, framework, standard, version, or documentation uncertainty still uses the researcher helper when needed

## Trace Links

- UC-001 through UC-014 feed `product-breakdown/01-product/product-commitments.md`
