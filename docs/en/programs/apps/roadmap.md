# The overall plan

**Status: draft (2026-11-06), agreed in outline by the project owner.** It says what we plan and why, so anyone can see
where we are heading and help. Why we do this at all: see the [manifesto](../../manifesto.md).

## How everything is ordered

Everything is sorted by purpose, not by what a tool looks like. Four questions decide where something belongs:

| Question | Then it is a |
|----------|--------------|
| Does it have its own data, with its own rules? | **Program** |
| Does it put programs together for a purpose? | **Suite** |
| Does it show something without knowing what the data means? | **Component** (a **workbench** is a large component) |
| Is it one way of using a program? | **Frontend**, possibly with built-in filters |

Every topic has one [interface](../../interfaces/index.md), the same for every provider. **Each standard has exactly one
owning program, so there is one point of truth,** and other programs reach it through that interface.

Whether views like the gallery or kanban should *also* be offered as stand-alone programs is still open. They can
appear as stand-alone apps by being frontends, without having their own data.

## Programs

| Purpose | Program | Status |
|---------|---------|--------|
| Keep objects, share them between programs | [`fs-store`](https://github.com/FreeSynergy/fs-store), [`fs-hub`](https://github.com/FreeSynergy/fs-hub) | Exist |
| Sign in, system access | [identity wrapper](../platform/identity.md) over Kanidm | Planned |
| Belong together, decide who may do what | [`fs-groups`](../platform/groups.md) | Draft interface, code in progress, **new** |
| Keep and find anything | [`fs-files`](files/design.md) | Provisional draft interface, code in progress |
| Know who someone is, with roles | [`fs-people`](https://github.com/FreeSynergy/fs-people) | Core with roles and draft interface, no GUI |
| Be somewhere at some time | [`fs-calendar`](https://github.com/FreeSynergy/fs-calendar) | Core exists, no GUI |
| Know where | [`fs-maps`](https://github.com/FreeSynergy/fs-maps) | Core exists, no GUI |
| Write and know together | [`fs-wiki`](https://github.com/FreeSynergy/fs-wiki) (crate `fs-text`) | Core exists; first workbench in [`fs-components`](https://github.com/FreeSynergy/fs-components) v0.1.0, app not finished |
| Say something to someone | [`fs-messenger`](messenger/contract.md) | Draft contract |
| Know what to do next | [`fs-tasks`](https://github.com/FreeSynergy/fs-tasks) ([design](tasks/design.md)) | Core exists, no GUI; draft interface |
| Remember what I or we did | [`fs-history`](history/index.md) | Planned, **new**; possibly a view |
| Know what we have and need | [`fs-resources`](resources/index.md) | Planned, **new** |
| Ask, and decide together | [`fs-surveys`](surveys/design.md) ([repo](https://github.com/FreeSynergy/fs-surveys)) | Draft interface, core in progress |
| Think visually | [`fs-whiteboard`](whiteboard/design.md) | Planned |
| Talk to AI, and work with every program through it | [A messenger frontend](assistant/index.md), not a program of its own | Idea |
| Show something, and bring it everywhere | [`fs-streaming`](streaming/design.md) | Planned |

[`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces) holds the contracts, [`fs-release`](https://github.com/FreeSynergy/fs-release) the [release](../platform/releases.md) workflows, and `fs-capnpc`, our Cap'n Proto compiler in pure Rust, supports them all. Details of what exists are in each repository's `DESIGN.md`.

## Views (workbenches, not programs)

| View | Shows data from |
|------|-----------------|
| Gallery, video library, music | `fs-files` |
| Kanban board, task list | `fs-tasks` |
| Timeline (Gantt) | `fs-tasks`, `fs-calendar` |
| Timeline of what happened | `fs-history` |
| Result dashboards | `fs-surveys`, others, using [charts](../../components/charts.md) |

## Suites

A program can belong to several suites.

| Suite | Contains |
|-------|----------|
| Groupware | People, calendar, wiki, maps, messenger |
| **Project management** | Tasks, history, resources, surveys, whiteboard, wiki, groups; possibly costs |
| **Democracy** | Surveys, groups, wiki, messenger, tasks, resources |
| Media | Files (with gallery), streaming |
| ERP, CRM, others | Later, sharing resources, tasks and people |

## Order

```text
1. Foundation     manifesto, interface catalogue, sharing model
                  fs-groups + identity wrapper, then fs-files
2. Components     shared ones first, plus charts; each built when the next program needs it
                  GUIs for the existing cores: people, calendar, maps, wiki
3. Work           fs-messenger with the AI frontend (we want to use it soon), GUI for fs-tasks, fs-history, then fs-surveys, fs-resources, fs-messenger
4. Together       live presence, fs-whiteboard
5. Suites         project management, democracy
6. Media          gallery frontends, fs-streaming
```

**Components come first, then the program.** We document components early, so we know what we have. We build each only
when the next program needs it, since components without a real user tend to get their interface wrong.

## What makes this worth doing

Findings from the [research notes](https://github.com/FreeSynergy/fs-documentation/tree/main/temp/research) of 2026-11-06:

- **Decisions as first-class objects.** No project tool we looked at treats a decision or vote as an object linked to tasks.
- **A survey that widens.** No tool found lets a poll start in a small group and move to its parent group, results carried over.
- **One task, several contexts.** Personal and group use are separate products elsewhere.
- **Capacity planning and baselines.** Open-source tools keep these behind paid plans or lack them.
- **Systemic consensing.** Described as a method, but no open-source tool found.
- **Simple, multi-platform, self-hosted streaming.** No open tool offers all three together.

The closed-source products were checked only partly; each note lists what was verified.

## Open decisions

| # | Question | Recommendation |
|---|----------|----------------|
| 1 | Should views also be stand-alone programs? | Discuss later |
| 2 | Prompt for export on leaving? | Postponed, not forgotten ([details](files/design.md#saving-and-exporting)) |

**Decided on 2026-11-06:** one `fs-people`, each person with several [roles](../../interfaces/roles.md); codecs are outsourced, open ones first; every existing core is reworked against the interface catalogue, and all interfaces live in
[`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces). Live collaboration merges properties with a logical clock and uses a CRDT only for shared text (`loro` and
`yrs` to be compared when needed).

## What is decided

ADR 0044 to 0054 in [`conventions/decisions`](https://github.com/FreeSynergy/fs-documentation/tree/main/conventions/decisions).
