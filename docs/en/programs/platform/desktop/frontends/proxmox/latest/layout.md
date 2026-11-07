# Proxmox VE - Structure & UI/UX

## Overview

After signing in, Proxmox VE shows a three-area layout: the resource tree on the left, the object header with action buttons at the top right, and below it tabs with tables and forms. Overlays (dialogues, consoles) lie on top of it; a task panel reports background actions.

## Window structure

### Main view

```
┌──────────────────────────────────────────────────────────────────────┐
│ Header: Proxmox logo | Search bar | Theme | User menu | Sign out     │
├────────────────────┬─────────────────────────────────────────────────┤
│ Resource tree      │ Object header: [pve1] [101 ubuntu-server]       │
│ ▼ Datacenter       │ Buttons: Start | Stop | Reboot | Migrate | ⋮    │
│   ▸ pve1           ├─────────────────────────────────────────────────┤
│     ▸ 101 ubuntu   │ Tabs: Summary Hardware Options Console …        │
│     ▸ 102 nginx    ├─────────────────────────────────────────────────┤
│   ▸ storage        │ Tables / forms / charts of the tab              │
│                    │ ┌────────────────────────────────────────────┐  │
│                    │ │ disk0   qc0  scsi0  32G  Local-LVM  [⋮]   │  │
│                    │ └────────────────────────────────────────────┘  │
├────────────────────┴─────────────────────────────────────────────────┤
│ Task panel (expandable): running/backups/migrations with status      │
└──────────────────────────────────────────────────────────────────────┘
```

### Dialogue (example *Create VM*)

```
┌──────────────────────────────────────────────────────────┐
│  Create VM                                       [X]     │
├──────────────────────────────────────────────────────────┤
│  (General) (OS) (System) (Disks)                         │  ← step bar
│  Node [pve1 ▾]  VM ID [103 ]  Name [____________]       │
├──────────────────────────────────────────────────────────┤
│             [< Back]  [Next >]  [Create]                 │
└──────────────────────────────────────────────────────────┘
```

### Console view

```
┌──────────────────────────────────────────────────────────┐
│  Console: xterm.js (VM 101)     [Menu ⚙: keys, clipboard]│
├──────────────────────────────────────────────────────────┤
│                                                          │
│   terminal/graphics-style console (noVNC or xterm.js)    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Header bar | Top | Search, theme switch, user/token menu |
| Resource tree | Left | Datacenter, nodes, VMs, containers, storage, pools |
| Object header | Top right | Name, status, start/stop/reboot/migrate/console buttons |
| Tabs | Centre right | Summary, hardware, options, console, backup, … |
| Tables | Within the tab | Disks, networks, rules, jobs with action menus (`⋮`) |
| Task panel | Bottom | Background tasks (UPID) with progress and error link |
| Overlays | Centre | Creation wizards, edit dialogues, console, shell |

## UI/UX

### Design principles

- **One object in focus**: tree selection controls everything, no multiple windows
- **Tabs per subject area**: hardware, options, security clearly separated
- **Wizards for complex tasks**: VM/storage creation in steps with validation
- **Actions close to the object**: buttons sit in the object header, row actions in the `⋮` menu

### Colour scheme and themes

- Light/dark/auto via the theme switch in the header bar (version-dependent)
- Status colours: green = running, grey = stopped, red = error; consoles have their own colour scheme
- Own logos/themes for companies possible (version-dependent)

### Interactions

- **Search at the top**: filters the tree by VMID, name, tag, IP
- **Double-click**: opens the default action (console or tab, depending on the object)
- **Drag and drop**: drag boot order; otherwise rare
- **Right-click**: occasional context actions in the tree (version-dependent)
- **Live updates**: charts and status values are updated automatically

### Responsive design

- **Desktop**: full layout; tree collapsible for more table width
- **Tablet**: tree overlays the content, tabs horizontally scrollable
- **Mobile**: usable, but tables and consoles remain small – not the primary target mode
- **Full-screen console**: the console tab can be maximised to fill the area (version-dependent)

### Accessibility

- **Keyboard**: tabs, tables and dialogues operable via `Tab`/`Enter`; consoles capture keyboard input
- **Screen reader**: tables have header assignment, but dynamic panels are medium-quality for readers (ExtJS legacy, version-dependent)
- **Focus indicator**: visible, dialogues trap focus
- **Zoom**: browser zoom without cut-off buttons; tables then scroll horizontally

### Performance

- **API-driven interface**: each tab loads its data on selection; large inventory lists are paginated
- **Console stream**: noVNC/xterm.js load the client and network, not the API
- **Task asynchrony**: long actions continue as tasks (UPID), the UI does not block
- **Recommendation**: in very large environments, use search/filter instead of expanding the whole tree

## See also

- [menu.md](menus.md) - Tree structure and roles in detail
- [features.md](features.md) - Feature areas
- [shortcuts.md](shortcuts.md) - Keyboard and console keys
- [api.md](api.md) - REST API behind every UI action
