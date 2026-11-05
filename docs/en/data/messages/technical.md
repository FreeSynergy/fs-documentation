# Messages – technical explanation

Decisions: ADR 0018 (one messenger, encrypted only, connectors), ADR 0019/0020 (`fs-store`, envelope +
content + log), ADR 0027 (UUIDv7). Evidence: [standards.md](standards.md).

## Principle: original + envelope

Every message is stored **as received** (the original, possibly signed) **plus** a normalised envelope:

| Part | Chat (MIMI) | E-mail | Matrix |
|------|-------------|--------|--------|
| original | MIMI content (CBOR) | raw MIME (RFC 5322) | event JSON |
| envelope `type` | `Note` | `Note` (`name` = subject) | `Note` |
| `mediaType` of the payload | MIMI content type per draft -10 | `message/rfc822` | Matrix event |
| `context` (conversation) | MIMI room / topic | JMAP `threadId` | room / `m.thread` root |
| `inReplyTo` | MIMI reply id | `In-Reply-To` header | `m.in_reply_to` |
| extracted index fields | sender, body text | JMAP `Email` fields (from, to, subject, sentAt, textBody, attachments) | sender, body |

Signatures stay verifiable because the original is never rewritten.

## Storage (ADR 0020)

- `id` = UUIDv7 (ours). **Alias table** `message_alias(id, scheme, external_id)` for `Message-ID`, Matrix `event_id`, MIMI id — gap, see standards.
- Extracted columns: `id`, `context`, `in_reply_to`, `attributed_to`, `published`, `updated`, `encryption`, `kind` (`mail`/`chat`/`comment`), full-text fields.
- **Encryption state** per message, vendor property `freesynergy.net:encryption` (ADR 0028): `mls` · `openpgp` · `megolm` · `transport-only` · `none`. Outgoing `transport-only`/`none` is refused or asked about (ADR 0018); incoming is **marked**, with a link to the library guide on encrypting mail (ADR 0031).
- Content stored encrypted at rest (ADR 0024); sensitive marking applies (ADR 0029).

## Log mapping (AS2 activities)

| Action | Activity | MIMI | Matrix | E-mail |
|--------|----------|------|--------|--------|
| send | `Create` | message | `m.room.message` | SMTP/JMAP submission |
| edit | `Update` (id of the **first** version stays) | edit (replaces) | `m.replace` | — (gap) |
| delete | `Delete` + tombstone | empty body, first-version id | redaction | move to trash / expunge |
| react | `Like` / `EmojiReact`, undo via `Undo` | reaction | `m.annotation` | — (gap) |
| read | `Read` | message-status | `m.receipt` | RFC 9007 MDN |
| delivered | gap | message-status | — | DSN |

## Threading

- `context` = conversation (room, mail thread, comment thread); `inReplyTo` = direct parent.
- Display flat (chat) or as a tree (comments, mail) from the same fields.

## Projections

| Target | Projection |
|--------|------------|
| Frontends | Cap'n Proto (ADR 0021) — frontends never see protocols |
| Outgoing mail | MIME + OpenPGP v6 + RFC 9788 header protection + Autocrypt |
| Matrix | `matrix-sdk` connector |
| MIMI | `mimi-content` + OpenMLS |
| Search | full text over extracted fields |

## Open technical points

- Edit history display (all versions from the log, or only the last?)
