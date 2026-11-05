# Taiga - Description

## What the program does

Taiga is lean, handsome agile software for self-hosting: a project chooses scrum or
kanban, epics keep the big picture in view, issues the day-to-day. As an AGPL project
(earlier Taiga project, today with a commercial SaaS operation) it is the most open of
the modern agile suites.

## Advantages

- **fast + good looking**: few clicks, clear boards
- **self-hostable** (Docker), cloud optional
- **dev integration**: references/branches out of Git

## Differentiation

| System | Difference |
|--------|------------|
| **OpenProject** | broader (Gantt/CPM, costs, time tracking); Taiga is more agile/leaner |
| **Redmine** | long-serving, plugin-heavy; Taiga is modern |
| **Jira** | workflow depth/commercial; Taiga is OSS simplicity |

## Technical details

- **Backend**: Python/Django (taiga-back), PostgreSQL, RabbitMQ (events), Celery
- **Frontend**: Taigo (Angular), separate services (events, subscriptions)
- **Auth**: OAuth2 (password grant for scripts), bearer tokens; LDAP/OIDC (enterprise)
- **Deploy**: official Docker Compose, Helm charts (community), Taiga Cloud SaaS
- **Licence**: AGPL (core)

## Who it suits

- small/medium dev teams wanting OSS + scrum/kanban without ballast
- FreeSynergy frontends: sprint/story/epic terms map directly as the agile model ([models.md](../../../../../../data/models.md))
