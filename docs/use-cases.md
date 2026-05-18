# Use Cases

## Actors

- Product owner: clarifies value, scope, stakeholder outcomes, and acceptance criteria.
- Developer: uses the harness to produce or consume strict implementation packets.
- External coding agent: implements work from the generated handoff packet.
- Architect or technical lead: reviews maintainability, integration, and long-term fit.
- QA or validation owner: defines evidence that the complete task worked.
- Reviewer agents: independent support-agent roles that check requirements, architecture, QA, completeness, and known mistakes.
- Harness operator: runs the CLI or future UI and manages configuration.

## UC-001: Create A Requirement Contract

Goal: turn a rough task into a binding, checklistable contract.

Input:

- stakeholder note
- rough feature request
- bug report
- technical improvement idea

Output:

- task objective
- in scope and out of scope
- functional requirements
- architecture and integration obligations
- quality and testing obligations
- acceptance criteria
- completion checklist
- waiver rules

Primary value:

- prevents lost requirements and vague completion

## UC-002: Preserve Architecture During Agentic Development

Goal: keep coding-agent work adapted to the existing solution.

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

## UC-003: Check Persistent Known Mistakes

Goal: prevent agents from repeating project-specific mistakes.

Input:

- requirement contract
- architecture context
- versioned known mistakes

Output:

- relevant known mistakes
- task-specific prevention rules
- checks to run before completion
- new lesson candidates

Primary value:

- reduces repeated correction loops

## UC-004: Produce External Coding-Agent Handoff

Goal: generate a strict packet that an external coding agent can implement from.

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

- improves coding-agent reliability without embedding code editing in the harness

## UC-005: Run Reviewer Council Before Completion

Goal: get independent support-agent feedback before treating work as ready.

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

- catches partial solutions and drift before handoff or completion

## UC-006: Enforce Completion Decision

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

## UC-010: Review External Agent Evidence

Goal: validate the actual output from a coding agent, not only the handoff packet.

Input:

- changed files
- diff or diff summary
- test output
- external agent final response
- waiver requests

Output:

- evidence bundle
- independent reviewer findings
- deterministic gate status

Primary value:

- closes the loop between planned contract and actual implementation result

## UC-007: Compare Model Choices By Role

Goal: use different models for different harness roles without changing business logic.

Input:

- role requirements
- cost constraints
- model availability
- quality observations

Output:

- model assignment
- fallback recommendation
- cost and quality tradeoff notes

Primary value:

- keeps workflow design separate from provider and model selection

## UC-008: Prepare A Pull Request Review Brief

Goal: generate a PR-ready checklist and review brief from the planned slice.

Input:

- final agile brief
- changed files or implementation notes
- test results

Output:

- PR description draft
- reviewer checklist
- risk summary
- demo notes
- validation evidence

Primary value:

- improves handoff quality and review focus

## UC-009: Capture New Lessons From Failures

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

## Future Use Cases

- Attach project documents and architecture decisions as retrieval context.
- Integrate with GitHub issues and pull requests.
- Integrate with Jira or Linear.
- Add human approval interrupts inside LangGraph.
- Add controlled built-in code-editing agents after external handoff is mature.
