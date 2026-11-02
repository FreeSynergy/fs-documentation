# Kontaktdaten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.** Diese Datei spiegelt nur die für Kontakte einschlägigen Einträge.

## Kernstandards (alle ✅ beim RFC Editor geprüft, Stand 2026-10-31)

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **JSContact, RFC 9553** | ✅ | kanonisches Speicher- und Austauschmodell (Beschluss 1) |
| **vCard Format Extensions for JSContact, RFC 9554** | ✅ | verlustlose Brücke JSContact ↔ vCard |
| **vCard 4.0, RFC 6350** | ✅ | Datei-Austausch; geprüfte Eigenschaften u. a. `FN`, `N`, `NICKNAME`, `PHOTO`, `BDAY`, `GENDER`, `ADR`, `TEL`, `EMAIL`, `IMPP`, `LANG`, `TZ`, `GEO`, `TITLE`, `ROLE`, `ORG`, `MEMBER`, `RELATED`, `CATEGORIES`, `NOTE`, `UID`, `URL`, `KEY`, `KIND`, `SOURCE` |
| **jCard, RFC 7095** | ✅ | JSON-Form von vCard |
| **xCard, RFC 6351** | ✅ | XML-Form von vCard |
| **CardDAV, RFC 6352** | ✅ | Ordner-Zugriff und Sync für Interop |

## Querschnittsstandards, die Kontakte betreffen

| Standard | Beleg | Verwendung |
|----------|-------|------------|
| Language Tags, RFC 5646 | ✅ | `preferredLanguages`, `localizations` |
| `geo:`-URI, RFC 5870 | ✅ | `Address.coordinates` (Details in [geodata/](../geodata/index.md)) |
| JSON Patch, RFC 6902 + JSContact `PatchObject` | ✅ | teilweise Änderungen |

## JSContact-`Card` — geprüfte Feldliste (Auszug RFC 9553, ✅)

`@type`, `version`, `uid`, `name` (Objekt mit `components[]`, `kind` ∈ `title`, `given`, `given2`, `surname`, `surname2`, `credential`, `generation`, `separator`; dazu `full`, `isOrdered`, `defaultSeparator`, `sortAs`, `phonetic`), `nicknames`, `organizations`, `titles`, `emails`, `onlineServices`, `phones`, `preferredLanguages`, `calendars`, `schedulingAddresses`, `addresses`, `cryptoKeys`, `directories`, `links`, `media`, `localizations`, `anniversaries`, `keywords`, `notes`, `personalInfo`.

Die vollständige Detailbeschreibung liegt in [jscontact/beschreibung.md](jscontact/beschreibung.md) und [jscontact/speicherung.md](jscontact/speicherung.md).

## Offene Standard-Punkte

- **`lifecycle` (lead/prospect/customer/churned):** ❌ in vCard 4.0 nicht enthalten (belegt). Ersatz: `extensions`-Mechanismus von JSContact — ⚠️ Mechanismus noch Feld für Feld belegen.
- **Rollen-Enum der Card** (`individual`/`organization`/…): ⚠️ Begriffe aus vCard `KIND` bekannt, die exakte JSContact-Schreibweise noch belegen.
