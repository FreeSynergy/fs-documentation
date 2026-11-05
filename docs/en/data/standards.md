# Data standards (state of 2026-10-31)

This file decides **which existing standard covers which data area**. Goal:
invent nothing where something already exists; and where we do invent, do it
knowingly.

**Evidence:** every entry has a status.

| Status | Meaning |
|--------|---------|
| ✅ evidenced | specification retrieved 2026-10-31 directly from the RFC Editor or w3.org, title/number/field names checked |
| ⚠️ unchecked | known to me, **not** looked up in this round — evidence it before use |
| ❌ evidenced that it does not exist | negatively checked (the source does not contain the term / the answer was 404) |

## Basic decision: three separate layers

Conflicts arise not between formats but between **field names**. So we
separate:

| Layer | Question | Our rule |
|-------|----------|----------|
| **Storage** | what does a record look like in the database? | existing JSON/text models, field-accurate (JSContact, JSCalendar, GeoJSON, …) |
| **Transport** | how do programs talk to each other? | envelope: AS2/ActivityPub; Cap'n Proto internally (ADR 0021), JSON-LD externally — **both derived projections** of the canonical standard model (decision 4) |
| **Vocabulary** | what are the fields called on the outside? | one canon internally, one mapping table per target system |

Rule no. 1: **one field, one owner.** `name` belongs to the resource, not to
the module. No module gets a `crmContactName`.

## Evidenced standards per data area

### Contacts, people, organisations

| Standard | Evidence | Coverage |
|----------|----------|----------|
| **vCard Format Specification, RFC 6350** | ✅ | data exchange. Property names checked: `FN`, `N`, `NICKNAME`, `PHOTO`, `BDAY`, `ANNIVERSARY`, `GENDER`, `ADR`, `TEL`, `EMAIL`, `IMPP`, `LANG`, `TZ`, `GEO`, `TITLE`, `ROLE`, `LOGO`, `ORG`, `MEMBER`, `RELATED`, `CATEGORIES`, `NOTE`, `PRODID`, `REV`, `SOUND`, `UID`, `CLIENTPIDMAP`, `URL`, `VERSION`, `KEY`, `FBURL`, `CALADRURI`, `CALURI`, `KIND`, `SOURCE`, `BEGIN`/`END`, `XML` |
| **jCard: The JSON Format for vCard, RFC 7095** | ✅ | JSON form of vCard |
| **xCard: vCard XML Representation, RFC 6351** | ✅ | XML form (not CardDAV — see the correction list) |
| **CardDAV, RFC 6352** | ✅ | access/sync to contact folders |
| **JSContact: A JSON Representation of Contact Data, RFC 9553** | ✅ | **the most interesting find**: a modern, pure-JSON contact model. `Card` with `@type`, `version`, `uid`, `name`, `nicknames`, `organizations`, `titles`, `emails`, `onlineServices`, `phones`, `preferredLanguages`, `calendars`, `schedulingAddresses`, `addresses`, `cryptoKeys`, `directories`, `links`, `media`, `localizations`, `anniversaries`, `keywords`, `notes`, `personalInfo` |
| **vCard Format Extensions for JSContact, RFC 9554** | ✅ | the official JSContact ↔ vCard bridge, which makes the choice "JSContact as storage" connectable |

In JSContact `name` is **not a string** but an object `Name` with
`components[]` (`kind` = `title`, `given`, `given2`, `surname`, `surname2`,
`credential`, `generation`, `separator`), plus `full`, `isOrdered`,
`defaultSeparator`, `sortAs`, `phonetic`. That is much better than
`firstName`/`lastName` — it covers Chinese, Spanish and Icelandic names without
us having to invent a field.

**`lifecycle` (lead/prospect/customer/churned) from our CRM does not exist in
vCard 4.0** (❌ evidenced: the term occurs nowhere in RFC 6350). That is a real
gap — see "What we have to invent".

### Calendars, appointments, participants, tasks

