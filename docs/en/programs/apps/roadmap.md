# Next programs — roadmap

**Status: under review (2026-11-06).** We are rethinking the overall structure before continuing, so the list, the
order and the split into programs below may change. No code exists yet for any program on this page. This page says what
we plan and why, so that anyone can see where we are heading and help.

## Decided so far by the project owner

- **RustFS** is an optional backend for `fs-files`. We hope to work together with the project, including online delivery.
- **`fs-projectmanagement` is a suite**, combining kanban, surveys, timeline, whiteboard, wiki and further modules.
  A cost module may join after looking at what such programs do and need.
- **Workbenches and programs must not be confused.** Whether the gallery is a program, or a view of `fs-files`, is open.
- **New requirements:** `fs-groups` (group management, nested groups, working with Kanidm through SCIM) and `fs-timeline`.
- **Surveys** support several decision types, such as consensus and majority, and can start in a small group and widen
  to parent groups. The democracy suite is as important as project management, and surveys are part of both.
- **Charts** are many and varied, and are needed by surveys, project management and others.
- **Streaming** is about distribution: record once, publish to YouTube, Odysee and other platforms at once, live and not
  live, without a SaaS provider, plus a recording tool far simpler than OBS and management of videos.

The sections below predate these decisions and will be reworked once the overall plan is agreed.

## What already exists

These repositories are public since 2026-11-06. All are data cores without a GUI so far, refactored to ADR 0043.

