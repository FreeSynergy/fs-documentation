# Synology DSM - Structure & UI/UX

## Overview

DSM imitates a desktop in the browser: a narrow upper bar, an app bar at the bottom edge, a desktop area with widgets and freely positionable windows. Each application (File Station, Control Panel, Package Centre …) opens a window with its own title bar and often its own tabs. Several windows and several browser tabs can work in parallel.

## Window structure

### Desktop view

```
┌──────────────────────────────────────────────────────────────────────┐
│ [Main menu]              [     Search     ] [Notices] [Account]     │
├──────────────────────────────────────────────────────────────────────┤
│  Desktop area                                    ┌────────────────┐ │
│                                                  │ System Pulse    │ │
│   ┌───────────────────────────┐                  │ CPU 12 % · RAM │ │
│   │ File Station (window)     │                  │ Volume 68 %    │ │
│   │ Title: - + x              │                  │ Net ↓ 3 MB/s   │ │
│   │ [Folder][Preview][Tasks]  │                  ├────────────────┤ │
│   │ ┌───────┬───────────────┐ │                  │ Storage        │ │
│   │ │Tree   │ File list     │ │                  │ warnings (2)   │ │
│   │ └───────┴───────────────┘ │                  └────────────────┘ │
│   └───────────────────────────┘                                    │
│                                                  ┌────────────────┐ │
│                                                  │ Clock / date   │ │
│                                                  └────────────────┘ │
├──────────────────────────────────────────────────────────────────────┤
│  App bar: [Files][Control Panel][Package Centre][Drive] (…)          │
└──────────────────────────────────────────────────────────────────────┘
```

### Main menu (overlay)

```
┌────────────────────────────────────────────┐
│  Search field in menu                      │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌──────┐ │
│  │ File   │ │Control │ │Package │ │Drive │ │
│  │Station │ │ panel  │ │ centre │ │      │ │
│  └────────┘ └────────┘ └────────┘ └──────┘ │
│  [Edit arrangement]  [All programs]        │
└────────────────────────────────────────────┘
```

### Dialogue (confirmation / wizard)

```
┌──────────────────────────────────────────┐
│ Dialogue title                   [✕]     │
├──────────────────────────────────────────┤
│  Field · Selection · Switch              │
│  Advanced ▸                              │
├──────────────────────────────────────────┤
│          [Cancel]  [Next/OK]             │
└──────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Upper bar | Top | Main menu, universal search, notifications, account menu |
| App bar | Bottom | Pinned applications, running windows |
| Desktop area | Centre | Background, desktop widgets, window shadows |
| Window | freely movable | Title bar, tab/toolbar, work area |
| Sidebar in window | Left | Folder tree, categories, filters |
| Status bar in window | Bottom | Selection info, task progress |
| Overlay dialogues | Centred | Forms, wizards, confirmations |
| Toast / message | Top right | Success, errors, running tasks |

## UI/UX

### Design principles

- **Desktop metaphor**: windows, bars, docking – users find their way around as at a desk
- **Dense table views**: lists with columns, filters and bulk actions instead of individual cards
- **Make rights visible**: packages that are not enabled do not appear in the menu at all
- **Wizards for risk**: critical steps (volume, share deletion) with review page and confirmation

### Colour scheme and themes

- **Light and dark mode** (DSM 7), selectable in the account menu or following the system setting
- **Accent colour** and icon style in the desktop settings
- **Background images** (existing selection or own image)
- **High-contrast status colours** for warning (yellow), error (red), success (green)
- **Accessibility options** in the display settings (text size, contrast depending on DSM version)

### Interactions

- **Windows**: move via title bar, resize at edges, maximise/restore, overlap with focus change
- **Window arrangement**: dock at screen edges, side by side, minimise all
- **Drag and drop**: drag files from Finder/Explorer into File Station, target folder is highlighted
- **Multiple selection**: click with `Ctrl`/`Cmd`, range with `Shift`, expanding selection in lists
- **Context menus**: right-click on files, icons, desktop and bar objects
- **Animations**: windows open/close with a short fade, menus unfold, progress bars for tasks; deliberately subtle
- **Task Center**: long-running operations (copy, delete, upload) run as a task with progress and cancel

### Responsive design

- **Desktop browser**: full desktop with windows and widgets
- **Tablet**: windows displayed large, bar reduced, touch gestures for swiping between windows
- **Narrow browser / mobile**: single-component view, menu as overlay, file list in one column
- **Own apps** (DS file, Drive, Surveillance) replace the portal on small devices with tailored interfaces
- **QuickConnect links** redirect to the mobile variant

### Accessibility

- **Keyboard**: forms, lists and dialogues operable via `Tab`/`Enter`/`Esc`; mass actions mostly remain mouse-oriented
- **Focus indicator**: active field and active file are marked
- **Screen reader**: labels for icons and dialogues improved in current DSM versions, but not comprehensive
- **Colour independence**: status additionally with symbol and text
- **Languages**: full localisation, including German
- **Zoom**: browser zoom works, window layout adapts

### Performance

- **Index-based search**: Universal Search works against an index, not against live directory scans
- **Tasks instead of blocking**: copy/delete operations run asynchronously with a task list
- **Deferred loading**: large folders load section by section
- **Resource monitor** shows which package burdens the system; packages can be stopped specifically
- **Recommendation**: restrict indexing, schedule thumbnail generation, limit log retention

## See also

- [menu.md](menus.md) - Menu items by role
- [features.md](features.md) - Packages and services
- [shortcuts.md](shortcuts.md) - Keyboard operation and system commands
- [api.md](api.md) - `entry.cgi` and session handling
