# OpenProject - Features

## Overview

OpenProject bundles task management, scheduling, agile methods, documentation and
billing in one web application. Which modules are visible depends on the edition
(community/enterprise) and the project settings.

## Feature areas

### 1. Work packages

- **Types**: requirements, tasks, milestones, risks, bugs (customisable types)
- **Attributes**: status, priority, assignee, version, dates, duration, progress; additional fields via custom fields
- **Relations and dependencies**: dependent/predecessor, splitting, related work packages
- **Detail view**: right split screen with description, activities, comments, attachments, watchers
- **Inline editing**: change fields directly in the table (version-dependent)
- **Copy, move, share**: copy work packages between projects, share by link

### 2. Tables, queries and filters

- **Module "work packages"**: filterable, sortable table with configurable columns
- **Save queries**: private and public queries with filters, sorting, grouping
- **Filter criteria**: project, type, status, assignee, version, date, free text and much more
- **Export**: CSV export of the table view (further formats version-dependent)

### 3. Scheduling and milestones

- **Gantt chart**: move bars by drag & drop, draw dependencies
- **Roadmap**: milestones and versions per project as a timeline
- **Baseline comparison**: planned vs. actual dates (enterprise; version-dependent)
- **Portfolios and project reports**: summarised evaluations (enterprise; version-dependent)

### 4. Agile boards and backlogs

- **Board types**: scrum (sprint backlog), kanban, task boards, mixed forms (availability version-dependent)
- **Sprints**: backlog column, sprint assignment, active sprints with burndown
- **Epics**: epics as a bracket over several projects in the backlog
- **Columns and WIP limits**: configure via the board settings
- **Board reports**: burndown and cycle analysis

### 5. Time and costs

- **Time entries**: bookings per work package, date and activity
- **Cost reports**: incurred and planned costs per project and user
- **Budgets**: budgets and cost rates per project (version/edition-dependent)
- **Utilisation**: actual vs. planned comparison in the reports

### 6. Collaboration and documentation

- **Wiki**: pages with nested navigation and history
- **Forums**: discussion forums per project
- **Meetings**: calendar of appointments, minutes, tasks created directly from meetings
- **Activities and messages**: project activity stream, watch subscriptions
- **Files**: uploads and attachments on work packages

## Modules and integrations

- **Modules activatable per project**: activities, work packages, board, Gantt, milestones, dates, wiki, files, messages, meetings, budget and time/costs (names version-dependent)
- **Calendar subscription**: iCal feed for "my work" and project activities
- **Mail intake**: create and update work packages by e-mail (IMAP configuration)
- **File integrations**: linking with Nextcloud/OneDrive (version/edition-dependent)
- **Webhooks**: events to external systems (see [api.md](api.md))

## Configuration

- **Administration**: types, status, workflows, custom fields, projects, users, roles and permissions
- **System settings**: colour scheme, mandatory login, passwords, e-mail, time zone, language
- **Project roles**: granular permissions per role (see modules, edit, administer)
- **Instance configuration**: environment variables (database, secret, instance URL) with Docker/package installation

## What OpenProject does NOT do

- **No documented shortcut list**: there are no centrally maintained application shortcuts (see [shortcuts.md](shortcuts.md))
- **No fully offline-capable native client**: the UI is responsive, but an offline mode is missing
- **No real-time co-editing in the wiki**: pages are edited one after another, with a collision warning
- **No app marketplace**: extensibility runs via API, webhooks and built-out core modules; a plugin system like Redmine's does not exist
- **Not everything is free**: baselines, portfolios and some SSO/file integrations are enterprise features (version-dependent)
- **No database other than PostgreSQL**

## Extensions and plugins

- **No plugin system**: OpenProject relies on API, webhooks and built-out core modules instead of plugins
- **REST API v3**: scripts, dashboard connections and BI evaluations via the documented interface
- **Webhook receivers**: CI/CD chains and chat bots react to work package events
- **Visual adjustment**: own colour scheme/CSS; deep UI extensions are not intended
- **BIM/IFC views** for construction planning as an add-on module (version/edition-dependent)
