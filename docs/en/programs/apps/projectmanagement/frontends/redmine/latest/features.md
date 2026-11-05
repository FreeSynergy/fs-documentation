# Redmine - Features

## Overview

Redmine keeps the core small yet covers the whole project day-to-day: issues, time
tracking, wiki, forums, file storage, roadmap and reports. Almost everything can be
activated per project, permissioned per role and extended via plugins.

## Feature areas

### 1. Issues and trackers

- **Trackers**: own issue kinds (bug, support, task ...) with their own fields, status and workflows
- **Attributes**: status, priority, category, milestone (version), assignee, due date, estimated time
- **Relations**: relates to, duplicates / is duplicated by, blocks / is blocked by, precedes / follows
- **Journals**: complete history per issue including field changes and notes
- **Watch, copy, share**: subscribe to issues, clone them, share via a private link
- **Custom fields**: text, list, selection, boolean, date, user, project — per tracker and role visibility

### 2. Time tracking

- **Bookings** per issue with activity, hours and comment; also possible per project without an issue
- **Book later / copy time entries** and summary entries per day
- **Reports**: time evaluation by user, activity, issue, project; cumulative view
- **Remaining time** from estimate minus bookings per issue

### 3. Projects and roles

- **Projects with subprojects**: roles and permissions apply per project, memberships per member and project
- **Modules per project** switchable: issues, time tracking, wiki, boards (forum), documents, files, news, calendar, roadmap
- **Workflow configuration**: allowed status transitions, field permissions and buttons per role and tracker
- **Enumerations**: status, priorities, activities, time-tracking activities maintainable centrally

### 4. Documentation and communication

- **Wiki** per project with Textile/Markdown (markdown since Redmine 2.x, Textile is the default), history, locks
- **Boards (forums)** with topics, replies, admin functions
- **News** per project with comments, collected on the my page
- **Files and attachments**: document folders, attachments on issues/wiki, unlimited file types (configurable)

### 5. Roadmap, calendar and Gantt

- **Roadmap**: open milestones with due issues, progress bars
- **Calendar**: dates/expected end per issue as a month view, iCal subscription
- **Gantt**: static Gantt chart of the issue dates (core, without drag & drop; interactive via plugin)

### 6. Queries and reports

- **Filterable issue lists** project-internal or across projects, grouping, column choice
- **Public queries** shareable with everyone or with groups
- **Export**: CSV and Atom feed in the core; PDF via browser print or plugins
- **Reports module** (administration): issues, time tracking by user/project/months

### 7. Version control

- **Repository browsers** for Git, Subversion and Mercurial (CVS dropped; version-dependent)
- **Commit references**: `Issues #123`, `Refs #999` link commits to issues automatically
- **Changeset notes** in the issue journal

### 8. Notifications

- **E-mail notifications** on changes to watched or assigned issues
- **My notifications** (Redmine 4.2+): in-app notifications with a bell
- **RSS/Atom** for issues, activities, calendar

## Modules and integrations

- **Repositories**: Git/SVN integrated, webhooks via plugin
- **Calendar**: ICS feed per project/user with a token URL
- **WebDAV**: not in the core (plugin), the files plugin `redmine_webdav` is widespread
- **Auth connections**: LDAP in the core; SAML/OAuth/CAS via plugins

## Configuration

- **Administration**: users, groups, projects, roles, trackers, status, workflows, custom fields, boards, e-mail notifications, authentication, sessions
- **Project settings**: modules, tracker permissions, wiki settings, board assignment
- **Instance**: `config/configuration.yml` (e-mail, repositories, uploads), environment variables, `settings.yml` settings via the UI

## What Redmine does NOT do

- **No agile boards in the core**: no kanban/scrum without plugins (e.g. easyGantt/redmineup boards — third party, partly paid)
- **No real-time editing and no WebSockets**: pages reload the classic way
- **No native apps**: browser UI only (responsive)
- **No webhooks in the core**: incoming/outgoing only as a plugin
- **No two-factor auth in the core** (plugin; version-dependent whether it has since been shipped)
- **No modern theme/dark mode as standard**: dark rendering only via CSS themes
- **No undo** for saved changes (only the journal retrospective)

## Extensions and plugins

- **Plugin architecture**: own Rails plugins with migrations, routes, permissions; large catalogue at redmine.org/projects/redmine/wiki/plugins
- **Widespread plugins**: easyGantt/interactive Gantt plugins, kanban plugins, `redmine_webhook`, `redmine_recaptcha`, themes (RedmineUP, Curious Mind and others)
- **Themes**: CSS-based, easy to swap (`public/themes/`)
- **Scripts**: REST API for automation; `rake` commands for maintenance (see [shortcuts.md](shortcuts.md))
