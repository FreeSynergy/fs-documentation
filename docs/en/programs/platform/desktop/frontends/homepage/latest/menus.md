# Homepage - Menu Items

## Overview

Homepage has **no application menu**: there is no menu bar, no sidebar and no settings dialogs. The entire interface is a single, statically rendered page; changes are made in configuration files. This article therefore describes the **operating and configuration areas** in the order in which they appear on the page, and marks each item as "read-only" or "changeable only via file".

> If you are looking for a dashboard with menus and mouse configuration, you will find it in [../homarr/menu.md](../../homarr/latest/menus.md).

## Main menu items (operating and configuration areas)

### 1. Header (`header`)
- **Function**: greeting, time/date, search bar, bookmark bar
- **Details**:
  - read-only; content via `config/settings.yaml` (`header`, `language`, time format)
  - bookmarks from `config/bookmarks.yaml` appear as small icons
  - search bar visible only if a search provider is configured

### 2. Information widgets at the top (`widgets`)
- **Function**: weather, utilisation, stocks, Glances values, Kubernetes status
- **Details**:
  - read-only; order and position in `config/widgets.yaml`
  - each entry has `type` and `position` (`left`/`right`)

### 3. Service groups (`services`)
- **Function**: the actual content: groups with tiles
- **Details**:
  - file only: `config/services.yaml` defines groups, icons, links, descriptions
  - service widgets are attached to the tile as `_<service>`
  - arrangement of the groups via `layout` in `settings.yaml`

### 4. Docker/Kubernetes views
- **Function**: automatically generated tiles from containers or pods
- **Details**:
  - enable the provider in `config/settings.yaml`
  - set container labels or annotations on the workload
  - fine-tuning (name, icon, group) in `config/docker.yaml` / `config/kubernetes.yaml`

### 5. Footer (`footer`)
- **Function**: own text, notice about the version
- **Details**: file only, in `config/settings.yaml`

### 6. Design and theme area
- **Function**: colour scheme, background, opacity, font
- **Details**:
  - `theme` (light/dark/system-compatible), `color`, `background`, `image`, `opacity` in `settings.yaml`
  - own design via `config/custom_css.css`
  - browser switch light/dark only takes effect if `theme: system` is set

### 7. Configuration files (the "settings dialog")
- **Function**: all settings of the instance
- **Details**:

| File | Area | Typical keys |
|-------|---------|--------------------|
| `settings.yaml` | global behavior | `title`, `theme`, `color`, `layout`, `providers`, `launch`, `language` |
| `services.yaml` | groups and tiles | `name`, `href`, `icon`, `description`, `_sonarr` |
| `widgets.yaml` | info widgets | `type`, `position`, `properties` |
| `docker.yaml` | container assignment | service name → container |
| `kubernetes.yaml` | pod view | grouping, namespaces |
| `bookmarks.yaml` | bookmarks | `name`, `icon`, `href` |
| `custom_css.css` / `custom_js.js` | fine-tuning | selectors, browser logic |

### 8. Server-side areas (no UI)
- **Function**: proxy routes, log, health check
- **Details**:
  - `/api/services/proxy`, `/api/widgets/...` (see [api.md](api.md))
  - Docker/container log for configuration and connection errors
  - `/api/healthcheck` for container health checks
  - **Note**: these endpoints are not part of the operating interface and are not documented as a stable API

## Context menus

**There are no context menus.** Neither right-click on a tile nor hover tools are available. Replaced by:

| Expected | Available instead |
|----------|----------------------|
| Right-click → edit tile | change the entry in `config/services.yaml`, reload the page |
| Hover → actions (stop, start) | not available – Homepage triggers no actions |
| Drag & drop of tiles | not available – grid is set in `layout` |
| "Add widget" dialog | add the `_<service>` key to the tile |
| Icon selection via gallery | write the `icon:` value (SVG/PNG in the config folder or icon set) |

## Menus by user role

Homepage does **not distinguish roles** in the application. Only the access levels that the operation sets up are effective:

### Visitor (default, without sign-in)
- View the entire page, click tiles, use the search bar
- No editing, no personal settings
- **Important**: without proxy protection every visitor sees all data and icons – Homepage is not an access protection

### Visitor behind proxy authentication
- Access only after login at the proxy (Basic Auth, OAuth proxy, Authentik, Tailscale)
- Afterwards identical view as above
- No finer distinction than "all or nothing"

### Signed-in user (only with `HOMEPAGE_AUTH_ENABLED`)
- Session sign-in of the application, afterwards the same page
- Serves to protect the internal proxy routes, not to manage rights
- There are still no roles such as "editor" or "read-only"

### Administrator (file level)
- Access to `config/`, `.env` and the container volume
- May change YAML files, CSS/JS and environment variables
- Decides on Docker socket access and the MCP endpoint (`HOMEPAGE_MCP_ENABLED`)
- **Recommendation**: maintain the config folder in Git and approve changes via pull requests

### Read-only workstation
- Reached via a second virtual host or a `/r/` path of the proxy with read-only forwarding to the same container
- Technically and legally identical, since Homepage offers no write interface

## Shortcuts

Keyboard control exists only in the form of browser and field standards; for a list including keys marked as missing, see [shortcuts.md](shortcuts.md).
