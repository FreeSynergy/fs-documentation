# Planka - Features

## Overview

Planka focuses on the kanban core: drag cards, assign, comment, tick off. Still, real
team features are in there — real-time sync, checklists, custom fields (community),
webhooks and notification services. The pro edition adds view types and admin comfort.

## Feature areas

### 1. Projects, boards and lists

- **Hierarchy**: project -> board -> list (column) -> card
- **List actions**: add, rename, move, archive cards, empty list
- **Board backgrounds**: project-owned background images, selectable per board
- **Archive**: archive boards and cards instead of deleting, restorable

### 2. Cards

- **Description in markdown**: headings, lists, code, links; editor with preview (the markdown editor is an integral part)
- **Due dates** with date/time and overdue marking
- **Stopwatch per card** (community edition)
- **Labels**: coloured labels per board, cards can be marked with several colours
- **Assignees** per card, notification on assignment
- **Checklists (tasks)**: subtasks with a progress bar
- **Custom fields** (community): own field types per project/board (scope version-dependent)
- **Attachments**: drag & drop, image preview, file management per card
- **Comments** with markdown; activity log per card

### 3. Real time and notifications

- **Socket.IO sync**: card moves, changes and new comments appear immediately
- **Watch/subscribe**: watch cards and boards, notification stream in the app
- **E-mail notifications** over SMTP
- **Notification services**: connection to over 100 providers (chat/push services via the notification-service menu; provider choice version-dependent)

### 4. Collaboration and permissions

- **Project managers** can be appointed per project (administer boards/members)
- **Board memberships**: members per board, who-may-do-what roughly via project/board membership
- **Guest roles** with restricted permissions: pro edition only
- **User administration**: admins create accounts, set roles, issue API keys

### 5. Webhooks and automation

- **Webhooks** (community): defined events to external HTTPS endpoints (via admin API/webhook administration)
- **REST API** with token auth for your own scripts (see [api.md](api.md))
- **Examples**: CI trigger on card move, notification bots, reporting pulls

### 6. Views and comfort (pro edition)

- **Personal dashboard** over all projects
- **Calendar, timeline, card and media views**
- **Recurring cards** and **templates** (card/board templates)
- **One card in several boards**
- **PDF/HTML export**, **five themes** with accent colour, **optimised phone/tablet view**

## Modules and integrations

- **No plugin system**: integration runs over REST API, webhooks and notification services
- **Notes app** (testing phase) as its own companion program for notes
- **Import**: card imports from other systems (a Trello import existed in older versions; status version-dependent)

## Configuration

- **`.env` environment variables**: `DATABASE_URL`, `APP_URL`, `SECRET_KEY`/`SESSION_SECRET`, initial admin (`ADMIN_EMAIL`, `ADMIN_PASSWORD` on first creation, version-dependent), SMTP, OIDC (pro)
- **Docker Compose** delivers the standard stack (app + PostgreSQL)
- **User level**: language, appearance (light/dark mode, community: toggle present; further themes = pro), password, e-mail, 2FA setup

## What Planka does NOT do

- **No Gantt, no roadmap** in the community edition (timeline only pro)
- **No time-tracking evaluation** (stopwatch without reports/billing)
- **No scrum artefacts**: no sprints, burndowns or backlog planning
- **No granular workflow permissions** (no per-role status permission)
- **No native community app**: phone/tablet optimisation is pro; community stays in the web browser
- **No darkroom for anonymous opening**: guest/reader roles only with a pro licence
- **No offline mode** and no local cache for trips

## Extensions and plugins

- **API-first**: Swagger reference as the basis for your own tools and code generation
- **Community clients**: unofficial clients for scripts; official SDKs are missing
- **Extensible while self-hosted**: source code visible (fair-code), own features possible — but distribution then requires a licence if pro features are touched (respect the license guide)
