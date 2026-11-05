# Research: Geodata · Projects · Profile · Login standards

Researched: 2026-11-05 · by: Claude subagent

Policy context: use the newest viable standard. Storage is original + AS2 envelope + content standard + activity log. IDs are UUIDv7. Identity: Kanidm (OIDC/SCIM) for login, DID + VC 2.0 between instances, Web of Trust (RLTP) for trust, and trust lists that act like an identity broker.
These items were verified elsewhere and are not repeated here: SCIM RFCs/dates, DID Core, VC 2.0, RFC 9421, FEP-8b32/521a, the AS2 profile, JSContact, JSCalendar 2.0 and RFC 10051 dates.

Legend: ✅ = verified against a primary source today · ⚠️ = secondary source, partly from memory, or unclear status.

---

## A. Geodata

### A1. ISO 19160 Addressing

| Part | Title | Status | Src |
|---|---|---|---|
| 19160-1:2015 | Conceptual model | published 2015-12-09, no newer edition | ✅ |
| 19160-2:2023 | Assigning and maintaining addresses for objects in the physical world | published 2023 | ✅ |
| 19160-3:2020 | Address data quality | published | ✅ |
| 19160-4:2023 | International postal address components and template language | **Ed. 2, 2023-04-13** (Ed. 1 was 2017) | ✅ |
| 19160-5 | Address rendering for purposes other than mail | **cancelled** (only a 2018 report exists) | ✅ |

- **Part 1 (conceptual model):** "defines a conceptual model for address information (address model) … Lifecycle, metadata, and address aliases are included … presented in UML." The model gives a common representation that lets you cross-map between national models. It does not replace them. Its core classes include `Address`, `AddressComponent` and `AddressableObject`.
  URL: https://committee.iso.org/sites/tc211/home/projects/projects---complete-list/iso-19160-1.html ✅
- **Part 4 (postal):** it "specifies postal address components organized into three hierarchical levels: elements … constructs … segments". Examples: the element "organization name / postcode", the construct "organization identification", and the segment "addressee specification". It also covers sub-elements such as door type and door indicator, plus **element codes**, **rendering rules (postal address templates)** and a **machine-processable template language**. It does not fix field lengths.
  URL: https://committee.iso.org/sites/tc211/home/projects/projects---complete-list/iso-19160-4.html ✅
