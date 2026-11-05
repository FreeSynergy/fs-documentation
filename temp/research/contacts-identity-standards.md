# Contacts + Identity: Standards Fact-Check

Researched: 2026-11-05 · by: Claude subagent

Scope: the FreeSynergy data domains **contacts** and **identity**. Only primary sources were used (rfc-editor.org, datatracker.ietf.org, w3.org/TR, codeberg.org/fediverse/fep, docs.joinmastodon.org, github.com/real-life-org, plus schema.org for its own term).
✅ = seen in the primary source · ⚠️ = inference, or an absence that cannot be proven

---

## 1. RFC 9553: JSContact (Standards Track, May 2024)

### (a) `Card.kind` ✅
Optional, default `"individual"`. The enumerated values are **`individual`, `group`, `org`, `location`, `device`, `application`**. Vendor-specific values such as `"example.com:baz"` are also allowed (§1.8.2).
> "kind: String (optional; default: "individual"). The kind of the entity the Card represents."
URL: https://www.rfc-editor.org/rfc/rfc9553#section-2.1.4

### (b) Vendor-specific extensions: §1.8 / §1.8.1 (properties), §1.8.2 (values) ✅
A property name is formed as `<domain-prefix>:<name>` (ABNF `v-extension = v-prefix ":" v-name`). The prefix MUST be a domain name under the vendor's control. It does not have to resolve. `ietf.org` and its subdomains are reserved. The name MUST NOT contain `~` or `/`. The value can be any JSON value. Vendor properties MAY appear in any JSContact object, and implementations **MUST preserve** them.
> "Vendor-specific property names MUST start with a vendor-specific prefix followed by a name … The vendor-specific prefix MUST be a domain name under control of the service or application"
URL: https://www.rfc-editor.org/rfc/rfc9553#section-1.8.1
→ Suggested CRM field: `"freesynergy.org:lifecycle": "lead"`. This assumes the project controls the domain `freesynergy.org`, which is ⚠️ and needs checking. The RFC strongly encourages IANA registration (§3) if other systems need to interoperate on the field.

### (c) `relatedTo` / `relation` ✅
Yes. `Card.relatedTo` is `String[Relation]`. Each key is the **uid of the related Card**, and the `Relation.relation` value is a set of type→true. The initial values match the vCard RELATED TYPE values (RFC 6350 §6.6.6): `acquaintance, agent, child, co-resident, co-worker, colleague, contact, crush, date, emergency, friend, kin, me, met, muse, neighbor, parent, sibling, spouse, sweetheart`. If the set is empty, the relationship is undefined.
> "The set of Card objects that relate to the Card. The value is a map, where each key is the uid property value of the related Card"
URL: https://www.rfc-editor.org/rfc/rfc9553#section-2.1.8
No relation value means "same person / duplicate". `me` is inherited from vCard and is used for the user's own card. It is not an alias marker (⚠️ interpretation). The only identity semantics is `uid`: "An identifier that associates the object as the same across different systems, address books, and views" (§2.1.9). The RFC recommends UUID **v4** for `uid`.

### (d) Merge / alias of two cards ⚠️ (none found)
I grepped RFC 9553, 9554, 9555 and 9610 (JMAP for Contacts) for "merge", "alias", "same person" and "duplicate" and found no merge or alias mechanism. The newer CALEXT outputs (datatracker, calext WG) don't add one either:
- **RFC 9982** (May 2026, Standards Track, updates 9555): "JSContact Version 2.0". It makes `uid` **optional** and changes nothing else. ✅ https://www.rfc-editor.org/rfc/rfc9982
- **RFC 10050** (Sept 2026, Standards Track): "Protocol-Specific Profiles for JSContact" (profiles registry). ✅ https://www.rfc-editor.org/rfc/rfc10050
- Active drafts: `draft-ietf-calext-jscontact-cryptographic-key`, `draft-ietf-calext-rfc9555bis`, `draft-ietf-calext-vcard4-bis`. None of them is about merging, judging by their titles (⚠️ titles only).
→ Merging duplicates is application logic. Options are keeping the same `uid`, or a vendor property such as `"freesynergy.org:mergedInto"`.

---

## 2. ActivityStreams 2.0 Vocabulary (W3C Recommendation, 23 May 2017) ✅
URL: https://www.w3.org/TR/activitystreams-vocabulary/

- **`Profile`** (`as:Profile`): "A Profile is a content object that describes another Object, typically used to describe Actor Type objects. The describes property is used to reference the object being described by the profile."
- **`describes`**: "On a Profile object, the describes property identifies the object described by the Profile." Domain `Profile`, range `Object`.
- **`Relationship`**: "Describes a relationship between two individuals. The subject and object properties are used to identify the connected individuals." Its properties are `subject | object | relationship`, and it inherits all Object properties.
  - **`subject`**: "identifies one of the connected individuals … for a Relationship object describing 'John is related to Sally', subject would refer to John." Domain Relationship, range Link | Object.
  - **`relationship`**: "identifies the kind of relationship that exists between subject and object." Domain Relationship, range Object.
