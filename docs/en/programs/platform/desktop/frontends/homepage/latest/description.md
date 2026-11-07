# Homepage - Description

## Overview

Homepage is an open-source, **statically rendered** dashboard for self-hosted environments. The state of the dashboard lies entirely in YAML files in the folder `config/`; there is no database and no user management. Over 170 bundled widget modules fetch live data from services such as Sonarr, Radarr, Pi-hole, Jellyfin, Proxmox, UniFi or Tailscale.

## What Homepage does

Homepage builds a single overview page from configuration files: a header with search bar and information widgets (weather, system utilisation, stocks, date), below it **groups** of services. Each service is a tile with icon, name, description and optionally a **service widget** that displays the numbers and status of the service (e.g. running downloads, open requests, block statistics).

Requests to the services run via internal proxy routes of the container (`/api/services/proxy`). Keys thus stay on the server and CORS problems disappear. Docker and Kubernetes environments can supply services automatically: container labels or ingress/pod annotations create tiles without manual work. Changes to the YAML files take effect on the next page load; a web interface for editing does not exist.

## Advantages

- **Configuration as code**: everything in `config/*.yaml`, versionable in Git, back-up-able by copying files
- **No backend state**: no database, no users, no migrations
- **Very many integrations**: over 170 widget modules for media, network and infrastructure services
- **Live data without own API work**: proxy handlers take over authentication and JSON shaping
- **Automatic detection**: Docker labels and Kubernetes annotations create tiles
- **Lightweight**: one container, port 3000, no workers, no queues
- **Customizable**: themes, background images, custom CSS/JS, custom API widgets

## Distinction from other systems

### Homepage vs. Homer
- **Both** are static and YAML-configured; **Homer** remains with links and icons
- **Homepage** has live widgets, Docker/Kubernetes detection and a server proxy, **Homer** does not
- **Homer** runs as pure HTML delivery, **Homepage** needs a running Next.js process

### Homepage vs. Dashy
- **Dashy** offers sign-in functions, roles and an extensive theme system, **Homepage** deliberately forgoes these
- **Dashy** configures `conf.yml` with an optional UI editor, **Homepage** only files
- **Homepage** has significantly more ready-made service integrations, **Dashy** excels at status checks and widgets for own data

### Homepage vs. Homarr
- **Homarr** configures everything in the web interface and stores in SQLite, **Homepage** stores YAML files
- **Homarr** can trigger actions (restart a container), **Homepage** predominantly displays
- **Homepage** can be run without login and database, **Homarr** requires both

## Technical details

- **Backend**: Node.js with Next.js (pages router); internal API routes under `src/pages/api/`
- **Database**: **none** – state lies exclusively in `config/*.yaml` and optionally `.env`
- **Frontend**: React, Tailwind CSS, SWR for querying the widget data, `next-i18next` for translations
- **Authentication**: by default **none** (protection via reverse proxy, VPN or firewall); newer versions offer an optional, lightweight session sign-in via `HOMEPAGE_AUTH_ENABLED`
- **Hosting**: Docker/OCI image `ghcr.io/gethomepage/homepage` (port 3000), Kubernetes, bare metal with Node.js; HTTPS and host header check via the proxy

## Who is Homepage suited for?

- **Homelab users** who want to maintain their configuration in files and Git
- **Environments with many services** that need live figures (media stack, DNS filter, virtualisation) in one overview
- **Admins who do not want an additional login** and handle access via reverse proxy, Tailscale or VPN
- **Less suited** for teams with individual rights, for users who want to configure everything with the mouse, and for environments in which actions (restart, control) are needed from the dashboard
