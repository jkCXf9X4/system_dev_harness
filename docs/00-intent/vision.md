# Vision

## Product Vision

The current solution is an OpenCode workspace that provides a guarded agentic development control system. It uses repository-local agents and versioned markdown to turn a request into a contract, preserve architecture, apply lessons, package handoffs, and gate completion through independent review.

It is not intended to be another unconstrained coding agent. It is intended to be the control layer around agentic development: define the task contract, preserve architectural intent, inject known lessons, create an implementation packet, and require reviewer approval before work is considered ready to execute or complete.

## Core Thesis

```text
task input
  -> orchestrator
  -> requirement contract
  -> architecture context
  -> known mistake check
  -> implementation packet
  -> external or builder handoff
  -> implementation evidence intake
  -> independent reviewer agents
  -> deterministic completion gate
  -> revise / waive / approve route
  -> final control report
```

The solution should make this loop repeatable, inspectable, and hard to shortcut.

## Problems To Solve

- Agents may satisfy only the visible surface of a task and stop early.
- Architecture drift can slip in when workflow rules are hidden in prompts.
- Repeated mistakes are easy to repeat if lesson memory is not versioned.
- Information can become disconnected when moved or rewritten without updating the chain.
- Review is less useful if it happens after the wrong solution has already been built.
- Handoffs are weak when they do not require a strict completion checklist.

## Desired Outcomes

- Every task has a checklistable requirement contract.
- Architecture and integration constraints are explicit before coding starts.
- Known repeated mistakes are checked for every task.
- Handoffs are strict, reviewable, and traceable.
- Reviewer agents challenge completeness, requirements, architecture, QA, and mistake avoidance.
- Completion requires reviewer approval against evidence.
- Missing contract items require explicit waivers with reason, risk, owner, and follow-up action.
- The current solution remains traceable through the package `docs/` tree

## Non-Goals

- Hidden orchestration code outside the repository-local OpenCode setup.
- Unguarded autonomous software delivery.
- Replacing product ownership, architecture ownership, or engineering judgment.
- Building a generic chatbot.
- Optimizing for the largest possible number of agents.

## Guiding Principles

- Contract completeness over plausible partial output.
- Architecture preservation over locally convenient implementation.
- Persistent mistake memory over repeating the same correction loop.
- Reviewer approval over self-assessed completion.
- Explicit waivers over silent requirement loss.
- OpenCode-native workflow definitions over custom runtime code.
- Versioned markdown over ephemeral context.

## Trace Links

- Feeds: `docs/01-product/product-commitments.md`
- Informs: `docs/00-intent/use-cases.md`
