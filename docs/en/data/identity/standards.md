# Identity (Web of Trust) – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** For this domain the section "follow-up research 2026-11-02: identity / Web of Trust" there counts as a full-text substitute.

## Inventory

| Piece | Evidence | Role in FreeSynergy |
|-------|----------|---------------------|
| ❌ **no established WoT spec in a standards body** | ❌ | own/co-authored spec — spec candidate no. 2 |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ repo reviewed 2026-11-02 | combines W3C **Verifiable Credentials** + **DIDComm v2.1** + **Ed25519** + **ECIES**; principle "Verification ≠ Trust"; BIP39 → HKDF → Ed25519/X25519; `did:key`; relays only see ciphertext; authorization UCAN-inspired, verifiable offline |
| **RLTP (Real Life Trust Protocol), gen 3** (`real-life-org/trust-protocol`) | ✅ existence reviewed | successor — fixes at Anton land there; we orient our docking points on it |
| **AS2 type `Relationship`** (Vocabulary) | ✅ vocabulary read | formal docking point: "A attests B for key K" |
| **ActivityPub/AS2 `publicKey` on the actor** | ✅ vocabulary read | keys that attestations dock onto |
| **W3C DID Core / VC Data Model** | ⚠️ *cited* as evidenced by Anton's spec; the W3C documents themselves not retrieved | evidence before using fields directly |
| **Signature mechanisms for ActivityPub objects** | ❌ old reference was 404 (correction list in the register) | must be researched anew before signatures are specified |

## Provisional rules (standards-close decisions)

1. Attestations are **objects of their own** (subject – relation – object + key + time + method), not fields on the profile.
2. They travel in the AS2 envelope as `Create` on `Relationship` (decision 2).
3. **A login proves no identity** — [login/](../login/index.md) and trust are separate layers.
4. Key aliases: one actor can have several keys; attestations point at **keys**, person trust aggregates across keys (aggregating = app computation, not storage).

## Open standard points

- Evidence W3C DID Core and the VC Data Model field by field (⚠️) and compare with Anton's use of them
- Signature mechanism (❌) — candidates from Anton's stack: Ed25519 signatures, JWS; that is not yet evidenced for our ActivityPub
- Write `identity/mapping.md`: WoT spec terms ↔ AS2 `Relationship`/`publicKey` (task in [requirements.md §7](../requirements.md))
