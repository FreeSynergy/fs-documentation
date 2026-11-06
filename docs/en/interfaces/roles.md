# Roles of a person

**Status: draft (2026-11-06), first provider in [`fs-people`](https://github.com/FreeSynergy/fs-people) v0.2.0.** Back to the [interfaces](index.md). ADR 0052.

## Idea

`fs-people` keeps people. There is one person, once, however many things they are to others. The same woman can be my
contact, my customer and a user of a system, without existing three times. She has one record, and several **roles**.

Roles follow standards wherever one exists, and they are defined in public, before programs use them. Everyone can also
**define their own role, in exactly the same way** as ours: a role made by you is not a second-class one.

## Two different things

| Kind | Question | Standard |
|------|----------|----------|
| **Relation** | What is this person to me? | vCard `RELATED` (RFC 6350 §6.6.6), JSContact `relatedTo` |
| **Role** | What is this person within a group or organisation? | W3C Organization Ontology: `org:Role`, `org:Membership` (Recommendation, 2014) |

## Where a role is kept

A role assignment is an **object of its own** (AS2 `Relationship`), never part of the person's card. So no export of a card can
reveal a role.

`fs-people` ships four role definitions so far: `ai`, `user`, `member` and `customer`. Supplier, employee and volunteer are
researched (see the table below), but not shipped yet.

## Known roles and relations

| Name | Kind | Standard | Owner | State |
|------|------|----------|-------|-------|
| Contact, friend, acquaintance, colleague, co-worker, neighbour, family, emergency contact | Relation | vCard `RELATED` types `contact`, `friend`, `acquaintance`, `colleague`, `co-worker`, `neighbor`, `kin`, `child`, `parent`, `sibling`, `spouse`, `emergency` | `fs-people` | Standard |
| User | Role | SCIM `User` (RFC 7643); Kanidm | `fs-people` configures users (ADR 0055); how this relates to the identity wrapper is open | Standard |
| Member of a group | Role | `org:Membership`, AS2 `Group`, SCIM `Group` | `fs-groups` | Standard |
| Customer | Role | Terms for a party in a sale: UBL 2.3 `CustomerParty` (§2.4), schema.org `customer` (on `Order` and `Invoice`), FIBO `Customer`. ❌ No standard for customer as a lasting role of a person. None in vCard, JSContact, SCIM or `org` | Later CRM | **Term exists, role is a gap: own specification** |
| Lead, prospect | Role | ❌ None found. Vendors only, such as the HubSpot lifecycle stage. No term in schema.org, UBL, FIBO's products ontology, vCard, JSContact or SCIM | Later CRM | **Gap, own specification** |
| AI | Marked participant, so everyone knows it is not human; names the person who hosts it (ADR 0054) | JSContact `kind` `application` (RFC 9553 §2.1.4); the link to the operator is still a gap | `fs-people` | Kind confirmed, operator open |
| Supplier | Role | Terms for a party in a sale: UBL 2.3 `SupplierParty` (§2.4), FIBO `Supplier`. schema.org has only `seller` and no supplier term. ❌ No standard for supplier as a lasting role of a person | Later ERP | **Term exists, role is a gap: own specification** |
| Employee | Role | `org:Role` with `org:Membership` (the ontology names salary and employment contract, §2.2); schema.org `EmployeeRole`; SCIM `userType` (RFC 7643 §4.1.1) and enterprise extension (§4.3); LDAP `employeeType` (RFC 2798 §2.5). In SCIM and LDAP the value is free text. Meaning: ILO ICSE-18 | Later ERP | Standard |
| Volunteer | Role | `org:Role` fits as a shape, but has no volunteer term. Meaning: ILO, 19th ICLS (2013), for statistics only. ❌ No data standard for a person as a volunteer. A UK ontology (volunteeringdata.io) describes opportunities, not people | Others, later | **Gap, own specification** |

## Defining a role yourself

`org:Role` is a subclass of `skos:Concept` (`org` §5.3.5). So a role is a described concept. The ontology allows extra
properties through "extension vocabularies" (§5.3.5) and allows profiles that add terms (§3).

**Proposal, not decided.** A role file is a SKOS concept scheme written as JSON-LD. Ours and yours have the same format. Only
the base address differs, and each role's full id is that base plus its short id.

| Field | Meaning | Maps to |
|-------|---------|---------|
| `id` | Short id, unique in the file | `@id`, relative to the file's base |
| `type` | `org:Role` for a role inside an organisation, otherwise `skos:Concept` | `@type` |
| `names` | Name per language | `skos:prefLabel` |
| `description` | Plain words per language | `skos:definition` |
| `broader` | Optional: the more general role, also in another file | `skos:broader` |
| `closeMatch` | Optional: the same idea in another file | `skos:closeMatch` |
| `standard` | The standard it follows, as text; none means a gap | `skos:note` |
| `standardRefs` | Optional: addresses of the standard's terms | `rdfs:seeAlso` |
| `fields` | What is extra about a person in this role; each field names its standard or says it has none | Own term `fs:roleField` |
| `owner` | The program responsible for it | Own term `fs:roleOwner` |
| `scope` | `personal`, `group` or `public` | Own term `fs:roleScope` |
| `cardKind` | Optional: the JSContact `kind` that cards with this role must have | Own term `fs:cardKind` |

Our role:

```json
{
  "@context": ["https://freesynergy.net/ns/roles.jsonld",
               {"@base": "https://freesynergy.net/ns/roles/"}],
  "id": "",
  "type": "skos:ConceptScheme",
  "names": {"en": "FreeSynergy roles"},
  "roles": [{
    "id": "employee",
    "type": "org:Role",
    "names": {"en": "Employee", "de": "Mitarbeiter"},
    "description": {"en": "Someone who works for pay in an organisation."},
    "standard": "org:Role; schema.org EmployeeRole",
    "standardRefs": ["https://schema.org/EmployeeRole"],
    "fields": [{"name": "employeeNumber",
                "standard": "SCIM enterprise User (RFC 7643, section 4.3)"}],
    "owner": "ERP (later)",
    "scope": "group"
  }]
}
```

Your role, in a file of the same form:

```json
{
  "@context": ["https://freesynergy.net/ns/roles.jsonld",
               {"@base": "https://<instance>/roles/kal/"}],
  "id": "",
  "type": "skos:ConceptScheme",
  "names": {"de": "Meine Rollen"},
  "roles": [{
    "id": "treasurer",
    "type": "org:Role",
    "names": {"de": "Kassenwart"},
    "broader": "https://freesynergy.net/ns/roles/member",
    "owner": "kal",
    "scope": "personal"
  }]
}
```

The context file `roles.jsonld` does not exist yet.

**What this proposal would change.** All four definitions in `known.json` keep their fields as they are. A test with a JSON-LD
parser read them unchanged. These things would change:

- The file becomes one object for the scheme, instead of an array.
- Roles are found by their full id. Today `id` alone is the key, so your `customer` would clash with ours.
- Your file must be able to sit next to ours. Today, loading a file replaces all definitions.
- `owner` holds placeholder text today (`CRM (later)`), not an id.

**Assignments (proposal).** A role assignment names the role by its full id. A role of type `org:Role` is exported as
`org:Membership` in addition to the AS2 `Relationship`, because `org` §3 does not allow other terms instead of its own where
its own fit. A personal role has no organisation, so it is only a `Relationship`.

**Not covered.** No standard read here defines the fields of a role, its owner or its scope, so these are our own terms. Value
types for fields are not defined yet. SHACL (W3C) is a candidate, but it is not read yet.

Definitions are configuration, so they can be added while programs run, and can be shared through a git repository
(ADR 0036, 0045).

## To decide

Our proposals for the project owner. None of these is decided.

1. **Format:** accept SKOS in JSON-LD as described above. This needs a change in `fs-people`.
2. **Address:** `https://freesynergy.net/ns/roles/` as the base of our roles. Existing examples use `https://freesynergy.net/ns#`.
   Who controls this domain is not checked here.
3. **Customer and supplier:** `org:Role` means a role "in an organization" (§5.3.5), and a customer or supplier stands outside
   it. We propose the type `skos:Concept` for these two, not `org:Role`.
4. **Companies:** UBL's party may be "an individual, a group, or a body" (§2.2.8), and a supplier is often a company. `fs-people`
   keeps people. Should it also keep cards of kind `org`? We propose yes for these two roles.
5. **Lead and prospect:** three roles (lead, prospect, customer), or one role with a stage? We propose three. A lead is not a
   kind of customer, and a person moves on by ending one assignment and starting the next.

## Open

1. **Is the role definition format itself a standard?** Answer: partly. SKOS is a W3C Recommendation (2009) and covers id, names,
   description, hierarchy and mapping (SKOS Reference §3 to §10). `org:Role` is already a `skos:Concept`, so SKOS fits as the base.
   SKOS has no JSON form of its own and is expressed as RDF (§1.3). JSON-LD 1.1 (W3C Recommendation, 2020) gives it one, and its
   language maps (§4.6.2) have the same shape as our `names`. SKOS does not cover fields, owner or scope. SKOS is not meant as a
   formal knowledge language (§1.3), so it describes a role and enforces nothing. The format above is our own profile of these
   standards (`org` §3), not a standard itself. It is a proposal.
2. **Who owns customer data:** the program that has the role, or `fs-people`? We propose that `fs-people` holds the person,
   and each role's owner holds that role's fields.
3. **Safety:** a role must never leak. That I am someone's customer is not everyone's business (ADR 0029). **Known gap:** the
   hub decides by object type, so a program allowed to read the type `Relationship` could see role assignments through it. This
   belongs to the sharing interface and is not solved yet.
