# Roles: source notes

Date: 2026-11-06. Goes with `docs/en/interfaces/roles.md`. Status: draft.

Each claim says what was checked and where. "Read" means the source was downloaded and the passage was read. "Searched" means a
text search over that downloaded source. A search that finds nothing supports "not in this document" and nothing wider.

"No standard exists" always means: none found in the sources listed here. It is not proof that none exists anywhere.

## Sources not read

| Source | Why | Effect |
|--------|-----|--------|
| ISO 9000:2015 (terms for customer and provider) | iso.org returned 403 | Not used in `roles.md`. It may hold a useful definition of "customer". Paid standard, not checked |
| UN/EDIFACT code list 3035 (party function codes) | unece.org returned 403 (Cloudflare block). The block was not worked around | Not used in `roles.md`. A third-party search snippet says BY = buyer, SU = supplier. Unverified. schema.org does link `seller` to `unece:Seller` (read) |
| ILO resolutions themselves (19th ICLS 2013, 20th ICLS 2018) | ilo.org page returned 403 | Definitions taken from other ILO documents that quote or describe them. See below |
| EN 16931 (e-invoice) | Paid, not tried | Not used |
| HR Open Standards schemas | Only the home page was read; the page shows member and download areas, and the schemas were not read | Not used in `roles.md`. It may hold employee data formats. **Open check** |
| SHACL | Not read | Named in `roles.md` only as an unread candidate |
| Salesforce and other CRM vendor models | One vendor (HubSpot) read as an example. The Microsoft Dataverse lead URL returned 404 | Enough to show vendor use, and says nothing about all vendors |

## 1. SKOS and `org:Role`

| Claim | Verified where |
|-------|----------------|
| SKOS Reference is a W3C Recommendation of 18 August 2009 | Read, https://www.w3.org/TR/skos-reference/ , header |
| Organization Ontology is a W3C Recommendation of 16 January 2014 | Read, https://www.w3.org/TR/vocab-org/ , header |
| `org:Role` is a subclass of `skos:Concept`. Quote: "subClassOf: skos:Concept" | Read, `org` §5.3.5 |
| Roles use SKOS: "The normal SKOS lexical properties should be used when labelling the Role" | Read, `org` §5.3.5 (usage note) |
| Extension: "Additional descriptive properties for the Role, such as a Salary band, may be added by extension vocabularies" | Read, `org` §5.3.5 |
| `org:Role` is "a role that a Person or other Agent can take in an organization" | Read, `org` §5.3.5 |
| `org:Membership` is an n-ary relationship between an Agent, an Organization and a Role. `org:member` and `org:organization` are functional | Read, `org` §5.3.4 |
| Annotating a membership with "duration, salary, reference to the employment contract" | Read, `org` §2.2 (non-normative) |
| Conformant data does "not use terms from other vocabularies instead of ones defined in this vocabulary that could reasonably be used"; use in addition is allowed | Read, `org` §3 |
| A profile may add "classes and properties for additional terms not covered in ORG" and controlled vocabularies | Read, `org` §3 |
| `skos:Concept` is "an idea or notion; a unit of thought" | Read, SKOS §3.1 |
| Concept schemes: `skos:inScheme`; S9 says a scheme is disjoint with a concept | Read, SKOS §4.3, §4.4 |
| S14: "A resource has no more than one value of skos:prefLabel per language tag" | Read, SKOS §5.4 |
| `skos:definition` is one of the documentation properties, which are also extension points | Read, SKOS §7.1, §7.3 |
| `skos:broader` is a hierarchical link | Read, SKOS §8.1 |
| Mapping links are between concepts "in different concept schemes" | Read, SKOS §10.1 |
| "SKOS is not a formal knowledge representation language" | Read, SKOS §1.3 |
| "SKOS data are then expressed as RDF triples" | Read, SKOS §1.3 |
| SKOS defines no formal conformance. A graph is inconsistent only if it leads to a logical contradiction | Read, SKOS §1.8 |
| Notations are by convention unique in a scheme | Read, SKOS §6.5.3 |
| SKOS Reference and Primer do not mention JSON | Searched both, no hit |
| JSON-LD 1.1 is a W3C Recommendation of 16 July 2020 | Read, https://www.w3.org/TR/json-ld11/ , header |
| Language maps: `@container: @language` | Read, JSON-LD 1.1 §4.6.2 (this section is marked non-normative) |
| Ordinary JSON can be read as JSON-LD with a context, including a top-level array | Read, JSON-LD 1.1 §6.1 |
| Reverse properties exist | Only the section title (§4.8) was seen. The behaviour was confirmed by the test below |
| `rdfs:seeAlso` points to a resource with more information | Read, RDF Schema 1.1 §5.4.1 |
| ESCO publishes a whole classification in SKOS, so a job-related vocabulary in SKOS exists in practice | Read, ESCO page on SKOS. Not used in `roles.md` |

