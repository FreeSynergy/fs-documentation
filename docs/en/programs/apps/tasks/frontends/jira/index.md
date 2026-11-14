# Jira

> Category: [tasks](../../index.md)

## What it is

Jira (Atlassian) is issue and project tracking with workflows: issues move through statuses (To Do→In Progress→Done), with sprints (Jira Software), types, priorities and powerful JQL. SaaS (Cloud) and Data Center; REST API v2/v3.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |
| [dialogs.md](latest/dialogs.md) | Every dialog: purpose, fields, buttons, default, cancel |
| [workflows.md](latest/workflows.md) | Step-by-step workflows: goal, prerequisites, steps, failures, undo |
| [acceptance.md](latest/acceptance.md) | Acceptance checklist: each workflow as a yes/no click test |
| [gaps.md](latest/gaps.md) | What our program cannot do for these workflows, and what it needs |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.atlassian.com/jira-software-cloud/ | official help of Jira Cloud (start page) | ✅ 2026-11-14 |
| https://support.atlassian.com/jira-software-cloud/docs/use-keyboard-shortcuts/ , what-is-the-command-palette/ , navigate-all-work-with-your-keyboard/ , search-issues-projects-and-more-with-the-your-keyboard/ , and ten "... with your keyboard" articles | official keyboard shortcut pages | ⚠️ 2026-11-14, incomplete (in-app list not read) |
| https://support.atlassian.com/jira-software-cloud/docs/what-is-the-new-navigation-in-jira/ , manage-and-customize-the-project-navigation/ , configure-a-company-managed-board/ , configure-columns/ , configure-swimlanes/ , edit-multiple-issues-at-once-from-the-backlog/ , edit-a-sprint-in-a-company-managed-project/ , delete-a-sprint/ | official help, menus | ✅ 2026-11-14 |
| .../create-a-work-item-and-a-subtask/ , plan-a-sprint/ , complete-a-sprint/ , transition-an-issue/ , clone-an-issue/ , delete-multiple-issues/ , view-a-work-item/ , save-your-search-as-a-filter/ | official help, dialogs and workflows | ✅ 2026-11-14 |

Earlier text of this dossier (description, features, layout, api, the three older tables in menus and shortcuts) has no source list: `[nicht belegt]`.
