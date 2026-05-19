# Use Cases

## Actors

- Requester: provides the task, bug report, or improvement idea.
- Orchestrator: coordinates the workflow and routes work to specialist agents.
- Planner: normalizes the request and defines the work order.
- Discovery agent: finds the smallest relevant file set and search targets.
- Contract agent: turns the task into a verifiable requirement contract.
- Architecture agent: extracts guardrails, boundaries, design quality goals, and forbidden shortcuts.
- Architect: protects modularity, simple solutions, readability, and coherent module responsibilities.
- Improvement agent: explores codebase improvement opportunities and turns them into backlog candidates.
- Lessons agent: checks the task against persistent mistakes.
- Packet agent: produces the strict implementation packet.
- Handoff agent: turns the packet into a paste-ready coding brief.
- Builder: makes the approved changes.
- OpenCode build agent: handles small bounded implementation tasks that do not need the full guardrail workflow.
- Verifier: runs focused checks and summarizes evidence.
- Review agents: independently review requirements, architecture, QA, completeness, and lessons.
- Completion gate: computes approved, blocked, or waiver-required outcomes.
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

## UC-002: Create A Requirement Contract

Goal: turn the task into a binding, checklistable contract.

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

## UC-005: Produce An Implementation Packet And Handoff

Goal: generate a strict packet that a coding agent can implement from.

Input:

- requirement contract
- architecture context
- known mistake checks

Output:

- mission
- implementation behavior
- step-by-step guidance
- required tests and checks
- definition of done
- stop conditions

Primary value:

- improves coding-agent reliability without embedding code editing in the control docs

## UC-006: Implement Changes And Verify

Goal: carry out the approved changes and collect focused evidence.

Input:

- implementation packet
- handoff brief
- relevant files

Output:

- changed files
- verification output
- implementation evidence

Primary value:

- keeps execution and evidence collection separate from approval

## UC-007: Review Implementation Evidence

Goal: get independent support-agent feedback before treating work as complete.

Input:

- implementation packet
- requirement contract
- architecture constraints
- known mistake checks
- implementation evidence

Output:

- requirements review
- architecture review
- QA review
- completeness review
- known mistake review
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

Goal: update persistent mistake memory after a failed or corrected task.

Input:

- reviewer findings
- failed tests
- human feedback
- repeated correction pattern

Output:

- new known mistake candidate
- prevention rule
- future check wording

Primary value:

- turns mistakes into future guardrails

## UC-010: Produce A Final Control Report

Goal: summarize the run in a concise, reviewable report.

Input:

- structured artifacts
- gate decision
- evidence bundle

Output:

- final status
- key evidence
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

Goal: run a separate exploratory workflow that identifies improvement work and feeds a backlog without polluting contained feature implementation.

Input:

- current feature set
- current requirements
- implementation evidence
- reviewer findings
- known module and pattern friction
- repository structure and change history

Output:

- refactoring candidates
- pattern switch candidates
- module responsibility switch candidates
- tuning opportunities
- improvement rationale and priority
- follow-up contract seeds
- backlog-ready improvement entries

Primary value:

- turns delivery evidence and requirement pressure into deliberate codebase improvement while keeping feature diffs scoped and verifiable

Workflow boundary:

- continuous improvement discovery is read-only and exploratory
- candidates must not be implemented inside a contained feature task unless they are explicitly part of that task contract
- accepted candidates become backlog entries or future task contracts before code changes begin

## Small Task Handoff

## UC-013: Hand Off Small Tasks To OpenCode Build

Goal: route small, low-risk tasks directly to OpenCode's built-in `build` primary agent when the full guardrail path would add unnecessary overhead.

Input:

- small bounded request
- obvious target files
- low-coupling change
- minimal verification needs

Output:

- compact task summary
- narrow file set
- minimal implementation steps
- minimum checks
- stop conditions
- escalation criteria if the task grows beyond small-task scope

Primary value:

- lets the orchestrator avoid unnecessary ceremony by producing a compact build-agent handoff for trivial or low-risk work

## Trace Links

- UC-001 through UC-013 feed `docs/02-product-commitments/product-commitments.md`
