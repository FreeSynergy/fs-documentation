# Calendar Systems

## In short

Calendar keeps your events, including the ones that repeat, in the right time zone. It shows them by month, week, day or as an agenda, and your tasks appear beside them. It answers the question: where do I need to be, and when?

## What is different here

- Events follow the open JSCalendar standard (RFC 8984), and this program owns it.
- Events import and export as iCalendar and as JSCalendar JSON; the original file text is kept for every event.
- An event keeps its wall-clock time across daylight saving. If a file holds a time zone the program cannot read, it refuses that event rather than store it at the wrong time.
- Tasks are not copied in. The calendar asks the Tasks program for them.
- Events marked sensitive are left out of exports unless you release them by name.

## Where it stands today

Latest tag: `v0.7.0`. You can create, edit, delete and list events, find what happens in a time range, and use repeating events with single occurrences changed, removed or added. Invitations can be sent, accepted, tentatively accepted and declined. The agenda mixes events and tasks. A small server and a first, provisional window (month, week, day, agenda, import and export) exist.

Not there yet: editing repeat rules or single occurrences, answering invitations, alerts and several calendars in the window; CalDAV, invitations by e-mail and free/busy calculation. The calendar server is not yet connected to a task server. Importing large files is slow (about 45 seconds for 4,000 events). Some late corrections to the core have been tested but not yet reviewed by a second reader. The interface is a draft with no consumer yet.

## Planned facets

Proposed, not built:

- Calendar: your events and appointments.
- Booking: reserving things and places, together with `fs-resources`.

## Overview

This section contains documentation for various calendar and time management systems.

## Available Systems

- **google-calendar** - Google's calendar service
- **outlook-calendar** - Microsoft calendar
- **ical** - iCalendar format support
- **davical** - CalDAV server
- **nextcloud-calendar** - Calendar app for Nextcloud
- **kolab** - Groupware with calendar
- **caldav** - Calendar access protocol
- **sabredav** - CalDAV and CardDAV server
- **memacs** - Calendar data extraction
- **planner** - Task and calendar management
- **taskwarrior** - Task management with calendar
- **org-mode** - Emacs organization mode
- **todoist** - Task management with calendar
- **toodledo** - Task and time management
- **clockwork** - Calendar synchronization

## What is a Calendar System?

A calendar system is software for organizing appointments, meetings, and tasks. Calendar systems include:

- Manage appointments and events
- Recurring appointments (recurrences)
- Calendar sharing and collaboration
- Appointment reminders and notifications
- Calendar subscriptions
- Integration with email and other tools

## Application Areas

- **Personal time management**: Plan appointments and tasks
- **Team calendars**: Team appointments and appointment coordination
- **Business calendars**: Company appointments and events
- **Education**: School and university calendars
- **Events**: Event management and calendars

## Benefits of Calendar Systems

- **Overview**: All appointments in one place
- **Time savings**: Automation and reminders
- **Collaboration**: Share and collaborate on calendars
- **Integration**: Connection with other tools
- **Synchronization**: Synchronization across devices
- **Mobile access**: Access appointments anywhere

## Selection Criteria

When choosing a calendar system, consider the following criteria:

- **Features**: Which features are required?
- **Integration**: How well does the system fit into the existing infrastructure?
- **Synchronization**: Synchronization across devices
- **Ease of use**: How user-friendly is it?
- **Security**: Data protection and security
- **Open Source**: Is the system open source?

## Related Categories

- [Project Management](../../suites/projectmanagement/) - Project management
- [Helpdesk](../helpdesk/) - Support and ticket systems
- [Contact/CRM](../people/) - Contact management

## Quick Start

1. **Select calendar system**: Choose a system based on requirements
2. **Installation/Account**: Install system or create account
3. **Configuration**: Customize and configure the system
4. **Import appointments**: Import existing appointments
5. **Integration**: Integration with other tools

## More Information

Further information can be found in the documentation of individual calendar systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (6), by function, nothing copied (ADR 0012/0013):

- [DAViCal](frontends/davical/index.md) — DAViCal is a CalDAV/CardDAV server written in PHP on PostgreSQL — a lean, protocol-faithful self-hosted calendar/contact store with web administration.
- [Google Calendar](frontends/google-calendar/index.md) — Google Calendar (calendar.google.com) is Google's calendar service: a web interface plus apps for Android, iOS, Wear OS and Apple Watch, coupled with Gmail, Meet, Tasks and (with a premium subscrip…
- [Merkuro Calendar](frontends/merkuro/index.md) — Merkuro Calendar is the **modern calendar client of the KDE desktop environment** (Qt 6/QML/Kirigami, convergent on desktop and Plasma Mobile).
- [Nextcloud Calendar](frontends/nextcloud-calendar/index.md) — The calendar app of the Nextcloud server: a web interface (Vue 3 + FullCalendar) above the CalDAV backend (sabre/dav) of the Nextcloud server.
- [Outlook calendar](frontends/outlook-calendar/index.md) — The calendar component of the Microsoft Outlook line: web app (outlook.com / Outlook on the web), the new and the classic Outlook for Windows, Outlook for Mac and iOS/Android — data in the mailbox …
- [GNOME Planner](frontends/planner/index.md) — Planner is the project planner on GNOME (app ID `app.drey.Planner`): tasks with start/finish, work, costs and dependencies (FS/SS/FF/SF with lag), resources with their own working calendars, critic…

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
