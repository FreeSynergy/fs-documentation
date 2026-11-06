# Roles of a person

**Status: draft (2026-11-06).** Back to the [interfaces](index.md). ADR 0052.

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

## Known roles and relations

| Name | Kind | Standard | Owner | State |
|------|------|----------|-------|-------|
| Contact, friend, acquaintance, colleague, co-worker, neighbour, family, emergency contact | Relation | vCard `RELATED` types `contact`, `friend`, `acquaintance`, `colleague`, `co-worker`, `neighbor`, `kin`, `child`, `parent`, `sibling`, `spouse`, `emergency` | `fs-people` | Standard |
| User | Role | SCIM `User` (RFC 7643); Kanidm | Identity wrapper | Standard |
| Member of a group | Role | `org:Membership`, AS2 `Group`, SCIM `Group` | `fs-groups` | Standard |
| Customer, lead, prospect | Role | ❌ none found in vCard or JSContact; so far a vendor property (`lifecycle`) | Later CRM | **Gap, own specification** |
| AI | Marked participant, so everyone knows it is not human (ADR 0054) | JSContact `kind` `application`, to be checked | `fs-people` | Open |
| Supplier, employee, volunteer | Role | To be researched | Later ERP, others | Open |

## Defining a role yourself

Following `org:Role`, a role is a described concept, and the ontology expects domains to bring their own. A role
definition is an object, for ours and for yours alike:

| Field | Meaning |
|-------|---------|
| Id, name, description | What the role is, in plain words and in several languages |
| Standard | The standard it follows, if any |
| Fields | What is extra about a person in this role; each field names its standard or says it has none |
| Owner | The program responsible for it |
| Scope | Personal, a group, or published for everyone |

Definitions are configuration, so they can be added while programs run, and can be shared through a git repository
(ADR 0036, 0045).

## Open

1. **Is the role definition format itself a standard?** Candidates: SKOS (which `org:Role` builds on). Not read yet.
2. **Who owns customer data:** the program that has the role, or `fs-people`? We propose that `fs-people` holds the person,
   and each role's owner holds that role's fields.
3. **Safety:** a role must never leak. That I am someone's customer is not everyone's business (ADR 0029).
