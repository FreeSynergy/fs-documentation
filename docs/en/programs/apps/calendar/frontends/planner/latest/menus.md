# GNOME Planner – Menu items

Source: `data/ui/main-window.ui` plus the action tables in `src/planner-window.c`, `planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`, `planner-usage-view.c` and the plugin `.ui` files (release 0.14.92). The labels below are the English originals from the source; the German release renders them via `po/de`.

## Window layout

Menu bar at the top, below it the toolbar, on the left the **view bar with the four view icons** (user guide), on the right the work area; a status bar at the bottom. The views (Gantt, tasks, resources, resource usage) are switched via the left bar or the **View** menu; the menu and toolbar contents of **Edit**, **View** and **Actions** change with the active view.

## Main menus

| Menu | Entries |
|------|---------|
| **File** | New project (Ctrl+N) · Open… (**F3**) · Recent files · **Import ▶** · ─ · Save (Ctrl+S) · Save As… (Ctrl+⇧+S) · **Export ▶** · ─ · Page Setup… · Print… (Ctrl+P) · Print Preview (Ctrl+⇧+P) · ─ · Close (Ctrl+W) · Quit (Ctrl+Q) |
| **Edit** | Undo (Ctrl+Z) · Redo (**Ctrl+R**) · ─ · Select All (Ctrl+A) |
| **View** | Radio: Gantt Chart · Tasks · Resources · Resource Usage · ─ · view-specific items (see below) |
| **Actions** | entirely view-dependent (see below) |
| **Project** | Manage Calendars… · Edit Day Types… · ─ · Edit Project Phases… · ─ · Edit Project Properties… |
| **Help** | User Guide (F1) · About |

Entries with "…" open dialogs; items without a stated accelerator have no shortcut.

## Import and Export submenus (plugin-dependent)

| Place | Entry | Plugin |
|-------|-------|--------|
| File → Import | MS Project XML… | msp (always built) |
| File → Import | EDS (Evolution/LDAP resources) | eds (experimental, off in the default build) |
| File → Import | Open from Database… | sql (when libgda is available) |
| File → Export | HTML… | html |
| File → Export | Save to Database | sql |

Note: the "Export → Planner 0.11 format" still mentioned in the user guide was removed in 0.14.92 (NEWS #248); the menu item no longer exists. Likewise there is no "Settings" menu any more (the preferences entry is commented out in the source; the view fine-tuning lives in GSettings).

## Actions menu per view

**Tasks** — `task-view.ui`:
Insert Task (Ctrl+I) · Insert Tasks… · Remove Task (Ctrl+D) · Link Tasks · Unlink Task · ─ · Indent Task (Ctrl+⇧+I) · Unindent Task (Ctrl+⇧+U) · ─ · Move Task Up / Move Task Down · ─ · Constraint Reset · ─ · Edit Task (Ctrl+⇧+E) · ─ · Edit Custom Properties…

**Gantt (Gantt Chart)** — `gantt-view.ui`:
as for Tasks, but without "Edit Custom Properties".

**Resources** — `resource-view.ui`:
Insert Resource (Ctrl+I) · Insert Resources… · Remove Resource (Ctrl+D) · ─ · Edit Resource Properties… (Ctrl+⇧+E) · Edit Groups… · Edit Custom Properties…

**Resource Usage** — no entries in the Actions menu.

## View menu: toggleable items per view

| View | Items |
|------|-------|
| Tasks | Edit Visible Columns · Highlight Critical Tasks |
| Gantt | Zoom In/Zoom Out/Best Fit · Edit Visible Columns · Highlight Critical Tasks · Show Guide Lines · Nonstandard Days |
| Resources | Edit Visible Columns |
| Resource Usage | Zoom In/Zoom Out/Best Fit · Edit Visible Columns |

## Toolbar

Fixed items: New project · Open · Save · ─ · Print · Print Preview · ─ · Undo · Redo; then the typical actions of the active view (e.g. insert/remove task, link/unlink, indent/unindent, move up/down, zoom).

## Context menus (right click)

**Task tree/Gantt** (`src/planner-task-popup.c`):
Insert Task · Insert Subtask · Remove Task · ─ · Unlink Task · ─ · Assign Resources… · Edit Task…

**Resource list** (`data/ui/resource-view.ui`, popup):
Insert Resource · Remove Resource · Edit Resource Properties…

## Menus by role

Planner is single-seat software without user accounts — **no role-dependent menus**.