| Standard | Evidence | Coverage |
|----------|----------|----------|
| **iCalendar, RFC 5545** | ✅ | core format; `RRULE` is already part of it |
| **jCal: The JSON Format for iCalendar, RFC 7265** | ✅ | JSON form of iCalendar |
| **JSCalendar: A JSON Representation of Calendar Data, RFC 8984** | ✅ | **second key find**. Object types `Event`, `Task`, `Group`. Properties checked: `@type`, `uid`, `relatedTo`, `prodId`, `created`, `updated`, `sequence`, `method`, `title`, `description`, `descriptionContentType`, `showWithoutTime`, `locations`, `virtualLocations`, `links`, `locale`, `keywords`, `categories`, `color`, `recurrenceId`, `recurrenceRules`, `excludedRecurrenceRules`, `recurrenceOverrides`, `excluded`, `priority`, `freeBusyStatus`, `privacy`, `replyTo`, `sentBy`, `participants`, `requestStatus`, `useDefaultAlerts`, `alerts`, `localizations`, `timeZone`, `timeZones`; event: `start`, `duration`, `status`; task: `due`, `start`, `estimatedDuration`, `percentComplete`, `progress`, `progressUpdated` |
| **Participant model in RFC 8984** | ✅ | `name`, `email`, `description`, `sendTo` (`imip`, `other`), `kind` (`individual`, `group`, `location`, `resource`), `roles` (mandatory, at least one: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact`), `locationId`, `language`, `participationStatus` (`needs-action`, `accepted`, `declined`, `tentative`, `delegated`), `participationComment`, `expectReply`, `scheduleAgent`, `scheduleForceSend` |
| **iTIP, RFC 5546** | ✅ | invitation protocol (request/reply/withdraw) |
| **CalDAV Scheduling Extensions, RFC 6638** | ✅ | calendar server integration |
| **Calendar Collection Synchronization (CalDAV SYNC), RFC 6578** | ✅ | sync mechanism — our field `syncToken` has its evidence here |
| **Event Publishing Extensions to iCalendar, RFC 9073** | ✅ | new properties `STYLED-DESCRIPTION` (rich-text description, `VALUE=TEXT` or `VALUE=URI`, `FMTTYPE`, `DERIVED`) and `STRUCTURED-DATA` (arbitrary structured data on an appointment, e.g. `application/ld+json`) |
| **"VALARM" Extensions for iCalendar, RFC 9074** | ✅ | our `reminders` |
| **Parameter Value Encoding in iCalendar and vCard, RFC 6868** | ✅ | escape rules both formats share |

JSCalendar is more interesting for us than jCal: jCal is the JSON shell **over
the iCalendar grammar** (property lists with parameters), JSCalendar is a real
object model. For a database JSCalendar would be the working representation,
jCal/iCalendar the export.

Note the naming conflict that **the standards themselves** have: JSCalendar
uses `title` for the display name, JSContact uses `name` (as an object),
schema.org uses `name`, AS2 uses `name`. That cannot be resolved by choosing
"the one standard" — it can only be resolved by a rule (see `mappings.md`).

### Activities, notifications, webhooks

| Standard | Evidence | Coverage |
|----------|----------|----------|
| **Activity Streams 2.0 Core + Vocabulary (W3C Recommendation 2017)** | ✅ (status corrected 2026-11-05) | `@context: "https://www.w3.org/ns/activitystreams"`; `id` is an **absolute IRI** (Core §4.1); relative IRIs should not be used (§2.2); media type `application/activity+json` is registered with IANA in Core §8.1; language variants via `nameMap`, `contentMap`, `summaryMap`; `Link` objects with `href`, `mediaType`, `width`, `height` |
| **AS2 does not contain the type `Hashtag`** | ❌ evidenced | the term occurs nowhere in Core or Vocabulary. Mastodon defines `Hashtag` as a subtype of `Link` and refers to `activitystreams#Hashtag` — an extension, not the core |
| **schema.org has no type `Hashtag`** | ❌ evidenced | `schema.org/Hashtag` returns HTTP 404 |
| **AS2 is not an RFC** | ❌ evidenced | RFC 9332 is "Dual-Queue Coupled Active Queue Management (AQM) …" — nothing to do with ActivityStreams. Anyone citing AS2 cites the W3C report |
| **WebFinger, RFC 7033** | ✅ | discovering actors via `acct:` / e-mail |
| **W3C Web Annotation Model** | ✅ | motifs incl. `classifying`, `tagging`, `commenting`, `describing`, `editing`, `bookmarking`; selectors `TextQuoteSelector`, `TextPositionSelector`, `RangeSelector`; structure `body` / `target`. **This is the right standard for "giving a part of a text a tag" without rewriting the text** |
| **AS2 `Profile` + `describes`** | ✅ 2026-11-05 | "describes another object, usually an actor" — **envelope type for contact cards** (ADR 0020): a card is *my description* of someone, `describes` points to that person's actor/DID |
| **AS2 `Relationship` (`subject`, `object`, `relationship`)** | ✅ 2026-11-05 | envelope for attestations and for confirmed "same person" links. AS2 itself has **no** "same as" property (✅ checked) |
| **JMAP, RFC 8620 (basis) and RFC 8621 (mail)** | ✅ | reference for how to address, patch and synchronise JSON resources cleanly |

### Places, files, API cross-section

| Standard | Evidence | Coverage |
|----------|----------|----------|
| **The GeoJSON Format, RFC 7946** | ✅ | geometries |
| **`geo:` URI, RFC 5870** | ✅ | required in JSContact `Address.coordinates` |
| **Language Tags, RFC 5646** | ✅ | used in JSContact/JSCalendar for `language`/`locale` |
| **Addr-spec, RFC 5322 §3.4.1** | ✅ | JSCalendar `Participant.email` must follow this format |
| **Web Linking, RFC 8288** | ✅ | `Link` header, pagination |
| **Problem Details for HTTP APIs, RFC 9457** | ✅ | our error block in `api.md` is a variant of it |
| **JSON Patch, RFC 6902** | ✅ | partial changes; JSContact and JSCalendar both define their own patch object (`PatchObject` in RFC 9553, paths like `participants/<id>/participationStatus` in RFC 8984) |

### Further sources whose reachability was checked (HTTP 200)

| Source | URL checked | Status |
|--------|-------------|--------|
| ODRL License Vocabulary (rights-structured statements) | `https://www.w3.org/TR/odrl-model/` | ✅ URL checked, **content not read** |
| W3C Organization Ontology (teams, hierarchy, roles) | `https://www.w3.org/TR/vocab-org/`, `https://www.w3.org/ns/org` | ✅ URL checked, **content not read** |
| LD Vocabulary: Personal Information (field names for people) | `https://www.w3.org/TR/ldp/` | ✅ URL checked, **content not read** |
| JSON-LD 1.1 | `https://www.w3.org/TR/json-ld11/` | ✅ URL checked |
| Activity Streams 2.0 Core / Vocabulary | `https://www.w3.org/TR/activitystreams-core/`, `https://www.w3.org/TR/activitystreams-vocabulary/` | ✅ content read |
| Web Annotation Model | `https://www.w3.org/TR/annotation-model/` | ✅ content read |

## Naming: what the standards actually say

Evidenced 2026-10-31 directly at schema.org:

| Term | Evidence | Definition |
|------|----------|------------|
| `name` | ✅ | `Thing > Property :: name`, subproperty of `rdfs:label`; listed as equivalent: `cmns-txt:hasName`, `dct:title`, `og:title` |
| `headline` | ✅ | `Thing > Property :: headline`, "Headline of the article", used on `CreativeWork` |
| `Article` | ✅ | `Thing > CreativeWork > Article` |

So for a text/document the following already holds today: **`name` is the
general display name, `headline` specifically is the headline of a work.** Two
different things — we should keep them apart in the heading topic.

## What we have to invent (survey so far)

| Gap | State |
|-----|-------|
| `Contact.lifecycle` (lead/prospect/customer/churned) | ❌ not in vCard 4.0; replacement not found so far → **real gap** |
| Board/project structure (board → list → task → relations, WBS) | ⚠️ the candidates (W6C XML Schema, MSPDI, PMI WBS) are **not evidenced**. Check them first, then decide |
| Whiteboard: shapes, layers, z-order as a queryable model | ⚠️ InkML found as an old W3C contribution; **no successor document found** — my earlier claim about an "Ink Annotation Module" was unevidenced and is withdrawn |
| ERP: invoice, order, article, amounts | ⚠️ EN 16931 / CII / XRechnung / Peppol / GS1 / ISO 4217 / IBAN **not looked up in this round**. Evidence each one before use |
| "A heading in the text becomes the `name` of the resource" | ❌ no standard found that prescribes this. But there are building blocks: Web Annotation (`classifying`, `RangeSelector`), AS2 `name`/`nameMap`, schema.org `headline`. The **rule** would have to be our own |

## Correction list

Mistakes from the earlier conversation, so they do not end up in a file:

| Said wrongly | Correct (evidenced) |
|--------------|---------------------|
| "jCard = RFC 9073, jCal = RFC 9074" | **jCard = RFC 7095, jCal = RFC 7265**. RFC 9073 = Event Publishing Extensions, RFC 9074 = VALARM Extensions |
| "AS2 = RFC 9332" | AS2 has **no** RFC. RFC 9332 = Dual-Queue Coupled AQM |
| "vCard 4.0 (RFC 6350/6351)" implying CardDAV | RFC 6351 = **xCard**. CardDAV = **RFC 6352** |
| "RRULE extension RFC 7953" | RFC 7953 = **Calendar Availability**. RRULE is part of RFC 5545 |
| schema.org version "16.0" | a made-up number. Checked: schema.org says "V30.1 \| 2026-09-16" on the pages retrieved |
| "W3C is currently producing an Ink Annotation Module" | unevidenced, withdrawn |
| "E-invoicing: receiving from 2025, issuing 2027/2028" | **not looked up in this round** — do not use as a deadline |
| "ActivityPub signs with `Authorization: Signature`, reference `w3id.org/security/httpsig`" | that reference returns **HTTP 404**. **Resolved 2026-11-05:** HTTP Message Signatures **RFC 9421** (Feb 2024, ✅); object proofs **FEP-8b32** (draft, Data Integrity `eddsa-jcs-2022`, ✅); keys as `Multikey` per **FEP-521a** (final 2025-06-14, ✅). Mastodon verifies RFC 9421 since 4.5.0 (✅). Details: `temp/research/contacts-identity-standards.md` |

## Decisions (2026-11-01)

| No. | Decision |
|-----|----------|
| 1 | **Canonical payload per domain:** contacts → JSContact (RFC 9553/9554), appointments and tasks → JSCalendar (RFC 8984, covers `Event` **and** `Task`), places/addresses → GeoJSON + JSContact `Address` (+ ISO 19160, ✅ URL checked), messages → AS2 `Note`/`Article`, profile → AS2 `Actor` projection onto JSContact. |
| 2 | **Envelope for every exchange: ActivityStreams 2 + ActivityPub.** Changes going out are `Create`/`Update`/`Delete` on typed objects; the domain payload is carried by the object as an extension. `to`/`cc`/`bto`/`bcc` are disclosure control (they decide **where copies land**) — but **not access control**; authorization is enforced per resource separately. |
| 3 | **IDs:** internally **UUIDv7, RFC 9562** (time-sortable standard, ✅; replaces ULID 2026-11-05, ADR 0027) — externally absolute IRI `https://<instance>/<domain>/<uuid>` (AS2 Core §4.1 requires absolute IRIs — ✅ evidenced). The IRI is the resolvable handle, the UUIDv7 the stable identity (host migration stays possible, decentralised operation included). |
| 4 | **The source of truth is the evidenced standard model** (JSContact, JSCalendar, …). We use Cap'n Proto internally (ADR 0021), JSON-LD/AS2 externally — both as projections generated from it. (Corrects the earlier direction "protobuf as the only source".) |
| 5 | **Extend instead of invent:** first use the standard's extension points (e.g. `extensions` in JSContact for `lifecycle` — ⚠️ mechanism still to be evidenced); only where those do not exist, design our own specs. |

**Still open (deliberately not decided):**

1. **The `name` rule:** one mandatory field `name` for everything
   nameable, `title`/`headline`/`displayName` only as export aliases?
   *Proposal 2026-11-05 (ADR 0030):* content standards keep their own field (`title` in JSCalendar,
   `name.full` in JSContact, subject in mail); the **AS2 envelope always has `name`**, derived from it.
   Nothing is renamed; cross-program views read only the envelope.
2. **Publication paths for our own specs:** W3C community groups (AS2
   kinship: Social Web Incubator CG) vs. IETF datatracker — to be chosen per
   spec individually.

The earlier open decision "reach" is answered by decisions 1+4: the standards
apply **all the way into the database** (working representation); file formats
are export.

## AS2 mapping per domain (ADR 0014, 0020)

Every stored object = **AS2 envelope** (`id`, `type`, `attributedTo`, `to`/`cc`/`bto`/`bcc`/`audience`,
`published`, `updated`, `context`) + **domain content** + **activity log** (`Create`, `Update`, …).

| Domain | Content standard | AS2 envelope type | State |
|--------|------------------|-------------------|-------|
| contacts | JSContact `Card` (RFC 9553) | `Profile` (`describes` → person's actor/DID) | ✅ 2026-11-05 |
| identity — own person | DID document / Controlled Identifier (W3C) | `Person` (actor) with `Multikey` (FEP-521a) | ✅ 2026-11-05 |
| identity — attestation | VC 2.0 + `eddsa-jcs-2022` (as RLTP) | `Relationship` | ✅ 2026-11-05 |
| identity — same person (hub matching, ADR 0019) | — | `Relationship`, relation `owl:sameAs` | decided 2026-11-05 (ADR 0029) |
| messages | chat: MIMI content (draft -10); e-mail: original MIME + JMAP `Email` fields; Matrix events | `Note` (`context` = conversation) | ✅ 2026-11-05, see [messages/](messages/standards.md) |
| events | **JSCalendar 2.0** (`draft-ietf-calext-jscalendarbis-22`) `Event`/`Task` | `Event`; log `Invite`/`Accept`/`TentativeAccept`/`Reject` | ✅ 2026-11-05, see [events/](events/standards.md) |
| documents | text: original + CommonMark/GFM; blocks: own spec; structure: schema.org `Book`/`Collection`; annotations: Web Annotation | `Article`, `Document`, `Collection`/`OrderedCollection`, `Annotation` | ✅ 2026-11-05, see [documents/](documents/standards.md) |
| geodata | GeoJSON (JSON-FG 1.0 where needed); in images Exif 3.1 + XMP + IPTC 2025.1 | `Place` | ✅ 2026-11-05 |
| projects | JSCalendar 2.0 `Task` + RFC 9253/10051 semantics; board: own spec | `Collection` (board), task envelope; ForgeFed `TicketDependency` | ✅ 2026-11-05 |
| profile | JSContact (self card) | `Profile` (`describes` → myself) | ✅ 2026-11-05 |
| login | OIDC / WebAuthn L3 / SCIM; federation: OpenID Federation 1.0 (proposed) | `Person` actor, WebFinger | ✅ 2026-11-05 |

## Gaps → own specifications (ADR 0014)

| Gap | Evidence | Candidate |
|-----|----------|-----------|
| merging/aliasing two cards of the same person | ❌ none in RFC 9553/9554/9555/9610/9982/10050 (✅ checked 2026-11-05) | hub-matching spec (ADR 0019) |
| `Contact.lifecycle` | ❌ in vCard/JSContact; extension mechanism ✅ (RFC 9553 §1.8.1) | vendor property `freesynergy.net:lifecycle` (ADR 0028), later CRM spec |
| marking of sensitive data (GDPR Art. 9 categories) | ⚠️ W3C DPV candidate, unchecked | ADR 0029 |
| board/project structure | ❌ | spec candidate no. 3 |
| Web of Trust | ❌ in standards bodies | co-author with RLTP; trust-mark profile for OpenID Federation |
| task relations "blocks"/"duplicates" in JSCalendar | ❌ | relation vocabulary (OpenProject set as reference) |
| profile field → DPV category table, consent record | ❌ | ADR 0029 |
| SCIM provisioning server (Kanidm is sync-source only) | ❌ in Kanidm | own SCIM server in the hub |
| WebFinger link profile (actor, OIDC issuer, DID) | ❌ | discovery spec |

## Domain directories

Every data domain has a directory with `index.md`, `description.md`,
`technical.md`, `standards.md`, `examples.md` (decision 2026-11-02, see
[requirements.md → §4](requirements.md)); each standard inside it additionally
has a subdirectory with `description.md` + `storage.md` (schema analogous to
components):

| Domain | Directory |
|--------|-----------|
| Contact data | [contacts/](contacts/index.md) |
| Messages | [messages/](messages/index.md) |
| Appointments | [events/](events/index.md) |
| Geodata | [geodata/](geodata/index.md) |
| Login / accounts | [login/](login/index.md) |
| Identity (Web of Trust) | [identity/](identity/index.md) |
| Profile | [profile/](profile/index.md) |
| Documents | [documents/](documents/index.md) |
| Projects | [projects/](projects/index.md) |

## Follow-up research 2026-11-02 — the evidence is fully here, do not download it again

> **Rule (explicit instruction 2026-11-02):** Everything that was retrieved
> and written down here is recorded in the document in full. **It does not have
> to be loaded from the web again.** Only do follow-up research where an entry
> is expressly marked ⚠️ as unchecked.

### Login: OIDC, OAuth, WebAuthn (retrieved 2026-11-02 directly)

| Standard | Evidence | What is evidenced (quote/excerpt, so nothing has to be loaded again) |
|----------|----------|-----------------------------------------------------------------------|
| **OpenID Connect Core 1.0, incorporating errata set 2** | ✅ retrieved 2026-11-02 at `openid.net/specs/openid-connect-core-1_0.html` | "OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It enables Clients to verify the identity of the End-User based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User." Authors: Sakimura, Bradley, Jones, de Medeiros, Mortimore; final with errata set 2, **2023-12-15**. Core parts: ID token, authorization code flow, token endpoint, ID-token validation, claims about the end user. → **moved from ⚠️ to ✅** |
| **The OAuth 2.0 Authorization Framework, RFC 6749** | ✅ retrieved 2026-11-02 at `rfc-editor.org/rfc/rfc6749` | October 2012, Proposed Standard, obsoletes RFC 5849 (OAuth 1.0). The RFC editor notes updates by **RFC 8252** (native apps), **RFC 8996** (deprecating TLS 1.0/1.1) and **RFC 9700** (best current practices for OAuth security). → **moved from ⚠️ to ✅** |
| **Web Authentication: An API for accessing Public Key Credentials – Level 2 (WebAuthn)** | ✅ retrieved 2026-11-02 at `w3.org/TR/webauthn-2/` | W3C Recommendation **2021-04-08**. Quote from the abstract: "This specification defines an API enabling the creation and use of strong, attested, scoped, public key-based credentials by web applications, for the purpose of strongly authenticating users." Credentials are scoped per relying party. **Newly added to our login register.** |
| **SCIM, RFC 7643 (core schema) / RFC 7644 (protocol)** | ✅ 2026-11-05 | September 2015, Proposed Standard. Newer: **RFC 9865** (cursor pagination, Oct 2025), **RFC 9944** (device schema, May 2026), **RFC 9967** (SCIM events as Security Event Tokens, May 2026). Every program speaks SCIM (ADR 0024) |

### Identity / Web of Trust: Anton's repo reviewed (retrieved 2026-11-02, `github.com/real-life-org/web-of-trust`)

State of facts (written down in full, **do not download again**):

- Self-description: "A decentralized trust infrastructure for real-life communities. People meet in person, verify each other's identity via QR code, and build reputation through attestations over time. No central server sees your data. Everything is end-to-end encrypted and stored locally."
- **Principle: verification ≠ trust.** Verification only confirms "this really is that person" (personal meeting + QR scan). Trust arises only through **attestations over time**. That covers exactly our provisional rule 1 in [identity/index.md](identity/index.md) (attestations are their own objects).
- **Protocol: "WoT Spec" v0.1.0-draft** — combines **W3C Verifiable Credentials**, **DIDComm v2.1**, **Ed25519** and **ECIES**.
- Identity keys: **BIP39 mnemonic** (12 words) → HKDF master key → **Ed25519** (signature) + **X25519** (key agreement); DID method **`did:key`** (W3C DIDs).
- Encryption: AES-256-GCM (CRDT updates, group content), X25519-ECIES asymmetric, GroupKeys; relays only see ciphertext.
- Architecture: CRDT-based (Yjs default, Automerge alternative); services `wot-relay` (WebSocket, ACK+outbox), `wot-vault` (encrypted backup), `wot-profiles` (public profile discoverability, JWS-signed); authorization **UCAN-inspired**, verifiable offline.
- Generation 2 (this repo, ~2044 commits on 2026-11-02) has a successor: **Real Life Trust Protocol (RLTP), Gen 3**, in `real-life-org/trust-protocol`. Fixes move towards Gen 3.
- **Our docking points:** attestation ↔ AS2 `Relationship` object; `did:key`/Ed25519 ↔ `publicKey` on the actor; `wot-profiles` ↔ our `profile/` projection; keep an eye on RLTP.
- **Consequence for the register:** W3C **DID Core** and **VC Data Model** are evidenced *as cited* through Anton's spec.
- **Update 2026-11-05 (✅):** DID Core 1.0 = W3C Recommendation 2022-07-19 (DID 1.1 is Candidate Recommendation, 2026-03-05); **VC Data Model 2.0, Data Integrity 1.0, EdDSA cryptosuites, Controlled Identifiers 1.0** = Recommendations 2025-05-15. **RLTP gen 3** (`real-life-org/trust-protocol`, last commit 2026-11-05, library 0.12.0, Editor's Drafts): Ed25519 `did:key` with **separate identifiers per relationship**, credentials **VC 2.0 + `eddsa-jcs-2022`**, transport not fixed (first adapter: ToIP TSP via mediator). Gen 2 (`web-of-trust`) is still in production, not archived.

### Projects: standards search 2026-11-02 (search results, title evidence — not read in full text)

| Candidate | Evidence | Assessment |
|-----------|----------|------------|
| **ISO 21502:2020 "Project, programme and portfolio management — Guidance on project management"** (ISO/TC 258) | ✅ existence evidenced (ISO OBP register no. 74947, TC-258 page) | **process guidance, not a data format.** Useful for us as a vocabulary/role reference, not as a storage model. |
| **MSPDI — Microsoft Office Project 2007 XML Data Interchange Schema (`mspdi_pj12.xsd`)** | ✅ existence evidenced (Microsoft Learn docs on task elements, calendars; durations in tenths of a second) | **de-facto exchange format**, not a standard from an open standards body. Candidate import/export target. |
| **W6C XML Schema** | ⚠️ still unevidenced (did not come up in the search) | Do not use further until evidenced. |
| **JSON-Xchange for boards/tasks (RFC/W3C)** | ❌ nothing found again | Our **spec candidate no. 3 stands**; the basis remains JSCalendar `Task` (✅). |

**Result for open question 6.1:** there is no open ISO/DIN/RFC/W3C **data
standard** for project/board structures; ISO 21502 is process management, MSPDI
is a proprietary de-facto export. → our own spec, with JSCalendar `Task` as the
task object.

## See also

- [Data models](models.md)
- [Standard fields](fields.md)
- [Data formats](formats.md)
- [Field mappings](mappings.md)
- [Conventions](conventions.md)
- [Data API](api.md)
