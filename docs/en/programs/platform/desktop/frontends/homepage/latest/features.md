# Homepage - Features

## Overview

Homepage knows three configuration levels: **settings** (`config/settings.yaml`) control appearance and behavior, **services** (`config/services.yaml`) build the tiles including service widgets, and **information widgets** (`config/widgets.yaml`) fill the header and footer. Supplementary files describe containers (`docker.yaml`), pods (`kubernetes.yaml`), bookmarks (`bookmarks.yaml`) and Proxmox (`proxmox.yaml`).

---

## 1. Page layout and header

- **Header** with greeting, time/date, search bar and freely combinable information widgets
- **Footer** with its own text (`footer`)
- **Layout entry** in `settings.yaml`: order and column distribution of the groups, `columns` for the tile grid
- **Start page options**: `header`, `footer`, `widgets` at the top/bottom, display of version and update notices
- **Language and formatting**: `language`, 12/24-hour clock, date formats, line break per group

## 2. Service groups and tiles

- **Groups** (`services.yaml`): own names, any number, arrangement via the layout
- **Tile**: `href`, `icon` (from bundled icon sets, own SVG under `config/icons/`), `description`, `namespace`
- **Click behavior**: `settings.yaml → launch` controls same tab or new tab
- **Custom classes/colours** via `class` and custom CSS
- **Supply from Docker/Kubernetes**: groups can be filled automatically from labels or annotations

## 3. Service widgets (live data on the tile)

- **One widget per tile** via the key `_<service>` in `services.yaml`, e.g. `_sonarr`, `_pihole`, `_qbittorrent`
- **Broad selection** (excerpt): Sonarr, Radarr, Lidarr, Prowlarr, Bazarr, qBittorrent, Transmission, SABnzbd, Deluge, Jellyfin, Plex/Tautulli, Emby, Pi-hole, AdGuard Home, NextDNS, UniFi, Tailscale, OPNsense, pfSense, Proxmox, Portainer, Uptime Kuma, Healthchecks, Immich, Nextcloud, Home Assistant, Paperless-ngx, Grafana, Prometheus, ntfy, Gotify
- **Multiple rows per widget**: example qBittorrent shows up/down speed and active tasks, Jellyfin shows active streams
- **Schema stored per service**: which endpoints can be queried is checked by the application when validating the configuration
- **Custom API widget**: any HTTP endpoint plus JSON path → own number without source code

## 4. Information widgets

- **search**: search bar with providers (`duckduckgo`, `google`, `bing`) or own search URL, suggestions via `/api/search/searchSuggestion`
- **resources**: CPU, RAM, disk of the host (container with `/proc` access) or via Glances
- **glances / myspeed / speedtest**: measurements of external services
- **weather, openweathermap, openmeteo**: weather with units and location
- **stocks, date, datetime, greeting, logo, longhorn, kubernetes, unifi_controller, customapi**
- **Position**: `position` (left/right/top/bottom) and order in `widgets.yaml`

## 5. Docker and Kubernetes integration

- **Docker socket** mounted into the container (`/var/run/docker.sock:ro`) or TCP endpoint used
- **Labels** on the container create tiles: `homepage.group`, `homepage.url`, `homepage.name`, `homepage.icon`, `homepage.directory`, `homepage.style`
- **`docker.yaml`**: assignment container ↔ service, so that service widgets address the correct instance
- **Kubernetes**: provider `kubernetes` in `settings.yaml`, pods/deployments with `homepage.*` annotations, `kubernetes.yaml` for grouping and namespaces
- **Status displays**: `running`, `exited`, `paused` with their own colour via custom CSS

## 6. Configuration and operation

- **Files** in the volume `/app/config`: `settings.yaml`, `services.yaml`, `widgets.yaml`, `bookmarks.yaml`, `docker.yaml`, `kubernetes.yaml`, `proxmox.yaml`
- **Secrets** via environment variables: `HOMEPAGE_VAR_*` (value) and `HOMEPAGE_FILE_*` (file content), inserted as `{{HOMEPAGE_VAR_X}}` in every config file
- **Required environment variables**: `HOMEPAGE_ALLOWED_HOSTS` (host header check), optionally `PUID`/`PGID`, `PORT`
- **Optional sign-in**: `HOMEPAGE_AUTH_ENABLED` with `NEXTAUTH_SECRET` or `HOMEPAGE_AUTH_SECRET` and `NEXTAUTH_URL`/`HOMEPAGE_EXTERNAL_URL`
- **Checking the files**: the application logs configuration errors in a structured way; widget and YAML errors appear in the Docker log with file and key
- **Changes take effect**: save the file, reload the page; no restart needed, except for environment variables

## 7. What Homepage CANNOT do

- **No web interface for editing**: layout and widgets are created exclusively in YAML
- **No users, roles or passwords** (standard installation): the page is identical for everyone who reaches it
- **No database and no session state**: no saved settings per visitor
- **Hardly any actions**: Homepage's widgets predominantly read; controlling containers or approving requests is not part of the feature set
- **No monitoring with alerting**: values are snapshots, no long-term curves with alerts
- **No plugin market**: new integrations are source code contributions in the repository
- **No native mobile app**: display in the browser, on mobile laid out differently
- **No multi-tenancy**: one instance = one dashboard

## 8. Extensions and custom adjustments

- **`custom_css.css` and `custom_js.js`** in the config folder: own design, own logic in the browser
- **Custom API widgets** (`_customapi`, info widget `customapi`) for any JSON sources
- **Own widget modules**: module folder under `src/widgets/<name>/` with descriptor, proxy handler and React component; details in [../gethomepage/api.md](../../gethomepage/latest/api.md)
- **Icon sets**: bundled sets (including the `icons` key), own SVGs in the config folder
- **Bookmarks** (`bookmarks.yaml`) as a bookmark bar in the header
- **MCP endpoint** (`/api/mcp`, disabled by default) for AI assistants that may read configuration files and — if permitted — write them
- **Language files**: translations are maintained in the project and delivered per release

---

## Comparison with the other dashboard types

| Feature | Homepage | Homer | Dashy | Homarr |
|----------|----------|-------|-------|--------|
| Configuration | `config/*.yaml` | `config.yml` | `conf.yml`/`conf.json` | Web interface |
| Database | none | none | none | SQLite |
| Own sign-in | no (optionally enableable) | no | yes | yes |
| Live widgets | over 170 modules | none | status checks | integration widgets |
| Actions on infrastructure | no | no | limited | yes |
| Automatic detection | Docker/Kubernetes | no | no | Docker |

---

## See also

- [menu.md](menus.md) - Operating areas and configuration menus
- [structure.md](layout.md) - Page structure, themes, interactions
- [api.md](api.md) - Proxy endpoints and widget data sources
- [../gethomepage/index.md](../../gethomepage/index.md) - Library layer of the widgets
