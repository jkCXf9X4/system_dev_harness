# Known Risks

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Docs/template synchronization drift | Medium | High | Package docs must stay aligned with `.opencode/templates/product-breakdown/`. Currently synchronized manually. |
| Iteration cap exceeded in practice | Low | Medium | The 3-iteration revision loop cap may be too low for complex tasks. Review after real usage. |
| Improvement candidates accumulate without implementation | Medium | Low | Backlog grows stale. Schedule regular grooming rounds. |
| Stale references after renames | Low | Medium | `git grep` scan after each rename catches most issues, but cross-repository references (target repos) cannot be automatically updated. |