# Identity (Web of Trust) – technical explanation

## Principle (rule 1, provisional)

Attestations are **objects of their own**, not fields on the profile:

`Attestation = { attesting actor, referenced actor, claim (e.g. "has key K", "is person P"), key, time, meeting method/place (optional) }`

This matches Anton's model ("build reputation through attestations over time", ✅ reviewed 2026-11-02).

## Storage perspective (ADR 0020)

- *Content*: the attestation as **W3C VC 2.0 credential** with an `eddsa-jcs-2022` proof (as RLTP, ✅ 2026-11-05).
- *Envelope*: AS2 **`Relationship`** (`subject` = attesting actor, `object` = attested actor/key, `relationship` = claim type), addressed with `to`/`audience`.
- Extracted columns: `id`, `subject`, `object`, `claim_type` (our enum: `person_key`/`identity_encounter`/`vouching`), `key_ref` (`Multikey` ID or `did:key`), `method` (`qr-in-person`/`remote`/…), `attested_at`, `place` (optional, [geodata/](../geodata/index.md)).
- **No trust values in the table:** a score is a **computation** over the chain, not stored (otherwise it silently goes stale).

## Flow in the envelope (decision 2)

1. Two people meet and scan QR (pattern from Anton's project).
2. The client produces the attestation → `Create` on an **AS2 `Relationship`** object (✅ vocabulary read): `subject` = the attesting party, `relationship` = claim type, `object` = the attested party.
3. Receiving instances store the attestation unchanged and verify the VC proof (`eddsa-jcs-2022`); the transport between instances is signed with RFC 9421 (✅).

## Mapping sketch onto Anton's WoT spec (✅ facts from standards.md; `mapping.md` still open)

| Piece at Anton | On our side |
|----------------|-------------|
| Attestation (core object of the WoT spec) | AS2 `Relationship` + own fields (`claim_type`, `method`) |
| `did:key` (Ed25519), pairwise per relationship in RLTP | `Multikey` on the actor ↔ `cryptoKeys` in the contact card |
| `wot-profiles` (JWS-signed profile publication) | [profile/](../profile/index.md) projection + FEP-8b32 proof |
| UCAN-inspired capabilities | authorization layer (envelope/instance), not data model |
| RLTP (gen 3) | watch; migration follows gen 3 |

## Open technical points

- Create `identity/mapping.md` as a file of its own (task from [requirements.md §7](../requirements.md))
- Trust chain questions (depth, expiry periods) as an API, not as a schema
