# Research: Standards for the data domain "messages" (fs-messenger)

Researched: 2026-11-05 · by: Claude subagent

Legend: ✅ verified at the primary source during this research · ⚠️ partly verified / from secondary source / status may change soon

Context (already decided): one program `fs-messenger` for e-mail, chat and messengers; encrypted messages only; own data model = AS2 envelope + content in a domain standard + append-only AS2 activity log; connectors Matrix (matrix-rust-sdk), IMAP/JMAP/SMTP, later bridges; MLS (RFC 9420) for group encryption.

---

## 1. IETF MIMI (More Instant Messaging Interoperability)

### 1.1 Documents and status (WG document list, fetched 2026-11-05) ✅

No MIMI document is an RFC yet. All are Internet-Drafts.

| Area | Document | Version / date | Status |
|---|---|---|---|
| Architecture | draft-ietf-mimi-arch | -03, 2026-07-06 | WG document |
| Protocol (provider-to-provider, HTTPS + MLS) | draft-ietf-mimi-protocol | -07, 2026-11-02 | WG document |
| **Content format** | **draft-ietf-mimi-content** | **-10, 2026-11-02** | WG document, intended status *Informational*; milestone "Mar 2025 forward to IESG" missed |
| Room policy | draft-ietf-mimi-room-policy | -04, 2026-07-06 | WG document |
| Discovery | draft-interop-mimi-discovery-requirements | -03, 2025-06-20 | **Expired** (adopted by the WG, but no successor) |
| Identifiers / identity | draft-mahy-mimi-identity (-05, 2026-07-06), draft-barnes-mimi-identity-arch (-04, 2026-11-01) | individual drafts | not adopted |
| Read/delivery receipts | draft-mahy-mimi-message-status | -02, 2026-11-01 | individual draft |
| Attachments | draft-robert-mimi-attachments | -06, 2026-06-29 | individual draft |
| AV/image metadata | draft-mahy-mimi-av-metadata | -02, 2026-11-01 | individual draft |
| Hub retraction | draft-mahy-mimi-hub-retracted-messages | -00, 2026-07-02 | individual draft |
| Message-ID in MLS AAD | draft-mahy-mimi-msgid-aad | -03, 2026-11-01 | individual draft |
| Portability | draft-kohbrok-mimi-portability | -06, 2026-06-29 | individual draft |

Source: https://datatracker.ietf.org/wg/mimi/documents/

Related MLS dependency: draft-ietf-mls-extensions-11 (2026-11-02, intended Proposed Standard) supplies the content-advertisement extension that MIMI content relies on. ✅ https://datatracker.ietf.org/doc/draft-ietf-mls-extensions/

### 1.2 Is it MLS-based? ✅ Yes
> "describes a profile suitable for instant messaging interoperability of messages end-to-end encrypted inside the MLS (Message Layer Security) Protocol."
> "it is sufficiently flexible that it can be used in other contexts, including without encryption."

https://datatracker.ietf.org/doc/draft-ietf-mimi-content/

### 1.3 What the MIMI content format contains ✅ (draft-ietf-mimi-content-10)

**Encoding:** CBOR (RFC 8949), schema in CDDL. Media type `application/mimi-content`.
> "we do not want to base64 encode body parts with binary media types (ex: images). This rules out using JSON"

**Container (`mimiContent`):**
```
mimiContent = [ salt: bstr .size 16, replaces: null / MessageId, topicId: bstr,
                expires: null / Expiration, inReplyTo: null / MessageId,
                mimiExtensions: extensions, nestedPart: NestedPart ]
```
- **Message ID** = 32 bytes: `hashAlg(1 byte) || SHA-256(senderUri, roomUri, message, salt)[0..30]`. It is derived, not transmitted.
  > "a 32-octet message ID which is calculated from the hash of the message (including the salt), the sender URI, and the room URI."
- **Ordering:** the hub assigns an "accepted timestamp" in milliseconds.
- **Body:** `NestedPart` = disposition + language + one of `NullPart | SinglePart(contentType, content) | ExternalPart | MultiPart(chooseOne/singleUnit/processAll)`. These map onto multipart/alternative, related and mixed. Default text type: `text/markdown;variant=GFM-MIMI`. HTML is allowed.
- **Dispositions:** unspecified, render, reaction, profile, inline, icon, attachment, session, preview.

