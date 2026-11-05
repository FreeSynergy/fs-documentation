# Messages

E-mail, chat, messenger and comments — **one** domain, because for people a message is a message
(ADR 0018). Encrypted only. Stored as **original + AS2 envelope + activity log** (ADR 0020).

## Standards in this domain (details: [standards.md](standards.md))

| Kind | Content | Encryption |
|------|---------|------------|
| chat / messenger | MIMI content (draft -10, pinned) | MLS (RFC 9420) |
| e-mail | original MIME + JMAP `Email` fields (RFC 8621) | OpenPGP v6 (RFC 9580), header protection (RFC 9788), Autocrypt |
| Matrix | Matrix spec v1.19 events (connector) | Megolm, MLS planned upstream |
| comments | AS2 `Note` / Web Annotation | as the resource |

Envelope for all: AS2 `Note` with `context` (conversation), `inReplyTo`, `attachment`, audience fields.

## Open points

- Own-spec candidates: delivered/read state, expiry, encrypted attachments, edit identity, thread
  profile, message-ID aliases, reactions/edits for e-mail ([standards.md](standards.md))
- Incoming unencrypted messages: mark or quarantine (ADR 0018)

## See also

- [standards.md → Activities](../standards.md)
- [comments (proposed domain)](../index.md) — for text-fragment tags/comments the **W3C Web Annotation Model** (✅) is the right standard