### Does it fit `known.json`?

Read: `fs-people/crates/fs-people-core/src/roles/known.json`, `definition.rs`, `registry.rs`, `assignment.rs`.

**Test.** rdflib 7.6.0, in a temporary environment under `/tmp`. No project file was changed.

The context used in the test, which is the draft for `roles.jsonld`:

```json
{
  "@version": 1.1,
  "skos": "http://www.w3.org/2004/02/skos/core#",
  "org": "http://www.w3.org/ns/org#",
  "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
  "fs": "https://freesynergy.net/ns#",
  "id": "@id",
  "type": "@type",
  "names": {"@id": "skos:prefLabel", "@container": "@language"},
  "description": {"@id": "skos:definition", "@container": "@language"},
  "roles": {"@reverse": "skos:inScheme"},
  "broader": {"@id": "skos:broader", "@type": "@id"},
  "closeMatch": {"@id": "skos:closeMatch", "@type": "@id"},
  "standard": "skos:note",
  "standardRefs": {"@id": "rdfs:seeAlso", "@type": "@id", "@container": "@set"},
  "fields": {"@id": "fs:roleField", "@container": "@set"},
  "name": "fs:fieldName",
  "owner": "fs:roleOwner",
  "scope": "fs:roleScope",
  "cardKind": "fs:cardKind"
}
```

Results:

- All four definitions of `known.json`, unchanged, with only the context added to each item, gave 20 triples. Labels came out as
  language-tagged `skos:prefLabel`, descriptions as `skos:definition`.
- Each subject had at most one `skos:prefLabel` per language (S14).
- Both examples in `roles.md` parsed (ours as shown, the second with `https://example.org/roles/kal/` instead of `<instance>`).
  Each role got `skos:inScheme` pointing to its file, and `id: ""` became the scheme's own address. The two examples used the
  inline context, since the `roles.jsonld` file does not exist.
- `@type` values and `skos:broader` came out as written. `closeMatch` is in the context, but no test data used it.

**Limits of the test.** It shows that the JSON maps to the intended RDF. It was not run through an OWL reasoner, so SKOS
consistency (§1.8) beyond S14 was not proven. It was not run through the Rust code.

Fit, field by field:

| `known.json` | SKOS or other | Note |
|--------------|---------------|------|
| `id` | `@id` | A short id only works relative to a base |
| `names` | `skos:prefLabel` | Same shape as a language map |
| `description` | `skos:definition` | Same shape as a language map |
| `standard` | `skos:note` | Free text; cannot be checked by machine, so `standardRefs` is proposed |
| `fields` | None | Own term. `RoleField` has no value type and no `extra`, so unknown keys in a field are dropped (read, `definition.rs`) |
| `owner`, `scope`, `cardKind` | None | Own terms |

Follow-ups for code, not done here, since code was out of scope:

- `RoleDefinition` keeps unknown keys through `extra` (`#[serde(flatten)]`), so `type`, `broader`, `closeMatch` and `standardRefs`
  would survive parsing but not be used.
- `parse` in `registry.rs` expects an array.
- `load` swaps the whole set, and `id` is the map key, so files cannot sit side by side and ids can clash.
- `AI_ROLE` is the short id `ai`. `RoleAssignment.role` is a plain string, which can hold a full id.
- `definition.rs` says it mirrors `people.capnp`. That file was not read, and it would need the same change.

