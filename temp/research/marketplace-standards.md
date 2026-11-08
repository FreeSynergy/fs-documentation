# Marketplace standards research (planning only)

Date of research: 2026-11-08. Scope: standards and specifications relevant to a classified-ads style marketplace (give away, swap, lend, sell). No code, no recommendations. Every statement carries a link. Items that could not be verified are marked **not verified**.

Method note: WebFetch was used for the primary pages named below. Where a fact is marked "(search snippet only)", it came from a web search result and the linked page was not fetched by the agent.

---

## 0. What our own pages already say

Source: `/srv/FreeSynergy/.wt-doc-d/docs/en/programs/suites/marketplace/index.md`, `.../marketplace/requirements.md`, `.../marketplace/frontends/index.md`, and the `index.md` of each frontend under `.../marketplace/frontends/<program>/index.md` (arcemall, cs-cart-multivendor, ebay, etsy, kleinanzeigen, sharetribe). The `latest/*.md` files were not read in this pass.

1. The category is for platforms where "different people and organizations offer things to each other, like eBay or Etsy, not like a shop of your own" (`.../marketplace/index.md`).
2. Six frontends are documented: sharetribe, arcemall, cs-cart-multivendor, ebay, etsy, kleinanzeigen (`.../marketplace/index.md`, `.../marketplace/frontends/index.md`).
3. Kleinanzeigen is described as a regional classifieds marketplace in Germany with local pickup and "without a public API" (`.../frontends/kleinanzeigen/index.md`).
4. Sharetribe is described as open-source marketplace software (Ruby on Rails, "Sharetribe Flex" API-first) plus SaaS versions (`.../frontends/sharetribe/index.md`).
5. `requirements.md` for `FreeSynergy.Marketplace` has empty tables for Required, Optional and Not planned; no capability or standard is recorded yet (`.../marketplace/requirements.md`).
6. Our own program for the category is `FreeSynergy.Marketplace` (ADR 0017); its capabilities and status live in requirements (`.../marketplace/frontends/index.md`).
7. Every frontend index has the placeholder "_To do: what does this program do that others don't?_" under "Notable ideas" (all six `index.md` files).
8. Every frontend index reports `themes/index.md` as a missing required file (all six `index.md` files, generated block).
9. Arcemall documentation is marked "thin": API details are "only described as officially published", the rest "verify current status" (`.../frontends/arcemall/index.md`).
10. The standards rule is that each capability names its data standard (ADR 0014) and frontends are analysed without copying (ADR 0013) (`.../marketplace/requirements.md`, `.../marketplace/frontends/index.md`). The index also contains two duplicate sections ("Skin documentation" and "Mask documentation") that refer to a `masks/<program>/` path, while the files live under `frontends/` (`.../marketplace/index.md`).

---

## 1. ValueFlows (REA: Resources, Events, Agents)

