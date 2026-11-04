# GNOME Planner – Features

All features verified against the source release **0.14.92** (files in parentheses) and the bundled user guide (`docs/user-guide/C/planner.xml`, state V0.14).

## Task planning (task view)

- Tasks nested hierarchically; milestones as a task with duration 0; summary tasks implicit from children (`mrp-storage-mrproject.c`, `task-dialog.ui`)
- Properties per task: name, start/finish, work, duration, progress (%), priority, notes, type milestone, mode "fixed duration" (`fixed-work`/`fixed-duration`) (`task-dialog.ui`, DTD)
- Dependencies FS/SS/FF/SF with lag, creatable in the "Predecessors" dialog **or** by dragging an arrow between bars in the Gantt (then always FS) (`mrp-relation.h`, user guide "Creating Dependencies with the Gantt Chart")
- Constraints: ASAP (default), "start not earlier than" (SNET), "must start on" (MSO); undo via Actions → reset constraint. ALAP and "finish not later than" are declared but **not implemented** (`mrp-types.h`)
- Computation: forward/backward scheduling (`mrp_task_get_latest_start/finish`), slacks, critical path (`mrp_task_get_critical`), highlightable in Gantt/tasks (`planner-gantt-*`, GSettings `highlight-critical-path`)
- Creating/changing hierarchy by indenting/outdenting, moving with/without dependencies, multi-selection
- An experimental priority-driven scheduling (resources withdrawn in favour of a task with priority 9999 and a fixed start) — only when built with the Meson option `simple-priority-scheduling` (`meson_options.txt`, user guide "Scheduling")

## Resources and costs

- Resources of type **work** or **material**, short name, e-mail, groups, assignment level (units %), notes (`resource-dialog.ui`, `mrp-resource.h`)
- Cost rate per resource; cost computation per task and per project; a cost column in the task/Gantt view (`mrp-resource.c` "standard cost", `mrp_task_get_cost`, the `cost` column in `planner-task-tree.c`)
- Assignments task↔resource with percentages; the **resource usage** view with a utilisation chart and zoom (`planner-usage-view.c`, `planner-usage-chart.c`)
- Resource import from Evolution contacts or LDAP (EDS plugin, experimental, disabled by default) (`planner-eds-plugin.c`, `meson_options.txt`)

## Calendars

- Project base calendar with a default week and per-day **intervals** (e.g. 08:00–12:00, 13:00–17:00) (`mrproject-0.6.dtd`, `planner-calendar-dialog.c`)
- Own calendar day types with a description, overridable weekdays, individual deviations/public holidays per date (`calendar-dialog.ui`, `day-type-dialog.ui`, `working-time-dialog.ui`)
- A base-calendar hierarchy (sub-calendars inherit) and **a calendar of its own per resource**; tasks follow the calendar of the assigned resource (`mrp-calendar.c`, user guide "Calendar Tab")

## Project management

- Project properties: name, start, organisation, manager, phase, default calendar; fixed project phases with phase switching (`project-properties.ui`, `planner-phase-dialog.c`)
- **Custom properties** at project, task and resource level with the types date/duration/float/int/text/text-list/cost; they appear as columns (`mrp-property.c`, DTD, user guide)
- Several projects open at the same time, each in its own window (`planner-window.c`, user guide "Editing Multiple Projects")
- Undo/redo for most actions, but expressly not for all of them (user guide "Caution")

## Charts and output

- Gantt chart with bars, milestone diamonds, dependency arrows, non-standard days, guidelines, zoom (`planner-gantt-chart.c`, view options)
- Printing/PDF: the GTK print dialog; selectable views via checkboxes (Gantt/tasks/resources/usage), paper/layout tab, print preview (`planner-print-dialog.c`, `planner-print-job.c`)
- HTML export as a single file: a Gantt image, a task list (% complete, start, finish, work, resources), a resource table; can also be published to a web address (`planner-html-plugin.c`, `data/stylesheets/html1_*.xsl`)

## Import, export, storage

- Native: `*.planner` (`*.mrproject` also readable), MIME `application/x-planner`, DTD version 2 (`data/mime/`, `mrp-storage-mrproject.c`)
- Old formats (Planner ≤ 0.11) are still read when opening (`mrp-old-xml.c`); the export into the 0.11 format was removed in 0.14.92 (NEWS #248)
- Import: MS Project **XML** (MS Project 2002+; no native `.mpp`), without calendars/groups/custom fields (`planner-msp-plugin.c`, `msp2planner.xsl`)
- Optionally stored in **PostgreSQL**: "Open from Database…"/"Save to Database…", the database is created automatically if needed; the schema under `data/sql/` (experimental) (`planner-sql-plugin.c`, user guide "Configuring a Planner database")

## What Planner does NOT offer

- **No calendar sync:** no CalDAV, no ICS import/export, no connection to Google/Outlook/Nextcloud calendars — the calendars are internal working-time calendars
- **No PERT/network view any more:** the former three views (incl. the dependency network) do not exist in that form; today: Gantt, tasks, resources, resource usage (`planner-window.c` registers exactly these four)
- **No import of native `.mpp` files** — only MS Project XML
- **No multi-user editing:** no locking/conflict management; the SQL storage shares data but still opens projects per workplace
- **No web/mobile version**, no online collaboration, no API for live access
- **No agile mode** (Kanban/Scrum/burndown) and no ticket system
- **No budget/order management:** only cost rates and simple cost addition; no invoices, contribution margins, payment tracking
- **No reminders/notifications** and no event model
- **No extensible third-party plugins:** libplanner has been private since 0.14.91, out-of-tree plugin support was dropped; the bundled plugins (html, msp, sql, eds) are in-tree modules
- **Resource calendars without public-holiday import** from external services (holidays have to be maintained manually as individual days)
- **No GTK4/Libadwaita:** still GTK3 (partly GtkUIManager); no Flatpak package

## Extensions and integrations

| Integration | Path |
|-------------|------|
| PostgreSQL | SQL plugin (libgda), Meson `database-gda`; schema `data/sql/database.sql` |
| Evolution Data Server / LDAP | EDS plugin for resource import, Meson `eds` (default: off) |
| MS Project | XML exchange only, via `msp2planner.xsl` |
| HTML websites | the HTML export dialog (file or URL) |
| Print PDF | the GTK print dialog "Print to file" |
| Scripts/converters | `.planner` is XML; the SQL schema as a structured second access path |
