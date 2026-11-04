# GNOME Planner – Keyboard shortcuts

All shortcuts are taken from the action table of the source release **0.14.92**: `src/planner-window.c` (lines 209–300) plus `planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`. The accelerators are hard-coded in the program in GtkUIManager format (`<Control>`/`<Shift>`); they are not configurable through GSettings.

> State: Planner 0.14.92 (GTK 3.22+, app ID `app.drey.Planner`).

## File

| Shortcut | Function | Source |
|----------|----------|--------|
| `Ctrl+N` | new project (opens another window) | `FileNew` |
| `F3` | open project… | `FileOpen` |
| `Ctrl+S` | save | `FileSave` |
| `Ctrl+⇧+S` | save as… | `FileSaveAs` |
| `Ctrl+P` | print… | `FilePrint` |
| `Ctrl+⇧+P` | print preview | `FilePrintPreview` |
| `Ctrl+W` | close project | `FileClose` |
| `Ctrl+Q` | quit | `FileExit` |

**Careful:** Open has **no** Ctrl+O but **F3** — a typical reflex error in Planner.

## Edit

| Shortcut | Function | Source |
|----------|----------|--------|
| `Ctrl+Z` | undo | `EditUndo` |
| `Ctrl+R` | redo (**not** Ctrl+⇧+Z) | `EditRedo` |
| `Ctrl+A` | select all (task/resource list) | `SelectAll` per view |

## Task and resource actions (the tasks, Gantt and resources views)

| Shortcut | Function | Source |
|----------|----------|--------|
| `Ctrl+I` | insert a task respectively resource | `InsertTask` / `InsertResource` |
| `Ctrl+D` | remove the selected task(s)/resource | `RemoveTask` / `RemoveResource` |
| `Ctrl+⇧+E` | edit task / edit resource properties | `EditTask` / `EditResource` |
| `Ctrl+⇧+I` | indent task (create a sub-structure) | `IndentTask` |
| `Ctrl+⇧+U` | unindent task | `UnindentTask` |

For link/unlink tasks, moving up/down, constraint reset, milestones and the dependency types there are **no** shortcuts — they live in the **Actions** menu respectively the context menu; in the Gantt dependencies can also be created by dragging an arrow between bars.

## Gantt view

| Shortcut | Function | Source |
|----------|----------|--------|
| `Ctrl+Plus` | zoom in | `ZoomIn` (`planner-gantt-view.c` line 177) |
| `Ctrl+Minus` | zoom out | `ZoomOut` (line 180) |

"Best fit" (zoom to fit) has no accelerator, only a toolbar/menu item.

## Help

| Shortcut | Function |
|----------|----------|
| `F1` | user guide (yelp) |

## Miscellaneous

- **Menu access:** classic GTK mnemonics (`Alt` + the underlined letter of the menus File/Edit/View/Actions/Project/Help).
- **Switching views:** without a shortcut — via the view bar on the left or the **View** menu (radio items).
- **Cell editing:** in the tables by double-click/overwriting the column (GtkTreeView standard), no accelerator of Planner's own.
- **Opening files directly:** `planner projekt.planner` on the console or double-click in the file manager (desktop file `Exec=planner %F`, MIME `application/x-planner`); several files become several windows.
- **No Mac version:** the official builds are Linux (distributions) and Windows (project wiki); a Homebrew build is not part of the project.

## Explicitly not present

- No Ctrl+O (Open = F3), no Ctrl+W for "remove task" (Ctrl+W = close window)
- No shortcuts for switching views, for import/export, or for the calendar dialogs
- No configurable shortcuts (no keyboard schemas in `app.drey.Planner.gschema.xml`)
