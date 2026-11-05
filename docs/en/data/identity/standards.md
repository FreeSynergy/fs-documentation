# Identity (Web of Trust) – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** For this domain the section "follow-up research 2026-11-02: identity / Web of Trust" there counts as a full-text substitute.

## Inventory

| Piece | Evidence | Role in FreeSynergy |
|-------|----------|---------------------|
| ❌ **no established WoT spec in a standards body** | ❌ | own/co-authored spec — spec candidate no. 2 |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ repo reviewed 2026-11-02 | combines W3C **Verifiable Credentials** + **DIDComm v2.1** + **Ed25519** + **ECIES**; principle "Verification ≠ Trust"; BIP39 → HKDF → Ed25519/X25519; `did:key`; relays only see ciphertext; authorization UCAN-inspired, verifiable offline |
| **RLTP (Real Life Trust Protocol), gen 3** (`real-life-org/trust-protocol`) | ✅ existence reviewed | successor — fixes at Anton land there; we orient our docking points on it |
| **AS2 type `Relationship`** (Vocabulary) | ✅ vocabulary read | formal docking point: "A attests B for key K" |
| **AS2 actor keys** | ✅ | `Multikey` (FEP-521a), `publicKey` legacy — keys that attestations dock onto |
| **Signature mechanisms for ActivityPub objects** | ❌ old reference was 404 (correction list in the register) | must be researched anew before signatures are specified |

## Provisional rules (standards-close decisions)

1. Attestations are **objects of their own** (subject – relation – object + key + time + method), not fields on the profile.
2. They travel in the AS2 envelope as `Create` on `Relationship` (decision 2).
3. **A login proves no identity** — [login/](../login/index.md) and trust are separate layers.
4. Keys are published as `Multikey` (FEP-521a, ✅), `publicKey` only for compatibility. One actor can have several keys; attestations point at **keys**, person trust aggregates across keys (aggregating = app computation, not storage).

## Open standard points

- ~~Evidence DID Core / VC~~ → ✅ 2026-11-05 (status above); field-level comparison with RLTP still open
- ~~Signature mechanism~~ → ✅ RFC 9421 (transport) + FEP-8b32 (objects) + FEP-521a (`Multikey`)
- **Pairwise identifiers (RLTP):** one person has a different DID per relationship → hub matching (ADR 0019) cannot rely on one DID per person; open
- Write `identity/mapping.md`: WoT spec terms ↔ AS2 `Relationship`/`publicKey` (task in [requirements.md §7](../requirements.md))
