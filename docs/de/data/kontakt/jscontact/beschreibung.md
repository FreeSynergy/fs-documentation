# JSContact – Beschreibung

JSContact ist ein standardisiertes, **reines JSON-Kontaktmodell**: RFC 9553 („JSContact: A JSON Representation of Contact Data", IETF, 2024). Eine Kontaktkarte ist ein Objekt `Card` mit wohldefinierten Eigenschaften – ohne Zeilenformat, ohne Escaping-Regeln wie bei vCard. Für FreeSynergy ist JSContact das **kanonische Modell der Domäne Kontakte** (Beschluss 1 in [standards.md](../../standards.md)).

## Warum diese Wahl

- Reines JSON – feldgenau speicherbar, ohne eigenem Parser (vCard braucht RFC 6350 + jCard RFC 7095 als Übersetzer)
- `name` ist ein strukturiertes Objekt `Name` mit `components[]` (`kind` = `title`, `given`, `given2`, `surname`, `surname2`, `credential`, `generation`, `separator`) sowie `full`, `isOrdered`, `defaultSeparator`, `sortAs`, `phonetic` – deckt chinesische, spanische und isländische Namensformen ab, ohne erfundene Felder (siehe [standards.md → Kontakte](../../standards.md))
- Offizielle Brücke zu vCard existiert: RFC 9554 („vCard Format Extensions for JSContact") – verlustloser Austausch in beide Richtungen
- JSON-Patch-Objekt (`PatchObject`) für teilweise Änderungen ist Teil des Standards
- `extensions`-Mechanismus für eigene Felder: erweitern statt erfinden (Beschluss 5)

## Aufbau der `Card` (RFC 9553 §2)

| Eigenschaft | Typ | Bedeutung |
|-------------|-----|-----------|
| `@type` | string | iCalART-URI der Card (Discriminator) |
| `version` | string | Modellversion (z. B. `2019-10-31`) |
| `uid` | string | stabile, wiederholbare Kennung der Card |
| `name` | `Name` | strukturierte Namensbestandteile (siehe oben) |
| `nicknames` | string[] | Rufnamen, Handles |
| `organizations` | `Organization[]` | Firma/Abteilung je Karte |
| `titles` | string[] | Berufsbezeichnungen |
| `emails` | map | E-Mail-Adressen mit Typen (`work`, `home`, …) |
| `onlineServices` | map | Accounts in Diensten (Social, Messaging) |
| `phones` | map | Telefonnummern mit Typen und `uri` |
| `preferredLanguages` | map | Sprachpräferenzen (Language Tags, RFC 5646) |
| `calendars` | map | Kalender-URIs der Person |
| `schedulingAddresses` | map | Scheduling-Adressen (`mailto:`) |
| `addresses` | `Address[]` | Postadressen mit Komponententypen (`locality`, `region`, `postcode`, `street`, …) und `coordinates` als `geo:`-URI (RFC 5870) – Bezug zu [geodaten](../../geodaten/index.md) |
| `cryptoKeys` | map | öffentliche Schlüssel (OpenPGP, Fingerprints) |
| `directories` | map | Ordner, in denen die Card lebt |
| `links` | map | Links zu Web-Profilen |
| `media` | map | Fotos, Audio, Logos (URL oder Data-URI) |
| `localizations` | map | locale-abhängige Übersetzungen von Textfeldern |
| `anniversaries` | map | besondere Daten (Geburtstag, Jubiläen) als `Annual`-Objekte |
| `keywords` / `notes` | map | Verschlagwortung, Freitext |
| `personalInfo` | `PersonalInfo` | `birthDate`, `deathDate`, `gender`, `subType` |
| `extensions` | map | standardisierter Erweiterungspunkt für eigene Felder |

## Abdeckung unserer Anforderungen

| Anforderung | JSContact | Hinweis |
|-------------|-----------|---------|
| Personen- und Firmenkarten | ✅ | `Organization[]`, `kind`-Unterscheidung via `personalInfo.subType` |
| Mehrere Adressen/Telefonnummern je Karte | ✅ | maps mit Typ-Schlüsseln |
| Historie/Revision | ⚠️ | Standard definiert kein Revisionsmodell – Umsetzung siehe [speicherung.md](speicherung.md) |
| Kundenstatus (`lifecycle`: lead/prospect/customer/churned) | ❌ | existiert in keinem Standard → als `extensions`-Erweiterung (⚠️ Mechanismus noch belegen, offener Punkt in [kontakt/index.md](../index.md)) |
| Feld-Mapping unserer Alt-Felder (`firstName`/`lastName`, `street`/`city`) | ✅ | siehe [mappings.md → Contact](../../mappings.md) |

## Siehe auch

- [kontakt/index.md](../index.md) – Domäne Kontakte (Standards, offene Punkte)
- [standards.md](../../standards.md) – Belegtabrik und Beschlüsse
- [mappings.md](../../mappings.md) – Feld-für-Feld-Mapping in alle Richtungen
- [felder.md](../../felder.md) – Feldkatalog
- [api.md](../../api.md) – einheitliches API-Muster (Patch, Fehlerblock)
