# Identity (Web of Trust)

Who is an actor — and whom may one trust? Approach: **Web of Trust with meetings in the real world** (an external project we want to help support, standard in progress).

## Inventory

| Piece | Evidence | Role in FreeSynergy |
|-------|----------|---------------------|
| ❌ **no established WoT spec in a standards body** | ❌ | own/co-authored spec — our spec candidate no. 2 after block/document |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ repo reviewed 2026-11-02 | combines W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; principle "Verification ≠ Trust"; successor RLTP (gen 3). All facts in [standards.md → follow-up research](../standards.md) — **do not download again** |
| **AS2 type `Relationship`** (Vocabulary) | ✅ vocabulary read | formal docking point for statements like "A attests B for PGP key K" |
| **ActivityPub `publicKey` on the actor** | ✅ vocabulary read | key that attestations dock onto |
| **Signature mechanisms for ActivityPub objects** | ❌ (old reference was 404, see correction list) | must be researched anew before any use |

## Provisional rules

1. Attestations are **objects of their own** (subject – relation – object + key + time + place/method of the meeting), not fields on the profile.
2. Attestations travel in the AS2 envelope (`Create` on a `Relationship` object), so WoT exchange works like all data (decision 2).
3. A "login" proves no identity — login ([login/](../login/index.md)) and trust are separate layers.

## Open points

- ~~review Anton's repo~~ → **done 2026-11-02**, facts in standards.md; mapping it as `mapping.md` onto `Relationship`/`publicKey` is still open
- Signature research (which mechanism is actually evidenced?) — Anton's stack gives indications (Ed25519, JWS, UCAN-inspired), W3C DIDs/VC still ⚠️

## See also

- [standards.md → correction list](../standards.md) (signature reference 404)
- [profile/](../profile/index.md), [login/](../login/index.md)
