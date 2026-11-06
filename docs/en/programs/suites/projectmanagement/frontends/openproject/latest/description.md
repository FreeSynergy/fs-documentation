# OpenProject - Description

## Overview

OpenProject is the leading free self-hosted project management software. It covers
classic (waterfall) and agile methods in one application: tasks (work packages),
milestones, Gantt plans, Scrum/Kanban boards, time tracking and costs.

## What OpenProject does

OpenProject manages **projects with work packages** (requirements, tasks, milestones,
risks) including status, priority, version, assignee, relations and dependencies.
Agile teams use **boards** (scrum backlog, sprint boards, task boards, kanban) with
sprints and epics. On top of that come **Gantt charts and a roadmap**, **time and cost
tracking** with budgets, a **wiki**, **meetings** with minutes, **discussion forums**,
**messages** and file downloads. Roles, permissions and configurable workflows
(status/transitions per type and role) steer the process. The software appeared in 2012
as a fork of ChiliProject and is under continuous development.

## Advantages

- **Everything in one application**: tasks, Gantt, agile boards, wiki, meetings, time tracking, costs
- **Self-hosted and free**: community edition under a free licence, your own data sovereignty
- **Configurable workflows**: status, transitions and fields configurable per type and role
- **REST API v3 with API browser**: well documented interface including webhooks
- **SSO options**: LDAP/AD, SAML and OpenID Connect (depending on version and edition)
- **Translated**: UI in German, English and many other languages
- **Commercial support**: enterprise edition with extra features and a cloud offering

## Differentiation from other systems

### OpenProject vs. Redmine
- **Redmine** is a lean issue tracker with a huge plugin landscape, **OpenProject** ships more features out of the box (Gantt, agile boards, meetings)
- **OpenProject** has a more modern UI and REST API v3, **Redmine** a simple XML/JSON API
- Both are open source; **OpenProject** clearly separates community and enterprise features

### OpenProject vs. Jira
- **Jira** is commercial (SaaS/Data Center) with a huge marketplace, **OpenProject** is self-hosted and free
- **Jira** is optimised for software teams and customisability (JQL, schemas), **OpenProject** for integrated project planning
- **OpenProject** includes time/cost tracking natively, **Jira** only base fields (detailed reports as an app)

### OpenProject vs. Planka
- **Planka** is a pure kanban board, lightweight and fast, **OpenProject** a full project suite
- **Planka** has no Gantt, cost or meeting features, **OpenProject** very much does
- **OpenProject** is role- and workflow-heavy, **Planka** deliberately simple

## Technical details

- **Backend**: Ruby on Rails
- **Database**: PostgreSQL (required; other databases are not supported)
- **Frontend**: server-rendered views plus Angular components (e.g. work package table, boards)
- **Authentication**: local accounts, LDAP/AD; SAML and OpenID Connect depending on version/edition (enterprise parts version-dependent)
- **Hosting**: Docker/Podman images, package installation, Helm chart; optionally OpenProject Cloud (SaaS)

## Who OpenProject suits

- **Organisations with data-sovereignty requirements** (public authorities, education, companies with a self-hosting strategy)
- **Hybrid teams** mixing waterfall (Gantt, milestones) and agile (scrum, kanban)
- **Projects with time tracking and cost control** including budgets
- **Less suitable** for teams that only need a quick kanban board (then Planka or Trello)
