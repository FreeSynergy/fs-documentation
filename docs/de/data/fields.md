# Standardfelder

Felder sind die Bausteine der [Modelle](models.md). Über alle Programme hinweg werden sie **gleich benannt**, damit Komponenten, Frontends und Workflows ohne Übersetzungsschicht funktionieren.

## Standard-Verantwortung pro Feldgruppe

Nach der Regel in [conventions.md](conventions.md) braucht jedes Feld einen Beleg. Die vollständige Herleitung steht in [standards.md](standards.md) und [mappings.md](mappings.md). Hier die Kurzfassung pro Abschnitt. ✅ belegt, ⚠️ noch zu belegen.

| Feldgruppe | Verantwortlich | Beleg |
|-------------|---------|----------|
| ID-Felder (`id`, `externalId`) | JSContact `uid`, JSCalendar `uid` | ✅ RFC 9553 §2.1.9, RFC 8984 §4.1.2 |
| Zeitfelder (`createdAt`, `updatedAt`) | JSContact `created`/`updated` (Typ `UTCDateTime`), JSCalendar `created`/`updated`/`sequence` | ✅ RFC 9553 §1.4.5 und §2.1, RFC 8984 §4.1 |
| Zeitfelder (`start`, `timezone`, `recurrenceRule`) | JSCalendar `start`, `duration`, `timeZone`, `recurrenceRules` | ✅ Feldnamen belegt. **Unsere Formatregel „ISO 8601 mit Offset“ ist davon noch nicht abgedeckt** ⚠️ |
| Namensfelder (`name`, `firstName`, `lastName`) | JSContact `name.components[]` und `name.full`; schema.org `name`, `headline` | ✅ RFC 9553 §2.2.1; schema.org/Name, schema.org/headline |
| Kommunikationsfelder (`email`, `emails`, `phones`, `handle`) | JSContact `emails`, `phones`, `onlineServices`; vCard `TEL`, `EMAIL`, `IMPP` | ✅ RFC 9553 §2.3; RFC 6350 §6.4 |
| Status- und Prioritäts-Enums | JSCalendar `priority`, `freeBusyStatus`, `privacy`, `status`, `participationStatus` | ✅ RFC 8984 §4.4 und §5.1.3 |
| Berechtigungsfelder (`visibility`, `roles`, `permissions`, `scopes`) | **keine Verantwortung gefunden.** Kandidat ODRL (Erreichbarkeit geprüft, Inhalt nicht gelesen) | ⚠️ |
| Metadatenfelder (`tags`, `locale`, `revision`) | JSContact `keywords`, `language`, `localizations`; JSCalendar `categories`, `keywords`, `color` | ✅ RFC 9553 §2.7 und §2.8; RFC 8984 §4.2 |
| Inhaltsfelder (`body`, `bodyFormat`, `blocks`) | RFC 9073 `STYLED-DESCRIPTION` (`FMTTYPE`, `DERIVED`), JSCalendar `descriptionContentType` | ✅ RFC 9073 §6.5; RFC 8984 §4.2.3 |
| UI- und Interaktionsfelder (`ariaLabel`, `role`, …) | sind **keine** Datenbankfelder — sie gehören in die Komponenten-Dokumentation | ⚠️ Beleg aus HTML/ARIA noch nicht nachgeschlagen |

Folge: Die Feldnamen in dieser Datei bleiben unsere **interne** Schreibweise. Was beim Export nach außen daraus wird, steht in [mappings.md](mappings.md).

## ID-Felder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `id` | string | ✅ | eindeutige, undurchsichtige Ressourcen-ID | `"doc_01HZXD8R7M"` |
| `externalId` | string | ➖ | ID im Quellsystem bei der Synchronisation | `"_mediaWiki:1234"` |
| `slug` | string | ➖ | URL-lesbarer Pfadteil, eindeutig innerhalb des übergeordneten Objekts | `"project-a/overview"` |
| `parentId` | reference | ➖ | übergeordnete Ressource | `"doc_01HZXC"` |

Regeln:

- Präfix + sortierbare ID (`<type>_<uuid>` (UUIDv7)), nach außen keine laufenden Nummern
- `slug` nur für adressierbare Ressourcen (`Document`, `Space`, `Team`)

## Zeitfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `createdAt` | datetime | ✅ | Zeitpunkt der Anlage (System) | `"2026-10-01T09:00:00+02:00"` |
| `updatedAt` | datetime | ✅ | letzte Änderung (System) | `"2026-10-30T18:22:10+01:00"` |
| `deletedAt` | datetime \| null | ➖ | Zeitpunkt des Soft-Deletes | `null` |
| `start` / `end` | datetime | ✅ (Event) | Beginn und Ende | `"2026-11-05T10:00:00+01:00"` |
| `dueAt` | datetime \| null | ➖ | Fälligkeit einer Aufgabe | `"2026-11-01T17:00:00+01:00"` |
| `allDay` | boolean | ➖ | Termin ohne Uhrzeit | `true` |
| `timezone` | string | ✅ (Event) | IANA-Zeitzone | `"Europe/Berlin"` |
| `recurrenceRule` | string \| null | ➖ | RRULE nach RFC 5545 | `"FREQ=WEEKLY;BYDAY=WE"` |
| `duration` | duration | ➖ | ISO-8601-Dauer | `"PT1H30M"` |

Regeln:

- immer ISO 8601 mit Offset, nie „nackte“ lokale Zeitstempel
- `date`-Felder (`YYYY-MM-DD`) nur für Daten ohne Uhrzeit (z. B. Geburtsdatum)
- Dauern als ISO-8601-Dauer (`PT30M`), nicht als Minutenzahl

## Typen und Darstellung

| Typ | Notation | Beispiel |
|------|----------|----------|
| `string` | `"..."` | `"Anna Weber"` |
| `number` | Zahl ohne Tausendertrennzeichen | `19.99` |
| `integer` | ganze Zahl | `42` |
| `boolean` | `true` / `false` | `false` |
| `datetime` | ISO 8601 mit Offset | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | ISO-8601-Dauer | `"PT30M"` |
| `enum` | Kleinbuchstaben, Singular | `"active"` |
| `array[]` | Liste von Werten oder Referenzen | `["tag_01", "tag_02"]` |
| `object` | freies Objekt, gültig gegen ein JSON Schema | `{"layout":"grid"}` |
| `reference` | ID-String mit dem Modell der Referenz in der Doku | `"user_01HZXA"` |
| `markdown` | Markdown-Text | `"**Wichtig**: …"` |
| `richtext` | Blockstruktur (Blockarray) | `[{"type":"heading", …}]` |
| `html` | nur beim Import aus fremden Systemen | `"<b>…</b>"` |
| `null` | fehlender Wert | `null` |

## Namensfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `firstName` | string | ✅ | Vorname | `"Anna"` |
| `lastName` | string | ✅ | Nachname | `"Weber"` |
| `displayName` | string | ✅ | Anzeigename (das System kann ihn ableiten) | `"Anna Weber"` |
| `name` | string | ✅ | einheitlicher Name für Organisationen/Boards | `"Nordwind GmbH"` |
| `pronouns` | string | ➖ | Pronomen für die Anrede | `"sie/ihr"` |
| `title` | string | ✅ | Titel einer Ressource | `"Einführung"` |

## Kommunikationsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `email` | string | ➖ | Haupt-E-Mail (User) | `"anna@example.org"` |
| `emails` | array[] | ➖ | mehrere Adressen (Contact) | `[{"type":"work","value":"…"}]` |
| `phones` | array[] | ➖ | Nummern im Format E.164 | `[{"type":"mobile","value":"+4930123456"}]` |
| `urls` | array[] | ➖ | Webadressen | `[{"type":"profile","value":"https://…"}]` |
| `handle` | string | ➖ | Kontoname in einem Dienst | `"@anna:matrix.org"` |
| `channelId` | reference | ✅ (Message) | Zielkanal | `"chan_01HZYC"` |

## Status- und Prioritäts-Enums

