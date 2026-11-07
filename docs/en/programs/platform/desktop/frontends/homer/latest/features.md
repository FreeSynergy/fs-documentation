# Homer - Features

## Overview

Homer consists of a static page and a YAML description. Everything Homer can do follows from this file: structure, labelling, searchability, appearance. There is no server logic, no sign-in and no actions against services.

---

## 1. Tiles (services)

- **Basic data**: `name`, `url`, `icon`
- **Target frame**: `target` controls whether the link opens in the same tab, a new tab or a window
- **Icon sources**: bundled icon sets, own files in the folder `assets/icons/`, URL to an image
- **Search words**: `keywords` add terms by which a tile can be found
- **Small marker**: `tag` attaches a label to the tile (colouring depends on version/CSS)
- **No resize, no drag & drop**: size and order result from the file and the browser window

## 2. Groups and columns

- **Groups** (`apps`) bundle tiles, for example "Media", "Network", "Tools"
- **Group header**: name, optional logo/image, optional symbol (`class` for icon classes)
- **Number of columns** adjustable globally; on small screens the page wraps automatically
- **Order** of groups and tiles corresponds to the order in the file

## 3. Search

- **Enable** via `search: true`
- **Client-side filter**: typing reduces the visible tiles immediately
- **Matched against** name and `keywords`; upper/lower case does not matter
- **No search index** on a server, no spelling correction beyond simple matching

## 4. Header and footer area

- **Title and subtitle** (`title`, `subtitle`), own document title in the browser tab
- **Logo** on the left, own favicon
- **Icon links** at the top right (`links`): own symbols with name, icon, URL and target frame — typically for Git, status page or admin tools
- **Footer** (`footer`) as text, for example version number or notice
- **Header can be hidden** (`header`) when the page is used as a new-tab page

## 5. Appearance

- **Light and dark scheme** (`theme`, optionally automatic switch)
- **Own stylesheet** via `stylesheet`, so that colours, spacing and font are fully adjustable
- **CSS variables** can be overridden in the theme without editing the bundled files
- **Messages** for loading, error and offline state (`message`) are configurable

## 6. Configuration

- **Main file**: `assets/config.yml` (mounted as a volume in the container)
- **Alternative files**: `?config=<name>` in the URL loads a different file of the same installation (newer versions)
- **Download button**: the own configuration can be downloaded from the page (`download-config`)
- **Icons** are stored under `assets/icons/`
- **Templates**: the official image creates a template if no configuration exists; environment variables can fill placeholders (version-dependent)
- **Changes take effect** after reloading the page, without restarting a service

## 7. Extended display types (version-dependent)

Newer versions can fill tiles with more than one link:

- **RSS**: headlines of a feed in the tile
- **Text / HTML**: short, fixed content
- **JSON values**: display one field from an HTTP endpoint

The associated field names have changed several times in the project. Before use, the bundled example file of the version in use should be checked.

## 8. Operation and updates

- **Delivery**: container image, static folder or CDN
- **Update**: pull new image or replace files, reload the page
- **Backup**: `config.yml`, icon folder and own CSS files are sufficient
- **Multiple environments**: identical files for test and production, separated by folder or repository

## 9. What Homer CANNOT do

- **No live status displays** in the actual sense (no indicators, no reachability check)
- **No actions**: no start, stop or restart of containers and services
- **No user management, no roles, no sign-in**
- **No individualized view** per person: everyone sees the same file
- **No API, no webhooks, no automation** via HTTP
- **No drag & drop** and no layout management in the interface
- **No password challenge for the config**: `assets/config.yml` is publicly readable without upstream protection
- **No history, no charts, no notifications**

## 10. Extensions and integration routes

- **Version control as an extension**: config in Git, changes via pull requests, rollout via CI/CD
- **Multiple configurations**: different files for teams, devices or roles (`?config=`)
- **Own CSS** instead of a theme system: one stylesheet is enough for a complete appearance
- **Own processing in the browser**: the source code is a small Vue application; a fork allows own display types
- **External data sources**: if values are needed in the tile, an own endpoint supplies the data and a display type (version-dependent) shows them
- **Combination with proxy portals**: Homer links to a portal with single sign-on, the protection stays with the proxy

---

## Comparison of dashboard types

| Feature | Homer | Homarr | Heimdall | Dashy |
|----------|-------|--------|----------|-------|
| Backend | No | Yes | Yes | Optional |
| Configuration | `config.yml` | Interface | Interface + `.env` | `conf.yml`/`conf.json` |
| Sign-in | No (proxy) | Yes | Yes | Yes |
| Status displays | Limited | Yes | Yes | Yes |
| Size/readability of the config | Very high | Not available | Not available | Medium to high |

---

## See also

- [menu.md](menus.md) - Page areas and operating roles
- [structure.md](layout.md) - Columns, groups and tiles
- [api.md](api.md) - `config.yml` as interface
- [shortcuts.md](shortcuts.md) - Keyboard and browser keys
