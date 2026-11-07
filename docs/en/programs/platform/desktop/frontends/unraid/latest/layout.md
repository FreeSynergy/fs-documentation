# Unraid - Structure & UI/UX

## Overview

In the browser, Unraid shows a classic server administration page: the tab bar at the top, below it the content of the active tab as a section with tables and forms. There is no window management and no movable panels — every function is its own, completely reloaded page.

## Window structure

### Standard page (example tab *Main*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Header: Unraid logo | Main Shares Users Docker VMs Apps Plugins ... │
│                                   | Bell | Connect | Help | Logout   │
├──────────────────────────────────────────────────────────────────────┤
│ Identification / status section (device name, update, sign-in)       │
├──────────────────────────────────────────────────────────────────────┤
│ Array overview                                                       │
│ ┌──────────┬──────────┬──────────┬──────────┬──────────┐             │
│ │ PARITY-1 │ DISK 1   │ DISK 2   │ ...      │ CACHE    │             │
│ │ symbol   │ symbol   │ symbol   │          │ symbol   │             │
│ │ used/tot │ used/tot │ used/tot │          │ used/tot │             │
│ └──────────┴──────────┴──────────┴──────────┴──────────┘             │
├──────────────────────────────────────────────────────────────────────┤
│ Message area (errors/warnings as coloured banners)                   │
└──────────────────────────────────────────────────────────────────────┘
```

### Dialogue (example *Add New Share*)

```
┌──────────────────────────────────────────┐
│  Add New Share                    [X]    │
├──────────────────────────────────────────┤
│  Share Name        [____________]        │
│  Security          (public|secure|priv)  │
│  Include/Exclude   [disk list]           │
│  Allocation        [____________]        │
├──────────────────────────────────────────┤
│           [Cancel]        [Apply]        │
└──────────────────────────────────────────┘
```

### Container view (tab *Docker*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Docker: application search | Docker Settings | Add Container         │
├──────────────────────────────────────────────────────────────────────┤
│ ┌────────────┬─────────┬────────┬─────────────────────────────┐      │
│ │ Name       │ Path    │ Port   │ Actions                     │      │
│ ├────────────┼─────────┼────────┼─────────────────────────────┤      │
│ │ jellyfin   │ /mnt... │ 8096   │ WebPUI | Logs | Console | ..│      │
│ │ sonarr     │ /mnt... │ 8989   │ WebPUI | Logs | Console | ..│      │
│ └────────────┴─────────┴────────┴─────────────────────────────┘      │
└──────────────────────────────────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Tab bar | Top | Tabs (Main, Shares, Docker, VMs, …) as page switches |
| Icon menu | Top right | Notifications, Connect, help, sign out |
| Status/identification section | Top of page | Device info, update and sign-in status |
| Table/form area | Centre | Array table, share list, container and VM lists |
| Message area | Top/bottom | Errors, warnings, success banners |
| Dialogues | Overlay | Create/edit shares, containers, VMs, users |
| webVNC window | Tab VMs | Browser console of the virtual machine |

## UI/UX

### Design principles

- **Tabs instead of a menu tree**: each task area is its own page, no nested menu
- **State first**: array colours (green/yellow/red) and capacity bars dominate the Main view
- **Forms instead of click streaks**: changes almost always via an edit dialogue with Apply
- **Few overlay layers**: at most one dialogue at a time, no nested panels

### Colour scheme and themes

- Base theme dark blue/orange; light/dark and alternative themes via the identification setting or Dynamix plugins (version-dependent)
- Status colours are fixed: green = ok, yellow = warning/attention, red = error/failure
- Table rows and buttons follow a uniform Dynamix style

### Interactions

- **Click on drive icon**: detail view with SMART values and assignment options
- **Drag and drop**: only in exceptional cases (fine system layout by plugins), not in the core
- **Confirmation dialogues** for risky actions (stop array, delete share, assign disk)
- **Progress bars** for parity check, mover and formatting on the Main page
- **Autocomplete**: app store search in the Docker/Apps tab

### Responsive design

- **Desktop**: full table width, all tabs visible
- **Narrow windows**: tables scroll horizontally, tab bar stays at the top (no dedicated mobile layout)
- **Mobile**: operable, but unsuitable for array work; webVNC restricted on small screens
- Browser zoom helps with dense tables (version-dependent)

### Accessibility

- **Keyboard**: form fields reachable via `Tab`, `Enter` triggers default buttons, `Esc` closes some dialogues
- **Screen reader**: simple table structure, but status relies heavily on colours and symbols — text alternatives are uneven
- **Focus indicator**: browser standard, not additionally designed
- **Language**: core UI English, translations via language plugins

### Performance

- **Server-side rendering**: every tab change reloads the whole page — slow with many shares/containers
- **Polling**: status values (temperatures, parity progress) are reloaded at intervals
- **Slow disks**: SMART queries can noticeably slow pages, as can spin-up-delayed drives
- **Recommendation**: choose plugin count and monitoring intervals deliberately, restrict log searches

## See also

- [menu.md](menus.md) - Tabs and roles in detail
- [features.md](features.md) - Array, Docker, VMs, plugins
- [shortcuts.md](shortcuts.md) - Keyboard operation
- [api.md](api.md) - GraphQL API and automation
