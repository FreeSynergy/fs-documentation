# Identity (Web of Trust)

Who is an actor — and whom may one trust? Approach: **Web of Trust with meetings in the real world** (an external project we want to help support, standard in progress).

## Inventory

| Piece | Evidence | Role in FreeSynergy |
|-------|----------|---------------------|
| ❌ **no established WoT spec in a standards body** | ❌ | own/co-authored spec — our spec candidate no. 2 after block/document |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ repo reviewed 2026-11-02 | combines W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; principle "Verification ≠ Trust"; successor RLTP (gen 3). All facts in [standards.md → follow-up research](../standards.md) — **do not download again** |
| **AS2 type `Relationship`** (Vocabulary) | ✅ vocabulary read | formal docking point for statements like "A attests B for PGP key K" |
| **AS2 actor keys** | ✅ | `Multikey` (FEP-521a), `publicKey` legacy — keys that attestations dock onto |
| **W3C DID Core 1.0** | ✅ Recommendation 2022-07-19 (DID 1.1: Candidate Recommendation 2026-03-05) | identity between instances (ADR 0024); method `did:key` (as RLTP) |
| **W3C VC Data Model 2.0, Data Integrity 1.0, EdDSA cryptosuites, Controlled Identifiers 1.0** | ✅ Recommendations 2025-05-15 | attestations are VC 2.0 credentials with `eddsa-jcs-2022` proofs (as RLTP) |
| **RLTP gen 3** (`real-life-org/trust-protocol`) | ✅ checked 2026-11-05: Editor's Drafts, library 0.12.0 | Ed25519 `did:key`, **separate identifiers per relationship**, VC 2.0; transport open (first adapter ToIP TSP) |
| **HTTP Message Signatures, RFC 9421** | ✅ Feb 2024 | signing requests between instances; Mastodon verifies since 4.5.0 |
| **FEP-8b32 Object Integrity Proofs** | ✅ draft | signatures on AS2 objects (Data Integrity, `eddsa-jcs-2022`) |
| **FEP-521a** | ✅ final 2025-06-14 | actor keys as `Multikey` (replaces the old `publicKey`) |
| **MLS, RFC 9420** | ✅ July 2023 | group encryption (ADR 0018); binding MLS credentials to DIDs: ❌ no IETF draft found |

## Provisional rules

1. Attestations are **objects of their own** (subject – relation – object + key + time + place/method of the meeting), not fields on the profile.
2. Attestations travel in the AS2 envelope (`Create` on a `Relationship` object), so WoT exchange works like all data (decision 2).
3. A "login" proves no identity — login ([login/](../login/index.md)) and trust are separate layers.

## Open points

- ~~review Anton's repo~~ → **done 2026-11-02**, facts in standards.md; mapping it as `mapping.md` onto `Relationship`/`publicKey` is still open
- ~~Signature research~~ → ✅ 2026-11-05: RFC 9421, FEP-8b32, FEP-521a; DID Core/VC 2.0 status ✅ (`temp/research/contacts-identity-standards.md`)
- Layers (ADR 0024): **login** = Kanidm (OAuth2/OIDC, SCIM) · **identity** = DID · **trust** = Web of Trust attestations (VC 2.0)
- Pairwise DIDs (RLTP) vs. hub matching — open

## See also

- [standards.md → correction list](../standards.md) (signature reference 404)
- [profile/](../profile/index.md), [login/](../login/index.md)
