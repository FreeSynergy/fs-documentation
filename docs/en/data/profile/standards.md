# Profile – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**


## State 2026-11-05

Evidence: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Evidence | Role |
|----------|----------|------|
| schema.org `Person` | ✅ core, declared equivalent to `foaf:Person` | export projection (web/SEO) |
| FOAF 0.99 (2014-01) | ✅ unmaintained | not used |
| GDPR Art. 9 "Processing of special categories of personal data" | ✅ (via gdpr-info.eu mirror) | legal basis for marking (ADR 0029) |
| **W3C DPV 2.3** (2026-02-25, Final CG Report — not a Recommendation) | ✅ | marking vocabulary (ADR 0029): `dpv:SpecialCategoryPersonalData`; `pd:SexualPreference`, `pd:Sexual` (no `SexualOrientation`); GDPR extension has Art. 9(2)(a)–(j) legal bases |

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **AS2 `Actor`** (Core/Vocabulary) | ✅ read | wrapper of the public view: `id` (absolute IRI, Core §4.1), `name`/`nameMap`, `preferredUsername`, `publicKey` |
| **AS2 `Profile` type** (Vocabulary) | ✅ checked 2026-11-05: "describes another object, usually an actor"; property `describes` | **envelope of the public view**: a `Profile` whose `describes` points to **myself** (my actor/DID). Same type as a contact card, which describes *someone else* (ADR 0020) |
| **AS2 audience `to`/`cc`/`bto`/`bcc`** | ✅ Core read | disclosure control per field/field group; **no** access control (decision 2) |
| **JSContact `Card`** (RFC 9553) | ✅ | source of the displayed fields |
| **schema.org `Person`** | ⚠️ not verified; `name` ✅ | web/SEO export projection |
| **FOAF** | ⚠️ not evidenced (so far only known as a vocabulary) | legacy vocabulary for person links; only evidence it if interoperability requires |

## Canonical rule (decision 1)

Profile = **AS2 `Actor` projection onto JSContact**. The handle (actor) is the social identity; the contents come from the card; the rules decide the visibility.

## What the standards do NOT regulate here (gaps → our own decision)

1. **Field groups/purpose binding:** no standard says which fields may be released together → our field-group table in [technical.md](technical.md) (not yet decided).
2. **Sensitive fields:** no data standard marks something as "especially in need of protection"; that is legal application (GDPR Art. 9 — ⚠️ quotation not evidenced) plus our product rule.
3. **Profile completeness display** (progress rings etc.) is UI, not a data standard.

## Open standard points

- ~~Evidence the `Profile` type~~ → ✅ 2026-11-05: profile = AS2 `Profile` describing myself; the actor (`Person` with `Multikey`, FEP-521a) stays the identity
- Verify schema.org `Person` before the SEO export is built
- Take Anton's `wot-profiles` (JWS-signed profile discoverability, ✅ reviewed) as a reference for signed profile delivery — signatures: FEP-8b32 object proofs + RFC 9421 transport (✅ 2026-11-05)
