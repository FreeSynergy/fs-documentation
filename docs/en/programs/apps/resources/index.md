# Resources

`FreeSynergy.Resources` (`fs-resources`) answers: **what do we have, what do we need, and who has time?**

**Status: planned, no code yet (2026-11-06).** See the [overall plan](../roadmap.md).

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

1. Are things and people's time one program? They share planning, but feel very different.
2. What from ERP belongs here? ERP needs stock, and this program needs availability.