**What it models.** ValueFlows is "a vocabulary for the distributed economic networks of the next economy" and "implements the REA (Resources, Events, Agents) ontology, extended with concepts such as recipes, offers and requests, and ecological accounting" ([valueflo.ws](https://valueflo.ws/)). It "specifies the vocabulary, but not the technical protocol" ([valueflo.ws](https://valueflo.ws/)).

**Core classes (definitions as on the formatted spec page, paraphrased where noted):**
- **Intent**: "A desired, proposed, planned, or estimated economic flow, usually with one agent, that could become a commitment and/or economic event" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- **Proposal**: "A published request or offer, sometimes with what is expected in return" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- **Commitment**: "A planned economic flow scheduled or promised by one agent to another" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- **EconomicEvent**: "An observed economic flow" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- **Agreement**: "A set of reciprocal commitments among economic agents, or reciprocal economic events" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- **Agent**: "An identifiable entity that can commit to and/or perform economic and/or ecological activity under its own power or authority" ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)).
- Example from the UML page: "a Commitment for 40 hours of work might be fulfilled by 5 EconomicEvents of 8 hours" ([UML page](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/uml)).
- **Claim** (1.0): "A claim for future economic event(s) in reciprocity for events already occurred" ([hREA 1.0 compliance analysis](https://sensorica.github.io/nondominium/hREA/valueflows-1.0-compliance.html)).

**Actions (flow kinds).** The formatted spec describes actions as the "kind of flow, such as consume, produce, work, transfer, etc." and does not give a full list on the fetched page ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)). The hREA 1.0 compliance analysis lists 18 built-in actions: dropoff, pickup, consume, use, work, cite, produce, accept, modify, pass, fail, deliver-service, transfer-all-rights, transfer-custody, transfer, move, raise, and lower ([hREA 1.0 compliance analysis](https://sensorica.github.io/nondominium/hREA/valueflows-1.0-compliance.html)). Neither "give" nor "lend" appears in that list (same source). Whether this list equals the official spec list: **not verified** (the analysis is a third-party document).

**Gift economy, exchange, loan.** Mapping to give / swap / lend in the spec: **not verified**. The spec text that was fetched speaks of reciprocal commitments and agreements ([all_vf spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf)) but does not name gift, loan or swap cases.

**Version.** The hREA compliance analysis states "VF Spec Version: 1.0.0 (CC-BY-SA 4.0)" (analysis dated 2026-03-25, with a later update dated 2026-09-10) ([hREA 1.0 compliance analysis](https://sensorica.github.io/nondominium/hREA/valueflows-1.0-compliance.html)). The official repository contains a directory named `major-release-doc/VF-Release-1-0-0`, which is a directory name and not a version statement ([valueflows repo](https://github.com/valueflows/valueflows)). An archived 2021 copy of the ontology lists version 0.5 (search snippet only: [archived ontology 2021](https://akswnc7.informatik.uni-leipzig.de/dstreitmatter/archivo/w3id.org/valueflows/2021.06.16-141300/valueflows_type%3DgeneratedDocu.html)). The official "Release and Status" page was linked from valueflo.ws but its content was not retrieved: **not verified**.

**Licence.** "This vocabulary and documentation is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License" ([valueflo.ws](https://valueflo.ws/)). Repository licence shown as CC-BY-SA-4.0 ([valueflows repo](https://github.com/valueflows/valueflows)).

**Serialisations.**
- RDF Turtle: the file `all_vf.TTL` is described as "the system of record source for the specification" ([valueflows repo](https://github.com/valueflows/valueflows)).
- Ontology namespace: `https://w3id.org/valueflows/ont/vf#`, preferred prefix `vf` ([valueflo.ws](https://valueflo.ws/)).
- GraphQL: vf-graphql schemas, "maintained mostly by the projects using it" and "currently somewhat out of sync" ([valueflows repo](https://github.com/valueflows/valueflows)).
- JSON-LD: not mentioned on the fetched pages; **not verified**.

**Reference implementations and maturity.**
- hREA: "an implementation of the Valueflows specification", Apache 2.0 (the page gives no SPDX identifier) ([hREA](https://www.hrea.io/)). It reports that between May and September 2022 it "reached a fully usable API (v0.1.0-beta)" and that from September 2025 "enhancements based on application project feedback continue" ([hREA](https://www.hrea.io/)). hREA page does not state which ValueFlows version it implements: **not verified**.
- Bonfire ValueFlows extension: "implements ValueFlows for federated networks to conduct economic activities"; implemented: Intent, Proposal, Economic Event, Types of Action, Resource Specification, Economic Resource, Process Specification, Process; Claim and Value Calculations marked "WIP"; optional GraphQL API; licence AGPL-3.0; page "Updated 18 Oct 2026" ([Bonfire extension page](https://bonfirenetworks.org/extension/bonfire_valueflows)). The page does not mention ActivityPub: ([Bonfire extension page](https://bonfirenetworks.org/extension/bonfire_valueflows)). Bonfire core is licensed AGPL-3.0 or later; the README contains no ValueFlows mention ([bonfire-app](https://github.com/bonfire-networks/bonfire-app)).
- Nondominium (Sensorica): a Holochain app with ValueFlows-style structures; an hREA backend integration is "planned but not yet built" (search snippet only: [Nondominium docs](https://sensorica.github.io/nondominium/)). Phase 2 (resource lifecycle and governance) "still in progress" (search snippet only: [Nondominium README](https://cdn.jsdelivr.net/gh/Sensorica/nondominium@main/README.md)). **Not verified** beyond these snippets.
- Mutual Aid as a ValueFlows reference implementation: **not verified** (no source found).
- Holo-REA: **not verified** as a separate project name; the hREA page does not mention it.

---

## 2. schema.org (Offer, Demand, Product, Service, businessFunction)

**Version and licence.** Most recent release "Version 30.1, dated 2026-09-16"; previous releases 30.0 (2026-03-19), 29.4 (2025-12-08), 29.3 (2025-09-04), 29.2 (2025-05-13), 29.1 (2025-04-25) ([schema.org releases](https://schema.org/docs/releases.html)). Licence for vocabularies and documentation: Creative Commons Attribution-ShareAlike 3.0 ("Sponsors' copyrights ... under the Creative Commons Attribution-ShareAlike License (version 3.0)"), linking to http://creativecommons.org/licenses/by-sa/3.0/ ([schema.org terms](https://schema.org/docs/terms.html)). The page does not state the SPDX identifier; the text names CC BY-SA 3.0 as above.

**Offer properties relevant to the four cases** (from the Offer page; descriptions as stated there) ([schema.org Offer](https://schema.org/Offer)):
- `price` (Number or Text): "The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes." `priceCurrency` (Text, "preferably ISO 4217").
- `priceSpecification` (PriceSpecification): detailed price components.
- `businessFunction` (BusinessFunction): "Transaction type (sell, lease, repair, dispose)." "The default is http://purl.org/goodrelations/v1#Sell."
- `itemOffered` (AggregateOffer, CreativeWork, Event, MenuItem, Product, Service, or Trip).
- `seller` (Organization or Person): "Entity selling, leasing, or lending the goods or services; supersedes merchant and vendor."
- `offeredBy` (Organization or Person).
- `availability` (ItemAvailability), `availabilityStarts`, `availabilityEnds`, `validFrom`, `validThrough`, `eligibleQuantity`, `itemCondition`, `areaServed`, `availableAtOrFrom`, `availableDeliveryMethod`.
- `leaseLength` (Duration or QuantitativeValue): "Length of a lease, mainly for accommodations."
- Incoming: `makesOffer`, `offers` ([schema.org Offer](https://schema.org/Offer)).

**BusinessFunction values.** The BusinessFunction page lists eight "commonly used values": ConstructionInstallation, Dispose, LeaseOut, Maintain, ProvideService, Repair, Sell, Buy; the individual descriptions were not returned by the fetch ([schema.org BusinessFunction](https://schema.org/BusinessFunction)). "Give" is not in that list ([schema.org BusinessFunction](https://schema.org/BusinessFunction)). The full set of values and their descriptions: **not verified**.

**Mapping of the four cases to schema.org properties (what the fetched pages say):**
- **Sell**: default `businessFunction` is GoodRelations `Sell` ([schema.org Offer](https://schema.org/Offer)).
- **Lend / rent**: `seller` text covers "leasing, or lending"; `businessFunction` value `LeaseOut` exists ([schema.org Offer](https://schema.org/Offer), [schema.org BusinessFunction](https://schema.org/BusinessFunction)). `leaseLength` is described for accommodations ([schema.org Offer](https://schema.org/Offer)).
- **Give away (price 0)**: no property or value for "free" or "gift" was found in the fetched pages; `price` is a Number ([schema.org Offer](https://schema.org/Offer)). Whether a price of 0 is documented as giving away: **not verified**. `Dispose` is listed as a BusinessFunction value ([schema.org BusinessFunction](https://schema.org/BusinessFunction)); its description was not returned, so whether it means give-away is **not verified**.
- **Swap**: no property or value for barter or exchange was found in the fetched pages: **not verified**.

---

## 3. GoodRelations (purl.org/goodrelations)

**Status.** GoodRelations Language Reference "V 1.0, Release 2011-10-01 (last update 2011-10-01, author Martin Hepp)" ([GoodRelations v1 reference](http://www.heppnetz.de/ontologies/goodrelations/v1)). The project page tagline is "A paradigm shift for e-commerce. Since 2008." ([GoodRelations project](https://www.heppnetz.de/projects/goodrelations/)).

**Merge into schema.org.** Search results report that the e-commerce vocabulary was made available through schema.org in November 2012 and that the W3C wiki calls it "almost fully integrated" (search snippets only: [W3C public-vocabs, 2012 Nov 0037](https://lists.w3.org/Archives/Public/public-vocabs/2012Nov/0037.html), [W3C wiki GoodRelations](https://www.w3.org/wiki/GoodRelations)). The schema.org page for BusinessFunction and Offer still uses `http://purl.org/goodrelations/v1#` URIs ([schema.org BusinessFunction](https://schema.org/BusinessFunction)). Full extent of the merge: **not verified**.

**Licence.** "The GoodRelations ontology is available under the Creative Commons Attribution 3.0 license" ([GoodRelations project](https://www.heppnetz.de/projects/goodrelations/)).

**BusinessFunction values (v1).** Predefined individuals in the 2011 reference: ConstructionInstallation, Dispose, LeaseOut, Maintain, ProvideService, Repair, Sell, Buy; no "Give" ([GoodRelations v1 reference](http://www.heppnetz.de/ontologies/goodrelations/v1)). Individual rdfs:comment texts: **not verified** (not returned by the fetch). The purl.org address redirected to purl.archive.org and then to the heppnetz.de address; the ontology file itself was not fetched in full.

---

## 4. ActivityStreams 2.0 vocabulary and ActivityPub; FEPs

**W3C status.** Activity Streams 2.0 Vocabulary: "W3C Recommendation 23 May 2017", Social Web Working Group; licence statement "W3C liability, trademark and permissive document license rules apply" ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/)). ActivityPub: "W3C Recommendation 23 January 2018" ([ActivityPub](https://www.w3.org/TR/activitypub/)).

**Types that fit (definitions as stated):**
- `Offer`: "Indicates that the `actor` is offering the `object`." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- `Invite`: "A specialization of `Offer` in which the `actor` is extending an invitation for the `object` to the `target`." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- `Note`: "Represents a short written work typically less than a single paragraph in length." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- `Page`: "Represents a Web Page." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- `Place`: "Represents a logical or physical location." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- `Question`: "Represents a question being asked." ([AS2 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/))
- None of these types carries give / swap / lend / sell semantics in its definition (this statement is about the definitions quoted above).

**FEP repository.** Codeberg repository `fediverse/fep`, licence CC0 1.0 Universal ([FEP repo](https://codeberg.org/fediverse/fep)). The index uses the statuses DRAFT, FINAL, WITHDRAWN ([FEP repo](https://codeberg.org/fediverse/fep)). The process is FEP-a4ed ([FEP-a4ed](https://fediverse.codeberg.page/fep/fep/a4ed/)).

**FEPs found on marketplace / commerce / valueflows topics:**

| Number | Title | Status | Authors | Dates seen | Link |
|---|---|---|---|---|---|
| FEP-0837 | Federated Marketplace | DRAFT (type: Implementation) | silverpill (@silverpill@mitra.social) | received 2023-08-17; tracking issue #147 | [FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/), [source](https://codeberg.org/fediverse/fep/src/branch/main/fep/0837/fep-0837.md) |
| FEP-d767 | Extend ActivityPub with Valueflows | WITHDRAWN | Lynn Foster (lynnfoster@social.coop) | received 2023-04-02; withdrawn 2024-02-03; reason not stated | [FEP-d767](https://fediverse.codeberg.page/fep/fep/d767/), [source](https://codeberg.org/fediverse/fep/src/branch/main/fep/d767/fep-d767.md) |
| FEP-c07e | add product type to object | DRAFT (type: implementation) | potato (@potatomeow@fosstodon.org) | received 2026-03-15; tracking issue #786 | [FEP-c07e](https://fediverse.codeberg.page/fep/fep/c07e/), [source](https://codeberg.org/fediverse/fep/src/branch/main/fep/c07e/fep-c07e.md) |

FEP-0837 content (as stated): a minimal federated marketplace built on ActivityPub and the ValueFlows vocabulary; a `Proposal` with `purpose` `offer` or `request`; an `Intent` with action values such as `transfer` or `deliverService`; an `Agreement` with `stipulates` and `stipulatesReciprocal` Commitments; a reply to a proposal is "an `Agreement` object wrapped in `Offer` activity" ([FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/)). Licence CC0 1.0 ([FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/)).

FEP-d767 content (as stated): "A standard method to extend ActivityPub/ActivityStream with Valueflows vocabulary"; licence CC0 1.0 ([FEP-d767](https://fediverse.codeberg.page/fep/fep/d767/)).

FEP-c07e content (as stated): add a `Product` type beside `Note` and `Article` in the Object vocabulary ([FEP-c07e](https://fediverse.codeberg.page/fep/fep/c07e/)).

FEP process (FEP-a4ed): status FINAL, received 2020-10-16, finalized 2021-01-18; "A proposal with status WITHDRAWN remains in the repository and can be resubmitted"; "After at least 60 days the authors may request the proposal to be finalized" ([FEP-a4ed](https://fediverse.codeberg.page/fep/fep/a4ed/)).

No FEP titled with classifieds, listing, offer or commerce was visible in the repository index page as fetched ([FEP repo](https://codeberg.org/fediverse/fep)). Completeness of that index check: **not verified**. Lemmy or Mastodon classifieds FEPs: **not verified** (not found). Bonfire use of ValueFlows over ActivityPub: the Bonfire extension page does not describe ActivityPub ([Bonfire extension page](https://bonfirenetworks.org/extension/bonfire_valueflows)); the Bonfire coordination post says ValueFlows is "the economic counterpart to ActivityStreams" (search snippet only: [Bonfire coordination post](https://bonfirenetworks.org/posts/bonfire_coordination)). The `activity_pub` library exists (search snippet only: [Bonfire GitHub](https://github.com/bonfire-networks)). **Not verified** beyond these.

---

## 5. Other standards (checked)

**GS1 Web Vocabulary.** Official site: [ref.gs1.org/voc](https://ref.gs1.org/voc/). Described as "designed as an extension to schema.org" ([ref.gs1.org/voc](https://ref.gs1.org/voc/)). The fetched page did not render version, date or licence (template placeholders). Version: **not verified**. Licence: **not verified**; a search snippet names Apache 2.0 for the repository [github.com/gs1/WebVoc](https://github.com/gs1/WebVoc) (search snippet only, page not fetched). "Open Product Data Commons" licence: **not verified** (no source found).

**Not researched in this pass:** JSON-LD (W3C spec), Open Product Data as a separate project, Open Referral and UN/CEFACT (skipped as not relevant per brief).

---

## 6. Summary table

Column "covers" states only what the cited source says. "not verified" means the source was not found or not fetched.

| Standard | covers give / swap / lend / sell? | version | licence | official link | maturity statement from the project itself |
|---|---|---|---|---|---|
| ValueFlows (REA) | give: not verified (not in hREA action list); swap: "reciprocal commitments" in Agreement, no swap term verified; lend: not named (action list has "use", "transfer", "transfer-custody"); sell: not named, Proposal "what is expected in return" | 1.0.0 per hREA analysis; archived 0.5 (2021) | CC-BY-SA 4.0 ([valueflo.ws](https://valueflo.ws/)) | [valueflo.ws](https://valueflo.ws/), [spec](https://valueflows.gitbook.io/valueflows/mkdocs/docs/specification/all_vf) | "specifies the vocabulary, but not the technical protocol" ([valueflo.ws](https://valueflo.ws/)); "Release and Status" page not read |
| hREA (ValueFlows implementation) | not stated on the page | not stated | Apache 2.0, no SPDX ([hREA](https://www.hrea.io/)) | [hrea.io](https://www.hrea.io/) | "reached a fully usable API (v0.1.0-beta)" (2022); "enhancements ... continue" (from Sep 2025) ([hREA](https://www.hrea.io/)) |
| Bonfire ValueFlows extension | not stated | not stated | AGPL-3.0 ([Bonfire extension](https://bonfirenetworks.org/extension/bonfire_valueflows)) | [bonfirenetworks.org](https://bonfirenetworks.org/extension/bonfire_valueflows) | Claim and Value Calculations "WIP" ([Bonfire extension](https://bonfirenetworks.org/extension/bonfire_valueflows)) |
| schema.org Offer / BusinessFunction | give: not verified (no value; Dispose description not verified); swap: not verified; lend: `seller` "leasing, or lending", `LeaseOut`; sell: default `Sell` | 30.1 (2026-09-16) ([releases](https://schema.org/docs/releases.html)) | CC BY-SA 3.0 ([terms](https://schema.org/docs/terms.html)) | [schema.org/Offer](https://schema.org/Offer), [schema.org/BusinessFunction](https://schema.org/BusinessFunction) | page calls itself "development version" ([BusinessFunction](https://schema.org/BusinessFunction)) |
| GoodRelations | give: not in v1 list; swap: not verified; lend: LeaseOut; sell: Sell; dispose: Dispose | V1.0, release 2011-10-01 ([v1](http://www.heppnetz.de/ontologies/goodrelations/v1)) | CC BY 3.0 ([project](https://www.heppnetz.de/projects/goodrelations/)) | [purl.org/goodrelations](http://purl.org/goodrelations/v1) (redirects) | "Since 2008" ([project](https://www.heppnetz.de/projects/goodrelations/)); merged-into-schema.org status: search snippet only |
| ActivityStreams 2.0 vocabulary | no give/swap/lend/sell types; Offer = "offering the object" | W3C Rec 2017-05-23 ([AS2](https://www.w3.org/TR/activitystreams-vocabulary/)) | W3C document licence ([AS2](https://www.w3.org/TR/activitystreams-vocabulary/)) | [W3C AS2](https://www.w3.org/TR/activitystreams-vocabulary/) | W3C Recommendation |
| ActivityPub | not verified in this pass (protocol, not vocabulary) | W3C Rec 2018-01-23 ([ActivityPub](https://www.w3.org/TR/activitypub/)) | W3C document licence ([ActivityPub](https://www.w3.org/TR/activitypub/)) | [W3C ActivityPub](https://www.w3.org/TR/activitypub/) | W3C Recommendation |
| FEP-0837 Federated Marketplace | exchange via Proposal (offer/request) + Agreement; give/lend/sell not named | draft, 2023-08-17 | CC0 1.0 ([FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/)) | [FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/) | DRAFT ([FEP-0837](https://fediverse.codeberg.page/fep/fep/0837/)) |
| FEP-d767 Extend ActivityPub with Valueflows | not stated | withdrawn 2024-02-03 | CC0 1.0 ([FEP-d767](https://fediverse.codeberg.page/fep/fep/d767/)) | [FEP-d767](https://fediverse.codeberg.page/fep/fep/d767/) | WITHDRAWN ([FEP-d767](https://fediverse.codeberg.page/fep/fep/d767/)) |
| GS1 Web Vocabulary | not verified | not verified | not verified (Apache 2.0 for repo: search snippet only) | [ref.gs1.org/voc](https://ref.gs1.org/voc/) | "extension to schema.org" ([ref.gs1.org](https://ref.gs1.org/voc/)) |

---

## 7. Not verified / open questions

1. ValueFlows official "Release and Status" page content and spec version history beyond 1.0.0 (linked from [valueflo.ws](https://valueflo.ws/); not fetched).
2. ValueFlows JSON-LD serialisation: not seen on any fetched page.
3. Official ValueFlows action list: only the hREA compliance analysis was fetched ([hREA 1.0 analysis](https://sensorica.github.io/nondominium/hREA/valueflows-1.0-compliance.html)); whether it matches the official spec is not verified.
4. Gift, loan (lend), swap and sale semantics in ValueFlows: not verified.
5. Which ValueFlows version hREA implements: not stated on [hREA](https://www.hrea.io/).
6. Mutual Aid as a ValueFlows implementation: no source found.
7. Holo-REA as a named project: not verified.
8. Nondominium (Sensorica) status: search snippets only ([Nondominium docs](https://sensorica.github.io/nondominium/)); not verified by fetch.
9. Bonfire ValueFlows over ActivityPub: no source found that describes it ([Bonfire extension](https://bonfirenetworks.org/extension/bonfire_valueflows) does not mention it).
10. FEP coverage: completeness of the FEP index check for classifieds, listing, Offer or commerce topics: not verified; Lemmy and Mastodon classifieds FEPs: not verified (not found).
11. schema.org `BusinessFunction` individual descriptions (including Dispose) and the full value list: not verified (fetch returned only the names).
12. Whether a price of 0 or any other property denotes a give-away in schema.org: not verified.
13. Whether schema.org defines a swap or barter value: not verified.
14. GoodRelations merge into schema.org (date and completeness): based on search snippets ([public-vocabs 2012 Nov 0037](https://lists.w3.org/Archives/Public/public-vocabs/2012Nov/0037.html), [W3C wiki](https://www.w3.org/wiki/GoodRelations)); the pages were not fetched.
15. GoodRelations ontology file itself (individual comments, licence text in the file): not verified (large file, not read in full).
16. GS1 Web Vocabulary: version, release date and licence not rendered on [ref.gs1.org/voc](https://ref.gs1.org/voc/); Apache 2.0 for [github.com/gs1/WebVoc](https://github.com/gs1/WebVoc) is from a search snippet only; "Open Product Data Commons" licence claim: not verified.
17. JSON-LD (W3C) and Open Product Data as separate standards: not researched.
18. Mastodon / Lemmy marketplace or classifieds features: not researched.

**Count:** 18 open items in section 7; about 37 distinct source URLs cited in this file (official or project pages plus FEP and W3C pages; some are search-snippet-only and are labelled as such).
