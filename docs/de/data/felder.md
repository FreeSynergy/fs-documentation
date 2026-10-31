# Standardfelder

Felder sind die Bausteine der [Modelle](modelle.md). Sie sind über alle Programme hinweg **gleich benannt**, damit Komponenten, Skins und Workflows ohne Übersetzungsschicht funktionieren.

## ID-Felder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `id` | string | ✅ | eindeutige, opaque Ressourcen-ID | `"doc_01HZXD8R7M"` |
| `externalId` | string | ➖ | ID im Quellsystem bei Synchronisation | `"_mediaWiki:1234"` |
| `slug` | string | ➖ | URL-lesbarer Pfadteil, eindeutig im Elternobjekt | `"projekt-a/übersicht"` |
| `parentId` | reference | ➖ | übergeordnete Ressource | `"doc_01HZXC"` |

Regeln:

- Präfix + sortierbare ID (`<typ>_<ulid>`), keine laufenden Nummern nach außen
- `slug` nur für adressierbare Ressourcen (`Document`, `Space`, `Team`)

## Zeitfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `createdAt` | datetime | ✅ | Anlagezeitpunkt (System) | `"2026-10-01T09:00:00+02:00"` |
| `updatedAt` | datetime | ✅ | letzte Änderung (System) | `"2026-10-30T18:22:10+01:00"` |
| `deletedAt` | datetime \| null | ➖ | Soft-Delete-Zeitpunkt | `null` |
| `start` / `end` | datetime | ✅ (Event) | Beginn und Ende | `"2026-11-05T10:00:00+01:00"` |
| `dueAt` | datetime \| null | ➖ | Fälligkeit einer Aufgabe | `"2026-11-01T17:00:00+01:00"` |
| `allDay` | boolean | ➖ | Termin ohne Uhrzeit | `true` |
| `timezone` | string | ✅ (Event) | IANA-Zeitzone | `"Europe/Berlin"` |
| `recurrenceRule` | string \| null | ➖ | RRULE nach RFC 5545 | `"FREQ=WEEKLY;BYDAY=WE"` |
| `duration` | duration | ➖ | ISO-8601-Dauer | `"PT1H30M"` |

Regeln:

- immer ISO 8601 mit Offset, niemals lokale „nackte“ Zeitstempel
- `date`-Felder (`YYYY-MM-DD`) nur für Datumsangaben ohne Zeitpunkt (z. B. Geburtsdatum)
- Dauern als ISO-8601-Duration (`PT30M`), nicht als Minutenzahl

## Typen und Repräsentation

| Typ | Schreibweise | Beispiel |
|-----|--------------|----------|
| `string` | `"..."` | `"Anna Weber"` |
| `number` | Zahl ohne Tausenderpunkt | `19.99` |
| `integer` | Ganzzahl | `42` |
| `boolean` | `true` / `false` | `false` |
| `datetime` | ISO 8601 mit Offset | `"2026-10-31T06:00:00+01:00"` |
| `date` | `YYYY-MM-DD` | `"2026-10-31"` |
| `duration` | ISO 8601 Duration | `"PT30M"` |
| `enum` | lowercase, Singular | `"active"` |
| `array[]` | Liste von Werten oder Referenzen | `["tag_01", "tag_02"]` |
| `object` | freies Objekt, gültig gegen JSON Schema | `{"layout":"grid"}` |
| `reference` | ID-String mit Modellbezug in der Doku | `"user_01HZXA"` |
| `markdown` | Markdown-Text | `"**Wichtig**: …"` |
| `richtext` | Block-Struktur (Block-Array) | `[{"type":"heading", …}]` |
| `html` | nur bei Import aus Fremdsystemen | `"<b>…</b>"` |
| `null` | fehlender Wert | `null` |

## Namensfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `firstName` | string | ✅ | Vorname | `"Anna"` |
| `lastName` | string | ✅ | Nachname | `"Weber"` |
| `displayName` | string | ✅ | Anzeigename (System kann ableiten) | `"Anna Weber"` |
| `name` | string | ✅ | Einzelname für Organisationen/Boards | `"Nordwind GmbH"` |
| `pronouns` | string | ➖ | Anrede-Pronomen | `"she/her"` |
| `title` | string | ✅ | Titel einer Ressource | `"Einführung"` |

## Kommunikationsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `email` | string | ➖ | Haupt-E-Mail (User) | `"anna@example.org"` |
| `emails` | array[] | ➖ | mehrere Adressen (Contact) | `[{"type":"work","value":"…"}]` |
| `phones` | array[] | ➖ | Nummern im E.164-Format | `[{"type":"mobile","value":"+4930123456"}]` |
| `urls` | array[] | ➖ | Webadressen | `[{"type":"profile","value":"https://…"}]` |
| `handle` | string | ➖ | Account-Name in einem Dienst | `"@anna:matrix.org"` |
| `channelId` | reference | ✅ (Message) | Zielkanal | `"chan_01HZYC"` |

