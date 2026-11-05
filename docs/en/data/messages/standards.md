# Messages – standards

> Evidence: [standards.md](../standards.md) and `temp/research/messages-standards.md` (2026-11-05) —
> do not reload what is marked ✅. One program covers e-mail, chat and messengers, encrypted only
> (ADR 0018); always the newest viable standard (ADR 0026).

## Envelope and log (all message kinds)

| Standard | Evidence | Role |
|----------|----------|------|
| **ActivityStreams 2.0 (W3C Recommendation 2017)** | ✅ | envelope (ADR 0020): `id`, `type`, `attributedTo`, `to`/`cc`/`bto`/`bcc`, `published`, `updated`, **`context`** (= conversation), **`inReplyTo`**, **`attachment`**, `mediaType` |
| AS2 activities | ✅ | log: `Create`, `Update` (edit), `Delete`, `Like` + `Undo` (reaction), **`Read`** (read receipt) |
| FEP-c0e0 `EmojiReact` | ✅ draft | emoji reactions beyond `Like` |
| FEP-7888 / FEP-171b (context, conversation containers) | ✅ drafts, competing | inform our thread profile (gap below) |
| "MLS in ActivityPub" (W3C Social Web CG task force) | ✅ unofficial report | encrypted payload as `message/mls`; inner limited AS2 profile (`urn:uuid` ids, `Create/Update/Delete/Like/Undo/Read`) — the model for our envelope around encrypted content |
| W3C Social Web WG | ✅ chartered Jan 2026 | watch: next AS2/ActivityPub revision |

## Content per message kind

| Kind | Content standard | Evidence | Rule |
|------|------------------|----------|------|
| **Chat / messenger** | **MIMI content format** `draft-ietf-mimi-content-10` (CBOR, inside MLS) + `draft-mahy-mimi-message-status-02` (delivered/read) | ✅ drafts, 2026-11-02; Rust: `phnx-im/mimi-content` | pinned to -10 until RFC; covers reply, topic/thread, reactions, edits, deletes, expiry, encrypted external attachments |
| **E-mail** | **original MIME message** (RFC 5322) kept unchanged + **JMAP `Email` fields** (RFC 8621) extracted for index/display | ✅ | the original stays the source of truth so signatures remain verifiable |
| Matrix (connector) | Matrix spec **v1.19** (2026-07-08): `m.room.message`, relations `m.in_reply_to`, `m.thread`, `m.replace`, `m.annotation`, `m.receipt` | ✅ | original event kept, mapped onto the envelope |
| Comment on a resource | AS2 `Note` with `inReplyTo`/`context` → the resource | ✅ | |
| Comment on a text fragment | W3C Web Annotation Model | ✅ | |

## Encryption

| Standard | Evidence | Role |
|----------|----------|------|
| **MLS, RFC 9420** (OpenMLS 0.8) | ✅ | groups and chats; MIMI transport is HTTPS + MLS (`draft-ietf-mimi-protocol-07`) |
| **OpenPGP, RFC 9580** (v6 keys, AEAD/SEIPDv2, Ed25519/X25519) | ✅ (feature list ⚠️ from spec knowledge) | e-mail, via rPGP |
| **Post-quantum OpenPGP, RFC 9980** (June 2026) | ✅ | follow when rPGP supports it (ADR 0026) |
| **Header Protection, RFC 9788** (Aug 2025) | ✅ | protects subject etc. in encrypted mail |
| **Autocrypt** v1; v2 = `draft-autocrypt-openpgp-v2-cert-03` (July 2026, PQ hybrid keys) | ✅ v2 draft / ⚠️ v1.1 not re-fetched | key exchange in mail headers |

## Transport and interoperability

| Standard | Evidence | Role |
|----------|----------|------|
| **JMAP RFC 8620/8621** (+ RFC 9007 mail read receipts, 9404 blobs, 9425 quotas, 9661 Sieve) | ✅ | mail access; our own mail server stage 2 (ADR 0018) |
| SMTP / RFC 5322 §3.4.1 addresses | ✅ | mail between servers |
| MIMI protocol `-07`, architecture `-03`, room policy `-04` | ✅ drafts | messenger interoperability (DMA) |
| XMPP (RFC 6120/6121) | ⚠️ unverified | not planned |

## Gaps → own specification candidates (ADR 0014)

- "delivered" state and batched "read up to X" in AS2 (MIMI message-status covers it only inside MIMI)
- expiry (disappearing messages) as an AS2 property
- descriptor for encrypted attachments in AS2
- identity across edits: MIMI/Matrix point to the **first** version, AS2 `Update` changes in place
- one profile for thread vs. `context` vs. topic (FEPs compete)
- cross-protocol message-ID alias table (Message-ID, Matrix `event_id`, MIMI id, our UUIDv7)
- reactions and edits for e-mail
