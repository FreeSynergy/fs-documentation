# Jira - Description

## What the program does

Jira manages work as issues with a defined life cycle: who creates it, which status sequence it runs through, who works on what in which sprint. Its appeal (and price) is its malleability: workflows, fields and permissions are built per project.

## Advantages

- **The de-facto standard** in software engineering (KEY references in commits)
- A **workflow machine** with validators/automation
- The **API + webhooks** are mature

## Differentiation

| System | Difference |
|--------|------------|
| **Trello** | A board without a workflow engine; Jira = process |
| **OpenProject/Redmine** | Open alternatives, leaner administration |
| **Asana** | A task portfolio instead of an issue-workflow focus |

## Technical details

- **Model**: Jira Cloud (SaaS, Atlassian account) or Data Center (self-hosted, licensed)
- **Project models**: team-managed (simple) vs. company-managed (schemes)
- **Authentication**: Atlassian account/SSO; API: API token (email+token basic), PAT (data center), OAuth2 (apps)
- **Pricing**: free (<10 users), standard/premium/enterprise

## Who it suits

- Engineering/support organisations with a need for rules
- FreeSynergy frontends: the issue life cycle + status transitions as a workflow model ([models.md](../../../../../../data/models.md))
