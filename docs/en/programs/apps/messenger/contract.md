# Messenger — Contract (draft 0.2)

The interface between `fs-messenger` and every frontend (ADR 0021). **Draft**; compiles with `capnpc-embedded` 0.2.0 (capnp 1.4.0) + `capnpc` 0.23 (2026-11-05) — no C++ toolchain (ADR 0040).
The schema file lives in the interfaces repository: [`schema/messenger.capnp`](https://github.com/FreeSynergy/fs-interfaces/blob/main/schema/messenger.capnp) in `fs-interfaces` (ADR 0045); the owner program is `fs-messenger`.

## Why Cap'n Proto fits our idea of capabilities

Cap'n Proto RPC is **capability-based**: a frontend receives references to interfaces
(`Conversations`, `Compose`, `Rules`, …) and can only do what those references allow. That is the
technical form of "the program offers capabilities; a frontend uses them or not" (ADR 0021/0037).
The very simple frontend only ever asks for `conversations` and `compose`; the full one also for
`search` and `rules`.

## Shape

| Interface | Capabilities (requirements) |
|-----------|-----------------------------|
| `Messenger` (root) | `capabilities()` lists capability ids + contract version; hands out the others |
| `Accounts` | `account.add`, `account.remove`, `account.edit` |
| `Conversations` / `Conversation` | `conversation.list`, `conversation.open`, `conversation.pin`, `conversation.move`, `message.delete`, `message.flag`, `message.react`, `message.forward`, `message.edit`; `nextUnread` for frontend no. 1 |
| `Compose` / `Draft` | `message.send` (incl. schedule), `draft.save`, `attachment.add`, `encryptionPlan` = find an encrypted way (ADR 0018) |
| `Search` | `message.search` |
| `Rules` | rules as Sieve (optional capability) |
| `subscribe` + `Listener` | live updates: created, updated, deleted, delivery state (stored locally, ADR 0037) |

Data structures follow the storage model: `Envelope` (AS2 fields, ADR 0020), `Encryption` (ADR 0018),
`DeliveryState`, `original` as a blob (ADR 0030), sensitive categories (ADR 0029), UUIDv7 (ADR 0027).

## AIs in the contract (draft 0.2, `fs-interfaces` v0.16.0)

A `ToolCall` is what an AI wants to do or has done. It has a `revision`, raised by the engine on every change, so a late event can
never overwrite a newer state. `askedOf` names the person whose decision counts. A `ToolCallDecision` carries the `signer`, who must be
that person, and refers to a digest of the arguments, so the decision covers exactly what the person saw. Unset values never mean
something good: an unset `Encryption` is `unknown`, an unset `kind` is `unknown`. Approving is never offered to an AI (ADR 0054).

## Open

- shared `common.capnp` (Uuid, Timestamp, Cursor, Problem, Blob) for all programs
- generation of JSON / CLI / MCP from the schema
- contacts and calendar are used through their own programs' contracts, not duplicated here
