# Homer - Menu Items

## Overview

Homer has **no menus in the classic sense**: there is no navigation, no settings page and no administration interface. Operating elements are the header, the icon links, the search field and the tiles themselves. What is perceived as a "menu" arises from the configuration file.

## Operating elements on the page

### 1. Header
- **Function**: title, subtitle and logo of the start page
- **Details**:
  - `title` and `subtitle` as text
  - `logo` on the left, `icon` as favicon in the browser tab
  - `document-title` determines the tab title
  - header can be hidden via `header` (practical as a new-tab page)

### 2. Icon links (top right)
- **Function**: own, permanent links, for example to Git, status page or administration
- **Details**:
  - list `links` with `name`, `icon`, `url` and optional `target`
  - appear as small symbols with tooltip
  - order as in the file
  - no dropdown menus, every entry is a direct link

### 3. Search field
- **Function**: filter tiles by name and search words
- **Details**:
  - only visible if `search: true` is set
  - filters without reloading, display reduces immediately
  - deleting the text shows all tiles again
  - no suggestion menu, no match counters

### 4. Group headings
- **Function**: bundle tiles thematically
- **Details**:
  - `name` as heading
  - optional `logo` (image) and `class` (symbol)
  - headings are not linked and not collapsible

### 5. Tiles (services)
- **Function**: link to a service, recognizable by icon and name
- **Details**:
  - left click opens the target set in `target`
  - hover slightly highlights the tile
  - `tag` shows a small marker, `keywords` only act in the search
  - **no context menu from Homer**: right-click shows the browser menu (copy link, open again)

### 6. Configuration tool
- **Function**: download the own configuration (`download-config`)
- **Details**:
  - small button/link, depending on the setting
  - downloads the currently loaded `config.yml`
  - serves for backing up and transferring to another installation
  - **Caution**: the file contains internal URLs; without proxy protection it is readable by everyone

### 7. Footer
- **Function**: notice, version number or legal information
- **Details**:
  - free text via `footer`
  - no link collection, no action elements

## Configuration file as "menu level"

| Area | File section | Effect on the page |
|---------|-----------------|------------------------|
| Header | `title`, `subtitle`, `logo`, `header` | visible header area |
| Icon links | `links` | symbols at the top right |
| Search | `search` | search field on/off |
| Structure | `columns`, `apps` | number of columns, groups, tiles |
| Appearance | `theme`, `stylesheet` | light/dark scheme, own CSS |
| Messages | `message` | loading, error and offline notices |
| Export | `download-config` | download button |

## Menus by role

Homer knows **no accounts and no roles**. Differences arise exclusively in operation:

### Operator (write access)
- may change `assets/config.yml`, `assets/icons/` and own CSS files
- maintains changes in Git and rolls them out via deployment
- decides on icon links, group order and search words
- **No menu in Homer**: changes happen in the file and in the deployment

### Signed-in user (via reverse proxy)
- sees Homer only after an upstream protection (Basic auth, Authentik, Authelia) has accepted them
- operation identical to a guest: open tiles, search, possibly download the configuration
- role differences are exclusively rules of the proxy

### Read-only user (default case)
- sees exactly the delivered file
- cannot change anything, since no write option exists
- sensible operating mode: deactivate the download button so that the configuration is not visible

### Different views per person
- via several files: `?config=team-a.yml`, `?config=mobile.yml`
- the proxy can set these parameters per user group
- each file produces its own, self-contained start page

## Security-relevant notes

- Without an upstream proxy, **tiles, internal URLs and the complete configuration are publicly readable**
- do not activate `download-config` if the configuration should not be shared
- protected areas remain protected: Homer only links, it does not take over sign-in

## Shortcuts

The usable keys (mostly browser standard) are listed in [shortcuts.md](shortcuts.md).