## Status- und Prioritäts-Enums

| Feld | Werte | Bedeutung |
|------|-------|-----------|
| `status` (Ressource) | `draft`, `active`, `archived`, `deleted` | Lebenszyklus |
| `status` (Task) | `open`, `in_progress`, `done`, `archived` | Bearbeitungsstand |
| `status` (Document) | `draft`, `published`, `archived` | Veröffentlichung |
| `status` (Event) | `confirmed`, `tentative`, `cancelled` | Terminstatus |
| `status` (User) | `active`, `invited`, `disabled`, `deleted` | Kontostatus |
| `priority` | `low`, `normal`, `high`, `urgent` | Dringlichkeit |
| `visibility` | `private`, `workspace`, `public` | Sichtbarkeit |
| `role` | `owner`, `admin`, `editor`, `commenter`, `viewer` | Berechtigung |
| `lifecycle` (Contact) | `lead`, `prospect`, `customer`, `churned` | Kundenstatus |
| `response` (Attendee) | `accepted`, `declined`, `tentative`, `needsAction` | Zu- oder Absage zum Termin |

Regeln:

- Enums sind lowercase, Singular, mit Unterstrich statt Bindestrich (`in_progress`)
- Neue Werte sind additiv erlaubt, bestehende werden nie entfernt
- Anzeigetext kommt aus `locales/<code>.json`, nie aus dem Datenwert

## Berechtigungsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `visibility` | enum | ➖ | Sichtbarkeit der Ressource | `"workspace"` |
| `ownerId` | reference (User) | ➖ | Besitzer | `"user_01HZXA"` |
| `roles` | array[] | ✅ (User, Membership) | Rollenliste | `["editor"]` |
| `permissions` | array[] | ➖ | Einzelrechte | `["document:read", "document:write"]` |
| `scopes` | array[] | ➖ | API-Scopes einer Integration | `["read:documents"]` |

## Metadatenfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `tags` | array[] (Tag) | ➖ | Schlagwörter | `["doku", "wiki"]` |
| `category` | string | ➖ | Kategorie-Verzeichnis der App | `"wiki"` |
| `locale` | string | ➖ | Sprachcode der Ressource | `"de"` |
| `metadata` | object | ➖ | programmspezifische Zusatzdaten | `{"mediawikiNamespace":0}` |
| `revision` | number | ➖ | aktuelle Versionsnummer | `7` |
| `etag` | string | 🔁 | Änderungsmarke für `If-Match` | `"W/\"7-a1b2\""` |
| `source` | string | ➖ | Herkunft des Datensatzes | `"import:csv-2026-10"` |

## Inhaltsfelder

| Feld | Typ | Pflicht | Beschreibung | Beispiel |
|------|-----|---------|--------------|----------|
| `body` | markdown | ➖ | Fließtext (Nachricht, Kommentar) | `"Hallo zusammen"` |
| `bodyFormat` | enum | ➖ | Format von `body` | `"markdown"` |
| `blocks` | array[] (Block) | ✅ (Document) | strukturierter Inhalt | `[{"type":"heading", …}]` |
| `excerpt` | string | ➖ | Kurzvorschau, max. 280 Zeichen | `"Einführung in …"` |
| `wordCount` | number | 🔁 | Wortanzahl | `512` |

## UI- und Interaktionsfelder

Diese Felder erscheinen in Komponenten-Attributen ([components](../components/)) und in `structure.md`:

| Feld | Typ | Beschreibung | Beispiel |
|------|-----|--------------|----------|
| `ariaLabel` | string | Barrierefreie Beschreibung | `"Suche öffnen"` |
| `role` | string | ARIA-Rolle | `"button"` |
| `animation` | string | Animationsname | `"fade-in"` |
| `duration` | number | Animationsdauer in ms | `300` |
| `onTap` / `onSwipe` / `onShake` | function | Gesten-Callbacks | — |
| `columns` / `rows` / `span` | number | Grid-Layout eines Widgets | `4` |
| `order` | number | Sortierposition | `12` |

## Null-Werte und Defaults

| Fall | Schreibweise | Bemerkung |
|------|--------------|-----------|
| Wert bewusst leer | `null` | immer diese Form |
| Leere Liste | `[]` | nie `null` für Listen |
| Leerer Text in Pflichtfeld | nicht erlaubt | Validierungsfehler |
| Optional ohne Angabe | Feld weglassen | im Request; in Response `null` |

## Siehe auch

- [Datenmodelle](modelle.md)
- [Datenformate](formate.md)
- [Konventionen](konventionen.md)
- [Daten-API](api.md)