| Feature | How MIMI does it | ✅/⚠️ |
|---|---|---|
| Body | `SinglePart` with media type (Markdown GFM-MIMI, HTML, …) | ✅ |
| Reply | `inReplyTo` = MessageId; loops forbidden | ✅ |
| Thread/topic | `topicId` (opaque bytes; empty = none). Section 5.11 "Topics / Threading" | ✅ |
| Reaction | new message with `inReplyTo` = target and body disposition `reaction` (usually one emoji) | ✅ |
| Unlike | `replaces` = reaction message id, disposition `reaction`, NullPart | ✅ |
| Edit | `replaces` = id of the **first** version and a new body | ✅ |
| Delete | `replaces` = original id, NullPart body | ✅ |
| Expiring | `expires` = [relative: bool, time: uint32] | ✅ |
| Attachments | `ExternalPart`: url, contentType, size, encAlg/key/nonce/aad (AEAD), hashAlg/contentHash, filename, description, expires. Disposition is `attachment` or `inline` | ✅ |
| Mentions | links with `mimi://…/u/…` URIs inside the Markdown or HTML body | ✅ |
| Delivery/read receipts | **not in content-10**. They are in draft-mahy-mimi-message-status-02: `application/mimi-message-status`, a CBOR list of (messageId, status) with statuses 0 unread, 1 delivered, 2 read, plus expired and others | ✅ (individual draft ⚠️) |

> "Delivery notifications and read receipts are addressed in [I-D.mahy-mimi-message-status]. Calling and conferencing will also be addressed in another document."
> "If the same message is replaced more than once, the replaces data field refers to the message ID of the first instance of the message."

https://datatracker.ietf.org/doc/draft-mahy-mimi-message-status/

### 1.4 Rust implementations ✅
- **phnx-im/mimi-content** (Phoenix R&D, the OpenMLS maintainers): a Rust crate for the content container, message-ID derivation and message-status.
  > "The crate implements the message container and the message ID derivation of draft-ietf-mimi-content-10, and the message status report format of draft-mahy-mimi-message-status-02."
  https://github.com/phnx-im/mimi-content
- phnx-im also has a `mimi-room-policy` Rust repository. https://github.com/phnx-im
- **OpenMLS** (`openmls` 0.8.x): a Rust implementation of RFC 9420. https://docs.rs/openmls/latest/openmls/

---

## 2. JMAP

### 2.1 RFC 8621 – JMAP for Mail (Aug 2019, Proposed Standard) ✅
Main `Email` properties (all are top-level peers):
- **Metadata (server-set):** `id`, `blobId`, `threadId`, `mailboxIds` (map Id→true), `keywords` (`$seen`, `$flagged`, `$answered`, `$draft`, …), `size`, `receivedAt`
- **Header convenience:** `headers` (raw list), `header:{name}:as{Form}`, `messageId`, `inReplyTo`, `references`, `sender`, `from`, `to`, `cc`, `bcc`, `replyTo`, `subject`, `sentAt`
- **Body:** `bodyStructure` (full MIME tree of `EmailBodyPart`), `bodyValues`, `textBody`, `htmlBody`, `attachments`, `hasAttachment`, `preview`

> "the Email object contains 3 alternate properties with flat lists of body parts: "textBody"/"htmlBody" … "attachments""
> "In JMAP, a Thread is simply a flat list of Emails, ordered by date."

https://www.rfc-editor.org/rfc/rfc8621.html

### 2.2 Other JMAP RFCs and drafts (JMAP WG page, 2026-11-05) ✅
| Doc | Date | Status |
|---|---|---|
| RFC 8620 JMAP Core | 2019-07 | PS (updated by 9404, 9670) |
| RFC 8887 WebSocket | 2020-08 | PS |
| RFC 9007 MDN handling (read receipts for mail) | 2021-03 | PS |
| RFC 9219 S/MIME signature verification | 2022-04 | PS |
| RFC 9404 Blob management | 2023-08 | PS |
| RFC 9425 Quotas | 2023-06 | PS |
| RFC 9661 Sieve scripts | 2024-09 | PS |
| RFC 9670 Sharing | 2024-11 | PS |
| RFC 9610 Contacts | 2024-12 | PS |
| RFC 9749 VAPID for Web Push | 2025-03 | PS |
| draft-ietf-jmap-calendars-33 | 2026-10-13 | in RFC Editor queue |
| draft-ietf-jmap-blobext-03, -filenode-20, -emailpush-04, -metadata-05, -object-history-03, -mail-sharing-02, -conditional-02, -refplus-02 | 2026 | WG drafts |
| draft-ietf-jmap-smime-sender-extensions-04 | 2023 | expired; continued as draft-melnikov-jmap-smime-sender-extensions-alt-07 (2026-06) |

https://datatracker.ietf.org/wg/jmap/documents/

