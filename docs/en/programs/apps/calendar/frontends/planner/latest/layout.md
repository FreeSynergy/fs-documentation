# GNOME Planner – Structure and UI/UX

Basis: source release **0.14.92**.

## Window structure

```
┌────────────────────────────────────────────────────────────────────┐
│ File Edit View Actions Project Help                                │
│ [🆕][📂][💾] [🖨][🔍] [↩][↪] │ [view-specific icons]               │
├────┬──────────────────────────┬────────────────────────────────────┤
│ A  │ Task tree                │ Gantt canvas                       │
│ n  │ # Name     Start Finish  │  W27   W28   W29   W30            │
│ s  │ ├─ Concept 01.06         │  ▐█░░░░░░░                        │
│ i  │ │ └─ Review 10.06        │  ▐███░░░░░  ← critical path red   │
│ c  │ └─ Build   20.06         │      ◆      (milestone)           │
│ h  │   [Dur.] [%] [Cost]      │   dependency arrows draggable     │
│ t  │                          │                                    │
│ e  │                          │                                    │
│ n  │                          │                                    │
│ ▸4 │                          │                                    │
│ ⌄  │                          │                                    │
├────┴──────────────────────────┴────────────────────────────────────┤
│ Status bar (context info for menu items/actions)                   │
└────────────────────────────────────────────────────────────────────┘
```

- The left bar (`src/planner-sidebar.c`) holds the four view icons: **Gantt** (the default view at start), **tasks**, **resources**, **resource usage** (`planner-window.c` lines 664–667 register exactly these four views).
- Each view combines a GtkTreeView table on the left with a canvas on the right (Gantt bars respectively the utilisation chart of the usage view).
- One project = one window; several projects = several windows (Ctrl+N).

## Program flow (request flow)

1. **Start:** `planner [file …]` → `PlannerApplication` (GtkApplication, app ID `app.drey.Planner`, `src/planner-application.c`); the files/URIs passed each open a `PlannerWindow`.
2. **Opening:** file chooser (filters `*.planner`, `*.mrproject`) → `MrpProject` loads via the storage module `libplanner/mrp-storage-mrproject.c` (mrproject v2 format, DTD); very old formats (≤ 0.11) are diverted by `mrp-old-xml.c`; alternatively loading via SQL over libgda.
3. **Computing:** `MrpTaskManager` performs forward/backward scheduling (`mrp_task_get_latest_start/finish`), marks the critical path, computes slacks/costs; changes trigger re-scheduling.
4. **Editing:** UI actions run through the `PlannerCmdManager` (`planner-cmd-manager.c`) → undo/redo; the models (`planner-list-model.c`, `planner-gantt-model.c`, `planner-usage-model.c`) mirror the `Mrp*` objects into GtkTreeModels.
5. **Saving:** the storage module writes the XML back atomically; with SQL storage, "Save to Database".
6. **Output:** printing via `planner-print-job.c` (one page per selected view, PDF through the GTK dialog); HTML via `planner-html-plugin.c` + libxslt stylesheets.

## Directory/module structure (tarball)

| Directory | Contents |
|-----------|----------|
| `src/` | GTK UI: windows, the four views, dialogs, canvas drawing (`planner-gantt-*.c`), the plugins `planner-{html,msp,sql,eds,test}-plugin.c`, the vendored `libgnomecanvas/` for the canvas |
| `libplanner/` | the planning engine `Mrp*` (project, task, relation, resource, assignment, calendar, property, time `mrp-time.c`), storage modules (`mrp-storage-mrproject.c`, `mrp-storage-sql.c`, `mrp-storage-module-xml.c`), path/XDG helpers |
| `data/` | `ui/` (GtkBuilder files incl. all menus), `dtd/mrproject-0.6.dtd`, `sql/` (PostgreSQL schema + migrations), `stylesheets/` (HTML export, `msp2planner.xsl`), `mime/`, `images/`, desktop/GSettings files |
| `docs/` | user manual (DocBook, C/es/eu), the private libplanner API documentation (gtk-doc option) |
| `examples/` | example files `kitchen.planner`, `sample-1.planner` |
| `po/` | translations (50+ languages, German included) |
| `tests/` | C tests, `files/*.planner`, a legacy Python test |
| `installer/` | NSIS script for Windows builds |
| `eds-backend/` | an old experiment of an EDS calendar backend — **no longer built** (commented out in Meson) |

