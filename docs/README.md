# Documentation

This folder is the operator-facing entrypoint. Keep runnable guidance, examples, install and deploy steps, verification commands, usage instructions, troubleshooting, and contributor workflow here.

The product source and traceability docs stay in `product-breakdown/`. Link to them for product context instead of copying product text into guides.

## Guide Map

- [Getting Started](getting-started.md) - first run, minimum prerequisites, and the smoke check.
- [Install and Deploy](install-and-deploy.md) - how to copy the payload into a target repository and refresh it later.
- [Operation](operation.md) - blocked runs, waivers, and reruns.
- [Verification](verification.md) - smoke test guidance and expected runtime.
- [Product Breakdown](product-breakdown.md) - the source documentation hierarchy and traceability map.
- [Evolution](evolution.md) - roadmap, risks, and change history.

## Boundary With `product-breakdown/`

- `docs/` explains how to use, install, verify, operate, and contribute to the workflow package.
- `product-breakdown/` explains what the product is, who it is for, what is in or out of scope, and which stable decisions constrain it.
- Command examples and concrete walkthroughs belong here unless they are only high-level user-scenario illustrations.
- Do not duplicate product policy or example text across both trees; link to the product artifact when a guide needs context.
