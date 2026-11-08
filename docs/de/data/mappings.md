# Feld-Zuordnungen

Diese Datei ordnet **unsere bestehenden Felder** belegten Standards zu. Hier werden Konflikte sichtbar, bevor es Code gibt.

Regel: Ein Eintrag zählt nur, wenn er eine Quelle hat. Wie in [standards.md](standards.md): ✅ belegt (abgerufen am 2026-10-31 bei RFC Editor / w3.org / schema.org), ⚠️ ungeprüft, ❌ als fehlend belegt.

Jedes Beispiel hier ist **wörtlich aus den Spezifikationen übernommen oder aus deren Feldnamen zusammengesetzt** — keine erfundenen Felder.

## Contact

Unsere Definition steht in [models.md](models.md#contact). Dies ist der Vergleich:

| Unser Feld | Belegtes Gegenstück | Quelle | Hinweis |
|-----------|-----------------------|--------|------|
| `id` | `uid` (Pflicht in JSContact), vCard `UID` | ✅ RFC 9553 §2.1.9, RFC 6350 | Unsere ID ist eine interne UUIDv7. Das reicht für AS2 nicht (siehe unten) |
| `firstName` + `lastName` | `name.components[]` mit `kind`: `given`, `given2`, `surname`, `surname2`, `title`, `credential`, `generation`, `separator` | ✅ RFC 9553 §2.2.1.2 | **Das Zwei-Felder-Modell ist zu schwach.** JSContact deckt so Mittelnamen, einen zweiten Nachnamen (Spanisch), Anredetitel und Generationssuffix ab |
| — (fehlt) | `name.full` | ✅ RFC 9553 §2.2.1.1 | genau das einzelne `name`, das du willst |
| `displayName` | `name.full` oder `name` | ✅ RFC 9553, schema.org `name` | bei uns nur 🔁 abgeleitet — das passt, ableiten statt speichern |
| `emails[] {type, value}` | `emails` → `Resource` mit `uri`, `contexts`, `pref`, `label`, `mediaType`, `kind` | ✅ RFC 9553 §1.4.4, §2.3.1 | `type` heißt dort `contexts`; die üblichen Werte sind `private` und `work` |
| `phones[] {type, value}` | `phones` → `Resource` | ✅ RFC 9553 §2.3.3 | vCard-Seite: `TEL` mit `TYPE`-Parametern |
| — (fehlt) | `onlineServices` | ✅ RFC 9553 §2.3.2 | der richtige Ort für `handle` (`@anna:matrix.org`); vCard nennt es `IMPP` |
| `organization` | `organizations{}` mit `name`, `units[]` (`OrgUnit.name`), `sortAs`, `contexts` | ✅ RFC 9553 §2.2.3 | mehrwertig und mit Organisationseinheiten — besser als ein String |
| `jobTitle` | `titles` | ✅ RFC 9553 §2.2.5 | vCard-Seite: `TITLE` (Position) und `ROLE` (Funktion) sind **zwei verschiedene** Eigenschaften |
| `addresses[]` | `addresses{}` → `Address` mit `components[]` (`kind`: `number`, `name`, `block`, `locality`, `region`, `postcode`, `country`, `district`, `subdistrict`, `room`, `apartment`, `floor`, `building`, `direction`, `landmark`, `postOfficeBox`, `separator`), `countryCode`, `coordinates`, `timeZone`, `full`, `isOrdered`, `defaultSeparator`, `pref`, `contexts` (u. a. `billing`, `delivery`) | ✅ RFC 9553 §2.5.1 | unsere `street`/`houseNumber`/`postalCode`/`city` sind eine **westeuropäische Vereinfachung**; die Komponententypen sind der Standard |
| `lat`/`lng` (in Location) | `Address.coordinates` als `geo:`-URI | ✅ RFC 9553 §2.5.1.1, RFC 5870 | |
| `ownerId` | `relatedTo` mit `Relation.relation` | ✅ RFC 9553 §2.1.8 | Rollen sind dort Beziehungen zwischen Karten, kein Fremdschlüsselfeld |
| — (fehlt) | `keywords`, `notes`, `anniversaries`, `preferredLanguages`, `languages`, `media`, `links`, `cryptoKeys`, `calendars`, `schedulingAddresses`, `nicknames`, `speakToAs` (Pronomen, grammatisches Geschlecht), `localizations`, `members` | ✅ RFC 9553 §2.1–2.8 | gratis dazu, wenn wir das Modell übernehmen statt es neu zu bauen |
| `lifecycle` | **kein Gegenstück** | ❌ vCard 4.0 kennt so ein Konzept nicht | eine echte Lücke, siehe unten |

### Wie ein belegtes JSContact-Dokument aussieht

Aufbau aus RFC 9553 (§2.2.1, Abbildung 20) — Feldnamen unverändert übernommen:

```json
{
  "@type": "Card",
  "uid": "con_01HZXH7Q3T8V2B4C6D9E0F1A2K",
  "name": {
    "components": [
      { "kind": "surname", "value": "Weber" },
      { "kind": "separator", "value": " " },
      { "kind": "given", "value": "Anna" }
    ],
    "isOrdered": true
  },
  "emails": {
    "e1": { "uri": "mailto:anna@example.org", "contexts": { "work": true } }
  },
  "addresses": {
    "k23": {
      "contexts": { "work": true },
      "components": [
        { "kind": "number", "value": "12" },
        { "kind": "separator", "value": " " },
        { "kind": "name", "value": "Invalid Street" },
        { "kind": "locality", "value": "Berlin" },
        { "kind": "postcode", "value": "10557" },
        { "kind": "country", "value": "Germany" }
      ],
      "countryCode": "DE",
      "defaultSeparator": ", ",
      "isOrdered": true
    }
  }
}
```

Der Unterschied zu unserem heutigen Modell ist nicht nur kosmetisch: **`name` ist ein Objekt mit Teilen und einer `full`-Ansicht.** Deshalb können CRM, Messenger, Kalender und ERP dasselbe Feld lesen und es trotzdem unterschiedlich darstellen.

## Name: der Konflikt, den die Standards selbst haben

Belegt:

| System | Feld für „Anzeigename“ | Beleg |
|--------|--------------------------|----------|
| JSContact | `name` (Objekt mit `full`) | ✅ RFC 9553 §2.2.1 |
| JSCalendar | `title` (String) | ✅ RFC 8984 §4.2.1 |
| AS2 | `name`, mehrsprachige `nameMap` | ✅ W3C AS2 Core §4.1 |
| schema.org | `name` auf `Thing`, Untereigenschaft von `rdfs:label`; dazu `headline` auf `CreativeWork` | ✅ schema.org/Name, schema.org/headline |
| iCalendar | `SUMMARY` | ✅ RFC 5545 (Termin-Kopf) |

Das heißt: **Es gibt keinen einheitlichen Standardnamen.** „Immer `name`“ ist deshalb keine Aussage eines Standards, sondern **unsere eigene Regel** — und genau der Grund, warum wir sie vorab festlegen müssen.

Vorschlag (noch nicht entschieden):

1. Intern heißt das Anzeigefeld überall **`name`** (String, Pflicht, ein Wert pro Sprache über `nameMap`, wo nötig).
2. Strukturierte Namensteile nur für Personen und Organisationen (`nameComponents[]`, angelehnt an JSContact).
3. `title` in JSCalendar/ICS ist ein **Export-Alias**, kein eigenes Datenfeld. In der Datenbank gibt es neben `name` kein `title` und kein `displayName`.
4. Für Dokumente: `name` = Anzeigename der Ressource, `headline` nur, wenn wir für Texte schema.org-Kompatibilität wollen.

## Überschrift im Text → `name` der Ressource

Das ist dein Beispiel (eine Notion-Überschrift, die als Name in der Datenbank landen soll). Belegter Stand: **Kein Standard sagt, dass die erste Überschrift der Name eines Objekts ist.** Was es gibt und als Baustein nutzbar ist:

| Baustein | Was er liefert | Beleg |
|----------------|------------------|----------|
| W3C Web Annotation Model | eine Aussage **über** einen Teil eines Textes, ohne den Text zu ändern: `body` (das Tag/der Wert), `target` (die Stelle), Selektoren `RangeSelector`, `TextQuoteSelector`, `TextPositionSelector`; Motivation `classifying` = „das Ziel als etwas einordnen“ | ✅ |
| AS2 | `name` / `nameMap` als Anzeigename, `id` als **absoluter IRI** (Pflicht nach Core §4.1), `Link` mit `href`/`mediaType` | ✅ |
| schema.org | `name` (allgemein), `headline` (Überschrift eines `CreativeWork`) | ✅ |
| RFC 9073 | `STYLED-DESCRIPTION` (Rich-Text-Beschreibung, `VALUE=TEXT`/`URI`, `FMTTYPE`, `DERIVED`) und `STRUCTURED-DATA` (strukturierte Daten an einem Termin, z. B. `application/ld+json`) | ✅ |
| RFC 8984 | `descriptionContentType`, `localizations` | ✅ |

### Befund aus dem bestehenden Material (prüfbar, heute schon widersprüchlich)

Zwei Stellen in dieser Dokumentation beschreiben Inhalte **unterschiedlich** — und genau dazwischen liegt die Überschriften-Frage:

| Stelle | Was dort steht |
|-------|--------------------|
| `components/workbenches/fields/rich-text-editor/attributes.md` | Attribut `value`, Typ `string`, Beschreibung „value (HTML)“ |
| `data/models.md`, Modell `Block` | `type` mit den Werten `text`, `heading`, `image`, `table`, `code`, `callout`; typabhängige Attribute in `props`; `content` als `array[] \| markdown`; dazu `order`, `align` |

Daraus folgen drei Dinge, die wir aufräumen müssen, bevor „Überschrift → `name`“ funktionieren kann:

1. Es gibt **zwei Inhaltsdarstellungen** (HTML im Editor, Blockarray im Modell) und **kein** dokumentiertes Mapping zwischen beiden. Eine Überschrift ist in einem Fall `<h1>`, im anderen ein Block — welche der beiden Formen in der Datenbank landet, ist offen.
2. Der Block hat **kein Feld für die Überschriftenebene**. `level` (oder `depth`) existiert in `models.md` nicht. Ohne diese Ebene können wir nicht sagen, welche Überschrift die „Hauptüberschrift“ ist.
3. Für strukturierten Blockinhalt habe ich **keinen Standard** gefunden. Gängige Formen wie ProseMirror/TipTap-JSON oder das Markdown-AST sind de-facto-Formate fremder Implementierungen, von mir hier **nicht geprüft** ⚠️. Markdown mit Frontmatter in `formats.md` ist unsere eigene Konvention, kein Standard.

Was wir selbst entscheiden müssten, ist **eine einzige Regel** — zum Beispiel:
*„Ein Block mit `type: heading` und `level: 1`, der als erster Block eines Dokuments steht, schreibt seinen Text in den `name` des Dokuments; die Zuordnung wird als Annotation mit Motivation `classifying` gespeichert.“* Das wäre ein Kandidat für unsere eigene Spezifikation, weil genau diese Regel nirgends existiert.

Offene Punkte, bevor wir das entscheiden:

1. Was passiert, wenn jemand die Überschrift ändert — wird `name` mitgezogen, oder wird `name` danach entkoppelt?
2. Was passiert bei zwei H1-Blöcken?
3. Gilt dieselbe Regel für `Task` (Titel aus dem ersten Block?) und `Event` (`SUMMARY`)?
4. Sollen Tags/Erwähnungen im Text auf dieselbe Weise als Annotationen landen (Motivation `tagging`), damit sie modulübergreifend abfragbar sind?

## Event und Task

Grundlage ist **JSCalendar, RFC 8984** (siehe [standards.md](standards.md)). Unsere Definitionen stehen in [models.md](models.md#event) und [models.md](models.md#task).

| Unser Feld | JSCalendar-Gegenstück | Beleg | Hinweis |
|-----------|------------------------|----------|------|
| `title` | `title` | ✅ §4.2.1 | hier stimmen unsere Modelle und der Standard zufällig überein — bei Personen heißt dasselbe Konzept `name` |
| `start` | `start` | ✅ §5.1.1 | |
| `end` (bei uns Pflicht) | **gibt es nicht** — JSCalendar arbeitet mit `duration` | ✅ §5.1.2 | **echter Konflikt.** Beispiel aus RFC 8984 §6.1: `"start": "2020-01-15T13:00:00"`, `"timeZone": "America/New_York"`, `"duration": "PT1H"` |
| `allDay` | `showWithoutTime` | ✅ §4.2.4 | |
| `timezone` | `timeZone`, `timeZones` | ✅ §4.7.1, §4.7.2 | die Schreibweise unterscheidet sich |
| `locationId` | `locations` (Unterobjekte), `virtualLocations`, `Participant.locationId` | ✅ §4.2.5, §4.2.6, §4.4.6 | JSCalendar kennt mehrere Orte pro Termin, wir nur einen |
| `attendees[]` | `participants` (Map von Teilnehmer-IDs) | ✅ §4.4.6 | |
| `attendees[].response` | `participationStatus` | ✅ §4.4.6 | Werte: `needs-action`, `accepted`, `declined`, `tentative`, `delegated`. **Unser `needsAction` verletzt unsere eigene Enum-Regel** (fields.md: Kleinbuchstaben, `_`) → intern `needs_action` |
| — (fehlt bei uns) | `roles` — **Pflicht**, mindestens einer: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact` | ✅ §4.4.6 | unser Teilnehmermodell kann nicht unterscheiden: eingeladen, nur informiert, verantwortlich, Raum |
| — (fehlt bei uns) | `kind` des Teilnehmers: `individual`, `group`, `location`, `resource` | ✅ §4.4.6 | Räume und Geräte sind Teilnehmer — wichtig für Raumbuchung |
| — (fehlt bei uns) | `sendTo` (`imip`, `other`), `expectReply`, `scheduleAgent` (`server`, `client`, `none`), `participationComment` | ✅ §4.4.6 | Einladungen ohne zusätzliche Tabelle möglich |
| `recurrenceRule` (RRULE-String) | `recurrenceRules` — **Objekte**, keine Strings | ✅ §4.3.3 | RecurrenceRule: `@type`, `frequency` (`yearly`, `monthly`, `weekly`, `daily`, `hourly`, …), `interval`, `rscale`, `skip`, `firstDayOfWeek`, `byDay`, `byMonthDay`, `byMonth`, `byYearDay`, `byWeekNo`, `byHour`, `byMinute`, `bySecond`, `bySetPosition`, `count`, `until` |
| — (fehlt bei uns) | `excludedRecurrenceRules` §4.3.4, `recurrenceOverrides` §4.3.5, `excluded` §4.3.6, `recurrenceId` §4.3.1, `recurrenceIdTimeZone` §4.3.2 | ✅ | **Ausnahmen in Terminserien**, die unser Modell heute nicht abbilden kann — der häufigste Kalenderfehler |
| `status` | `status` (Event) | ⚠️ §5.1.3 | Eigenschaft belegt, **Werteliste nicht gelesen** — unsere Werte nicht als Standard ausgeben |
| `reminders` | `alerts`, `useDefaultAlerts` | ✅ §4.5.2, §4.5.1 | Hintergrund: RFC 9074 erweitert VALARM |
| `calendarId` (bei uns Pflicht) | **kein Gegenstück** in RFC 8984 | ❌ belegt | `calendarIds` kommt in RFC 8984 **nicht** vor. Die Kalenderzugehörigkeit liegt eine Ebene höher — welche Spezifikation das regelt, habe ich **nicht geprüft** ⚠️ |
| `priority` (`low`/`normal`/`high`/`urgent`) | `priority` | ⚠️ §4.4.1 | die Eigenschaft existiert, **Wertebereich nicht gelesen** |
| Task `dueAt` | `due` | ✅ §5.2.1 | |
| Task `estimate` | `estimatedDuration` | ✅ §5.2.3 | |
| Task `progress` (0–100) | `percentComplete` §5.2.4 **und** `progress` §5.2.5 | ⚠️ | JSCalendar hat beides. Der Wertebereich von `progress` ist für mich nicht belegt — **0–100 ist unsere Entscheidung, kein Standard** |
| Task `assigneeIds`, `boardId`, `order` | **kein Gegenstück** | ❌ | das ist die Lücke „Projektstruktur“ aus [standards.md](standards.md) |

### Belegtes JSCalendar-Dokument (Teilnehmer und Serien)

Feldnamen und Enum-Werte aus RFC 8984 §4.2–4.5 übernommen:

```json
{
  "@type": "Event",
  "uid": "evt_01HZXF2M3N4P5Q6R7S8T9U0V1W",
  "updated": "2026-10-30T18:22:10Z",
  "title": "Team-Sync",
  "start": "2026-11-05T10:00:00",
  "timeZone": "Europe/Berlin",
  "duration": "PT1H",
  "recurrenceRules": [
    { "@type": "RecurrenceRule", "frequency": "weekly", "byDay": ["WE"] }
  ],
  "participants": {
    "p1": {
      "@type": "Participant",
      "name": "Anna Weber",
      "email": "anna@example.org",
      "kind": "individual",
      "roles": { "attendee": true },
      "participationStatus": "accepted"
    },
    "p2": {
      "@type": "Participant",
      "name": "Raum 3.12",
      "kind": "location",
      "roles": { "attendee": true },
      "participationStatus": "accepted"
    }
  }
}
```

Nebenbefund: Für das Wiederholungsmuster verweist JSCalendar auf den Werttyp RECUR aus RFC 5545 **und RFC 7529** („Non-Gregorian Recurrence Rules …“, im JSCalendar-Feld `rscale`). Wenn wir RRULE nur als String speichern, verlieren wir diese Verbindung.

## Fremde Systeme, noch nicht geprüft

Diese habe ich **nicht** belegt, deshalb behaupte ich nichts über ihre Feldnamen:

| System | Stand |
|--------|--------|
| Mastodon (REST API, Kontofelder) | ⚠️ nicht geprüft. Belegt ist nur: Mastodon führt `Hashtag` als Untertyp von AS2 `Link` ein und verweist auf `activitystreams#Hashtag` |
| Kanidm (Attributnamen) | ⚠️ nicht geprüft |
| MS Project, W6C, MSPDI | ⚠️ nicht geprüft |
| EN 16931, CII, XRechnung, Peppol, GS1, ISO 4217 | ⚠️ nicht geprüft |
| LDAP/`inetOrgPerson` | ⚠️ nicht geprüft |

Diese Zeilen müssen einzeln belegt werden, **bevor** wir Feldnamen auf sie abbilden. Sonst bauen wir auf Gerüchten auf.

## Siehe auch

- [Daten-Standards](standards.md)
- [Datenmodelle](models.md)
- [Standardfelder](fields.md)
- [Datenformate](formats.md)
- [Konventionen](conventions.md)
