# Tasks

## In short

Tasks keeps what you, or your group, have to do. Each task can have a due date, a status, labels and links to other tasks. It answers one question: what do I, or we, do next?

**Command:** `fs-tasks`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- A task follows the open JSCalendar standard (RFC 8984). This program owns that standard for tasks, so the calendar and every other program reach tasks through one interface instead of keeping their own idea of a task.
- Lists, status views and, later, boards and timelines are different ways of looking at the same tasks.
- Your tasks import and export as iCalendar (VTODO), and the original text is kept.
- Tasks marked sensitive are left out of exports unless you release them by name.
- A task can start with you alone and be shared later.

## Where it stands today

Latest tag: `v0.0.2`. You can create, edit, assign, label, relate, list and delete tasks, and find them by due date range, progress, label, or a word in the title or description. Import and export of iCalendar tasks work. Other programs are told when a task changes, and an overwrite is refused if someone else changed the task meanwhile. A small server offers all of this over a local socket, and a first, provisional window shows a list and a status view. The calendar already shows tasks through this interface.

Not there yet: real boards (the status view is not a board; moving a card changes the task's status for everyone), repeating tasks beyond keeping them, assigning people, relations, checklists, comments, attachments and reminders in the window, and undo. The window reads the data directly, and there is no sign-in yet. The interface is a draft with one user (the calendar).

## Planned facets

Facets are parts of a program that look like apps of their own ([ADR 0061](../../../decisions/0061-facetten.md)). Each gets its own command, a link to `fs-tasks` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Proposed, not built:

- To-dos: tasks as simple lists of things to do.
- Tickets: tasks as requests that someone works through.

`FreeSynergy.Tasks` (`fs-tasks`) answers one question: **what do I, or we, do next?** Kanban boards, lists and timelines
are different ways of looking at the same tasks.

The [code lives here](https://github.com/FreeSynergy/fs-tasks). See the [overall plan](../roadmap.md).

- [Design](design.md)
- [Requirements](requirements.md), analysed from eight project tools, written when this was still planned as `fs-kanban`

Frontends analysed so far are under [project management](../../suites/projectmanagement/index.md).
