# Contacts

This domain covers contact records for **people, organisations, groups and devices** — with reachability (email, phone, messenger, postal address) and name information. Canonical model: **JSContact** (RFC 9553, ✅).

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **JSContact, RFC 9553** | ✅ | **canonical model** (storage + API payload) |
| **vCard Extensions for JSContact, RFC 9554** | ✅ | lossless bridge JSContact ↔ vCard |
| **vCard 4.0, RFC 6350** | ✅ | file exchange (import/export) |
| **jCard, RFC 7095** | ✅ | JSON form of vCard |
| **CardDAV, RFC 6352** | ✅ | access and sync on contact folders |

## Standard directories

| Standard | Directory |
|----------|-----------|
| JSContact | [jscontact/](jscontact/description.md) |

## Open points

- `lifecycle` (lead/prospect/customer/churned) exists in none of the standards (❌ evidenced) → as a JSContact extension via `extensions` (⚠️ mechanism still to be evidenced)
- Mapping of our legacy fields (`firstName`/`lastName`, `street`/`city`): see [mappings.md → Contact](../mappings.md)

## See also

- [standards.md](../standards.md) (evidence table, decisions)
- [mappings.md](../mappings.md) (field by field)
- [fields.md](../fields.md)
