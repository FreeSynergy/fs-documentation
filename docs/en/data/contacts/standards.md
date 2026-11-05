# Contacts – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** This file only mirrors the entries relevant to contacts.

## Core standards (all ✅ verified at the RFC Editor, as of 2026-10-31)

| Standard | Evidence | Role |
|----------|----------|------|
| **JSContact, RFC 9553** | ✅ | canonical storage and exchange model (decision 1) |
| **vCard Format Extensions for JSContact, RFC 9554** | ✅ | lossless bridge JSContact ↔ vCard |
| **vCard 4.0, RFC 6350** | ✅ | file exchange; verified properties include `FN`, `N`, `NICKNAME`, `PHOTO`, `BDAY`, `GENDER`, `ADR`, `TEL`, `EMAIL`, `IMPP`, `LANG`, `TZ`, `GEO`, `TITLE`, `ROLE`, `ORG`, `MEMBER`, `RELATED`, `CATEGORIES`, `NOTE`, `UID`, `URL`, `KEY`, `KIND`, `SOURCE` |
| **jCard, RFC 7095** | ✅ | JSON form of vCard |
| **xCard, RFC 6351** | ✅ | XML form of vCard |
| **CardDAV, RFC 6352** | ✅ | folder access and sync for interoperability |

## Cross-cutting standards that affect contacts

| Standard | Evidence | Use |
|----------|----------|-----|
| Language Tags, RFC 5646 | ✅ | `preferredLanguages`, `localizations` |
| `geo:` URI, RFC 5870 | ✅ | `Address.coordinates` (details in [geodata/](../geodata/index.md)) |
| JSON Patch, RFC 6902 + JSContact `PatchObject` | ✅ | partial changes |

## JSContact `Card` — verified field list (excerpt from RFC 9553, ✅)

`@type`, `version`, `uid`, `name` (object with `components[]`, `kind` ∈ `title`, `given`, `given2`, `surname`, `surname2`, `credential`, `generation`, `separator`; plus `full`, `isOrdered`, `defaultSeparator`, `sortAs`, `phonetic`), `nicknames`, `organizations`, `titles`, `emails`, `onlineServices`, `phones`, `preferredLanguages`, `calendars`, `schedulingAddresses`, `addresses`, `cryptoKeys`, `directories`, `links`, `media`, `localizations`, `anniversaries`, `keywords`, `notes`, `personalInfo`.

The complete detailed description lives in [jscontact/description.md](jscontact/description.md) and [jscontact/storage.md](jscontact/storage.md).

## Open standard points

- **`lifecycle` (lead/prospect/customer/churned):** ❌ not contained in vCard 4.0 (evidenced). **Mechanism ✅ (RFC 9553 §1.8.1, checked 2026-11-05):** vendor-specific properties are named `<domain>:<name>` and implementations must keep them → `"<our-domain>:lifecycle"`. Domain to be fixed (⚠️ proposed `freesynergy.org`, ownership unchecked).
- **`Card.kind` ✅ (2026-11-05):** `individual` (default), `group`, `org`, `location`, `device`, `application`, plus vendor values `<domain>:<value>`.
- **`relatedTo` ✅:** maps the other card's `uid` to relation types (the 20 vCard `RELATED` values: `friend`, `colleague`, `me`, `spouse`, …). **None means "same person".**
- **Merging/aliasing ❌ (checked 2026-11-05):** no RFC defines it (9553, 9554, 9555, 9610, 9982, 10050) → our own rule, see [technical.md](technical.md).
- **RFC 9982** makes `uid` optional (✅ per research) — we keep it mandatory for exchange stability.

Evidence: `temp/research/contacts-identity-standards.md` (2026-11-05).
