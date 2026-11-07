# Homarr - Description

## Overview

Homarr is an open-source dashboard for self-hosted environments (homelab, home server, small team infrastructure). It bundles links, container status and service integrations in visual boards that are set up entirely with mouse clicks.

## What Homarr does

Homarr provides a web interface in which so-called **boards** are created. A board is a grid of widgets: app links, status displays, charts, lists and content tiles. Via **integrations** (Docker, Portainer, Pi-hole, qBittorrent, Sonarr/Radarr, Jellyfin/Plex, calendars, among others) Homarr fetches live data and can trigger actions, such as restarting a container. The configuration is done entirely in the interface and stored in an SQLite database.

## Advantages

- **No config file needed**: boards, widgets and layouts are built in the UI via drag & drop
- **Live integrations**: status, utilisation and content of real services in the overview
- **Actions from the dashboard**: start/stop/restart containers, send requests to media tools
- **Multiple boards and users**: roles (admin/member), invitations, shared boards
- **Modern UI**: React/Mantine, themes, background images, blur, dark and light mode
- **Separate desktop and mobile layouts** per board
- **API reference available**: tRPC procedures are publicly documented

## Distinction from other systems

### Homarr vs. Heimdall
- **Homarr** is widget-centred (many small data tiles), **Heimdall** is tile-centred (app tiles with optional statistics overlays)
- **Homarr** is configured entirely via the UI, **Heimdall** combines UI administration with Laravel files/`.env`
- **Heimdall** is lighter in concept, **Homarr** has more integrations and board management

### Homarr vs. Homer
- **Homer** is a static page without a backend, **Homarr** is a full-stack application with database and login
- **Homer** is configured in `config.yml`, **Homarr** in the web interface
- **Homer** has no live actions, **Homarr** can act on Docker and services

### Homarr vs. Dashy
- **Dashy** is configured primarily via `conf.yml`/`conf.json` (with optional UI editor), **Homarr** only via the UI
- **Dashy** offers strong theming and status checks for links, **Homarr** stronger Docker/media integrations
- **Dashy** can also be hosted statically, **Homarr** requires a running server with authentication

## Technical details

- **Backend**: Node.js, Next.js (App Router), tRPC for the internal API, Drizzle ORM
- **Database**: SQLite as default (file in the data directory); external databases are not provided for
- **Cache/queues**: Redis was used for sessions and background jobs in older versions; current versions get by without a separate Redis service
- **Frontend**: React with Mantine components, `react-grid-layout` for the board grids
- **Authentication**: NextAuth with local accounts (credentials), OIDC/Keycloak, optionally header-based auth behind a reverse proxy; board permissions and roles
- **Hosting**: Docker/Compose (official image), Kubernetes/Helm, bare metal with Node.js; HTTPS via reverse proxy recommended

## Who is Homarr suited for?

- **Homelab users** who want to monitor Docker containers and media stacks centrally
- **Teams and families** who need different boards with different rights
- **Admins who do not want to maintain YAML files** but prefer to set everything up in the interface
- **Less suited** for pure link collections (then Homer is simpler) or for environments without persistent data