- **Are the element names public?** ⚠️ Only partly. The scopes and the terms in the ISO OBP preview are visible. The full list of element and sub-element codes and the template language are behind the ISO paywall (they come from UPU S42). The ISO/TC 211 Harmonized Model on GitHub (https://github.com/ISO-TC211/HMMG) publishes the UML for 19160-1, so the Part 1 class and attribute names are effectively public. The Part 4 code table is not.

### A2. Open geodata standards (newest)

| Standard | Newest version / status | Quote / note | URL | Src |
|---|---|---|---|---|
| OGC API – Features | Part 1 Core **1.0.1** (corr.; = ISO 19168-1:2020); Part 2 CRS by Ref **1.0.1**; Part 3 Filtering **1.0** + CQL2 1.0.0; Part 5 Schemas **1.0.0** (IS, joint with Common Part 3); Part 4 CRUD = **draft** | "Part 4: Create, Replace, Update and Delete draft" | https://www.ogc.org/standards/ogcapi-features/ , https://ogcapi.ogc.org/features/ | ✅ |
| GeoJSON RFC 7946 | Aug 2016, Proposed Standard, **still current** (not obsoleted) | "uses … World Geodetic System 1984, and units of decimal degrees" | https://www.rfc-editor.org/info/rfc7946 | ✅ |
| JSON-FG (OGC Features & Geometries JSON) | **Part 1: Core 1.0.0, OGC IS 21-045r1, released 2026-05-21** | "valid JSON-FG features … are also valid GeoJSON" (adds CRS, `time`, `featureType`, `place`, solids) | https://www.ogc.org/standards/json-fg/ | ✅ |
| CityJSON | spec **2.0.2** (latest; 2026-03-27 tag); 2.0 = OGC Community Standard (20-072r5, Nov 2023) | "implements a subset of the OGC CityGML data model (version 3.0)" | https://www.cityjson.org/specs/overview/ | ✅ |
| GeoParquet | **v2.0.0, released 2026-11-05** (today; rc.1 2026-07-19; 1.1.0 2024) | "2.0 makes the native Parquet GEOMETRY and GEOGRAPHY types the foundation" | https://github.com/opengeospatial/geoparquet/releases | ✅ |
| FlatGeobuf | spec **v3** (stable since 2020); OGC Community Standard process started 2023 (public comment Feb–Mar 2023). I could not confirm final approval | "initial stable specification version … 3.0 … early in 2020" | https://flatgeobuf.org/ | ⚠️ |
| PMTiles | **Version 3** spec | "single-file archive format for tiled data … MIME application/vnd.pmtiles" | https://github.com/protomaps/PMTiles/blob/main/spec/v3/spec.md | ✅ |
| OSM data model | nodes, ways, relations + tags | "three types of elements: nodes … ways … relations" | https://wiki.openstreetmap.org/wiki/Elements | ✅ |
| `geo:` URI | **RFC 5870**, June 2010, Proposed Standard (current) | "identifies a physical location in a two- or three-dimensional coordinate reference system" | https://www.rfc-editor.org/info/rfc5870 | ✅ |

### A3. Location metadata inside image files (gallery)

| Standard | Newest | Note | URL | Src |
|---|---|---|---|---|
| XMP | **ISO 16684-1:2019** (data model, serialization, core properties), **confirmed 2024-09-04**, no newer edition | holds IPTC and Exif-in-XMP | https://www.iso.org/standard/75163.html | ✅ (confirmation date via genorma ⚠️) |
| Exif | **Exif 3.1 = CIPA DC-008-2026, published 2026-01-30** (3.0 was 2023-05, which added UTF-8) | "CIPA DC-008-Translation-2026 … Exif Version 3.1" | https://cipa.jp/e/std/history_sec.html | ✅ |
| Exif→XMP mapping | **CIPA DC-010-2026 "Exif metadata for XMP"**, 2026-06-01 | needed when GPS tags are mirrored to XMP | same | ✅ |
| IPTC Photo Metadata | **2025.1 rev 1, 2025-11-26** (Core 1.5, Extension 1.8); location: `Location Created`, `Location Shown in the Image` (with GPS lat/long/alt, city, country, ISO code, world region, identifiers); also adds AI-generation properties | "version 2025.1 rev 1, 2025-11-26" | https://iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-2025.1.html | ✅ |

**Recommendation (opinion):** Use **GeoJSON (RFC 7946) as the content standard**. Where you need CRS, time or a feature type, upgrade it to **JSON-FG 1.0**, which stays GeoJSON-compatible. Use `geo:` URIs (RFC 5870) for compact references, for example AS2 `Place` plus a `geo:` link. Expose a server API that follows **OGC API – Features Parts 1/2/3**, and Part 4 only once it is final. Use **GeoParquet 2.0** for bulk export and analytics, and **PMTiles v3** for map tiles. Model addresses after the ISO 19160-1 concepts but serialize them as JSContact `addresses` (RFC 9553), with ISO 19160-4 only as a mapping reference because it is paywalled. In the gallery, keep the original file untouched and read **Exif 3.1 GPS + XMP (IPTC 2025.1 LocationCreated/LocationShown)**. Write edits into an XMP sidecar or embedded XMP, following CIPA DC-010 for the Exif↔XMP mapping.

**Gaps → own-spec candidates:**
1. A public address-component vocabulary. ISO 19160-4 codes are paywalled, so we need an FS address profile mapping JSContact ↔ ISO 19160-1 ↔ OSM `addr:*`.
2. A mapping from AS2 `Place` to JSON-FG `place`/`geometry`.
3. A gallery metadata precedence policy: Exif vs. XMP vs. IPTC vs. the FS record, and conflict resolution.
4. A privacy rule for stripping or coarsening GPS on federation.

---

## B. Projects

1. **ISO 21511:2018** "Work breakdown structures for project and programme management" ✅ exists. "This document provides guidance for work breakdown structures for organizations undertaking project or programme management … any type of project and programme." It is **guidance only**, with no data format. https://www.iso.org/standard/69702.html ✅
2. **schema.org `Project`** ✅ exists and is **core**: `isPartOf` is empty in the current release CSV, so it is not pending. Type path: `Thing > Organization > Project`. "An enterprise (potentially individual but typically collaborative), planned to achieve a particular aim. Use … subOrganization/parentOrganization to indicate project sub-structures." Subtypes: `ResearchProject`, `FundingAgency`. It has no task, status or dependency properties. https://schema.org/Project ✅
3. **Task relations / kanban data standards:**
   - **RFC 9253** (iCalendar relationships) `RELTYPE` values: temporal `FINISHTOSTART`, `FINISHTOFINISH`, `STARTTOFINISH`, `STARTTOSTART` (with a `GAP` lead/lag parameter), and also `FIRST`, `NEXT`, **`DEPENDS-ON`**, `REFID`, `CONCEPT`. RFC 5545 already had `PARENT`/`CHILD`/`SIBLING`. It also adds the `LINK` property (with `LINKREL`) and the `CONCEPT` and `REFID` properties. Quote: "DEPENDS-ON: … a task may be blocked waiting on the other, referenced, task." https://www.rfc-editor.org/rfc/rfc9253.html ✅
   - **RFC 10051** (Task Extensions to iCalendar):
     - STATUS for VTODO adds **`PENDING`** and **`FAILED`** to NEEDS-ACTION/IN-PROCESS/COMPLETED/CANCELLED.
     - Adds a **`VSTATUS`** sub-component carrying `REASON` (URI), `SUBSTATE` (`OK`/`ERROR`/`SUSPENDED`) and `DTSTAMP`.
     - Adds `PARTSTAT=FAILED`, `ESTIMATED-DURATION` and `TASK-MODE` (`AUTOMATIC-COMPLETION`/`AUTOMATIC-FAILURE`/`AUTOMATIC`/`SERVER`/`CLIENT`).
     - Task type is expressed with `CONCEPT`. Dependencies and milestones go through RFC 9253 `RELATED-TO` (`DEPENDS-ON`, temporal types) and child VTODOs.
     - Quote: "VSTATUS … is not intended to be used as a history of changes". So the activity log stays our own concern. https://www.rfc-editor.org/info/rfc10051 ✅
   - **JSCalendar `relatedTo`** (RFC 8984 §4.1.3, and carried into 2.0): a map from UID to a `Relation` object whose `relation` set uses `first`, `next`, `child`, `parent` plus IANA-registered or vendor values. It has **no `blocks`/`depends-on`/`duplicates`**. Task `progress` values: `needs-action`, `in-process`, `completed`, `failed`, `cancelled`. https://www.rfc-editor.org/rfc/rfc8984.html ✅ (whether JSCalendar 2.0 adds new relation values was not re-checked ⚠️)
   - **JMAP for Tasks** `draft-ietf-jmap-tasks-06`: **expired** (latest revision 2023-03-10). The WG milestone "Mar 2027 Submit JMAP Tasks document to IESG" still exists. https://datatracker.ietf.org/doc/draft-ietf-jmap-tasks/ ✅
   - **ForgeFed** (ActivityPub vocabulary for forges): `Ticket`, **`TicketDependency`**, `dependsOn`/`dependedBy`, `isResolved`/`resolvedBy`, `Project`. This is the only **AS2-native** option. The spec is "still under construction". https://forgefed.org/spec/ ✅ (status ⚠️ draft)
   - There is **no open standard for kanban boards** (columns, WIP limits, card order). ⚠️ No standard found.
4. **What the tools export:**
   - **OpenProject**: multiple work packages as PDF/XLS/CSV, a single one as PDF/Atom. The REST API v3 uses HAL+JSON. Its relation types are `relates, duplicates/duplicated, blocks/blocked, precedes/follows (with lag), includes/partof, requires/required`, which is a good reference vocabulary. https://www.openproject.org/docs/api/endpoints/relations/ ✅
   - **Taiga**: a full project dump as **.json**, importable into another Taiga. https://taiga.pm/export/ ✅
   - **Vikunja**: full user export as a **ZIP** with `data.json` and attachments. It imports CSV, Trello, Todoist, TickTick, WeKan, Planka (≥2.6.0) and MS To Do, and syncs tasks via **CalDAV**. https://vikunja.io/help/import-and-export/ ✅
   - **Planka**: imports Trello JSON. I found no documented native export format (Vikunja reads Planka over its live API). ⚠️

**Recommendation (opinion):** Use the **iCalendar VTODO + RFC 9253 + RFC 10051** semantics as the content standard for tasks, serialized as **JSCalendar 2.0 Task** in JSON. Keep `Project` as AS2 object/collection with schema.org `Project` typing. Express the AS2 envelope for dependencies with **ForgeFed `TicketDependency`**, because it federates. Map the OpenProject relation set onto RFC 9253 as follows: blocks→`DEPENDS-ON` (inverse), precedes→`FINISHTOSTART`+`GAP`, partof→`PARENT`. ISO 21511 serves only as conceptual guidance for WBS hierarchy.

**Gaps → own-spec candidates:**
1. A kanban board model: board, columns/lanes, card order via fractional index, WIP limits, swimlanes.
2. Relation types missing in JSCalendar (`depends-on`, `blocks`, `duplicates`, `relates`, temporal types). These could be registered as JSCalendar enum values or defined as an FS vendor extension (`freesynergy.org:depends-on`).
3. A task ↔ ForgeFed `Ticket` mapping.
4. An importer mapping for the Taiga JSON, Vikunja ZIP and OpenProject CSV/API formats.

---

## C. Profile

- **schema.org `Person`** ✅ core, "A person (alive, dead, undead, or fictional)." It declares `equivalentClass foaf:Person`. Key properties: `name`, `givenName`, `familyName`, `additionalName`, `honorificPrefix`/`Suffix`, `alternateName`, `image`, `email`, `telephone`, `address`, `birthDate`, `gender`, `nationality`, `affiliation`, `worksFor`, `jobTitle`, `knowsLanguage`, `knows`, `sameAs`, `url`, `identifier`, `description`. https://schema.org/Person ✅
- **FOAF**: the latest spec is **0.99, 14 January 2014** ("Paddington Edition"). No newer release exists, so in practice it is unmaintained and legacy. http://xmlns.com/foaf/spec/ ✅
- **GDPR Art. 9, title "Processing of special categories of personal data"**: "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation shall be prohibited." Art. 9(2)(a)–(j) lists the exceptions, with (a) being explicit consent. The text came from https://gdpr-info.eu/art-9-gdpr/ because EUR-Lex blocked the fetch. Official source: https://eur-lex.europa.eu/eli/reg/2016/679/oj ⚠️ (secondary mirror, wording is identical to the OJ)
- **W3C DPV**: **version 2.3, Final Community Group Report, 25 February 2026**, from the DPVCG Community Group, so it is **not a W3C Recommendation**. https://w3id.org/dpv/ ✅
  - `dpv:SpecialCategoryPersonalData` **exists**: "Sensitive Personal Data whose use requires specific additional legal permission or justification" (subclass of `dpv:SensitivePersonalData`). ✅
  - In the PD extension (`pd:` = `https://w3id.org/dpv/pd#`) the special-category concepts include `pd:Biometric`, `pd:Genetic`, `pd:Health` (+`HealthHistory`, `HealthRecord`), `pd:Ethnicity`, `pd:PoliticalAffiliation`, `pd:Religion`/`pd:ReligiousBelief`, `pd:PhilosophicalBelief`, `pd:TradeUnionMembership`, `pd:Sexual`, `pd:SexualHistory`, `pd:SexualPreference`. **There is no `pd:SexualOrientation`**; use `pd:SexualPreference` or `pd:Sexual`. ✅ (exact subclassing of each term under SpecialCategory was verified only for `pd:Biometric` ⚠️)
  - The EU-GDPR extension has legal-basis concepts for **Art. 9(2)(a)–(j)** (`A9-2-a` … `A9-2-j`). https://w3id.org/dpv/legal/eu/gdpr/ ✅

**Recommendation (opinion):** Use **JSContact (RFC 9553)** as the profile content standard and **schema.org `Person`** as the AS2/JSON-LD typing (AS2 `Person` actor plus a schema.org context). Drop FOAF except for `foaf:` aliases on import. Tag every profile field with a **DPV 2.3** data category. Store fields tagged `dpv:SpecialCategoryPersonalData` encrypted and opt-in. Never federate them by default. Every disclosure needs a recorded `eu-gdpr:A9-2-a` explicit-consent record in the activity log.

**Gaps → own-spec candidates:**
1. A profile-field → DPV category mapping table, including which JSContact and schema.org fields count as special category, for example `gender`, `knowsLanguage` with religion context, and health.
2. Per-field visibility and audience rules, expressed as AS2 audience plus VC selective disclosure.
3. A consent receipt format linking DPV consent to the activity log.

---

## D. Login

1. **WebAuthn Level 3**: **W3C Recommendation, 25 August 2026** (CR was 2026-05-26). https://www.w3.org/TR/webauthn-3/ ✅ Passkeys are WebAuthn discoverable credentials, and the term is a FIDO Alliance brand rather than a separate spec ⚠️.
2. **OAuth 2.1**: `draft-ietf-oauth-v2-1-**17**`, dated 31 Oct 2026. It is still an Internet-Draft (WG document, "Obsoletes: 6749, 6750 (if approved)"), with a WG milestone of Dec 2026 to submit to the IESG. https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ ✅
   **RFC 9700 = BCP 240** "Best Current Practice for OAuth 2.0 Security" (January 2025): "deprecates some modes of operation that are deemed less secure or even insecure." https://www.rfc-editor.org/info/rfc9700 ✅ (the date is from memory ⚠️)
3. **OpenID Federation 1.0**: **Final, published 17 February 2026.** "trust can be mediated by a third party … a trusted third party called a Trust Anchor."
   - Building blocks:
     - *Entity Configuration*: a self-signed JWT at `/.well-known/openid-federation` with `authority_hints`.
     - *Subordinate Statements*: issued by a superior through its `federation_fetch_endpoint`.
     - *Trust Chain*: leaf → intermediates → Trust Anchor.
     - *Metadata policy*: superiors constrain the metadata of their subordinates.
     - *Trust Marks*: "Statement of conformance to a well-scoped set of trust and/or interoperability requirements as determined by an accreditation authority".
     - Automatic and explicit client registration.
   - URL: https://openid.net/specs/openid-federation-1_0.html ✅
   - **This is very relevant.** It is essentially a standardized version of our idea of "trust lists acting like an identity broker".
4. **FedCM**: still only a **W3C First Public Working Draft, 20 Aug 2024**, with no later TR publication. https://www.w3.org/standards/history/fedcm-1/ ✅ The browser API is Chromium-driven ⚠️.
5. **WebFinger RFC 7033 JRD**: `subject` (URI), `aliases` (URI array), `properties` (URI→string|null), `links[]` with `rel` (required), `type`, `href`, `titles`, `properties`. "The value of the 'subject' member is a URI that identifies the entity that the JRD describes." https://www.rfc-editor.org/rfc/rfc7033 ✅
6. **Kanidm**: **v1.12.0, 2026-11-01** (it adds account signup); master is at 1.13.0-dev. Licence **MPL-2.0** ✅. Features:
   - **Passkeys/WebAuthn L3 + attested passkeys** ✅
   - **OAuth2/OIDC provider**, with Auth Code + PKCE (S256), Client Credentials, Token Exchange (RFC 8693), introspection, revocation, RFC 8414 metadata, JWT access tokens (RFC 9068), OIDC Discovery and ES256 ✅
   - **Read-only LDAPS gateway** ✅
   - **RADIUS** ✅
   - **SCIM: "only supported for synchronisation from another IDP at this time"**, meaning inbound sync (kanidm-ipa-sync and ldap-sync) and **not** a general SCIM server for provisioning ✅
   - HTTP JSON REST API (v1) plus CLI ⚠️ (the API is documented as Kanidm's own, not a standard)
   - **OpenID Federation: not supported.** It was raised in community discussion #4154 (Feb 2026) and linked to the "Implement trusts" issue #149 for 2.0.0 ✅
   - Also: TOTP, Argon2id, two-node replication, Unix PAM/nss, SSH keys.
   - Sources: https://kanidm.github.io/kanidm/stable/supported_features.html , https://github.com/kanidm/kanidm/releases/tag/v1.12.0
7. **SCIM RFC 7643 attribute names** ✅ https://www.rfc-editor.org/rfc/rfc7643
   - Common: `id`, `externalId`, `meta` (`resourceType`, `created`, `lastModified`, `location`, `version`), `schemas`.
   - **User, singular:** `userName`, `name` (`formatted`, `familyName`, `givenName`, `middleName`, `honorificPrefix`, `honorificSuffix`), `displayName`, `nickName`, `profileUrl`, `title`, `userType`, `preferredLanguage`, `locale`, `timezone`, `active`, `password`.
   - **User, multi-valued:** `emails`, `phoneNumbers`, `ims`, `photos`, `addresses`, `groups`, `entitlements`, `roles`, `x509Certificates`.
   - **Group:** `displayName`, `members`.
   - Enterprise extension: `employeeNumber`, `costCenter`, `organization`, `division`, `department`, `manager`.

**Recommendation (opinion):** Kanidm handles local login (passkeys first, OIDC to FS apps). Use OAuth 2.1 draft rules as defaults now (PKCE always, no implicit grant, exact redirect matching), in line with RFC 9700. **Adopt OpenID Federation 1.0 for instance-to-instance trust**: each FS instance publishes an Entity Configuration. FS trust lists become Trust Anchors or Intermediates, and **Trust Marks** express "member of trust list X / verified by RLTP level Y". This replaces a homegrown broker protocol. Keep DID + VC 2.0 for user-level portable identity claims. WebFinger JRD stays the discovery entry point, linking the AS2 actor, OIDC issuer and DID. Skip FedCM for now because it is still an FPWD and browser-specific.

**Gaps → own-spec candidates:**
1. **An FS federation bridge.** Kanidm has no OpenID Federation support, so we need a sidecar that publishes `/.well-known/openid-federation` for the Kanidm issuer and resolves trust chains for incoming RPs/OPs. Kanidm also cannot act as an upstream-IdP broker.
2. **An outbound SCIM server.** Kanidm only supports SCIM as a sync source, so FS needs its own SCIM 2.0 service provider (or a Kanidm REST → SCIM adapter) to provision apps.
3. A Trust Mark profile for RLTP / Web-of-Trust levels, including how a VC 2.0 credential and a Trust Mark JWT relate.
4. A WebFinger link-relation profile for FS (rels for AS2 actor, OIDC issuer, DID, federation entity).
