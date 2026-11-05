# GNOME Planner - API Documentation

**Version state: 0.14.92 (2023-12-16)** — source-code beta release, maintained (translation updates through April 2026), packaged in Debian stable (trixie, 0.14.92-1.1) and Arch extra (0.14.92-4).

## Status check (Is this worth documenting?)

- **Still developed/used?** Yes: releases 0.14.91 (2022) and 0.14.92 (2023) after a long pause; the repo `gitlab.gnome.org/World/planner` is active (last commits April 2026, mostly translations); distribution packages are current. → Document rather than delete.
- **Unique features** (even if development stalls): project-internal working calendars per resource, custom properties at project/task/resource level, optional PostgreSQL storage of projects via a plugin — no other calendar frontend in this series offers that.

## Overview

Planner is a pure desktop planner **with no server and no live API**. The programmatic interface is the file: the XML format `*.planner` (MIME `application/x-planner`) and — internally — the library **libplanner** (class prefix `Mrp*`). Since 0.14.91 libplanner is **private**: it is no longer installed, and out-of-tree plugin/programming access no longer officially exists (issue #238).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| `*.planner` / `*.mrproject` (XML) | Save/load projects, conversion | official, DTD in the source (`data/dtd/mrproject-0.6.dtd`) |
| libplanner (`Mrp*`, C/GObject) | Scheduling objects, CPM calculation, storage modules | **private** since 0.14.91 (not installed, no stable ABI) |
| SQL plugin (libgda → PostgreSQL) | "Open from Database…" / "Save to Database" | official, but experimental (Meson option `database-gda`) |
| HTML export (libxslt) | Reports as HTML | official |
| REST/GraphQL/WebSocket | — | ❌ not present |
| Webhooks | — | ❌ not present |

## The `*.planner` file format

- **Extensions/MIME:** `*.planner` (the default when saving) and `*.mrproject`; MIME type `application/x-planner`, a subtype of `application/xml`; magic marker `mrproject-version` (see `data/mime/app.drey.Planner.xml.in`). The former `.ppx` extension no longer occurs anywhere in the 0.14.92 source.
- **Schema:** DTD `data/dtd/mrproject-0.6.dtd`; root element `<project mrproject-version="2" …>` (the 0.11 legacy formats are read via `libplanner/mrp-old-xml.c`; exporting to the 0.11 format was removed in 0.14.92, bug #248).

Excerpt (abridged) from `examples/sample-1.planner` in the source tarball:

```xml
<?xml version="1.0"?>
<project name="Sample 1" company="Planner Community" manager="Richard Hult"
         phase="Implementation" project-start="20040701T000000Z"
         mrproject-version="2" calendar="1">
  <phases>
    <phase name="Design"/>
    <phase name="Implementation"/>
  </phases>
  <calendars>
    <day-types>
      <day-type id="0" name="Working" description="A default working day"/>
      <day-type id="1" name="Nonworking" description="A default non working day"/>
    </day-types>
    <calendar id="1" name="Default">
      <default-week mon="0" tue="0" wed="0" thu="0" fri="0" sat="1" sun="1"/>
      <overridden-day-types>
        <overridden-day-type id="0">
          <interval start="0800" end="1200"/>
          <interval start="1300" end="1700"/>
        </overridden-day-type>
      </overridden-day-types>
      <days/>
    </calendar>
  </calendars>
  <tasks>
    <task id="3" name="Report" work="0" start="20040708T104000Z"
          end="20040708T104000Z" percent-complete="0" priority="0"
          type="milestone" scheduling="fixed-work">
      <predecessors>
        <predecessor id="1" predecessor-id="2" type="FS"/>
      </predecessors>
    </task>
  </tasks>
  <resource-groups/>
  <resources>
    <resource id="1" name="Alvaro del Castillo" short-name="ACS" type="1"
              units="0" email="" note="" std-rate="0">
      <properties>
        <property name="cost" value=""/>
      </properties>
    </resource>
  </resources>
  <allocations>
    <allocation task-id="2" resource-id="1" units="75"/>
    <allocation task-id="15" resource-id="1" units="100"/>
  </allocations>
</project>
```

**Core elements of the DTD (0.6):**

| Element | Most important attributes | Notes |
|---------|---------------------------|-------|
| `project` | `mrproject-version="2"`, `name`, `project-start`, `company`, `manager`, `phase`, `calendar` | Order of children: `properties*`, `phases?`, `calendars?`, `tasks?`, `resource-groups?`, `resources?`, `allocations?` |
| `task` | `id`, `name`, `start`, `end`, `work`, `duration`, `percent-complete`, `priority`, `type=normal\|milestone`, `scheduling=fixed-work\|fixed-duration`, `note` | Subtasks are nested `task` elements; their own summary rows ("summary") are computed implicitly from the children |
| `predecessor` | `predecessor-id`, `type=FS\|FF\|SS\|SF`, `lag` | References by task `id` |
| `constraint` | `type`, `time` | Implemented: ASAP (default), SNET ("start not earlier than"), MSO ("must start on"); ALAP and FNLT are marked *unimplemented* in `mrp-types.h` |
| `property` / `properties` | `name`, `type=date\|duration\|float\|int\|text\|text-list\|cost`, `owner=project\|task\|resource`, `value` | User-defined columns; a DTD comment points to the dual role declaration/value |
| `calendar` | `id`, `name`; children `default-week`, `overridden-day-types`, `days`, nested `calendar` | Working/non-working days with day intervals (`interval start/end` = time HHMM); subordinate calendars inherit from the base calendar |
| `resource` | `id`, `name`, `short-name`, `email`, `type=1\|2` (work\|material), `group`, `units`, `std-rate`, `ovt-rate`, `calendar` | A dedicated calendar per resource is possible |
| `allocation` | `task-id`, `resource-id`, `units` | Resource↔task assignment in percent |

**Time units:** `start`/`end`/`project-start` as `YYYYMMDDTHHMMSSZ`; the internal time `mrptime` is a 64-bit second count since the Unix epoch (`libplanner/mrp-time.h`, Y2038-safe since 0.14.91); `work` is expressed in **seconds** (example above: `work="115200"` = 32 h).

## Authentication

None — local files; access rights via the filesystem/shares. Only the SQL plugin asks for server, database name, user and password at "Save to Database".

## Import/export as the "API"

| Direction | Format | Route / switch |
|-----------|--------|----------------|
| Import | MS Project **XML** (from MSP 2002, "Save As… XML") | `File → Import → MS Project XML…`; XSLT `data/stylesheets/msp2planner.xsl`; experimental; calendars, groups and custom fields are **not** imported |
| Import | Contacts/resources from Evolution Data Server or LDAP | `File → Import → EDS…` (plugin, Meson option `eds`, disabled by default) |
| Import/export | PostgreSQL database | `File → Import → Open from Database…` / `File → Export → Save to Database…` (libgda; schema `data/sql/database.sql`) |
| Export | HTML (Gantt image, task list, resource table) | `File → Export → HTML…` (XSLT under `data/stylesheets/`) |
| Export | PDF | GTK print dialog "Print to file"; the print dialog selects the views via checkboxes |
| Export | Planner 0.11 legacy format | ❌ removed in 0.14.92 (bug #248) |

## Example: evaluation via script

```python
import xml.etree.ElementTree as ET

t = ET.parse("projekt.planner")
root = t.getroot()

def walk(tasks):
    for task in tasks:
        work_h = int(task.get("work") or 0) / 3600.0   # seconds -> hours
        print(f"{task.get('name')}: {work_h:.1f} h "
              f"({task.get('start')} .. {task.get('end')})")
        walk(task.findall("task"))

walk(root.find("tasks"))
```

## Rate limits

Not applicable (no network API). The SQL plugin is only subject to the limits of the PostgreSQL connection.

## SDKs and libraries

- **libplanner** (C/GObject, classes `MrpProject`, `MrpTask`, `MrpResource`, `MrpCalendar`, `MrpRelation`, `MrpAssignment`, storage modules …): only built **internally** now; reference/documentation objects exist only with the Meson option `gtk_doc=true`, as a *private* API reference.
- **Python bindings:** not present; `tests/python/task-test.py` is a legacy test against the historical `mrproject` PyGTK module and does not run with current versions.
- **Converters:** `.planner` is plain XML → own scripts with XSLT/DOM; the SQL schema (`data/sql/`) is a second structured access route.

## Frontend note

A Planner frontend in FreeSynergy reproduces the four views (Gantt, tasks, resources, resource usage) and reads/writes `*.planner` XML; map the time/effort fields onto the standard model ([Fields](../../../../../../data/fields.md), [Task/project model](../../../../../../data/models.md); see also [data/projects](../../../../../../data/projects/)).