Inconsistencies seen in existing files, not changed:

- `known.json`, `customer` description: "No standard exists yet: a gap." Terms do exist now (see below), so the wording should be
  sharper.
- `known.json` has `user` with owner `identity wrapper`, while the table in `roles.md` says `fs-people` configures users and the
  relation is open.
- `docs/de/interfaces/roles.md` exists and was not changed (the task allowed one doc only). It is now behind the English page.

## 2. Standards per role

Existing claims in `roles.md` that were re-checked and hold: vCard `RELATED` and its types (RFC 6350 §6.6.6), JSContact
`relatedTo` (RFC 9553 §2.1.8), JSContact `kind` `application` (RFC 9553 §2.1.4).

### Terms common to several roles

| Claim | Verified where |
|-------|----------------|
| vCard `ROLE` is free text: "the function or part played in a particular situation" | Read, RFC 6350 §6.6.2. A single text value. This is on the card, so we should not use it for assignments (a card export would reveal it) |
| JSContact `titles` with kind `title` or `role`: free-text names | Read, RFC 9553 §2.2.5. On the card, same problem |
| JSContact vendor properties: "not meant for interoperation"; the prefix must be a domain under the vendor's control | Read, RFC 9553 §1.8, §1.8.1 |
| SCIM `roles`: "No vocabulary or syntax is specified" | Read, RFC 7643 §4.1.2 |
| SCIM draft Role resource: value, display, type, supported, assignment limits, containedBy | Read, draft-ietf-scim-roles-entitlements-01 §3.2. A draft, expired 19 April 2026 (per its header; a later version was not checked). It is about available permissions in a service, not about what a person is to someone |
| AS2 `Relationship` has subject, object, relationship. Membership of an organisation is a named use | Read, AS2 Vocabulary §5.2 and the Relationship class entry |
| schema.org `Role` has `roleName` (Text or URL), `startDate`, `endDate` | Read, https://schema.org/Role . Page shows V30.1 and notes it is the development version |
| OASIS CIQ xPRL: pairs of parties with `RelationshipType`, `RelationshipRole`, `OtherPartyRelationshipRole` | Read, xPRL V3.0 Committee Specification (Nov 2009), examples in the spec, downloaded from OASIS |
| xPRL names "LAND LINE CUSTOMER OF", "SUPPLIER" and employee only as examples | Read, xPRL §4. Exact subsection not noted |
| xPRL values are not a vocabulary: "They only provides some sample values (and in most cases no values)" | Read, xPRL §6.2. Files `RelationshipTypeList.gc` and `RelationshipRoleList.gc` hold empty values (checked) |
| xPRL is an XML format. The OASIS committee "was closed by TC Administration on 14 April 2016 and is no longer active" | Read, OASIS CIQ committee page. So it is not named in `roles.md` |

### Customer

| Claim | Verified where |
|-------|----------------|
| UBL 2.3 is an OASIS Standard of 15 June 2021 | Read, https://docs.oasis-open.org/ubl/os-UBL-2.3/UBL-2.3.html , header |
| "two main actors, Customer and Supplier". Customer party roles include Originator, Buyer, Delivery, Accounting Customer | Read, UBL 2.3 §2.4, Table 1 |
| "the role of a specific actor depends on the specific circumstances" | Read, UBL 2.3 §2.4 |
| `CustomerParty`: "A class to describe a customer party." Used in Order and Invoice | Read, UBL 2.3 Order and Invoice summary reports |
| A party is "an individual, a group, or a body having a role in a business function" | Read, UBL 2.3 §2.2.8 |
| schema.org `customer`: on `Invoice` and `Order`, "Party placing the order or paying the invoice" | Read, schema.org vocabulary file (JSON-LD, latest release) |
| schema.org `eligibleCustomerType` and `BusinessEntityType` are about who an offer is for, not about a person | Read, vocabulary file. Not used in `roles.md` |
| FIBO `Customer`: "party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers"; subclass of `Buyer`, which is a `cmns-pts:PartyRole` | Read, FIBO `FND/ProductsAndServices/ProductsAndServices.ttl`, master/latest |
| FIBO also has `Client` ("purchases professional services...") and a customer identifier | Read, same file |
| FIBO is licensed under MIT terms in the file header. OMG lists FIBO Foundations 1.2 as formal, December 2017 | Read, file header; https://www.omg.org/spec/EDMC-FIBO/FND/ . **Not checked:** whether these classes are in formal 1.2. They were read in the EDM Council's latest version |
| FIBO is built for finance | OMG page lists its category as Finance. A proposal may map to it, but should not depend on it |
| No customer term in vCard, JSContact, SCIM | Searched RFC 6350, 9553, 7643. Hits only for unrelated uses, such as "customer relationship" in RFC 6350 prose |
| `org` has no customer, supplier, client, lead or prospect term | Searched the whole document, no hit |

