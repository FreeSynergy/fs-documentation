# OpenProject - Menu items

## Overview

OpenProject's navigation consists of the project selector at the top left, the module
bar (left menu respectively the "main menu" button) and the user menu at the top
right. Which modules appear depends on the project and on the permissions; module
names are version-dependent.

## Main menu items

### 1. Project selector (top left)
- **Function**: switch project or choose the global view ("all projects")
- **Details**:
  - search field over all projects
  - recently visited projects
  - global modules when no project is selected

### 2. Overview (module)
- **Function**: project start page
- **Details**: project data, key figures, active milestones, project card, custom dashboard layout per version

### 3. Activities
- **Function**: chronicle of all changes in the project
- **Details**: filter by type (work package, wiki, file), date, user; subscription by e-mail

### 4. Milestones
- **Function**: list of all milestones of the project
- **Details**: grouped by status, link to dates and roadmap

### 5. Roadmap
- **Function**: timeline of versions and milestones
- **Details**: date boundaries of the versions, progress display

### 6. Work packages
- **Function**: table of all tasks and requirements
- **Details**:
  - filter bar and column choice
  - saved queries (left)
  - group view, timeline view (version-dependent)

### 7. Boards (agile boards)
- **Function**: scrum/kanban boards and task boards
- **Details**:
  - select board, open board settings
  - backlog view with sprints and epics
  - reports (burndown, cycle analysis)

### 8. Gantt
- **Function**: scheduling as a bar chart
- **Details**: drag & drop for dates, dependencies, baselines (enterprise, version-dependent)

### 9. Dates / meetings
- **Function**: calendar of appointments and meeting minutes
- **Details**: create meeting, minute points, derive tasks

### 10. Wiki, files, messages, forum
- **Function**: project documentation and communication
- **Details**: wiki with navigation; files as an upload area; forum with discussion threads

### 11. Time and cost reports / budget
- **Function**: time tracking, costs, budgets
- **Details**: reports by user/activity; budget mask (edition-dependent)

### 12. User menu (top right)
- **Function**: account, notifications, sign out
- **Details**:
  - bell: notifications and bookmarks
  - avatar: my account settings, language, colour scheme, sign out
  - help menu (? symbol): release notes, quick guide, keyboard (browser)

## Context menus

### Work package context menu
- In the table: right click respectively symbol for open, edit, copy, delete, share
- Detail split: the workflow's transitions as buttons, toggle watch, attach attachments
- Row selection: multi-selection for bulk editing (status, assignment)

### Query / column header menu
- show/hide columns, sort, group
- save query, set as default, share (link)

### Board context menu
- Card: open, move, assign, change label
- Column: add card, edit column (status assignment)
- Board settings: cards, sprints, filters, epics

## Menus by user role

### Administrator (instance admin)
- All project menus plus **administration**:
  - create/delete users, groups, projects
  - roles and permissions, types, status, workflows
  - custom fields, enumerations (priorities, activities)
  - system/login settings, webhooks, API documentation
  - plugins/integrations, messages (announcements)

### Editor (member with permissions)
- create/edit work packages, comment, book time
- use boards, move cards, edit wiki
- save own queries; no project or system settings

### Reader (read-only permission)
- view modules: work packages, Gantt, milestones, wiki, activities
- no edit buttons, no board actions
- depending on the project: anonymous view only for shared projects

## Notes

- Module names and order are admin-configurable and differ per version
- If a project hides individual modules, they disappear from the navigation bar
- The global navigation without a project selection shows only context-neutral modules
