# GNOME Planner Documentation

## Overview

Planner is the project planner on GNOME (app ID `app.drey.Planner`): tasks with start/finish, work, costs and dependencies (FS/SS/FF/SF with lag), resources with their own working calendars, critical path and slacks — shown in four views (Gantt, tasks, resources, resource usage). Projects stay XML files (`*.planner`, DTD `mrproject-0.6`); optionally an experimental plugin stores them in PostgreSQL. Import: MS Project XML and Evolution/LDAP contacts; export: HTML and print/PDF. State: **0.14.92 (December 2023)** — maintained again after a long standstill (translations up to 2026; packaged in Debian stable and Arch extra), but marked as beta. In this calendar series what matters for it is the working-calendar/time-axis logic, not an event calendar.

## File structure

- [description.md](description.md) - What Planner does, benefits, how it differs from MS Project, GanttProject, OpenProject, Nextcloud
- [features.md](features.md) - Verified features (0.14.92) and what Planner does NOT offer
- [structure.md](structure.md) - Window layout, program/module structure (src, libplanner, plugins), configuration, deployment
- [menu.md](menu.md) - Menus, bars and context menus taken from the GtkBuilder files
- [shortcuts.md](shortcuts.md) - Shortcuts from the source code (incl. Open = F3!)
- [api.md](api.md) - No REST: the `*.planner` file format, DTD, units, SQL storage, import/export paths

## Sources

All statements in this section come from the official source code of the current release and the official project pages:

| Source | Location / URL | Used for |
|--------|----------------|----------|
| Source release **0.14.92** (2023-12-16) | `https://download.gnome.org/sources/planner/0.14/planner-0.14.92.tar.xz` (unpacked and read locally) | all files |
| GitLab repository (active, last commits April 2026) | `https://gitlab.gnome.org/World/planner` + API `…/api/v4/projects/World%2Fplanner/repository/commits` | maintenance/usage status |
| Release download directory | `https://download.gnome.org/sources/planner/0.14/` (LATEST-IS-0.14.92; NEWS for 0.14.91/0.14.92) | version state, changes |
| `NEWS`, `README`, `planner.doap` in the tarball | maintainer (Mart Raudsepp), GPL v2+, homepage, dependencies | api.md, description.md |
| `src/planner-window.c` (lines 209–300) | action table: menus + accelerators (Ctrl+N, F3, Ctrl+R, F1 …), registered views (lines 664–667) | menu.md, shortcuts.md, structure.md |
| `src/planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`, `planner-usage-view.c` | view-specific actions and shortcuts (Ctrl+I/D/A, Ctrl+Shift+E/I/U, zoom) | shortcuts.md, features.md |
| `data/ui/main-window.ui`, `task-view.ui`, `resource-view.ui`, `gantt-view.ui`, `sql-plugin.ui`, `eds-plugin.ui` | the real menu structure incl. import/export submenus and placeholders | menu.md |
| `src/planner-task-popup.c`, `data/ui/resource-view.ui` (popup) | context menus | menu.md |
| `data/dtd/mrproject-0.6.dtd`, `examples/sample-1.planner`, `tests/files/*.planner` | the exact file format, elements/attributes, example | api.md |
| `data/mime/app.drey.Planner.xml.in`, `data/app.drey.Planner.desktop.in`, `data/app.drey.Planner.gschema.xml` | MIME `application/x-planner`, extensions `*.planner`/`*.mrproject`, GSettings schema with views/columns | api.md, structure.md |
| `libplanner/mrp-time.h`, `mrp-task.h`, `mrp-types.h`, `mrp-resource.h`, `mrp-project.h` | time units (64-bit seconds), early/late, critical path, constraint types (ALAP/FNLT unimplemented), material resources, costs | api.md, features.md |
| `meson.build`, `meson_options.txt`, `src/meson.build` | dependencies (GTK ≥ 3.22, libgda/EDS optional), in-tree plugins as shared modules, the EDS backend is not built | structure.md, features.md |
| `docs/user-guide/C/planner.xml` (user guide V0.14) | the four views, multiple projects, SQL configuration (PostgreSQL), MSP-XML limits, HTML content, the print dialog, priority scheduling | features.md, description.md, structure.md |
| Debian package | `https://packages.debian.org/search?keywords=planner` (trixie: planner 0.14.92-1.1; planner-dev only up to bullseye) | usage status, libplanner now private |
| Arch package | `https://archlinux.org/packages/extra/x86_64/planner/` (0.14.92-4, 2025-04-30) | usage status |
| GNOME wiki (retro, but official) | `https://wiki.gnome.org/Apps/Planner` | short description, Windows builds |
| Flathub search `app.drey.Planner` | no hit (state of the research) | "no Flatpak" |

**Corrections relative to the older version of this section** (based on the 0.14.92 source code): the PERT/dependency-network view no longer exists (today: four views incl. resource usage); the `.ppx` extension and the "LibMSP" `.mpp` import no longer occur in the release (only MS Project XML); since 0.14.91 libplanner is a private library with no third-party plugin support; "no cost module" is wrong (resource cost rates, cost/slack columns); the shortcuts Open=F3 and Repeat=Ctrl+R were corrected; the project is not abandoned but maintained again.
