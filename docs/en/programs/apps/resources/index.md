# Resources

`FreeSynergy.Resources` (`fs-resources`) answers: **what do we have, what do we need, and who has time?**

**Status: [core](https://github.com/FreeSynergy/fs-resources) v0.1.0, no GUI; provisional draft interface (2026-11-06).** See the [overall plan](../roadmap.md).

## Why

Projects need people and things. So does a democracy project at larger scale, and ERP later. The
[research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/projectmanagement-landscape.md) shows
capacity planning and full baselines are paid features or missing in the open-source tools examined, so this is a real gap.

## What it covers

| Purpose | Notes |
|---------|-------|
| Things: equipment, rooms, material | Lending and reservations relate to the calendar |
| People's time and capacity | Sensitive: the person should see and control it |
| Needs and offers | "This project needs 3 tents", and who can give them |

## Costs

A costs module may join later. The research suggests it needs three separate values: planned, committed and actual. We
will analyse what such programs do before deciding where it lives.

## Standards

No open standard found for a resource model. MSPDI is a candidate for import and export, but its fit is an assumption so
far. To be researched.

## Open questions

Answers so far are provisional. Details: [`DESIGN.md`](https://github.com/FreeSynergy/fs-resources/blob/main/DESIGN.md).

1. Things and people's time are **one program**.
2. Availability uses a plain stock number. Nothing else from ERP belongs here.
3. Costs stay out until they are analysed.

## Sharing hours with a group means trusting its members

Sharing is off by default and is set per group. A group only sees totals, but **totals do not protect anyone from a member who tries.** A member
can learn the exact hours of someone who is absent in one of two weeks, by changing their own capacity in small steps. A review
did this successfully. Rounding does not help. So share only with people you trust.

**Known open point:** a fault while accepting an offer, followed by an action on the reservation and a repeated decision, can leave offer and
reservation disagreeing.
