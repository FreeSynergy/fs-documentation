# Contacts – technical explanation

## Storage perspective

- **One table `contact`**, one row per `Card`. The canonical payload is the **JSContact JSON itself** (decision 4: the standard model is the source of truth, not an invented table shape).
- Columns **extracted** from the card (for indexes/filters): `id` (ULID), `uid` (JSContact `uid`, for exchange stability), `kind` (role: `individual`/`organization`/`group`/`device` — ⚠️ exact enum values from RFC 9553 still to be evidenced field by field), `name_sort` (derived from `name.components`), `created_at`, `updated_at`, `sync_token`.
- **IDs:** internally ULID, externally `https://<instance>/contacts/<ulid>` (decision 3).

## Keys and links

- `contact.id` ← referenced from everywhere: `events` participants refer to `email`/`sendTo`, the `login` account refers to the **self-card** (decision candidate 6), `profile` projections read the card.
- `cryptoKeys` in the card is the docking field for keys from [identity/](../identity/index.md) (vCard `KEY` ↔ JSContact `cryptoKeys`, ✅ bridge RFC 9554).

## Flow

1. **Create:** `Create` (AS2 envelope, decision 2) with a JSContact payload → validation against RFC 9553 → store.
2. **Change:** JSON Patch (RFC 6902) or the **JSContact's own patch object** (`PatchObject`, RFC 9553, ✅) → `Update` outwards.
3. **Sync:** clients use `sync_token` (pattern like RFC 6578); CardDAV RFCs (RFC 6352, ✅) for interoperability with external address books.
4. **Export/import:** jCard (RFC 7095) / vCard (RFC 6350) **losslessly** via RFC 9554.

## Projections

| Target | Projection |
|--------|------------|
| [profile/](../profile/index.md) | subset of the fields, audience-controlled (losslessness is deliberately lifted there) |
| [events/](../events/index.md) | `Participant` object from card parts (`name`, `email`, `language`) |
| CRM frontends | `lifecycle` and others as an `extensions` entry (⚠️) |
| gRPC/protobuf internally | generated from the canonical JSON (decision 4) |

## Merging and deleting

- Two cards for the same person: `merge` produces one card, the old `uid` is kept as an alias (our own decision, open for discussion — no standard evidenced).
- Deleting is a `Delete` in the envelope; attestations from [identity/](../identity/index.md) on the deleted card stay visible as broken references (deliberately: trust does not silently disappear).