**JMAP for chat:** there is no IETF/WG document. Mark Atwood's "draft-atwood-jmap-chat" exists only on GitHub (with Rust crates `jmap-chat-types` and `jmap-chat-server`) and is **not on the datatracker** (404). ⚠️ https://github.com/MarkAtwood/jmap-chat-spec

---

## 3. ActivityStreams 2.0 and Fediverse conversation vocabulary

- **AS2 Core and Vocabulary:** W3C Recommendation, 23 May 2017. ✅ A new **W3C Social Web WG** (charter 2026-01) maintains AS2 and ActivityPub. Its goal is a backwards-compatible iteration in Q3 2026 ⚠️ (https://www.w3.org/2026/01/social-web-wg-charter.html).
- **`context`** ✅
  > "Identifies the context within which the object exists or an activity was performed. The notion of "context" used is intentionally vague."
  https://www.w3.org/TR/activitystreams-vocabulary/#dfn-context
- **`Read`** ✅ > "Indicates that the actor has read the object." (Read also has the siblings `View` and `Listen`.)
- **`Like`** ✅ > "Indicates that the actor likes, recommends or endorses the object."
- **`attachment`** ✅ > "Identifies a resource attached or related to an object that potentially requires special handling. The intent is to provide a model that is at least semantically similar to attachments in email."
- **`Document`** ✅ > "Represents a document of any kind." `Image`, `Audio` and `Video` extend `Document`.

**FEPs** (all `DRAFT`, none `FINAL`; index at https://codeberg.org/fediverse/fep):
| FEP | Topic | Status | |
|---|---|---|---|
| FEP-7888 | Demystifying `context` ("was created in relation to"; deleting a context may GC its objects) | DRAFT, 2023-03-14 | ✅ |
| FEP-171b | Conversation Containers: the conversation is a collection owned by one actor, and every item is `Add(activity)` | DRAFT, 2024-11-23 | ✅ |
| FEP-2931 | Representing context with a Collection | DRAFT, 2025-03-22 | ✅ |
| FEP-11dd / f15d / c0d0 / 8c13 | Context ownership, relocation, locking, restricted threads | DRAFT, 2025–2026 | ✅ |
| FEP-76ea | Conversation threads | DRAFT, 2024-10-04 | ✅ |
| FEP-f228 | Backfilling conversations | DRAFT, 2025-02-17 | ✅ |
| FEP-c0e0 | Emoji reactions: `EmojiReact` (LitePub ns) = `Like` + `content` (one grapheme or `:shortcode:` + `Emoji` tag) | DRAFT, 2024-08-08 | ✅ |
| FEP-1970 | Chat links | DRAFT | ✅ |

> FEP-c0e0: "`EmojiReact` activity type is considered to be a part of [LitePub] vocabulary. Its full IRI is `http://litepub.social/ns#EmojiReact`."

---

## 4. E2EE for ActivityPub ✅

**"Messaging Layer Security in ActivityPub"** is written by the SWICG ActivityPub E2EE Task Force (Evan Prodromou et al., with Social Web Foundation support). It is a Community Group report with `specStatus: "unofficial"`, so it is not on the W3C Rec track. W3C event material says it has "two interoperable implementations". https://swicg.github.io/activitypub-e2ee/ · repo https://github.com/swicg/activitypub-e2ee

How it works:
- MLS wire objects (`PublicMessage`, `PrivateMessage`, `Welcome`, `GroupInfo`, `KeyPackage`) are AS2 object types in the context `https://purl.archive.org/socialweb/mls` (versioned 1.0.0). They carry `mediaType: "message/mls"`, `encoding: "base64"` and the bytes in `content`. Actors get a `keyPackages` collection. Routing topology is `FullMesh`.
- Each MLS message SHOULD have `conversation` (a server-maintained OrderedCollection) and MAY have `context`.
- **Inside** the MLS `application_data` there is a *limited AS2 profile*. It uses `urn:uuid:` ids (not dereferenceable), `Note`/`Article`/`Image`/…, `inReplyTo`, and inline base64 attachments. Activities are `Create`, `Update`, `Delete`, `Like`, `Announce`, `Undo`, **`Read`**, `Listen`, `View`, and `IntransitiveActivity` as padding/null message.
  > "Other activity or content types from the Activity Vocabulary, and from Activity Streams 2.0 extensions, may be used in this structure."
  > "Read. Indicates that the sender has read a Note or Article … The id property must match an object that was received as the object of a Create"
- In the encrypted profile, `attributedTo` and `to` are derived from the envelope. The `replies`, `likes` and `shares` collections are unset because reactions are tracked client-side.

No FEP and no IETF draft for MLS over ActivityPub was found. The FEP index has no E2EE/MLS entry. ⚠️

---

## 5. Matrix

- **Current spec:** **v1.19, released 8 July 2026.** ✅ https://spec.matrix.org/v1.19/changelog/v1.19/ (v1.19 adds encrypted history sharing MSC4268 and image packs MSC2545.)
- **`m.room.message` msgtypes** ✅: `m.text`, `m.emote`, `m.notice`, `m.image`, `m.file`, `m.audio`, `m.video`, `m.location`, `m.key.verification.request`.
- **Relations (`m.relates_to`)** ✅ https://spec.matrix.org/v1.19/client-server-api/
  - Replies: `m.in_reply_to: {event_id}`. This is a sub-key, not a `rel_type`.
    > "a subkey named m.in_reply_to is used to describe the reply's relationship, leaving the other properties of m.relates_to to describe the primary relationship"
  - Threads: `rel_type: m.thread` (event_id = thread root; `is_falling_back` + `m.in_reply_to` as fallback). Threads have their own receipts.
  - Edits: `rel_type: m.replace` + `m.new_content` (since v1.4). Like MIMI, it always points to the original event.
  - Reactions: `rel_type: m.annotation` + `key` (emoji). The server aggregates them.
  - Receipts: ephemeral `m.receipt` (`m.read`, `m.read.private`, threaded receipts).
- **MLS in Matrix** ✅ (GitHub API): all of these proposals are still open, so Matrix has not adopted MLS yet.
  - MSC2883 "Matrix-flavoured MLS" (decentralised MLS, WIP, open since 2020, updated 2026-06)
  - MSC4244 "RFC 9420 MLS for Matrix" (WIP, open)
  - MSC4256 "RFC 9420 MLS mode Matrix" (open, active, updated 2026-09-29)
- **Matrix and MIMI** ⚠️: Matrix.org (Travis Ralston) proposed *Linearized Matrix* (draft-ralston-mimi-linearized-matrix, last -04) as the MIMI transport. The WG instead adopted the HTTPS+MLS protocol (draft-ietf-mimi-protocol). Matrix people still take part in IETF, but Matrix is not the MIMI protocol. https://datatracker.ietf.org/doc/draft-ralston-mimi-linearized-matrix/

---

## 6. E-mail encryption (newest)

| Item | Status | |
|---|---|---|
| **RFC 9580 OpenPGP** | Proposed Standard, **July 2024**. Obsoletes RFC 4880, 5581 and 6637. New: **v6 keys and signatures** (SHA-256 fingerprints, salted signatures), **SEIPD v2 with AEAD** (OCB mandatory, also EAX and GCM), native **Ed25519/X25519 (and Ed448/X448)**, **Argon2** S2K. v3 keys and MD5 deprecated. Quote: "This document obsoletes RFCs 4880 …, 5581 …, and 6637" | ✅ status/date; ⚠️ feature list from spec knowledge |
| **RFC 9980 Post-Quantum Cryptography in OpenPGP** | Proposed Standard, **June 2026** (ML-KEM + X25519 hybrid, ML-DSA composite) | ✅ https://datatracker.ietf.org/doc/draft-ietf-openpgp-pqc/ |
| **RFC 9788 Header Protection for Cryptographically Protected Email** | Proposed Standard, **August 2025**. Updates RFC 8551 and also applies to PGP/MIME. > "This document updates the S/MIME specification (RFC 8551) to offer a different mechanism that provides the same cryptographic protections but with fewer downsides when handled by legacy clients." | ✅ https://www.rfc-editor.org/info/rfc9788 |
| **Autocrypt Level 1** (v1.1) | Community spec, stable, used by Delta Chat, Thunderbird and K-9 | ⚠️ (not re-fetched) https://autocrypt.org/level1.html |
| **Autocrypt v2** | draft-autocrypt-openpgp-v2-cert-03 (2026-07-06, individual, Informational; Gillmor/Krekel/Ziegelmayer). OpenPGP v6 certs with PQ hybrid ML-KEM-768+X25519, ratcheted rotating subkeys for "reliable deletion" (forward secrecy) | ✅ https://datatracker.ietf.org/doc/draft-autocrypt-openpgp-v2-cert/ · https://autocrypt2.org/ |

---

## 7. Recommendation (OPINION, not a verified fact)

### (a) Chat messages → **MIMI content (draft-ietf-mimi-content) as the canonical content payload**
- It is the only IETF format designed for content inside MLS, and it covers body, reply, topic/thread, reaction, edit, delete, expiry and encrypted external attachments in one container. A Rust crate already exists (`mimi-content`, tracks -10).
- Use draft-mahy-mimi-message-status for delivered/read state.
- Risk: it is still a draft. Pin to `-10`, store the draft version in the record, and expect breaking changes before the RFC.

### (b) E-mails → **RFC 5322/MIME raw blob (canonical) + JMAP `Email` (RFC 8621) as the parsed projection**
- Keep the original signed or encrypted MIME (OpenPGP RFC 9580 v6 + RFC 9788 header protection, Autocrypt v1 now and v2 later) as an immutable blob, because signatures must stay verifiable.
- Index it with the JMAP Email property set (threadId, keywords, from/to/…, textBody/htmlBody/attachments). Do **not** convert e-mail into MIMI CBOR as the source of truth. MIMI may be produced as a rendering view.

### (c) Unified internal message object → **AS2 envelope + typed content payload (`mediaType`)**
Follow the SWICG "MLS in ActivityPub" profile (it matches our decision almost exactly):

```jsonc
{ "@context": ["https://www.w3.org/ns/activitystreams", "<fs-messages ctx>"],
  "id": "urn:fs:msg:<uuid|mimi-msgid>", "type": "Note" /* Article for e-mail */,
  "attributedTo": "<actor>", "to": [...], "cc": [...], "bcc": [...], "audience": "<room>",
  "context": "<conversation/room collection>",         // FEP-7888/2931 semantics
  "published": "...", "updated": "...",
  "inReplyTo": "<msg id>",
  "mediaType": "application/mimi-content" | "message/rfc822" | "application/vnd.matrix.event+json",
  "fs:contentRef": "<blob hash>", "fs:source": {"protocol": "matrix|imap|jmap|mls", "nativeId": "..."},
  "attachment": [{ "type": "Document|Image|Audio|Video", "mediaType": "...", "url": "...", "fs:enc": {...} }] }
```

**Mapping table (opinion):**
| Concept | AS2 log activity | MIMI | Matrix | E-mail/JMAP |
|---|---|---|---|---|
| New message | `Create(Note/Article)` | new message | `m.room.message` | new Email |
| Conversation/room | `context` (+ `audience`) | room URI | room_id | (mailbox is not a conversation) |
| Thread | `context` = thread collection, or `fs:topic` | `topicId` | `m.thread` | `threadId` / References |
| Reply | `inReplyTo` | `inReplyTo` | `m.in_reply_to` | `inReplyTo` header |
| Edit | `Update` (object id = **first** version) | `replaces` + body | `m.replace` | n/a (new mail) |
| Delete/retract | `Delete` (keep `Tombstone`) | `replaces` + NullPart | redaction | `Email/set destroy` / flag |
| Reaction | `Like` or `EmojiReact` (FEP-c0e0) with `content` | `inReplyTo` + disposition reaction | `m.annotation` + key | none (gap) |
| Unreact | `Undo(Like/EmojiReact)` | `replaces` + NullPart | redact the annotation | none |
| Read receipt | `Read` (also `View`, `Listen`) | mimi-message-status `read` | `m.receipt` `m.read` | `$seen` keyword / MDN RFC 9007 |
| Delivered | `fs:Delivered` (custom) | message-status `delivered` | none (implicit) | DSN |
| Expiry | `endTime` or `fs:expires` | `expires` | (MSC only) | none |
| Attachment | `attachment[]` Document/Image/… | ExternalPart | `m.file`/`m.image` + EncryptedFile | MIME parts / `attachments` |

### Real gaps (candidates for an own FreeSynergy spec)
1. **AS2 term for "delivered"** and a **batched read state** ("read up to X"). AS2 only has per-object `Read`. MIMI message-status and Matrix receipts are batched.
2. **AS2 expiry/ephemeral property.** No standard term exists.
3. **Encrypted attachment descriptor in AS2** (key, nonce, hash, encAlg). SWICG inlines base64 instead. Mirror MIMI `ExternalPart` and Matrix `EncryptedFile`.
4. **Edit-chain identity:** AS2 `Update` mutates in place, while MIMI and Matrix refer to the first version. Define "version objects" in our append-only log.
5. **Stable cross-protocol message ID** (MIMI hash-derived vs Matrix event_id vs Message-ID vs AS2 IRI). We need a mapping/alias table spec.
6. **Thread vs context vs topic semantics**: the FEPs are all DRAFT and compete (7888/2931/171b/76ea). Pick one profile and document it.
7. **E-mail reactions/edits:** no standard. Optional bridge convention (e.g. RFC 9078 reaction disposition) only.
8. **Room membership/policy over MLS for non-MIMI transports** (MIMI room-policy is a draft). Reuse it rather than inventing one.