**Conclusion, ours:** terms exist for a party in a transaction. None found says "this person is a customer of this organisation" as a
lasting role with a start and an end, in a way that any standard specifies. So the role is ours, mapped to these terms through
`standardRefs`.

### Lead, prospect

| Claim | Verified where |
|-------|----------------|
| Not in schema.org | Searched the full vocabulary file. Only hit for "prospect" is `hasSponsorshipOffer` ("Sponsorship Prospectus"). No class or property named lead |
| Not in vCard, JSContact, SCIM | Searched. RFC 9553 has only "lead" as a verb |
| Not in UBL 2.3 main document | Searched. Only "lead" as a word, such as lead time |
| Not in GoodRelations | Searched. Only "delivery lead time" |
| Not in FIBO's products ontology | Searched `ProductsAndServices.ttl`, no hit for lead, prospect or prospective. **Only this one FIBO file was searched, not all of FIBO** |
| Vendor use: HubSpot lifecycle stages: Subscriber, Lead, Marketing Qualified Lead, Sales Qualified Lead, Opportunity, Customer, Evangelist, Other | Read, https://knowledge.hubspot.com/records/use-lifecycle-stages . A vendor's product, not a standard |
| Earlier note on a vendor property `lifecycle` | `temp/research/contacts-identity-standards.md` line 21. That note flags control of `freesynergy.org` as unchecked. Existing examples use `freesynergy.net` |
| General web search for a lead or prospect standard | One search gave only general pages and vendor documents. A weak signal, and not proof |

**Conclusion:** a gap. Ours to specify.

### Supplier

| Claim | Verified where |
|-------|----------------|
| UBL `SupplierParty`: "A class to describe a supplier party." Roles include Seller, Despatch, Accounting Supplier, Payee, Tenderer | Read, UBL 2.3 §2.4 Table 1 and the Order summary report |
| FIBO `Supplier`: "party that provides goods or services that some party wants or needs, especially over a long period of time"; a `cmns-pts:PartyRole` | Read, FIBO file above |
| schema.org has no `supplier` | https://schema.org/supplier returned 404; searched the vocabulary. Only `eligibleWithSupplier` on `FinancialIncentive` |
| schema.org `seller`: "An entity which offers (sells / leases / lends / loans) the services / goods" | Read, vocabulary file. `vendor` is "an earlier term for 'seller'" |
| No supplier term in vCard, JSContact, SCIM | Searched |

**Conclusion, ours:** same as customer. Terms exist, the lasting role is ours.

### Employee

