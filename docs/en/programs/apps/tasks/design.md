# Tasks — design

**Status: proposal (2026-11-06).** Back to the [overall plan](../roadmap.md) · [requirements](requirements.md).

## Idea

A person wants to know what to do next. A board, a list and a timeline are ways of seeing that, so they are views of one
program, not programs themselves. This replaces the earlier plan for `fs-kanban` and `fs-timeline`.

- **One program, personal or for a group.** A task's owner is a person or a group, and can change. Nothing is decided up front.
- **One task, several contexts.** The same task can appear on a project board, on my personal list and in the calendar.
- **The calendar and tasks share one object.** `fs-calendar` already implements JSCalendar `Task`. We propose moving it
  into a shared crate, and `fs-tasks` becomes its owner.

`fs-projectmanagement` is a suite on top: tasks, history, resources, surveys, whiteboard, wiki.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Task | JSCalendar 2.0 `Task` | [Projects standards](../../../data/projects/standards.md) |
| Dependencies | RFC 9253 | "blocks" and "duplicates" are a gap |
| Extended status | RFC 10051 | |
| Board, column (`List`), swimlane, limit | ❌ none | **Own specification** (candidate no. 3); first model in [projects technical](../../../data/projects/technical.md) |
| Moving a card | `Update` on `task_link`, not on the task | Moving a card on my board must not change the task for everyone |
| Link to a decision | Gap | Lets a task say why it exists; connects to `fs-surveys` |

## Open-source gaps worth closing

From the [research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/projectmanagement-landscape.md):
a decision as an object linked to tasks, one task in several scopes, and the personal and group use of the same data.
Capacity and baselines belong to [`fs-resources`](../resources/index.md).

## Patterns

| Pattern | Use |
|---------|-----|
| Repository | `TaskRepository`, `BoardRepository` over `Store` |
| Command | Moves and edits, with `apply` and `invert` for undo (ADR 0042) |
| Strategy | Mapping from column to status; ordering |
| Observer | Live updates to frontends and presence |
| Facade | `Tasks` as the single entry point of the core |

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Tasks` (root) | `capabilities()`, hands out the others |
| `Items` | `task.create`, `task.edit`, `task.assign`, `relation.create`, `label.assign` |
| `Boards` | `board.open`, `board.create`, `column.create`, `column.limit`, `card.move` |
| `subscribe` | Live changes |

Attachments go through `fs-files`, people through `fs-contacts`, groups through `fs-groups`.

## Views

Workbench `kanban-board` and a compact "my next tasks", `task-list`, and `timeline-gantt`, each usable inside other
programs. See [planned components](../../../components/planned.md).

## Open questions

1. Does the `fs-calendar` crate give up ownership of `Task`, or do both share a crate?
2. Are columns statuses? The analysed tools differ: in some, they are; in others, free lists. We propose optional mapping.
3. Time tracking: part of `fs-tasks`, or of `fs-history`? We propose recording it as history.
