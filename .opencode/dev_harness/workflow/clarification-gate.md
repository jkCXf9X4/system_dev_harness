# Initial Clarification Gate

Purpose: Distinguishes harmless assumptions from blocking uncertainty before routing work to delivery or improvement.

The planner must distinguish harmless assumptions from blocking uncertainty before routing work to delivery or improvement.

Set `user_feedback_required: true` and ask the user for clarification when uncertainty materially affects any of:

- requested outcome: implement now versus capture candidate
- target artifact, module, feature, or document
- intended behavior, acceptance criteria, or success definition
- scope boundary or out-of-scope work
- destructive, broad, irreversible, or high-blast-radius changes
- user preference that would materially change the solution
- external dependency, API, framework, standard, version, or documentation choice that cannot be resolved safely through researcher evidence

The planner may proceed with stated assumptions when all of these are true:

- the ambiguity is low impact
- the likely interpretation is strongly implied by the user's wording or repository context
- proceeding will not edit unrelated files, commit to durable product behavior, or perform destructive work
- the assumption can be verified or corrected by normal discovery, implementation, or review

Planner output must include the clarification fields from `.opencode/dev_harness/workflow/stage-output-schema.md`.

Open questions alone do not require a pause. Only questions that materially change route, scope, acceptance, safety, or durable behavior should block the workflow.