## Configuration

- **GSettings (dconf):** schema `app.drey.Planner` (`data/app.drey.Planner.gschema.xml`): window geometry, last view, last folder; child schemas per view with columns (`order`/`visible`/`width` for name, start, finish, duration, work, cost, slack, WBS, assigned, complete) and Gantt options (highlight critical path, guide lines, nonstandard days, printing allowed); plugin schemas (msp, sql connections).
- **Migration:** on the first start under GTK3 the old GConf2 settings are taken over once (mapping `data/planner.convert`); print settings live in `~/.config/planner-print-config`.
- **Environment variables:** `PLANNER_DATADIR`, `PLANNER_PLUGINDIR` override the data/plugin paths (`libplanner/mrp-paths-gnome.c`).
- **Build options** (`meson_options.txt`): `database-gda` (PostgreSQL plugin), `eds` (EDS import), `simple-priority-scheduling` (experimental), `gtk_doc`, `examples`.

## Data model (classes / format)

- `MrpProject` → task tree (`MrpTask` with parents/children, the root = the project), `MrpRelation` (FS/FF/SS/SF + lag), `MrpAssignment` (resource↔task, units %), `MrpResource` (work/material, costs, calendar), `MrpGroup`, `MrpCalendar`/`MrpDay` (weekly/day intervals), `MrpProperty` (custom fields), phases.
- Times: `mrptime` = int64 seconds since the epoch (safe past 2038), duration/work in seconds; the date in XML as `YYYYMMDDTHHMMSSZ`.
- Persistence: XML `*.planner` (DTD mrproject-0.6) **or** the PostgreSQL schema (`data/sql/database.sql`: tables for tasks, resources, relations, calendars …, migrations for 0.6→0.11→0.13).

## Plugin architecture

The plugins are shared modules (`.so`) in the installation plugin directory that `planner-plugin-loader.c` loads at runtime (`mrp_paths_get_plugin_dir`); they register actions into the menu placeholders `/MenuBar/File/Import placeholder` and `/MenuBar/File/Export placeholder`. Out-of-tree plugin support has not existed since 0.14.91 (libplanner is private) — in practice it can only be extended through patches in the source code.

## Deployments

- **Building:** `meson build && ninja -C build install`; dependencies GLib ≥ 2.56, GTK ≥ 3.22, libxml2, libxslt; optionally libgda 5 and evolution-data-server ≥ 3.6.
- **Distributions:** Debian (`planner`, `planner-data`, `planner-doc`; trixie: 0.14.92-1.1), Arch (`planner` 0.14.92-4 in extra), further packaging repositories (Fedora/openSUSE likewise on 0.14.9x). There is no `planner-dev` package since bookworm (private libplanner).
- **Windows:** an NSIS installer in the source code (`installer/`), prebuilt builds via the download page of the project wiki.
- **Flatpak:** not present (no entry on Flathub, state of the research).
- **Desktop integration:** `.desktop` with the categories `Office;ProjectManagement;`, icon `gnome-planner`, MIME `application/x-planner`.

## UI/UX and accessibility

- A classic GTK3 desktop layout, not responsive; on small screens scroll horizontally.
- The standard font/theme of the desktop; no themes of its own. The dialogs are modal GtkDialogs with tabs (task: General/Resources/Predecessors/Notes; resource: General/Calendar/Notes; project: General/Custom).
- Gantt bars: dragging moves, dragging an arrow from bar to bar creates an FS dependency; a scale/zoom bar; antialiased rendering since 0.14.91.
- Accessibility: the tables/dialogs follow the GTK standard; the Gantt/usage canvas is pure drawing and is **not** explorable by a screen reader.

## Performance

- The engine computes incrementally (change → re-scheduling of the affected task branches); even several hundred tasks stay interactive.
- The Gantt canvas draws its own row objects per line (`planner-gantt-row.c`); with very many resources the usage view becomes sluggish — concrete limits are not officially documented (not verified).