- **"same as" in AS2**: ⚠️ none. The text "sameAs" doesn't appear anywhere in the vocabulary document.
- **`owl:sameAs`** ✅ (https://www.w3.org/TR/owl-ref/): "owl:sameAs links an individual to an individual. Such an owl:sameAs statement indicates that two URI references actually refer to the same thing". This is a strict identity claim: all statements carry over between the two.
- **`schema:sameAs`** ✅ (https://schema.org/sameAs): "URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website." This is weaker and pragmatic.
- Fediverse practice ✅ (https://docs.joinmastodon.org/spec/activitypub/): Mastodon uses **`alsoKnownAs`** for account aliases. It is required for `Move`: "Mastodon checks that the new account has defined an alias pointing to the old account (via the alsoKnownAs property)".

---

## 3. RFC 9562: UUIDs ✅
- Published **May 2024**, **Proposed Standard**. **Obsoletes RFC 4122** (header: "Obsoletes: 4122").
- v7 (§5.7): "UUIDv7 features a time-ordered value field derived from the widely implemented and well-known Unix Epoch timestamp source, the number of milliseconds since midnight 1 Jan 1970 UTC, leap seconds excluded."
- URL: https://www.rfc-editor.org/rfc/rfc9562#section-5.7
- Note: JSContact §2.1.9 recommends **UUIDv4** for `uid`. UUIDv7 is still a valid `urn:uuid:` value.

---

## 4. HTTP Message Signatures + Fediverse signatures
- **RFC 9421** "HTTP Message Signatures": **February 2024**, **Proposed Standard**. ✅ https://www.rfc-editor.org/rfc/rfc9421
- **FEP-8b32** "Object Integrity Proofs": status **DRAFT** (received 2022-11-12). It uses W3C **Data Integrity** with proof type `DataIntegrityProof` and `proofPurpose: assertionMethod`. "[eddsa-jcs-2022] cryptosuite is RECOMMENDED". ✅ https://codeberg.org/fediverse/fep/src/branch/main/fep/8b32/fep-8b32.md
- **FEP-521a** "Representing actor's public keys": status **FINAL** (finalized 2025-06-14). It uses `Multikey` objects (Controlled Identifiers v1.0 §2.2.2) in `assertionMethod`, replacing the deprecated `publicKey`. ✅ https://codeberg.org/fediverse/fep/src/branch/main/fep/521a/fep-521a.md
- **FEP-844e** "Capability discovery": status **DRAFT** (received 2025-06-14). It is **not a signature spec**. It defines `implements` on an `Application` object, and its examples advertise RFC 9421 (Ed25519, ml-dsa-44) as capabilities. ✅ https://codeberg.org/fediverse/fep/src/branch/main/fep/844e/fep-844e.md
- Related: FEP-c390 Identity Proofs (DRAFT) and FEP-ef61 Portable Objects (DRAFT). ✅
- **Mastodon is moving to RFC 9421** ✅ (https://docs.joinmastodon.org/spec/security/):
  - 4.4.0 can verify RFC 9421 signatures behind a feature flag. 4.5.0 enables verification by default.
  - 4.7.0 (unreleased) adds Ed25519 verification. It also signs outgoing requests with RFC 9421 as a fallback when a request signed with the cavage draft fails with 400/401. RSA-PKCS1-v1_5-SHA256 is "still" the only supported algorithm.
  - Quote: "we strongly suggest implementers to also implement the up-to-date HTTP Message Signatures (RFC9421) … as we intend to eventually move away from this earlier draft."
  - 4.7.0 (unreleased) also verifies FEP-8b32 proofs with `eddsa-jcs-2022` and `mldsa44-jcs-2024`.

---

## 5. W3C identity specs ✅ (status taken from each /TR/ page)
| Spec | Status / date | URL |
|---|---|---|
| DID Core v1.0 | **Recommendation, 19 July 2022** | https://www.w3.org/TR/did-core/ |
| DID v1.1 | **Candidate Recommendation Snapshot, 05 March 2026**. Not yet a Recommendation | https://www.w3.org/TR/did-1.1/ |
| VC Data Model v2.0 | **Recommendation, 15 May 2025** | https://www.w3.org/TR/vc-data-model-2.0/ |
| VC Data Integrity 1.0 | **Recommendation, 15 May 2025** | https://www.w3.org/TR/vc-data-integrity/ |
| Data Integrity EdDSA Cryptosuites v1.0 (`eddsa-rdfc-2022`, `eddsa-jcs-2022`) | **Recommendation, 15 May 2025** | https://www.w3.org/TR/vc-di-eddsa/ |
| Controlled Identifiers v1.0 (Multikey) | **Recommendation, 15 May 2025** | https://www.w3.org/TR/cid-1.0/ |
| Quantum-Resistant Cryptosuites v1.0 | First Public Working Draft, 16 June 2026 | https://www.w3.org/TR/vc-di-quantum-resistant-1.0/ |

---

## 6. SCIM ✅ (rfc-editor metadata + datatracker scim WG)
| RFC | Title | Date | Status |
|---|---|---|---|
| 7643 | System for Cross-domain Identity Management: Core Schema | Sept 2015 | Proposed Standard, updated by 9865 and 9967 |
| 7644 | System for Cross-domain Identity Management: Protocol | Sept 2015 | Proposed Standard, updated by 9865 and 9967 |
| 9865 | Cursor-Based Pagination of SCIM Resources | Oct 2025 | Proposed Standard (updates 7643, 7644) |
| 9944 | Device Schema Extensions to the SCIM Model | May 2026 | Proposed Standard |
| 9967 | SCIM Profile for Security Event Tokens (SETs), i.e. "SCIM events" | May 2026 | Proposed Standard (updates 7643, 7644) |

Active WG drafts: `draft-ietf-scim-roles-entitlements`, `draft-ietf-scim-use-cases-reloaded`.
URLs: https://www.rfc-editor.org/rfc/rfc7643 · https://www.rfc-editor.org/rfc/rfc7644 · https://www.rfc-editor.org/rfc/rfc9865 · https://www.rfc-editor.org/rfc/rfc9967 · https://datatracker.ietf.org/wg/scim/documents/

---

## 7. MLS
- **RFC 9420** "The Messaging Layer Security (MLS) Protocol": **July 2023**, **Proposed Standard**. ✅ https://www.rfc-editor.org/rfc/rfc9420
  RFC 9750 (MLS Architecture) is in the same WG.
- **X.509**: already built into RFC 9420. Credential type `0x0002 x509` is registered next to `basic`. ✅ (§5.3, IANA table)
- **Other credential drafts** (datatracker, mls WG page) ✅:
  - `draft-mahy-mls-sd-cwt-credential-03`, "MLS Credentials using Selective Disclosure JSON and CBOR Web Tokens".
  - `draft-mahy-mls-credential-by-ref-00`, "Credentials By-Reference in MLS".
  - `draft-ietf-mls-extensions`.
- **DID-bound MLS credential**: ⚠️ none found. A datatracker title/name search for MLS combined with DID or "decentralized identifier" found no draft. Neighbouring documents exist, e.g. `draft-birkholz-did-x509` (did:x509 method), but nothing MLS-specific.

---

## 8. real-life-org/trust-protocol (RLTP, generation 3) ✅
URL: https://github.com/real-life-org/trust-protocol (Apache-2.0, spec text CC BY 4.0, created 2026-08-10)
- **Activity**: last commit **2026-11-05 05:57 UTC** (PR #153, site/deck navigation). The repo is very active.
- **Versions**:
  - All spec documents are **Editor's Drafts**.
  - Converged layers: Encounter 0.32, Identity 0.55, Access 0.58, Delivery Contract 0.85, Membership Tasks 0.21, Replication 0.26, Trust 0.31, Personhood Predicates 0.12.
  - Message Tasks 0.2 is an early casting. Succession 0.2 is parked. The Data layer is not published.
  - Library `@real-life/trust-protocol` **0.12.0** (lib/package.json).
- **Layers**: 1 Identity, 2 Encounter, 3 Trust, 4 Access, 5 Data. Delivery and Replication are "services behind ports".
- **DIDs**: Ed25519 **`did:key`**. "The waist is narrow — and in the 0.x stack it is `did:key`" (spec/identity-layer.md).
  - Identity is derived from one root seed: community anchor with pre-rotation, **per-relationship pair anchors**, per-group member anchors, and service identities.
  - "Relationships never converge into a person."
- **Credential format**:
  - **W3C VC 2.0** (`https://www.w3.org/ns/credentials/v2`). Encounter credentials have type `VerifiableCredential, DTGCredential, RelationshipCredential, EncounterCredential`.
  - Proofs are embedded `DataIntegrityProof` with **`eddsa-jcs-2022`**. Digests are multibase multihash over JCS (RFC 8785).
  - Aligned with ToIP DTGWG (Trust Tasks).
- **Transport**: "The specification names no transport and no CRDT". The first delivery adapter binds **ToIP TSP via the VTI mediator**. The Replication Contract maps p2panda, Keyhive, SECSYNC, NextGraph and Automerge.
- **real-life-org/web-of-trust**: ⚠️ **not formally deprecated or archived**. It isn't archived, and its last push was 2026-11-05. The README calls it "**generation 2** … in production" and names RLTP as the "successor": "Fixes here move toward generation 3. Users move to generation 3 once their identities are migrated, planned as the last step."
  - Gen 2 is specified in `real-life-org/wot-spec` (v0.1.0-draft: W3C VC, DIDComm v2.1, Ed25519, ECIES).
  - Status: superseded in design, but still the production line.
