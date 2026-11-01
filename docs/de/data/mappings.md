# Feld-Mappings

Diese Datei bildet **unsere bestehenden Felder** auf belegte Standards ab. Sie ist die Stelle, an der Konflikte sichtbar werden, bevor Code existiert.

Regel: Ein Eintrag gilt nur, wenn er eine Quelle hat. Wie in [standards.md](standards.md): ✅ belegt (am 2026-10-31 bei RFC Editor / w3.org / schema.org abgerufen), ⚠️ ungeprüft, ❌ negativ belegt.

Alle Beispiele hier sind **wörtlich den Spezifikationen entnommen oder aus ihren Feldnamen zusammengesetzt** — keine erfundenen Felder.

## Contact

Unsere Definition steht in [modelle.md](modelle.md#contact). Das ist der Abgleich:

| Unser Feld | Belegtes Gegenstück | Quelle | Anmerkung |
|-----------|---------------------|--------|-----------|
| `id` | `uid` (Pflicht bei JSContact), vCard `UID` | ✅ RFC 9553 §2.1.9, RFC 6350 | Unsere ID ist eine interne ULID. Für AS2 reicht das nicht (siehe unten) |
| `firstName` + `lastName` | `name.components[]` mit `kind`: `given`, `given2`, `surname`, `surname2`, `title`, `credential`, `generation`, `separator` | ✅ RFC 9553 §2.2.1.2 | **Zwei-felder-Modell ist zu arm.** JSContact deckt damit Mittelname, zweiter Familienname (spanisch), EhrenTitel, Generationszusatz ab |
| — (fehlt) | `name.full` | ✅ RFC 9553 §2.2.1.1 | das ist genau das, was Du als einen `name` willst |
| `displayName` | `name.full` bzw. `name` | ✅ RFC 9553, schema.org `name` | bei uns nur 🔁 abgeleitet — das passt, ableiten statt speichern |
| `emails[] {type, value}` | `emails` → `Resource` mit `uri`, `contexts`, `pref`, `label`, `mediaType`, `kind` | ✅ RFC 9553 §1.4.4, §2.3.1 | `type` heißt dort `contexts`; die COMMON-Werte sind `private` und `work` |
| `phones[] {type, value}` | `phones` → `Resource` | ✅ RFC 9553 §2.3.3 | vCard-Seite: `TEL` mit `TYPE`-Parametern |
| — (fehlt) | `onlineServices` | ✅ RFC 9553 §2.3.2 | für `handle` (`@anna:matrix.org`) der richtige Platz; vCard heißt das `IMPP` |
| `organization` | `organizations{}` mit `name`, `units[]` (`OrgUnit.name`), `sortAs`, `contexts` | ✅ RFC 9553 §2.2.3 | mehrwertig und mit Organisationseinheiten — besser als ein String |
| `jobTitle` | `titles` | ✅ RFC 9553 §2.2.5 | vCard-Seite: `TITLE` (Stelle) und `ROLE` (Funktion) sind **zwei verschiedene** Eigenschaften |
| `addresses[]` | `addresses{}` → `Address` mit `components[]` (`kind`: `number`, `name`, `block`, `locality`, `region`, `postcode`, `country`, `district`, `subdistrict`, `room`, `apartment`, `floor`, `building`, `direction`, `landmark`, `postOfficeBox`, `separator`), `countryCode`, `coordinates`, `timeZone`, `full`, `isOrdered`, `defaultSeparator`, `pref`, `contexts` (inkl. `billing`, `delivery`) | ✅ RFC 9553 §2.5.1 | unsere `street`/`houseNumber`/`postalCode`/`city` sind eine **Westeuropäisierung**; die Komponententypen sind der Standard |
| `lat`/`lng` (in Location) | `Address.coordinates` als `geo:`-URI | ✅ RFC 9553 §2.5.1.1, RFC 5870 | |
| `ownerId` | `relatedTo` mit `Relation.relation` | ✅ RFC 9553 §2.1.8 | Rollen sind dort Relationen zwischen Karten, kein Fremdschlüssel-Feld |
| — (fehlt) | `keywords`, `notes`, `anniversaries`, `preferredLanguages`, `languages`, `media`, `links`, `cryptoKeys`, `calendars`, `schedulingAddresses`, `nicknames`, `speakToAs` (Pronomen, grammatisches Geschlecht), `localizations`, `members` | ✅ RFC 9553 §2.1–2.8 | Gratis-Gewinn, wenn wir das Modell übernehmen statt nachzubauen |
| `lifecycle` | **kein Gegenstück** | ❌ vCard 4.0 enthält keinen solchen Begriff | echte Lücke, siehe unten |

### So sieht ein belegtes JSContact-Dokument aus

Struktur aus RFC 9553 (§2.2.1, Abbildung 20) — Feldnamen unverändert übernommen:

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
        { "kind": "name", "value": "Invalidstraße" },
        { "kind": "locality", "value": "Berlin" },
        { "kind": "postcode", "value": "10557" },
        { "kind": "country", "value": "Deutschland" }
      ],
      "countryCode": "DE",
      "defaultSeparator": ", ",
      "isOrdered": true
    }
  }
}
```

Der Unterschied zu unserem jetzigen Modell ist nicht Kosmetik: **`name` ist ein Objekt mit Teilen und einer `full`-Ansicht**, deshalb kann CRM, Messenger, Kalender und ERP dasselbe Feld lesen und trotzdem unterschiedlich rendern.

## Name: der Konflikt, den die Standards selbst haben

Belegt:

| System | Feld für „Anzeigename" | Beleg |
|--------|------------------------|-------|
| JSContact | `name` (Objekt mit `full`) | ✅ RFC 9553 §2.2.1 |
| JSCalendar | `title` (String) | ✅ RFC 8984 §4.2.1 |
| AS2 | `name`, mehrsprachig `nameMap` | ✅ W3C AS2 Core §4.1 |
| schema.org | `name` auf `Thing`, Unterproperty von `rdfs:label`; zusätzlich `headline` auf `CreativeWork` | ✅ schema.org/Name, schema.org/headline |
| iCalendar | `SUMMARY` | ✅ RFC 5545 (Termin-Kopf) |

Das heißt: **Es gibt keinen einzigen Standard-Namen.** „Immer `name`" ist deshalb keine Standard-Aussage, sondern eine **eigene Regel von uns** — und genau deshalb müssen wir sie vorher festschreiben.

Vorschlag (noch nicht entschieden):

1. Intern heißt das Anzeigefeld überall **`name`** (String, Pflicht, ein Wert pro Sprache über `nameMap` falls benötigt).
2. Strukturierte Namens**teile** nur bei Personen/Organisationen (`nameComponents[]` nach JSContact).
3. `title` in JSCalendar/ICS ist ein **Export-Alias**, kein eigenes Datenfeld. In der Datenbank gibt es kein `title` und kein `displayName` neben `name`.
4. Bei Dokumenten: `name` = Anzeigename der Ressource, `headline` nur, wenn wir schema.org-Kompatibilität für Texte wollen.

## Überschrift im Text → `name` der Ressource

Das ist Dein Beispiel (Notion-Überschrift, die als Name in die Datenbank soll). Belegter Stand: **kein Standard sagt, dass die erste Überschrift der Name eines Objekts ist.** Was existiert und dafür bausteintauglich ist:

| Baustein | Was es liefert | Beleg |
|----------|----------------|-------|
| W3C Web Annotation Model | eine Aussage **über** einen Textteil, ohne den Text zu verändern: `body` (der Tag/Wert), `target` (die Stelle), Selektoren `RangeSelector`, `TextQuoteSelector`, `TextPositionSelector`; Motiv `classifying` = „das Target als etwas klassifizieren" | ✅ |
| AS2 | `name` / `nameMap` als Anzeigename, `id` als **absoluter IRI** (Pflicht laut Core §4.1), `Link` mit `href`/`mediaType` | ✅ |
| schema.org | `name` (allgemein), `headline` (Schlagzeile eines `CreativeWork`) | ✅ |
| RFC 9073 | `STYLED-DESCRIPTION` (Rich-Text-Beschreibung, `VALUE=TEXT`/`URI`, `FMTTYPE`, `DERIVED`) und `STRUCTURED-DATA` (strukturierte Daten an einem Termin, z. B. `application/ld+json`) | ✅ |
| RFC 8984 | `descriptionContentType`, `localizations` | ✅ |

### Befund aus dem Bestand (überprüfbar, heute schon widersprüchlich)

Zwei Stellen in dieser Dokumentation beschreiben Inhalt bereits **verschieden** — und genau dazwischen liegt die Überschriften-Frage:

| Fundstelle | Was dort steht |
|------------|----------------|
| `components/inputs/rich-text-editor/attributes.md` | Attribut `value`, Typ `string`, Beschreibung „Wert (HTML)" |
| `data/modelle.md`, Modell `Block` | `type` mit Werten `text`, `heading`, `image`, `table`, `code`, `callout`; typabhängige Attribute in `props`; `content` als `array[] \| markdown`; weiter `order`, `align` |

Drei Folgen, die wir bereinigen müssen, bevor „Überschrift → `name`" funktionieren kann:

1. Es gibt **zwei Inhaltsrepräsentationen** (HTML im Editor, Block-Array im Modell) und **keine** dokumentierte Abbildung zwischen beiden. Eine Überschrift ist im einen Fall `<h1>`, im anderen ein Block — welche davon in der Datenbank steht, ist offen.
2. Der Block hat **kein Feld für die Überschriftenstufe**. `level` (oder `depth`) existiert in `modelle.md` nicht. Ohne diese Stufe können wir nicht sagen, welche Überschrift die „Hauptüberschrift" ist.
3. Für strukturierten Block-Inhalt habe ich **keinen** Standard gefunden. Verbreitete Formen wie ProseMirror-/TipTap-JSON oder Markdown-AST sind De-facto-Formate von fremden Implementierungen, von mir hier **nicht geprüft** ⚠️. Markdown + Frontmatter in `formate.md` ist eine eigene Konvention, kein Standard.

Was wir also selbst festlegen müssten, ist **eine einzige Regel** — zum Beispiel: *„Ein Block mit `type: heading` und `level: 1`, der als erster Block eines Dokuments steht, schreibt seinen Text in `name` des Dokuments; die Zuordnung wird als Annotation mit Motiv `classifying` gespeichert."* Das wäre ein Kandidat für eine eigene Spezifikation, weil es genau diese Regel nirgends gibt.

Offene Punkte dazu, bevor wir das entscheiden:

1. Was passiert, wenn jemand die Überschrift editiert — wird `name` nachgezogen, oder ist `name` danach entkoppelt?
2. Was passiert bei zwei H1-Blöcken?
3. Gilt dieselbe Regel für `Task` (Titel aus erstem Block?) und `Event` (`SUMMARY`)?
4. Sollen Tags/Mentions im Text auf dieselbe Weise als Annotationen landen (Motiv `tagging`), damit sie modulübergreifend abfragbar sind?

## Event und Task

Grundlage ist **JSCalendar, RFC 8984** (siehe [standards.md](standards.md)). Unsere Definitionen stehen in [modelle.md](modelle.md#event) und [modelle.md](modelle.md#task).

| Unser Feld | JSCalendar-Gegenstück | Beleg | Anmerkung |
|-----------|----------------------|-------|-----------|
| `title` | `title` | ✅ §4.2.1 | hier stimmen unsere Modelle und der Standard zufällig überein — bei Personen heißt dasselbe Konzept aber `name` |
| `start` | `start` | ✅ §5.1.1 | |
| `end` (bei uns Pflicht) | **gibt es nicht** — JSCalendar rechnet mit `duration` | ✅ §5.1.2 | **echter Konflikt.** Beispiel aus RFC 8984 §6.1: `"start": "2020-01-15T13:00:00"`, `"timeZone": "America/New_York"`, `"duration": "PT1H"` |
| `allDay` | `showWithoutTime` | ✅ §4.2.4 | |
| `timezone` | `timeZone`, `timeZones` | ✅ §4.7.1, §4.7.2 | Groß-/Kleinschreibung unterscheidet sich |
| `locationId` | `locations` (Unterobjekte), `virtualLocations`, `Participant.locationId` | ✅ §4.2.5, §4.2.6, §4.4.6 | JSCalendar kennt mehrere Orte pro Termin, wir nur einen |
| `attendees[]` | `participants` (Karte von Teilnehmer-IDs) | ✅ §4.4.6 | |
| `attendees[].response` | `participationStatus` | ✅ §4.4.6 | Werte: `needs-action`, `accepted`, `declined`, `tentative`, `delegated`. **Unser `needsAction` verstößt gegen unsere eigene Enum-Regel** (felder.md: lowercase, `_`) → intern `needs_action` |
| — (fehlt bei uns) | `roles` — **Pflicht**, mindestens eine: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact` | ✅ §4.4.6 | unser Teilnehmer-Modell kann nicht unterscheiden: eingeladen, nur informiert, Verantwortlicher, Raum |
| — (fehlt bei uns) | `kind` des Teilnehmers: `individual`, `group`, `location`, `resource` | ✅ §4.4.6 | Räume und Beamte sind Teilnehmer — wichtig für Raumbuchung |
| — (fehlt bei uns) | `sendTo` (`imip`, `other`), `expectReply`, `scheduleAgent` (`server`, `client`, `none`), `participationComment` | ✅ §4.4.6 | invitationsfähig ohne Extratabelle |
| `recurrenceRule` (RRULE-String) | `recurrenceRules` — **Objekte**, keine Strings | ✅ §4.3.3 | RecurrenceRule: `@type`, `frequency` (`yearly`, `monthly`, `weekly`, `daily`, `hourly`, …), `interval`, `rscale`, `skip`, `firstDayOfWeek`, `byDay`, `byMonthDay`, `byMonth`, `byYearDay`, `byWeekNo`, `byHour`, `byMinute`, `bySecond`, `bySetPosition`, `count`, `until` |
| — (fehlt bei uns) | `excludedRecurrenceRules` §4.3.4, `recurrenceOverrides` §4.3.5, `excluded` §4.3.6, `recurrenceId` §4.3.1, `recurrenceIdTimeZone` §4.3.2 | ✅ | **Ausnahmen von Serien** kann unser Modell heute nicht darstellen — häufigster Kalender-Bug |
| `status` | `status` (Event) | ⚠️ §5.1.3 | Eigenschaft belegt, **Werteliste nicht gelesen** — unsere Werte nicht als Standard ausgeben |
| `reminders` | `alerts`, `useDefaultAlerts` | ✅ §4.5.2, §4.5.1 | Hintergrund: RFC 9074 erweitert VALARM |
| `calendarId` (bei uns Pflicht) | **kein Gegenstück** in RFC 8984 | ❌ belegt | `calendarIds` kommt in RFC 8984 **nicht** vor. Die Kalender-Zugehörigkeit liegt eine Ebene darüber — welche Spec das regelt, habe ich **nicht geprüft** ⚠️ |
| `priority` (`low`/`normal`/`high`/`urgent`) | `priority` | ⚠️ §4.4.1 | Eigenschaft existiert, **Wertebereich nicht gelesen** |
| Task `dueAt` | `due` | ✅ §5.2.1 | |
| Task `estimate` | `estimatedDuration` | ✅ §5.2.3 | |
| Task `progress` (0–100) | `percentComplete` §5.2.4 **und** `progress` §5.2.5 | ⚠️ | JSCalendar hat beides. Der Wertebereich von `progress` ist mir nicht belegt — **0–100 ist unsere Festlegung, kein Standard** |
| Task `assigneeIds`, `boardId`, `order` | **kein Gegenstück** | ❌ | das ist die Lücke „Projektstruktur" aus [standards.md](standards.md) |

