# Kanban — design

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

## Idea

The board is a view; the work is a task. **A card is a JSCalendar `Task`**, the type `fs-calendar` already implements.
The board only adds what tasks do not have: columns and order.

`fs-kanban` is a program of its own, as requested. A later `fs-projectmanagement` adds Gantt charts, time tracking and
budgets, and uses the kanban workbench rather than building another board (ADR 0037).

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Card | JSCalendar 2.0 `Task` | Details in [projects standards](../../../data/projects/standards.md) |
| Dependencies | RFC 9253 | "blocks" and "duplicates" are a gap |
| Extended status | RFC 10051 | |
| Board, column (`List`), swimlane, WIP limit | ❌ none | **Own specification** (candidate no. 3 in [standards](../../../data/standards.md)); first model in [projects technical](../../../data/projects/technical.md) |
| Moving a card | `Update` on `task_link`, not on the task | Decided in [projects technical](../../../data/projects/technical.md); AS2 `Move` is an open candidate. Being in the activity log, history comes for free |
| Order in a column | gap | `position` as an in-between value, so one move changes one object and two people rarely conflict |

Column and task status are separate things. A board can map columns to a status (`Done` → `completed`), but a board
without that mapping must work too. Otherwise, moving a card on one person's board would change the task for everyone.

## Reuse between programs

How a task gets from one program to the other follows the lending model (ADR 0019 and following): `fs-hub` carries a
live reference, and the owning program keeps the object. We propose moving `Task` from `fs-calendar-core` into a small
shared crate, rather than having two implementations of the same standard.

## Patterns

| Pattern | Use |
|---------|-----|
| Repository | `BoardRepository`, `CardRepository` over `Store` |
| Command | Moves and edits as commands with `apply` and `invert`, for undo (ADR 0042) |
| Strategy | Mapping from column to status; card ordering |
| Observer | Live updates to frontends |
| Facade | `Kanban` as the single entry point of the core |

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Kanban` (root) | `capabilities()`, hands out the others |
| `Boards` | `board.open`, `board.create`, `board.archive` |
| `Board` | `column.create`, `column.move`, `column.limit`, `card.create`, `card.move` |
| `Card` | `card.edit`, `card.assign`, `label.assign`, `comment.add`, `attachment.add`, `relation.create` |
| `subscribe` | Live changes |

Attachments go through `fs-files`, comments follow the messages model. People come from `fs-contacts`. None of these
are duplicated here.

## Components

Workbench `kanban-board`, with a compact variant showing one column or "my cards" inside other programs. The widgets
`board-column` and `task-card` build on `sortable-list`. See [planned components](../../../components/planned.md).

## Stages

1. Core: boards, columns, cards as tasks, moves, undo, tests; contract; board specification draft.
2. Workbench, first simple frontend, cards visible in `fs-calendar`.
3. Labels, comments, attachments, WIP limits, swimlanes, filters.
4. Live collaboration, automation rules.

## Open questions

1. **Where do the frontends live?** Trello, Wekan and Planka are documented under `projectmanagement`. ADR 0017 would
   suggest moving the board programs to `kanban`. We propose leaving them for now, since a move is only cosmetic.
2. **Personal boards or shared boards first?** We propose personal first, then shared, since sharing needs the common
   sharing model (see [files](../files/design.md#open-questions)).
3. **Column-to-status mapping:** automatic by default, or opt-in? We propose opt-in.
