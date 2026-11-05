# Projects – technical explanation

## Principle: structure narrow, tasks reused

- **Task data stays JSCalendar objects in `calobj`** (table from [events/technical.md](../events/technical.md)). No second task schema.
- This domain introduces **four own, narrow models** (our own decision, open for discussion — spec candidate no. 3): `Project`, `Board`, `List`, `Relation`.

## Storage perspective

| Table | Payload | Note |
|-------|---------|------|
| `project` | JSON (own model) | references to the team and `contacts` |
| `board` | JSON | `project_id` (ULID) |
| `list` | JSON | `board_id`, `position` (sortable in-between value, our own decision) |
| `task_link` | `task_id` (→ `calobj`), `list_id`, `position` | **assignment** of a task to exactly one list (board view) — the task itself stays calendar-wise independent |
| `relation` | `from_id`, `to_id`, `kind` (enum) | relations between tasks |

## Keys and flow

- Externally: `https://<instance>/projects/<ulid>` (decision 3).
- Moving within a board = `Update` on `task_link` (not on the task!) — which is why `task.moved` is an envelope event about the assignment, not about the task (see [index.md](index.md), open point).
- Milestones: JSCalendar `Event` with `categories: ["milestone"]` (using ✅ verified fields; the convention itself is our own decision).

## Projections

| Target | Projection |
|--------|------------|
| Calendar view | milestones + task `due` from `calobj` |
| MSPDI export (✅ existence) | board/list structure ↔ MSPDI task tree; ⚠️ field mapping still to be created |
| CRM/ERP masks | project as an association to contacts |

## Open technical points

- **Positioning:** in-between values (e.g. LexoRank-like) vs. a version counter — no outside rule evidenced; needs our own decision.
- **WBS substructure:** ISO 21502 knows work breakdown as a concept (process), not as a data format; whether we allow `parent_id` on tasks (CONFLICT with the JSCalendar canon!) or represent it only via `relation` is **to be decided**. Proposal: only `relation` with `kind: "parent"`, so the JSCalendar payload stays canonical.
