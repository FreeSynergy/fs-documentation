# Heimdall - Features

## Overview

Heimdall consists of three elements: **apps** (tiles as links), **panels** (sectioned collections of tiles and content) and **enhanced apps** (packages that write live data of a service into a tile). In addition there are server statistics of the Heimdall machine and an administration for accounts and layouts.

---

## 1. Apps (app tiles)

- **Create**: title, target URL, icon, background colour
- **Icons**: upload, choose from bundled icon sets or automatically use the favicon of the target URL
- **Target behavior**: open tile in the same tab or in a new tab
- **Sorting**: arrange tiles via drag & drop within a panel
- **Colours**: free colour choice per tile, also usable for group assignment
- **No iframes**: Heimdall does not embed target applications, it only links

## 2. Enhanced apps (tiles with live data)

- **Principle**: an enhanced-app package knows the service, queries it server-side and renders values into the tile
- **Typical services** (selection, version-dependent): Pi-hole, NZBGet, Sonarr, Radarr, Emby, Plex, Portainer, Transmission, NZBHydra2, Jackett, Bazarr, Healthchecks, Miniflux
- **Credentials**: target URL plus API key or username/password, maintained separately per app
- **Encryption**: the values are stored encrypted in the database with the Laravel `APP_KEY`
- **Refresh**: values are fetched when the page is called; faulty connections appear as a notice in the tile
- **Installation**: packages are added as Composer dependencies (in Docker installations via the image's built-in mechanism)

## 3. Server statistics

- **Display**: CPU usage, memory, disk usage, network traffic of the machine on which Heimdall runs
- **Presentation**: figures and small charts in their own panels
- **Origin**: values are read locally on the server, not queried over the network
- **Limit**: snapshot when the page is loaded, no long-term curves and no alerts

## 4. Panels and layout

- **Panel types**: app panel, search panel, statistics panels, notice/support area
- **Layout editing**: own view in which panels are moved, wrapped and hidden
- **Delete/hide panel**: unused areas disappear from the view
- **Multiple panels**: content can be separated thematically, such as "Media", "Network", "System"
- **Layout per account**: the arrangement is saved per user

## 5. Search

- **Search field** in the search panel of the start page
- **Web search**: the search term is passed to a configured search engine (default: Google, other providers configurable)
- **No index search** across all apps: the name of an app is not filtered internally, but can only be found via the browser (text search `Ctrl+F`)

## 6. Accounts and rights

- **Standard installation**: one administrator account with email address and password, set up at the first start
- **Multiple users** (newer versions): create via the settings, roles administrator and normal user
- **Own layout** per user, app management depending on role
- **Disable sign-in**: for installations that are fully protected behind a proxy (version-dependent setting)
- **Public view**: mechanisms for making a dashboard visible without sign-in (version-dependent, use with care)

## 7. Configuration

- **`.env` in the project**: `APP_KEY` (encrypts secrets, keep it absolutely stable), `APP_URL`, database connection, optional auth settings
- **Persistent data**: back up the database file (SQLite) as well as uploaded icons and custom files in volumes
- **Web server level**: time zone, memory and execution times for PHP; HTTPS via reverse proxy
- **Update**: pull new image or update source code, then `php artisan` steps for migrations and cache

## 8. Customization

- **Tile colours** and icons as the most important design tools
- **Custom CSS/theme files**: custom stylesheets can be included; a theme catalogue like Dashy's does not exist
- **Support/notice area**: messages from the project (can be switched off, version-dependent)
- **Logo and title**: changeable via the settings or template files

## 9. What Heimdall CANNOT do

- **No container control**: no start, stop or restart of Docker containers
- **No free grid**: tiles sit in panels, size and position are bound to the panel system
- **No status checks** in the style of Dashy (neither indicators for all links nor adjustable check intervals)
- **No documented API** for automation and no webhooks
- **No monitoring**: no history, no notifications, no thresholds
- **No single sign-on**: OIDC/LDAP are not offered, a reverse proxy must handle this
- **No multilingual interface** in all versions; content is in English
- **No rights system** with fine-grained permissions per panel or app

## 10. Extensions and custom adjustments

- **Enhanced-app packages**: write own packages (Laravel class plus template) that query a service
- **Custom CSS**: adjust colour scheme, spacing and font
- **Template files (Blade)**: change header, footer and panels directly
- **Environment variables of the image**: time zone, user/group identifier and paths for Docker operation
- **Change database connection**: swap SQLite for MySQL/MariaDB or PostgreSQL, for example for backup concepts

---

## Comparison of dashboard types

| Feature | Heimdall | Homarr | Homer | Dashy |
|----------|----------|--------|-------|-------|
| Tiles with live data | Yes (enhanced apps) | Yes (integrations) | Limited | Yes (widgets) |
| Container actions | No | Yes | No | No |
| Layout editor | Panels, limited | Free grid | No | Grid via config |
| Configuration | Interface + `.env` | Interface | `config.yml` | `conf.yml`/`conf.json` |
| API for automation | No | tRPC | No | Optional REST API |

---

## See also

- [menu.md](menus.md) - Menu items and context menus
- [structure.md](layout.md) - Panel and tile structure
- [api.md](api.md) - Routes, enhanced apps and keys
- [shortcuts.md](shortcuts.md) - Keyboard control
