# Resources

## In short

Resources keeps what a group has and what it needs: things, rooms, material in stock, and people's time. You can reserve something for a stretch of time, post a need, or post an offer. It answers the question: what do we have, what do we need, and who has time? Two people cannot book the same room by accident, and nobody else can take your time.

**Command:** `fs-resources`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- Your own capacity, meaning your time, belongs to you. Only you decide what is shown and allocated. What a group sees is a share you give.
- A reservation is checked in one step, so two people cannot overbook together.
- Material that is used up is counted as used up.
- Things and people's time are one program on purpose, because they share planning.
- No standard for a resource model was found. Resources owns its interface, `resources.capnp` in `fs-interfaces`, a draft marked provisional.

## Where it stands today

Latest tag: `v0.0.1`. There is **no window and no server yet**. A server must refuse your capacity calls until it knows who is asking.

Today it handles things, rooms and material, with stock worked out from what has been finished. Reservations cannot overbook, and finishing one frees the thing or uses up the material. It can show the free time of a thing over a range, keep your own capacity, allocations and shares to groups in a store of its own, and work out the load of a group using the Groups interface. Needs and offers work, and accepting an offer makes the reservation. It has 115 tests and was checked by an independent reviewer over four rounds.

What is not there yet: costs, support for MSPDI (a project plan file format), and skills. There are no warehouses, batches or valuation. This is availability, not an ERP.

`FreeSynergy.Resources` (`fs-resources`) answers: **what do we have, what do we need, and who has time?**

**Status: [core](https://github.com/FreeSynergy/fs-resources) v0.0.1, no GUI; provisional draft interface (2026-11-06).** See the [overall plan](../roadmap.md).

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
