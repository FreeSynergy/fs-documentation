# Planka - Description

## Overview

Planka is an open-source kanban tool for self-hosting: projects contain boards, boards
contain lists (columns) with cards. Everything synchronises in real time between all
participants without reloading.

## What Planka does

Planka structures work over **projects > boards > lists > cards**. Cards carry
descriptions in markdown, due dates, coloured **labels**, assignees, **checklists
(tasks)**, attachments and comments; activities per card and board log every change. Via
**notification services** (e-mail/SMTP plus connections to over 100 providers) and
**webhooks** Planka can be wired into automations. The community edition can be hosted
free of charge; the commercial **pro edition** adds SSO (OIDC), guest roles,
calendar/timeline views, themes and mobile optimisation.

## Advantages

- **Extremely simple**: four concept levels, usable immediately, without configuration ballast
- **Real time**: changes appear instantly on all clients (Socket.IO)
- **Genuinely free self-hosted**: community edition without user-count or core-feature limits
- **Documented REST API**: official Swagger reference and webhooks included
- **Two-factor authentication** already in the community edition
- **Easy to operate**: Docker Compose with PostgreSQL, few environment variables
- **Multilingual**, incl. German and English UIs (internationalisation explicitly a feature)

## Differentiation from other systems

### Planka vs. Trello
- **Trello** is SaaS with board automation ("Butler") and mobile apps, **Planka** runs on your own infrastructure
- **Trello** has Power-Ups/marketplace, **Planka** extends via API and webhooks
- **Planka** stores data exclusively locally — privacy/GDPR argument against Trello

### Planka vs. Wekan
- **Wekan** (Meteor) ships many detail options early (swimlanes, templates), **Planka** deliberately stays minimalist
- **Planka** has a more modern, calmer UI and real time over Socket.IO; **Wekan** looks feature-overloaded
- **Wekan** is MIT-licensed, **Planka** fair-code (community free, pro commercial)

### Planka vs. OpenProject
- **OpenProject** is the full project suite (Gantt, costs, workflows), **Planka** is pure kanban
- **Planka** without time-tracking reports, Gantt and meeting modules (timeline only in pro)
- Both self-hosted; **Planka** set up in minutes, **OpenProject** noticeably larger to install and maintain

## Technical details

- **Backend**: Node.js (Express), ORM Bookshelf/Knex
- **Database**: PostgreSQL as the standard; MySQL/MariaDB and SQLite supported depending on version (version-dependent)
- **Frontend**: React with Redux/Redux-Sagas on Semantic UI React; drag & drop over react-beautiful-dnd
- **Real time**: Socket.IO channel for card/board synchronisation
- **Authentication**: local accounts, 2FA (community); SSO via OIDC and guest roles in the pro edition; API tokens for scripts
- **Hosting**: official Docker image + Docker Compose; reverse proxy with HTTPS recommended

## Who Planka suits

- **Small and medium teams** that want a fast, privacy-friendly kanban without scrum ballast
- **Private individuals and homelabs** hosting task boards themselves
- **GDPR-sensitive organisations** replacing Trello but wanting to keep its simplicity
- **Less suitable** for waterfall planning, time-tracking billing or strictly cadenced scrum processes
