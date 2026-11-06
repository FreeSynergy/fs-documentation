# Trello - Description

## What the program does

Trello visualises work as columns with cards — the state of a thing is its position. It is deliberately simple: everyone understands it without training, automation comes later via Butler and power-ups.

## Advantages

- **Getting started in minutes**, solidly free
- **Flexible**: retrospectives, recruiting pipelines, content calendars
- **The API is clean and stable** — the prototype of a good kanban interface

## Differentiation

| System | Difference |
|--------|------------|
| **Jira** | Issue tracking with workflows/sprints; Trello stays a board |
| **Planka** | A self-hosted clone with almost identical mechanics, without a power-up ecosystem |
| **Asana** | Tasks instead of cards with field depth; Trello is positional |

## Technical details

- **Model**: SaaS (Atlassian), boards in workspaces
- **Authentication**: Atlassian account (password/SSO); API: REST key + token, or OAuth2 for power-ups
- **Offline/mobile**: apps with basic offline persistence
- **Tiers**: free/standard/premium/enterprise

## Who it suits

- Teams for whom status is more visual than field-detail-needing
- FreeSynergy frontends: the Trello board model (board/list/card/label/checklist) as the canonical [task frontend](../../../../../../data/models.md)
