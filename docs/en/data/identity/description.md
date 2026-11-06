# Identity (Web of Trust) – description

**What this domain is:** the question of **whom one trusts** — attestations between actors, keys, and the certainty that an account/the person really is who one takes them to be. Approach: **Web of Trust with meetings in the real world** — Anton runs a real-life project on this (`real-life-org/web-of-trust`), repo **reviewed on 2026-11-02**; all facts in the central register ([standards.md → follow-up research](../standards.md)).

**Core principle (from Anton's project, ✅ reviewed):** **Verification ≠ Trust.** Verification only confirms: "this really is that person" (personal meeting + QR scan). **Trust** only arises through attestations over time.

**What it covers:**

- Attestation objects: subject – relation – object, plus key, time, place/method of the meeting
- Key docking: `publicKey` on the actor, `cryptoKeys` in the contact card, `did:key` (from Anton's stack)
- Answering trust questions: "how strong is the chain from me to X?" (the computation is an app topic, the data is here)

**Differentiation:**

| Layer | Domain | Mnemonic |
|-------|--------|----------|
| Access | [login/](../login/index.md) | a login proves **no** identity |
| Person data | [people/](../people/index.md) | what is known about the person |
| Self-image | [profile/](../profile/index.md) | what they show about themselves |
| **Trust in the image others have** | **identity/** | **whom one trusts** |

**Standard status:** ❌ no established WoT spec **in a standards body** was found. But: Anton's **WoT Spec v0.1.0-draft** (✅ repo reviewed) combines W3C **Verifiable Credentials**, **DIDComm v2.1**, **Ed25519**, **ECIES**; the successor **RLTP** (gen 3) lives in `real-life-org/trust-protocol`. That is our docking point — own/co-authored spec, spec candidate no. 2.
