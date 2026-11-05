# Messenger — Contract (draft 0.1)

The interface between `fs-messenger` and every frontend (ADR 0021). **Draft**, not compiled yet.
The schema file lives for now in the docs repo under `temp/contracts/messenger.capnp`; it moves to
the `fs-messenger` repository when that exists (ADR 0017).

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

## Open

- shared `common.capnp` (Uuid, Timestamp, Cursor, Problem, Blob) for all programs
- generation of JSON / CLI / MCP from the schema
- contacts and calendar are used through their own programs' contracts, not duplicated here
