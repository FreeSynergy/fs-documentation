# TrueNAS - Structure & UI/UX

## Overview

The TrueNAS web interface (SCALE) is a single-page application: the navigation sidebar on the left, a bar at the top with search field, job and alert icons, and on the right the content area with cards, tables and wizards. Status values arrive live via WebSockets; long actions run as jobs with a progress panel.

## Window structure

### Main view (example *Datasets*)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Header: TrueNAS version | Search bar "Search" | Jobs | Bell | User   │
├──────────────┬───────────────────────────────────────────────────────┤
│ Sidebar      │ Datasets                          [+ Create] [Manage] │
│ ▪ Dashboard  │ ┌───────────────────────────────────────────────────┐ │
│ ▪ Datasets   │ │ tank                 │ 42 % │ ZFS │ [⋮]          │ │
│ ▪ Pools      │ │  ├─ docs             │  3 % │     │ [⋮]          │ │
│ ▪ Shares     │ │  ├─ media            │ 31 % │     │ [⋮]          │ │
│ ▪ Apps       │ │  └─ app_configs      │  8 % │     │ [⋮]          │ │
│ ▪ System     │ └───────────────────────────────────────────────────┘ │
│              │ (filter, column selection, status banner)             │
└──────────────┴───────────────────────────────────────────────────────┘
```

### Wizard (example *Create Dataset*)

```
┌──────────────────────────────────────────┐
│  Dataset create            [X]           │
├──────────────────────────────────────────┤
│  Pool   [tank ▾]   Name  [____________]  │
│  (☑) Encryption   (☑) NFS/SMB presets    │
│  ▸ Advanced (compression, quota, …)      │
├──────────────────────────────────────────┤
│           [CANCEL]  [CREATE]             │
└──────────────────────────────────────────┘
```

### Job panel

```
┌──────────────────────────────────────────┐
│  Tasks                          [✕]      │
├──────────────────────────────────────────┤
│  ✅ Pool scrub      100 %   (2 h)        │
│  ⏳ Replication     42 %   [Abort]       │
│  ❌ Cloud Sync      error  [LOG]         │
└──────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header bar | Top | Version/build, global search, jobs, alerts, user/API menu |
| Sidebar | Left | Navigation items (datasets, pools, shares, apps, system …) |
| Content area | Right | Cards, tables, trees, form wizards |
| Action buttons | Top right of the content | Create/Add/Manage of the current area || Three-dot menus | Rows/objects | Context actions (snapshots, edit, delete) |
| Job panel | Overlay on the right | Running middleware jobs with log links |
| Toasts | Bottom | Success/error after actions |

## UI/UX

### Design principles

- **One area per screen**: no window management, page changes via sidebar
- **Guided wizards**: pool/dataset/app creation with defaults and warnings
- **Visible jobs**: long runs never invisible — job panel and status banner
- **Protection against destruction**: critical actions with confirmation dialogue (type manually in case of danger, version-dependent)

### Colour scheme and themes

- Light default scheme, dark mode switchable depending on version (user menu)
- Status: green = ok/started, blue = info, yellow = warning, red = error; alert bell with counter
- Accent colour and density remain consistent via NG-ZORRO components

### Interactions

- **Global search**: finds pages, datasets, shares, users (since 23.x, version-dependent)
- **Trees**: dataset/iSCSI trees with expansion and row menus
- **Forms**: inline validation, required-field marking, tooltips on technical terms
- **Live tables**: status columns update without rebuilding (WebSocket push)
- **Drag and drop**: practically absent — exceptions such as app sorting (version-dependent)

### Responsive design

- **Desktop**: full layout, sidebar fixed
- **Narrow windows**: sidebar becomes an icon bar/overlay, tables get horizontal scrolling
- **Mobile**: operation of the core areas works, forms remain long
- **Kiosk operation**: web UI on touch monitors/displays as a common pattern

### Accessibility

- **Keyboard**: sidebar links, tables and dialogues reachable via `Tab`/`Enter`
- **Screen reader**: ARIA roles on dialogues and menus; live regions for toasts/jobs
- **Focus indicator**: recognisable, wizards set focus on the first field
- **Language**: UI localised in many languages; the German version contains untranslated technical terms depending on the version

### Performance

- **SPA with WebSocket backend**: tab switches without complete reloads; initial load noticeable (Angular bundle)
- **Table pagination**: large dataset/snapshot lists are loaded server-side
- **Job-based**: scrub/replication do not block the UI; retrieve logs when needed
- **Recommendation**: limit the number of snapshots per dataset, restrict report queries by time

## See also

- [menu.md](menus.md) - Page structure and roles
- [features.md](features.md) - Feature areas
- [shortcuts.md](shortcuts.md) - Keyboard and console menu
- [api.md](api.md) - Middleware API and CLI
