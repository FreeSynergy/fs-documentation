# JSContact – description

JSContact is a standardised, **pure JSON contact model**: RFC 9553 ("JSContact: A JSON Representation of Contact Data", IETF, 2024). A contact card is a `Card` object with well-defined properties — no line format, no escaping rules as in vCard. For FreeSynergy, JSContact is the **canonical model of the contacts domain** (decision 1 in [standards.md](../../standards.md)).

## Why this choice

- Pure JSON — storable field by field, without its own parser (vCard needs RFC 6350 + jCard RFC 7095 as translators)
- `name` is a structured `Name` object with `components[]` (`kind` = `title`, `given`, `given2`, `surname`, `surname2`, `credential`, `generation`, `separator`) plus `full`, `isOrdered`, `defaultSeparator`, `sortAs`, `phonetic` — covers Chinese, Spanish and Icelandic name forms without invented fields (see [standards.md → Contacts](../../standards.md))
- An official bridge to vCard exists: RFC 9554 ("vCard Format Extensions for JSContact") — lossless exchange in both directions
- The JSON patch object (`PatchObject`) for partial changes is part of the standard
- `extensions` mechanism for own fields: extend instead of invent (decision 5)

## Structure of the `Card` (RFC 9553 §2)

| Property | Type | Meaning |
|----------|------|---------|
| `@type` | string | URI of the card (discriminator) |
| `version` | string | model version (e.g. `2019-10-31`) |
| `uid` | string | stable, repeatable identifier of the card |
| `name` | `Name` | structured name components (see above) |
| `nicknames` | string[] | call names, handles |
| `organizations` | `Organization[]` | company/department per card |
| `titles` | string[] | professional titles |
| `emails` | map | email addresses with types (`work`, `home`, …) |
| `onlineServices` | map | accounts in services (social, messaging) |
| `phones` | map | phone numbers with types and `uri` |
| `preferredLanguages` | map | language preferences (Language Tags, RFC 5646) |
| `calendars` | map | calendar URIs of the person |
| `schedulingAddresses` | map | scheduling addresses (`mailto:`) |
| `addresses` | `Address[]` | postal addresses with component types (`locality`, `region`, `postcode`, `street`, …) and `coordinates` as a `geo:` URI (RFC 5870) – relation to [geodata](../../geodata/index.md) |
| `cryptoKeys` | map | public keys (OpenPGP, fingerprints) |
| `directories` | map | folders in which the card lives |
| `links` | map | links to web profiles |
| `media` | map | photos, audio, logos (URL or data URI) |
| `localizations` | map | locale-dependent translations of text fields |
| `anniversaries` | map | special dates (birthday, anniversaries) as `Annual` objects |
| `keywords` / `notes` | map | tagging, free text |
| `personalInfo` | `PersonalInfo` | `birthDate`, `deathDate`, `gender`, `subType` |
| `extensions` | map | standardised extension point for own fields |

## Coverage of our requirements

| Requirement | JSContact | Note |
|-------------|-----------|------|
| Personal and company cards | ✅ | `Organization[]`, `kind` distinction via `personalInfo.subType` |
| Several addresses/phone numbers per card | ✅ | maps with type keys |
| History/revision | ⚠️ | the standard defines no revision model – implementation see [storage.md](storage.md) |
| Customer status (`lifecycle`: lead/prospect/customer/churned) | ❌ | exists in no standard → as an `extensions` extension (⚠️ mechanism still to be evidenced, open point in [people/index.md](../index.md)) |
| Field mapping of our legacy fields (`firstName`/`lastName`, `street`/`city`) | ✅ | see [mappings.md → Contact](../../mappings.md) |

## See also

- [people/index.md](../index.md) – contacts domain (standards, open points)
- [standards.md](../../standards.md) – evidence table and decisions
- [mappings.md](../../mappings.md) – field-by-field mapping in all directions
- [fields.md](../../fields.md) – field catalogue
- [api.md](../../api.md) – unified API pattern (patch, error block)
