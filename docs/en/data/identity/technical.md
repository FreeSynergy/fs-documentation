# Identity (Web of Trust) – technical explanation

## Principle (rule 1, provisional)

Attestations are **objects of their own**, not fields on the profile:

`Attestation = { attesting actor, referenced actor, claim (e.g. "has key K", "is person P"), key, time, meeting method/place (optional) }`

This matches Anton's model ("build reputation through attestations over time", ✅ reviewed 2026-11-02).

## Storage perspective

- **Table `attestation`**: `id` (ULID), `subject` (who attests, IRI), `object` (whom/what, IRI), `claim_type` (enum, our own decision: `person_key`/`identity_encounter`/`vouching`), `key_ref` (`publicKey` ID of the object or `did:key`), `method` (`qr-in-person`/`remote`/…), `attested_at`, `place` (optional, reference to [geodata/](../geodata/index.md)), `signature_ref`.
- **No trust values in the table:** a score is a **computation** over the chain, not stored (otherwise it silently goes stale).

## Flow in the envelope (decision 2)

1. Two people meet and scan QR (pattern from Anton's project).
2. The client produces the attestation → `Create` on an **AS2 `Relationship`** object (✅ vocabulary read): `subject` = the attesting party, `relationship` = claim type, `object` = the attested party.
3. Receiving instances store the attestation unchanged; signature verification after the key research (⚠️/❌ — signature mechanisms for ActivityPub are still **not evidenced** on our side, the old reference was 404; Anton's stack uses Ed25519/JWS as an indication).

## Mapping sketch onto Anton's WoT spec (✅ facts from standards.md; `mapping.md` still open)

| Piece at Anton | On our side |
|----------------|-------------|
| Attestation (core object of the WoT spec) | AS2 `Relationship` + own fields (`claim_type`, `method`) |
| `did:key` (Ed25519) | `publicKey` on the actor ↔ `cryptoKeys` in the contact card |
| `wot-profiles` (JWS-signed profile publication) | [profile/](../profile/index.md) projection + signature (⚠️ mechanism open) |
| UCAN-inspired capabilities | authorization layer (envelope/instance), not data model |
| RLTP (gen 3) | watch; migration follows gen 3 |

## Open technical points

- Create `identity/mapping.md` as a file of its own (task from [requirements.md §7](../requirements.md))
- Signature mechanism research (which one is actually evidenced?) — before any implementation
- Trust chain questions (depth, expiry periods) as an API, not as a schema
