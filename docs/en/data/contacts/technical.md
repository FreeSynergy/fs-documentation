# Contacts – technical explanation

## Storage perspective (ADR 0019, 0020)

- **Object = envelope + content + log.**
  - *Envelope* (AS2 **`Profile`**, ✅): `id`, `type: Profile`, `describes` (the person's actor IRI or DID, if known), `attributedTo` (who wrote this card), `to`/`cc`/`bto`/`audience` (who may see it), `published`, `updated`.
  - *Content*: the **JSContact `Card`** JSON (RFC 9553) — the standard model is the source of truth.
  - *Log*: AS2 activities `Create`/`Update`/`Delete` per card, written by `fs-store` in the same transaction.
- Columns **extracted** for indexes: `id`, `uid` (JSContact), `kind` (✅ `individual`/`group`/`org`/`location`/`device`/`application`), `describes`, `name_sort` (from `name.components`), emails/phones (normalised, for hub matching), `created_at`, `updated_at`.
- **IDs:** see [standards.md → decision 3](../standards.md) (ULID today, UUIDv7 proposed); externally `https://<instance>/contacts/<id>`.

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
| CRM frontends | `lifecycle` as vendor property `<domain>:lifecycle` (✅ mechanism, RFC 9553 §1.8.1) |
| Cap'n Proto internally (ADR 0021) | generated from the canonical JSON (decision 4) |

## Same person in several programs (ADR 0019)

- No standard defines merging (❌ checked 2026-11-05). Our rule: **link, don't merge.**
- The hub finds candidates (same normalised e-mail/phone, same `describes`/DID) and proposes them; a person confirms.
- A confirmed link is stored as an AS2 **`Relationship`** between the two cards (relation ⚠️ proposed: `owl:sameAs`). Both cards stay; views may show them combined. Undo = `Undo` on the relationship.
- `relatedTo` is **not** used for this — its values describe relations between *different* people (✅).

## Deleting

- Deleting is a `Delete` in the log; attestations from [identity/](../identity/index.md) on the deleted card stay visible as broken references (deliberately: trust does not silently disappear).
