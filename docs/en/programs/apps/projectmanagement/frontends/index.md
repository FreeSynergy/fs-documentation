# Projectmanagement — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Projectmanagement` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Asana](asana/index.md) | [latest](asana/latest/description.md) | Asana is task and project work at portfolio level: tasks with fields (due date, assignees, dependencies, custom fields) in projects (list/table/timeline/kanban), teams, workloads and rules automation. |
| [Jira](jira/index.md) | [latest](jira/latest/description.md) | Jira (Atlassian) is issue and project tracking with workflows: issues move through statuses (To Do→In Progress→Done), with sprints (Jira Software), types, priorities and powerful JQL. |
| [OpenProject](openproject/index.md) | — | OpenProject is an open-source project management system for self-hosting (Community Edition plus a commercial Enterprise Edition) with work packages, Gantt planning, agile boards, time and cost tra… |
| [Planka](planka/index.md) | — | Planka is a self-hosted, plain kanban board (fair-code: free Community Edition plus a commercial Pro Edition) with projects, boards, lists and cards in real-time collaboration. |
| [Redmine](redmine/index.md) | — | Redmine is a free, web-based project management and issue tracking application based on Rails: multiple projects with issue trackers, time tracking, wiki, forums, Gantt/calendar and role-based perm… |
| [Taiga](taiga/index.md) | — | Taiga is the agile open-source project management tool (AGPL, Python/Django + a modern frontend "Taigo"): Scrum (sprints, points) and kanban in one, plus epics, issues, wiki and a CRM module. |
| [Trello](trello/index.md) | [latest](trello/latest/description.md) | Trello (Atlassian) is the digital kanban board: boards with lists and cards, due dates, labels, members, checklists and automation via "Butler". |
| [Wekan](wekan/index.md) | — | Wekan is the open Trello clone (Meteor/Node, MongoDB): boards, lists, cards, swimlanes, labels and checklists — self-hosted, with OAuth2/LDAP and outgoing webhooks. |

## File set per program (ADR 0012)

```
programs/apps/projectmanagement/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
