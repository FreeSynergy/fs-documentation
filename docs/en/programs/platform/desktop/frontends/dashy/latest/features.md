# Dashy - Features

## Overview

Dashy combines two worlds: a **text-based configuration** (`conf.yml`, alternatively JSON) and a **rich interface** with status indicators, widgets, views, themes and optional write access via the editor or REST API. The Vue application renders what the file describes; what the server adds is checks, login and the API.

---

## 1. App tiles

- **Fields per tile**: `title`, `url`, `description`, `icon`, `target`/opening mode, `keywords`/`tags`, `colour`
- **Opening modes**: same tab, new tab, new window pop-up, modal, workspace, copy to clipboard
- **Tags**: make tiles findable, even if the term does not appear in the title or URL
- **URL aliases**: `alias` allows jumping via an address, for example `dashy.local/jelly`
- **Hideable on the start page**: `displayData.hideFromHomepage`; the tile remains visible in search and workspace
- **Hotkeys**: `hotkey` with a digit `0`–`9` launches a tile with a key press
- **Display options**: compact tile, hide name, hide icon, font size, custom colour, borderless

## 2. Sections and pages

- **Sections** (`sections`) group tiles, with a heading, their own layout and optional widgets
- **Subpages** (`pages`) live in their own configuration files and appear in the page menu
- **Number of columns** per section is controllable; tiles snap into a grid
- **Order** follows the file; changeable via drag & drop in edit mode

## 3. Status checks

- **Globally enabled** via the configuration; afterwards the server checks every tile
- **Check URL per tile** possible if the target URL cannot be tested directly
- **Expected response** configurable (response text/status), so that "reachable but broken" becomes recognizable
- **States**: unknown, checking, reachable, unreachable, error — shown as a dot on the tile
- **Interval** configurable; very short intervals noticeably increase load
- **Note**: with purely static hosting (CDN, Netlify) the checks are dropped, because no server performs them

## 4. Search and start page functions

- **Instant search**: typing filters immediately, without focusing a field; handles upper/lower case and typos generously
- **Search fields**: title, URL, provider, description, alias and `tags`
- **Web search**: `Enter` sends the term to a configured search engine (DuckDuckGo, Google, Brave, Searx, Whoogle via a custom URL, and more)
- **Custom shortcut commands** (`searchBangs`): `/w term` opens Wikipedia, `:git term` opens GitHub, etc.
- **Open URL directly**: if the term looks like a URL, Dashy jumps there directly (can be disabled)
- **OpenSearch**: Dashy registers itself as a search engine in the browser (`/opensearch.xml`)
- **Launchpad**: all tiles from all pages in a grid view

## 5. Views

| View | Purpose |
|---------|-------|
| Start page | normal view with sections and widgets |
| Minimal | header, search field, tiles without extras |
| Workspace | one section displayed large, good for filling the screen |
| Login | sign-in screen when authentication is configured |
| Download | download the configuration (if permitted) |

## 6. Widgets

- **Built-in types** (selection, depending on version): clock, weather, RSS feeds, stock and crypto values, news overview, work status, embedded page via iframe
- **Integration** per section: type, options, refresh interval, alignment
- **Custom widgets**: Vue component in the designated folder of the user data; a build is required for purely static operation
- **No actions**: widgets display values, they do not start containers or call write APIs of connected services

## 7. Themes and appearance

- **Many built-in schemes** (light, dark, colourful), applicable via configuration and in the theme editor
- **Custom values** via CSS variables; a custom stylesheet can additionally be included
- **Per section/tile** colours and density configurable
- **Fonts**, icon sizes and spacing configurable
- **Multilingual**: interface in many languages, via `appConfig.lang`

## 8. Authentication and roles

- **HTTP Basic auth** via the server (user/password via environment variables)
- **OIDC providers** (Keycloak, Zitadel and others) for single sign-on
- **Local users** with hashed keys, roles `admin` and `user`, optional two-factor code
- **Minimum role** for functions such as editing, export or API write access
- **Hide configuration** when nobody should have write access

## 9. Configuration

- **File**: `user-data/conf.yml` (YAML) or `conf.json`; multiple subpages in their own files
- **Interactive editor** in the interface: edit and save sections, tiles, themes and basic settings
- **Optional REST API** for read and write access (must be enabled via `ENABLE_API=true`)
- **Backup**: every write action stores a timestamped backup in `user-data/config-backups/`
- **Import/export** of the file, optionally cloud backup with a key
- **Limits**: written files lose comments and formatting, size is limited, concurrent writes follow "last one wins"

## 10. What Dashy CANNOT do

- **No container control**: no start, stop or restart of Docker containers
- **No database**: all changes end up in the configuration file, there is no runtime data storage
- **No webhooks** and no event outputs
- **No monitoring system**: status indicators are snapshots without history or alerts
- **No plugin marketplace**: custom widgets and pages require files and in some cases a build
- **No fine-grained rights per tile**: visibility is controlled via roles and display properties, not via groups per object
- **Server functions drop away with static hosting** (status checks, auth, API)

## 11. Extensions

- **Custom widgets** (Vue component) and **custom views** in the project
- **Custom CSS/themes** for complete visual customization
- **REST API** for automation: create, change, delete tiles, replace pages
- **Integration into deployments**: configuration in Git, deployment checks the file against the bundled schema
- **Outward connection**: linking to portals, shorteners or monitoring systems instead of a built-in function

---

## Comparison of dashboard types

| Feature | Dashy | Homarr | Heimdall | Homer |
|----------|-------|--------|----------|-------|
| Configuration | File + editor + API | Interface | Interface + `.env` | File |
| Status checks | Yes | Yes (integrations) | Partly | No |
| Container actions | No | Yes | No | No |
| Themes | Very extensive | Medium | Limited | Limited |
| Built-in auth | Yes | Yes | Yes | No |

---

## See also

- [menu.md](menus.md) - Header, settings panel, right-click menus
- [structure.md](layout.md) - Views, grid and widgets
- [api.md](api.md) - REST API and authentication
- [shortcuts.md](shortcuts.md) - Keyboard and hotkeys
