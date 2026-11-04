# GNOME Planner – Description

**Version state: 0.14.92 (2023-12-16)** — actively maintained again after a long standstill since the mid-2010s (releases 0.14.91/0.14.92, translations up to 2026, packaged in Debian stable and Arch extra).

## What the program does

Planner is the classic project planner on GNOME: projects are built according to network-plan/CPM logic — tasks with start/finish, work, progress, priority and dependencies (FS/SS/FF/SF incl. lag), resources with working calendars and assignments, plus milestones, phases, project/resource groups and custom fields. The engine computes forward/backward dates (earliest/latest points), slacks and the critical path. Planning happens in four views (Gantt chart, tasks, resources, resource usage); results can be printed (also PDF) or exported as HTML. Projects remain simple XML files (`*.planner`); optionally a plugin stores them in PostgreSQL.

## Benefits

- **Free and local:** GPL v2+, no cloud, no accounts; `.planner` stays a readable XML file with a DTD in the source code
- **Genuine planning logic:** four dependency types with lag, early/late dates, slacks, critical path, fixed-duration/fixed-work modes, constraints (SNET/MSO)
- **The working calendar as a first-class object:** base/resource calendars with working days, time-of-day intervals and public holidays — calendar weeks "by hand", with no pressure to use external calendar services
- **A cost approach built in:** cost rate per resource, per-task cost and slack columns
- **Two storage locations:** a single file *or* a PostgreSQL database (experimental) — good for versioning and scripting
- **GTK3/Meson freshly refreshed:** since 0.14.91 a port to GTK 3.22, GSettings and Meson; time handling that is safe past 2038
- **Widely distributed:** packaged in all major distributions; Windows builds via the project wiki

## How it differs

| System | Difference |
|--------|------------|
| **MS Project** (and **ProjectLibre** as a clone) | commercial respectively Java, imports native `.mpp`, with budget/reporting facilities and a project server; Planner only imports MS Project **XML** and deliberately forgoes cost accounting and a server |
| **GanttProject** | Java, similar; but with PMML/PDF/MS Project export and active ongoing development; Planner is more GTK-native and can store into SQL databases, GanttProject has PERT-like views |
| **OpenProject / Planka / Taiga / Wekan** (series: project management) | web-based task/ticket systems with multiple users; Planner is a single-seat desktop tool without ticket logic, agile boards or web access |
| **Nextcloud Calendar/Tasks, ownCloud Tasks** | CalDAV/ICS-based event/task servers with device sync; Planner can neither read nor write ICS and has no CalDAV — it plans time axes and task networks, not events |
| **GNOME Merkuro / Thunderbird** (series: calendars) | event calendars with recurrences/invitations; Planner has no event model and no reminders |
| **Todoist & co.** | personal to-do lists with synchronisation; Planner plans task networks with dependencies and resources, without sync |

## Technical details

- **Language/toolkit:** C, GObject; GTK ≥ 3.22, GLib ≥ 2.56; the UI partly still uses GtkUIManager (GtkBuilder files under `data/ui/`)
- **Planning engine:** libplanner (`Mrp*` classes), **private** since 0.14.91 (not installed, no stable ABI)
- **Data storage:** a single file `*.planner` (XML, DTD `mrproject-0.6`); optionally PostgreSQL via the libgda plugin (experimental)
- **Further libraries:** libxml2, libxslt (HTML export, MSP-XML import); optionally evolution-data-server (resource import, off by default)
- **Platforms:** Linux (in all major distributions), a Windows installer in the source code (`installer/`, NSIS) and via the project wiki; no Mac build in the project
- **Licence:** GPL v2 or later
- **Maturity:** 0.14.9x are marked as "source code only beta"; experiments (SQL, EDS, priority scheduling) only via Meson switches

## Who it suits

- Association, construction, trade and migration projects with classic (waterfall) planning and CPM thinking
- Legacy MS Project holdings that exist as XML and are only to be maintained further, viewed or printed
- Anyone who wants to keep project states as a versionable XML file (git-friendly) or in their own database
- **Less suitable** for team event planning, agile boards or mobile capture — for that the calendar/PM entries of the series are the better choice
