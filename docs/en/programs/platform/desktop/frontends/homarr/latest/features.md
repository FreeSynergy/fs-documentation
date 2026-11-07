# Homarr - Features

## Overview

Homarr combines three building blocks: **boards** (layout grid), **widgets** (content tiles) and **integrations** (details of services including URL and key), which supply the widgets with live data and actions. Everything is changed at runtime via the web interface and stored in the SQLite database.

---

## 1. Boards (dashboards)

- **As many boards as you like**: for example "Homelab", "Media", "Family"
- **Grid layout** with adjustable number of columns, widget size in rows/columns, moving via drag & drop
- **Separate layouts** for desktop and mobile device (own grid per device)
- **Visibility**: public, only own, or released for specific users/groups
- **Duplicate, rename, delete** as well as selecting the start board per device
- **Reset** an accidentally bent arrangement

## 2. Widgets (tiles)

### Structural widgets
- **App tiles**: name, URL, icon, target (new tab/same tab), optional folder/link-list widget
- **Text, image, embedding (iframe), bookmark list** for pure content
- **Snippet tile ("public API"/JSON)**: shows values from any JSON source via JSON paths

### Status and diagnostic widgets
- **Status display** (reachability of a URL, green/yellow/red)
- **Server/board information**: version, host information, time/date
- **Charts** for traffic and utilisation (data source is stored as an integration)

### Integration widgets (selection, depending on version)
- **Docker**: container list with status, CPU/RAM, actions (stop, start, restart)
- **Portainer**: alternative container view for Portainer environments
- **Pi-hole / AdGuard Home**: block statistics, activity
- **Downloads**: qBittorrent, Transmission, Deluge, SABnzbd (activity, quota)
- **Media libraries**: Jellyfin, Plex, Emby (active streams, libraries)
- **Calendar**: appointments via CalDAV calendars
- **Media requests**: Overseerr/Jellyseerr (pending requests)
- **Indexers**: Sonarr, Radarr, Prowlarr
- **Weather, search, notifications, RSS** for informative tiles

## 3. Integrations (service connection)

- **Create integration**: select type, internal/external URL, key or username/password
- **Connection test** directly in the dialog ("test connection")
- **Multiple integrations of the same type** possible; widgets show the desired integration
- **Actions** from the widget: container restart, approve request, pause download
- **Keys stored encrypted** in the database (secrets are encrypted with the instance secret)

## 4. Search and start page functions

- Search bar in the header area, finds configured apps/links of the boards
- **Web search** via an adjustable search engine, including shortcut commands in the search text
- **Keyboard autocomplete** in dropdowns and selection fields
- **User settings**: default search engine, behavior of DuckDuckGo shortcut commands, search behavior

## 5. Authentication, roles and shares

- **Local accounts** with password (registration can be disabled), invitations for new users
- **OIDC / Keycloak** for single sign-on, optionally header-based authentication behind a reverse proxy
- **Roles**: administrator, member, unassigned or guest users
- **Board permissions**: board ownership, group sharing, public boards
- **Personal settings**: colour scheme, first day of the week, header layout, right-click on widgets

## 6. Configuration

- **No config file**: boards, widgets, integrations and users are stored in the database
- **Environment variables** for startup, in particular:
  - `SECRET_PASSWORD` (encrypts secrets, must remain stable)
  - `NEXTAUTH_SECRET` (session signing)
  - `DATABASE_URL` (path to the SQLite file)
  - Options for registration, header auth and time zone
- **Data directory** (volume) contains database and uploads (background images, icons)
- **Backups**: back up the database file and volume so that boards and secrets are preserved

## 7. What Homarr CANNOT do

- **No configuration via file**: there is no exportable YAML file that describes the dashboard
- **No reverse proxy replacement**: Homarr only starts services, it does not take over routing or certificate management
- **No monitoring in the sense of Prometheus/Grafana**: status values are snapshots, no long-term measurement with alerts
- **No offline use**: without a running server and login nothing works
- **No classic plugin API**: extensions are source code contributions, not a plugin system installable at runtime
- **No mobile app replacement**: display in the browser, no native apps
- **No multi-tenancy**: one instance is a community, not a separate multi-customer environment

## 8. Extensions and custom adjustments

- **Custom widgets**: as a React component in the source code; for homelabs the way is one's own fork
- **JSON/public API tile**: display data from any HTTP endpoint via a JSON path — without code the simplest way to a custom tile
- **Extending integrations**: new integration types are maintained in the repository and delivered via releases
- **CalDAV and RSS** as standard routes for calendar and news content
- **Icon sources**: local uploads, bundled icon sets and URLs
- **Updates via container images** (e.g. with Watchtower or a Compose restart)

---

## Comparison with the other dashboard types

| Feature | Homarr | Heimdall | Homer | Dashy |
|----------|--------|----------|-------|-------|
| Configuration | Web interface | Web interface + `.env` | `config.yml` | `conf.yml`/`conf.json` |
| Backend | Yes (Next.js) | Yes (Laravel) | No | Optional (Node) |
| Login/roles | Yes | Yes (simple) | No (proxy) | Yes |
| Container actions | Yes | Limited | No | No |
| Theme system | Yes | Limited | Limited | Very extensive |

---

## See also

- [menu.md](menus.md) - Menu items and operating levels
- [structure.md](layout.md) - Board structure and UI details
- [api.md](api.md) - tRPC procedures and integration proxy
- [shortcuts.md](shortcuts.md) - Keyboard control
