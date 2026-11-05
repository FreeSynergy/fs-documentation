# Projects

Boards, lists, task relations, milestones, roles in the project. This is the domain with the **biggest regular gap**: ❌ no established standard found (candidates W6C XML Schema, MSPDI, PMI WBS are ⚠️ unevidenced — see [standards.md](../standards.md)).

## Inventory

| Piece | Evidence | Role in FreeSynergy |
|-------|----------|---------------------|
| ❌ project/board structure | ❌/⚠️ | **our spec candidate no. 3** (after block/document and WoT) |
| **ISO 21502:2020** (ISO/TC 258) | ✅ existence evidenced 2026-11-02 | process guide for project management, **not a data format** — role/vocabulary reference |
| **MSPDI (`mspdi_pj12.xsd`)** | ✅ existence evidenced 2026-11-02 | de-facto XML import/export (MS Project); not an open standard |
| **JSCalendar `Task`** | ✅ | tasks as the canonical task object (reused from [events/](../events/index.md)) |
| **W3C Organization Ontology** (`vocab-org`) | ✅ URL verified, content unread | role/hierarchy building block for project memberships |
| **schema.org `Project`** | ⚠️ existence not verified | evidence before use |

## Provisional structure idea (our own decision, open for discussion)

`project` (relation to `Team`/`Contact`) → `board` → `list` → `task` (JSCalendar) with relations (blocks, duplicates) and `milestone` (JSCalendar `Event`). Relation types as enums following our enum rule.

## Open points

- Standards search completed (2026-11-02): no open RFC/W3C data spec found; details in [standards.md → follow-up research](../standards.md) — do not research again
- Order of the spec work: block/document first, because tasks often reference blocks
- Webhook/automation events (`task.moved`) are an envelope topic, not a domain model

## See also

- [standards.md → What we have to invent](../standards.md)
- [events/](../events/index.md) (task standard), [model overview](../models.md)
