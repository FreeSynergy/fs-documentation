# Messages – technical explanation

## Storage perspective

- **One table `message`**: canonical payload = AS2 object JSON (`Note`/`Article`) (decision 4). Extracted columns: `id` (ULID), `type`, `thread_id`, `in_reply_to` (ULID or IRI), `actor_id`, `created_at`, `updated_at`, `deleted` (tombstone marker).
- **Delivery copies:** `to`/`cc`/`bto`/`bcc` decide **where copies land** (decision 2). Internally: table `message_delivery` (`message_id`, `recipient_id`, `audience` ∈ `to|cc|bto|bcc`). The actual authorization runs separately through resource permissions — the audience fields do not replace it.

## Threading rule (our own decision — not fully defined in AS2)

AS2 knows `inReplyTo` but no complete thread mechanism (open point in [index.md](index.md)). Proposal:

- `thread_id` = ULID of the **root post** (one column, indexed)
- `in_reply_to` = direct parent post (tree structure)
- Display: flat (chat) or threaded (comments) — both rendered from the same columns

## Flow

1. Sending: `Create` (envelope) with a `Note`; the server checks permissions and creates the delivery copies.
2. Changing: `Update` — the edit window and the marking (`updated` ≠ `created`) are a product rule, not a standard.
3. Deleting: `Delete` + tombstone (content gone, metadata stays — the extent is still to be decided).
4. Recipient sync: the JMAP pattern (RFC 8620/8621, ✅) as a reference for efficiently fetching/patching JSON resources.

## Projections

| Target | Projection |
|--------|------------|
| Mail sending | RFC 5322 (✅ §3.4.1 address format) — SMTP transport is a topic of its own (not a data model) |
| JMAP endpoint | `Note` → JMAP email structure, field mapping open |
| Search/indexes | `content`/`contentMap` full text; `name` as the subject |
| Encryption | MLS (RFC 9420, ⚠️ not retrieved in this round) as a candidate for group E2EE |

## Open technical points

- Edit history: no AS2 rule — needs our own decision (revisions like in the wiki or not?).
- Delivery receipt (read/sent): no data standard; MLS delivery receipts ⚠️.