### Belegtes JSCalendar-Dokument (Teilnehmer und Serie)

Feldnamen und Enum-Werte sind RFC 8984 §4.2–4.5 entnommen:

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

Nebenbefund: JSCalendar verweist beim Wiederholmuster auf den RECUR-Werttyp aus RFC 5545 **und RFC 7529** („Non-Gregorian Recurrence Rules …", im JSCalendar-Feld `rscale`). Wenn wir RRULE nur als String speichern, verlieren wir diesen Anschluss.

## Noch ungeprüfte Fremdsysteme

Die habe ich **nicht** belegt und behaupte deshalb nichts über ihre Feldnamen:

| System | Stand |
|--------|-------|
| Mastodon (REST-API, Account-Felder) | ⚠️ nicht geprüft. Belegt ist nur: Mastodon führt `Hashtag` als Unterart von AS2 `Link` ein und verweist auf `activitystreams#Hashtag` |
| Kanidm (Attributnamen) | ⚠️ nicht geprüft |
| MS Project, W6C, MSPDI | ⚠️ nicht geprüft |
| EN 16931, CII, XRechnung, Peppol, GS1, ISO 4217 | ⚠️ nicht geprüft |
| LDAP/`inetOrgPerson` | ⚠️ nicht geprüft |

Diese Zeilen müssen einzeln belegt werden, **bevor** wir Feldnamen darauf mappen. Sonst bauen wir auf Gerüchten.

## Siehe auch

- [Datenstandards](standards.md)
- [Datenmodelle](modelle.md)
- [Standardfelder](felder.md)
- [Datenformate](formate.md)
- [Konventionen](konventionen.md)
