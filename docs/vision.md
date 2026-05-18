# Vision

## Product Vision

System Dev Harness is a guarded agentic development harness that helps teams use coding agents without losing requirements, architecture, completeness, or repeated-mistake awareness.

It is not intended to be another unconstrained coding agent. It is intended to act as the control system around agentic development: define the task contract, preserve architectural intent, inject known lessons, create an implementation packet, and require reviewer approval before work is considered ready to execute or complete.

## Core Thesis

AI coding agents are most useful when they operate inside a governed contract loop:

```text
task input
  -> requirement contract
  -> architecture context
  -> known mistake check
  -> implementation packet
  -> external coding-agent handoff
  -> reviewer council
  -> completion decision
  -> final control report
```

The harness should make this loop repeatable, inspectable, and hard to shortcut.

## Problems To Solve

- Agentic development tools often implement plausible partial solutions and stop before the full task is complete.
- Coding agents can disregard architecture, requirements, prior decisions, or existing solution patterns.
- Agents lose track of constraints over long tasks and repeatedly make the same mistakes.
- Review often happens after the wrong solution has already been implemented.
- Teams need a practical way to give coding agents strict task packets and independent support-agent feedback.

## Desired Outcomes

- Every task has a checklistable requirement contract.
- Architecture and integration constraints are explicit before coding starts.
- Known repeated mistakes are checked for every task.
- External coding agents receive strict implementation packets rather than vague prompts.
- Reviewer agents challenge completeness, requirements, architecture, QA, and mistake avoidance.
- Completion requires reviewer approval against the contract.
- Missing contract items require explicit waivers with reason, risk, owner, and follow-up action.

## Non-Goals

- Unguarded autonomous software delivery.
- Replacing product ownership, architecture ownership, or engineering judgment.
- Building a generic chatbot.
- Optimizing for the largest possible number of agents.
- Hard-coding one model provider as a permanent dependency.

## Guiding Principles

- Contract completeness over plausible partial output.
- Architecture preservation over locally convenient implementation.
- Persistent mistake memory over repeating the same correction loop.
- Reviewer approval over self-assessed completion.
- Explicit waivers over silent requirement loss.
- External coding-agent handoff before built-in code editing.
- Configurable model access over provider lock-in.