| Feld | Werte | Bedeutung |
|-------|--------|----------|
| `status` (Ressource) | `draft`, `active`, `archived`, `deleted` | Lebenszyklus |
| `status` (Aufgabe) | `open`, `in_progress`, `done`, `archived` | Fortschritt der Arbeit |
| `status` (Dokument) | `draft`, `published`, `archived` | Veröffentlichung |
| `status` (Termin) | `confirmed`, `tentative`, `cancelled` | Terminstatus |
| `status` (User) | `active`, `invited`, `disabled`, `deleted` | Kontostatus |
| `priority` | `low`, `normal`, `high`, `urgent` | Dringlichkeit |
| `visibility` | `private`, `workspace`, `public` | Sichtbarkeit |
| `role` | `owner`, `admin`, `editor`, `commenter`, `viewer` | Berechtigung |
| `lifecycle` (Contact) | `lead`, `prospect`, `customer`, `churned` | Kundenstatus |
| `response` (Teilnehmer) | `accepted`, `declined`, `tentative`, `needsAction` | Zu- oder Absage zu einem Termin |

Regeln:

- Enums sind klein geschrieben, im Singular, mit Unterstrich statt Bindestrich (`in_progress`)
- neue Werte dürfen additiv ergänzt werden, bestehende werden nie entfernt
- der Anzeigetext kommt aus `locales/<code>.json`, nie aus dem Datenwert

## Berechtigungsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `visibility` | enum | ➖ | Sichtbarkeit der Ressource | `"workspace"` |
| `ownerId` | reference (User) | ➖ | Besitzer | `"user_01HZXA"` |
| `roles` | array[] | ✅ (User, Membership) | Liste der Rollen | `["editor"]` |
| `permissions` | array[] | ➖ | einzelne Rechte | `["document:read", "document:write"]` |
| `scopes` | array[] | ➖ | API-Scopes einer Integration | `["read:documents"]` |

## Metadatenfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `tags` | array[] (Tag) | ➖ | Schlagwörter | `["docs", "wiki"]` |
| `category` | string | ➖ | Kategorie-Verzeichnis der App | `"wiki"` |
| `locale` | string | ➖ | Sprachcode der Ressource | `"en"` |
| `metadata` | object | ➖ | programmspezifische Zusatzdaten | `{"mediawikiNamespace":0}` |
| `revision` | number | ➖ | aktuelle Versionsnummer | `7` |
| `etag` | string | 🔁 | Änderungsmarker für `If-Match` | `"W/\"7-a1b2\""` |
| `source` | string | ➖ | Herkunft des Datensatzes | `"import:csv-2026-10"` |

## Inhaltsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|-------|------|----------|-------------|---------|
| `body` | markdown | ➖ | Fließtext (Nachricht, Kommentar) | `"Hallo zusammen"` |
| `bodyFormat` | enum | ➖ | Format von `body` | `"markdown"` |
| `blocks` | array[] (Block) | ✅ (Document) | strukturierter Inhalt | `[{"type":"heading", …}]` |
| `excerpt` | string | ➖ | kurze Vorschau, max. 280 Zeichen | `"Einführung in …"` |
| `wordCount` | number | 🔁 | Anzahl der Wörter | `512` |

## UI- und Interaktionsfelder

Diese Felder tauchen in den Komponenten-Attributen ([Komponenten](../components/)) und in `layout.md` auf:

| Feld | Typ | Beschreibung | Beispiel |
|-------|------|-------------|---------|
| `ariaLabel` | string | barrierefreie Beschreibung | `"Suche öffnen"` |
| `role` | string | ARIA-Rolle | `"button"` |
| `animation` | string | Name der Animation | `"fade-in"` |
| `duration` | number | Dauer der Animation in ms | `300` |
| `onTap` / `onSwipe` / `onShake` | function | Callbacks für Gesten | — |
| `columns` / `rows` / `span` | number | Rasterlayout eines Widgets | `4` |
| `order` | number | Sortierposition | `12` |

## Null-Werte und Defaults

| Fall | Notation | Hinweis |
|------|----------|---------|
| Wert bewusst leer | `null` | immer in dieser Form |
| leere Liste | `[]` | nie `null` für Listen |
| leerer Text in einem Pflichtfeld | nicht erlaubt | Validierungsfehler |
| optionales Feld ohne Wert | Feld weglassen | im Request; `null` in der Response |

## Siehe auch

- [Datenmodelle](models.md)
- [Datenformate](formats.md)
- [Konventionen](conventions.md)
- [Daten-API](api.md)