| Claim | Verified where |
|-------|----------------|
| `org:Role` with `org:Membership` fits an employee; no employee term is defined | Read, `org` §2.2, §5.3 |
| `org:remuneration` on a role | Read, `org` §5.3.5 |
| schema.org `EmployeeRole`: "A subclass of OrganizationRole used to describe employee relationships"; `baseSalary`, `salaryCurrency` | Read, https://schema.org/EmployeeRole |
| schema.org `employee` on `Organization`; `worksFor` on `Person` | Read, vocabulary file |
| SCIM `userType`: "Typical values used might be 'Contractor', 'Employee', 'Intern', 'Temp', 'External', and 'Unknown', but any value may be used" | Read, RFC 7643 §4.1.1 |
| SCIM enterprise extension: employeeNumber, costCenter, organization, division, department, manager | Read, RFC 7643 §4.3 |
| LDAP `employeeType`: same typical values, "any value may be used" | Read, RFC 2798 §2.5 |
| ILO: "Employees are workers employed for pay, on a formal or informal basis, who do not hold controlling ownership of the economic unit in which they are employed" | Read, ICSE-18 Manual (August 2023), section "C. Employees". Hosted by ILO (webapps.ilo.org) |
| ICSE-18 was adopted by the 20th ICLS in October 2018 | Read, the manual's Background. UNSD also lists ICSE-18 |

**Conclusion:** the best covered of the five. The shape and fields are standard. The value "Employee" is a typical example and not a
controlled term in SCIM and LDAP. The ILO meaning is for statistics.

### Volunteer

| Claim | Verified where |
|-------|----------------|
| No `VolunteerRole` in schema.org | https://schema.org/VolunteerRole returned 404. Searched: only hit is `ITVolunteerAssociationCharity`, an Italian nonprofit type |
| No volunteer term in `org`, vCard, JSContact, SCIM, FOAF, AS2 | Searched, 0 hits |
| ILO: "any unpaid, non-compulsory activity to produce goods or provide services for others" | Read, ILO Volunteer work measurement guide, section 3, quoting 19th ICLS Resolution I (October 2013, Geneva). **The resolution itself was not read** |
| That meaning leaves out civic participation such as voting | Read, same guide, section 3 |
| Volunteering and Social Action Ontology: describes "volunteering opportunities and volunteer-involving organisations". Its `Role` has title, commitment, applyLink, ages, skills. It describes a role on offer, and not a person holding it | Read, standard.volunteeringdata.io and `_pages/ontology.md` in its repository. ODI work commissioned by the UK DCMS. Its site mentions a "first draft" at an earlier stage. A post of 2026-03-26 links an ODI article whose address says "published standard" (article not read), so `roles.md` does not call it a draft. Its current formal status was not checked |
| schemaGov `volunteer` code: "Unpaid, usually on an advisory board or commission" | Read, schema.govfresh.com. Version `1.0.0-draft`, describes itself as a profile and not a standard. Government-only meaning. Not used in `roles.md` |
| Google job posting `employmentType` value `VOLUNTEER` | Read, Google Search Central. Vendor rule for job posts. Not used in `roles.md` |
| Salesforce has a volunteer data model | Search result only, not read. Vendor |

**Conclusion:** a gap. A meaning exists (ILO), a shape exists (`org:Role`), and no term or data format exists for a person as a
volunteer. The UK ontology is worth watching, since it is in active work and its roles could be linked to ours.

## 3. Proposal

Everything under "Defining a role yourself" and "To decide" in `roles.md` is a proposal by this research session. It is not a decision.

Reasons, each tied to the checks above:

- SKOS as the base: `org:Role` already is a `skos:Concept` (`org` §5.3.5).
- JSON-LD as the form: it keeps the JSON shape we have (test above). The project already uses JSON-LD with AS2.
- A file as a scheme: a git-shared file then has its own address, which separates your `customer` from ours (SKOS §4, §6.5.3).
- Own terms under `fs:`: `org` §3 and §5.3.5 allow this, and SKOS §7.1 calls its notes extension points.
- `https://freesynergy.net/ns#` as the prefix: already used in `docs/en/data/documents/examples.md`. Control of the domain was not checked.
- `skos:note` for `standard`: it keeps today's free text. `skos:closeMatch` was not used for links to standards, because SKOS §10.1
  defines it between concepts, and terms such as `schema:EmployeeRole` are classes. `rdfs:seeAlso` makes no such claim.
- `<instance>` in the personal example follows the id form `https://<instance>/documents/...` in the examples file above. The path
  `roles/kal/` is an example, not a defined rule.
