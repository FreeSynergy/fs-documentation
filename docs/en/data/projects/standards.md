# Projects – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** Research completed 2026-11-02.


## State 2026-11-05

Evidence: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Evidence | Role |
|----------|----------|------|
| JSCalendar 2.0 `Task` | ✅ | the task object |
| **RFC 9253** relations: `DEPENDS-ON`, `FIRST`, `NEXT`, `FINISHTOSTART`/`FINISHTOFINISH`/`STARTTOSTART`/`STARTTOFINISH` with lead/lag gap | ✅ | dependencies |
| **RFC 10051** task extensions: status `PENDING`/`FAILED`, `VSTATUS` (reason, substate), estimated duration, `TASK-MODE` | ✅ | richer task status (vendor property until JSCalendar has it) |
| JSCalendar `relatedTo` | ✅ only `first`, `next`, `child`, `parent` | no "blocks"/"duplicates" → gap |
| **ForgeFed** `TicketDependency` (ActivityPub for forges) | ✅ draft | federation-native dependency in the envelope |
| ISO 21511:2018 (WBS) | ✅ guidance only, no data format | vocabulary reference |
| schema.org `Project` | ✅ core, subtype of `Organization`; no task/status/dependency properties | export projection only |
| W6C XML Schema | not found again | dropped |
| kanban board standard | ❌ none | **own spec** (candidate no. 3) |

Reference vocabulary for relations (OpenProject): relates, duplicates, blocks, precedes/follows,
includes/partof, requires. Exports seen: Taiga JSON dump, Vikunja ZIP with `data.json`.

## Result of the standards search (2026-11-02)

| Candidate | Evidence | Assessment |
|-----------|----------|------------|
| **RFC / W3C / ISO data format for boards & tasks** | ❌ nothing found | **no open data spec** → own spec, spec candidate no. 3 |
| **ISO 21502:2020 "Project, programme and portfolio management — Guidance on project management"** (ISO/TC 258) | ✅ existence evidenced | **process guide, not a data format**; useful as a role/vocabulary reference |
| **MSPDI — Microsoft Office Project 2007 XML Data Interchange Schema (`mspdi_pj12.xsd`)** | ✅ existence evidenced | de-facto XML import/export (tasks, calendars; durations in tenths of a second); not an open standard |
| **W6C XML Schema** | ⚠️ still unevidenced | do not use until evidenced |

## Reused building blocks (✅)

| Building block | Evidence | Use |
|----------------|----------|-----|
| **JSCalendar `Task`** (RFC 8984) | ✅ | canonical task object — see [events/standards.md](../events/standards.md) for the field list |
| **JSCalendar `Event`** (RFC 8984) | ✅ | milestones |
| **ActivityStreams 2** (W3C) | ✅ | envelope for `task.moved` etc. (decision 2) |

## Further candidates (⚠️ unverified, deliberately not reloaded)

| Candidate | Status |
|-----------|--------|
| W3C Organization Ontology (`vocab-org`) | ✅ URL verified, **content unread** — building block for roles/hierarchy |
| schema.org `Project` | ⚠️ existence not verified |

## Our own decision (open for discussion — spec candidate no. 3)

Small, open core models: `Project`, `Board`, `List`, `task_link`, `Relation` with the enum `kind ∈ {blocks, duplicates, references, parent}` (enum rule: lowercase, singular). **Extend instead of invent (decision 5):** task fields are not duplicated; project fields live only in the structure models.
