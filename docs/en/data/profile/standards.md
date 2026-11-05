# Profile – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **AS2 `Actor`** (Core/Vocabulary) | ✅ read | wrapper of the public view: `id` (absolute IRI, Core §4.1), `name`/`nameMap`, `preferredUsername`, `publicKey` |
| **AS2 `Profile` type** (Vocabulary) | ✅ present in the vocabulary; field details ⚠️ section still to evidence | "A profile object contains minimal information about its owner." — candidate for the minimal view |
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

- Evidence the `Profile` type field by field and decide whether we use it as the response form or represent the actor directly
- Verify schema.org `Person` before the SEO export is built
- Take Anton's `wot-profiles` (JWS-signed profile discoverability, ✅ reviewed) as a reference for signed profile delivery — the signature mechanism remains ⚠️/❌ open
