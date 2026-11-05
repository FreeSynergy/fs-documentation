# Projects – description

**What this domain is:** boards, lists, milestones, project roles and **relations between tasks** (blocks, duplicates, references). This is our domain with the **biggest regular gap**: ❌ there is no open RFC/W3C/ISO **data standard** for it (research completed 2026-11-02, evidence in [standards.md → follow-up research](../standards.md)).

**What it covers:**

- `project` as the wrapper (relation to the team and the contacts involved)
- `board` → `list` → position/order
- `relation` between tasks: `blocks`, `duplicates`, `references` (our own enum decision, open for discussion)
- `milestone` (realised as a JSCalendar `Event`)
- roles in the project (owner, contributor, observer)

**What it does NOT cover:** the task **data** itself. A task is an unaltered JSCalendar `Task` object from [events/](../events/index.md). This domain only adds the structure around it.

**Differentiation:**

| Topic | Where it lives |
|-------|----------------|
| Task content (title, due date, progress) | [events/](../events/index.md) (JSCalendar, ✅) |
| People and organisations | [contacts/](../contacts/index.md) |
| Appointments/milestones in the calendar | [events/](../events/index.md) |
| Process management (phases, responsibility) | ISO 21502 is a **process guide, not a data format** (✅ evidenced 2026-11-02) |

**Standard status:** own spec = **spec candidate no. 3** (after block/document and WoT). Import/export counterparts: MSPDI (`mspdi_pj12.xsd`, ✅ existence, de-facto format).
