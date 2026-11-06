# Groups

`fs-groups`: belonging together, and deciding who may do what.

**Status: draft interface in [`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces) v0.3.0, code in progress (2026-11-06).** Back to the [overall plan](../apps/roadmap.md).

## Why it comes early

Tasks, contacts, surveys, files and sharing all depend on it. ADR 0037 says folder, group and mailing list are one
concept, and this program is where that concept lives. Sharing then means sharing with a group.

## Idea

- Groups can contain groups. A survey can begin in a small group and widen to a parent group.
- **A person starting alone and a group use the same programs.** Every object has an owner, a person or a group, and it
  can move from one to the other without any conversion.
- **Runs without Kanidm.** A program must work alone (ADR 0024). With Kanidm present, groups are mirrored there.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Group | AS2 `Group` | Actor, so a group can act |
| Exchange | SCIM `Group` (RFC 7643) | Only for mirroring; nesting does not carry reliably over SCIM between systems |
| Roles, hierarchy, invitations | Gap | Own specification |

## Point of truth

`fs-groups` decides which groups exist and who is in them (ADR 0055). A member Kanidm has in a mirrored group but `fs-groups`
does not is removed at the next sync.

## What we keep, what Kanidm keeps

From the [Kanidm research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/kanidm-control.md),
source read at 1.13.0-dev:

| Need | In Kanidm? | So |
|------|------------|----|
| Name, members, nesting | Yes | Mirrored |
| Tree without cycles | Accepts cycles | We enforce it |
| Type, parent, roles, own fields | No custom attributes offered | Kept here, keyed by group id |
| Invitations | No (open issue) | Ours |
| Fine-grained delegation | All or nothing | Ours |
| Federation between groups | No | Ours (ADR 0035) |

If Kanidm gains one of these, we hand it back, as stated in ADR 0047.

## Open questions

1. Must a hierarchy be a tree, or can a group have several parents? **Provisional answer, still to be confirmed by the project owner:** several parents are allowed, as a working group can belong to two departments, and cycles are refused.
2. Who may widen a survey to a parent group: its initiators, or the parent group?
3. How do decisions about group membership work: by appointment, or by a vote using `fs-surveys`?
