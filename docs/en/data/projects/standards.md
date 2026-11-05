# Projects – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** Research completed 2026-11-02.

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