| Repo | What it is | Tests |
|------|------------|-------|
| [`fs-store`](https://github.com/FreeSynergy/fs-store) | Object store, version 0.2 | 37 |
| [`fs-hub`](https://github.com/FreeSynergy/fs-hub) | Shares objects between programs; contacts and calendar already share data through it | 9 |
| [`fs-contacts`](https://github.com/FreeSynergy/fs-contacts) | Contacts core | 21 |
| [`fs-calendar`](https://github.com/FreeSynergy/fs-calendar) | Events and tasks (JSCalendar), including the `Task` that `fs-tasks` would build on | 45 |
| [`fs-maps`](https://github.com/FreeSynergy/fs-maps) | Maps core | 30 |
| [`fs-wiki`](https://github.com/FreeSynergy/fs-wiki) | Text core `fs-text`; round-trips all 1321 files of `docs/en` with none unstable | 46 |
| [`fs-capnpc`](https://github.com/FreeSynergy/fs-capnpc) | Cap'n Proto compiler in pure Rust (`capnp-compiler` 0.1.0), not yet on crates.io | 14 of 14 reference schemas identical |

Known limit: these repositories still refer to `fs-store` by a local path, so they do not build elsewhere until that is
switched to git dependencies. Details are in each repository's `DESIGN.md`.

## The programs

| Program | Repo | What it does | Design | Requirements | Effort |
|---------|------|--------------|--------|--------------|--------|
| Files | `fs-files` | Store, organise and share any file. The other programs keep their bytes here | [design](files/design.md) | [provisional](files/requirements.md) | M |
| Kanban | `fs-kanban` | Boards, columns, cards. A card is the same task the calendar shows | [design](kanban/design.md) | [analysed](kanban/requirements.md) | M |
| Surveys | `fs-surveys` | Build surveys, collect answers, read results, optionally anonymous | [design](surveys/design.md) | [provisional](surveys/requirements.md) | M |
| Gallery | `fs-gallery` | Photos and videos: albums, timeline, places, sharing | [design](gallery/design.md) | [analysed](gallery/requirements.md) | M |
| Whiteboard | `fs-whiteboard` | Infinite canvas for drawing, shapes and notes, together | [design](whiteboards/design.md) | [analysed](whiteboards/requirements.md) | L |
| Streaming | `fs-streaming` | Receive, forward and record live media | [design](streaming/design.md) | [analysed](streaming/requirements.md) | L (stage 1: M) |

*Analysed* means derived from the documented frontends. *Provisional* means we have not analysed any frontends for
this category yet, so the list comes from our architecture and must be checked against real programs (ADR 0013).
Effort compares these programs with each other; it is not a time estimate.

The [new components](../../components/planned.md) these programs need are listed on their own page.

## Proposed order

```text
fs-store, fs-hub, fs-calendar (exist)
   ├── fs-files ──┬── fs-gallery
   │              ├── fs-streaming (recordings land in fs-files)
   │              └── fs-whiteboard (embedded images)
   ├── fs-kanban (cards are fs-calendar tasks)
   └── fs-surveys
```

1. **`fs-files`**: the gallery, the whiteboard and streaming all store their bytes here, so it comes first.
2. **`fs-kanban`**: tasks already exist in `fs-calendar`, so this shows quickly that two programs share one object.
   It also produces `sortable-list`, a component most other programs want.
3. **`fs-surveys`**: mostly reuses existing field components. Its hard part is anonymity, not the interface.
4. **`fs-gallery`**: needs `fs-files`.
5. **`fs-whiteboard`**: the largest interface task, with an infinite canvas and live collaboration. It needs its own
   data specification, since no standard exists.
6. **`fs-streaming`**: stage 1 forwards media without decoding it, which is manageable. Stage 2 needs video encoding,
   which is the hard part. See the [streaming design](streaming/design.md).

Whiteboard, surveys and kanban are the priorities. Kanban and surveys can start in parallel with `fs-files`, as they
do not depend on it. The whiteboard is late only because of its size; its specification can start at any time.

## What every program has in common

These rules are already decided and apply to all six.

| Rule | Decision |
|------|----------|
| Runs alone, shares data with others | ADR 0017, 0019 |
| Data in standards, AS2 envelope; gaps get our own specification | ADR 0014, 0020 |
| Own `fs-store`, object-level sync through `fs-hub` | ADR 0019 |
| Cap'n Proto contract first; JSON, CLI and MCP are generated from it | ADR 0021 |
| At least one workbench plus a compact variant, usable inside other programs | ADR 0037 |
| Gestures only in the frontend, not in components | ADR 0037 |
| Up to four reference frontends | ADR 0038 |
| Design patterns, interfaces first, small files, documentation | ADR 0043, [coding rules](https://github.com/FreeSynergy/fs-documentation/blob/main/conventions/coding.md) |
| Licence `MIT OR Apache-2.0` | ADR 0016 |

## Work steps per program

1. Check requirements against the frontends (for provisional ones, analyse frontends first).
2. Write the data specification where a standard is missing.
3. Write the Cap'n Proto contract.
4. Build the core without a GUI, with tests, on `fs-store`.
5. Document the components and build them on Blinc.
6. Build the workbench, the compact variant and the first reference frontend ("very simple").

The docs change in the same step as the work, including the status on this page.

## Open decisions

These are decisions for the project owner. Each design page holds the details and any further questions.

| # | Question | Recommendation |
|---|----------|----------------|
| 1 | Is RustFS the storage engine, or one optional backend for `fs-files`? | Optional backend, because it is a separate server ([details](files/design.md#storage-backends)) |
| 2 | Is the order above right? | Yes, as proposed |
| 3 | Does kanban stay a separate program from project management? | Yes; `fs-projectmanagement` builds on its workbench later |
| 4 | Whiteboard collaboration: per-object sync or a CRDT? | Per-object first, behind an interface ([details](whiteboards/design.md#live-collaboration)) |
| 5 | How strong must survey anonymity be? | Two levels now; binding votes belong to the democracy suite ([details](surveys/design.md#anonymity)) |
| 6 | Streaming: is a C-based encoder acceptable for stage 2? | Decide when stage 2 starts ([details](streaming/design.md#stage-2-is-the-hard-part)) |

## Sources for the technology named here

Versions were read from crates.io and GitHub on 2026-11-06. A listed crate is a **candidate**, not a decision. None
has yet been checked for C dependencies, and each must pass ADR 0015 and ADR 0026 before use.
