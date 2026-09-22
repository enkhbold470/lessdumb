# Proposal: Weekly Release Train (v2)

Team: 4 engineers, one web app + one API, ~15 deploys/week today (each engineer ships their own PRs).

## Goals
- Fewer production incidents (we had 3 last quarter, all from untested DB migrations)
- More predictable releases

## Process
1. Code freeze every Wednesday 12:00.
2. Release manager (rotating) cuts a `release/YYYY-WW` branch.
3. All PRs merged since last release get a QA ticket in Jira; QA contractor tests each one manually (est. 6h/week).
4. Staging soak for 48 hours.
5. Change Advisory Board meeting Friday 10:00 (all 4 engineers + PM + CTO), 45 min, reviews every PR in the release.
6. Release manager fills the release checklist (22 items) in Confluence.
7. Deploy Friday 14:00; release manager on call through the weekend.
8. Hotfixes require CAB approval via email.
9. Post-release retro every Monday, 30 min.

## Tooling to build
- A Slack bot to remind people about the freeze and collect CAB approvals.
- A dashboard tracking checklist completion per release.
- Automate the Jira QA-ticket creation from merged PRs.

Please review this and tell me what to change before I send it to the CTO.
