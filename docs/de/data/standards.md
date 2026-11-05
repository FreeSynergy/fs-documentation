# Datenstandards (Stand 2026-10-31)

Diese Datei legt fest, **welcher existierende Standard welchen Datenbereich abdeckt**. Ziel: nichts erfinden, wo es schon etwas gibt; und wenn wir erfinden, dann wissentlich.

**Beleglage:** Jeder Eintrag hat einen Status.

| Status | Bedeutung |
|--------|-----------|
| ✅ belegt | Spezifikation am 2026-10-31 direkt beim RFC Editor bzw. bei w3.org abgerufen, Titel/Nummer/Feldnamen geprüft |
| ⚠️ ungeprüft | mir bekannt, in dieser Runde **nicht** nachgesehen — vor Verwendung belegen |
| ❌ belegt, dass es das nicht gibt | negativ geprüft (Quelle enthält den Begriff nicht / Antwort war 404) |

## Grundentscheidung: drei getrennte Schichten

Konflikte entstehen nicht zwischen Formaten, sondern zwischen **Feldnamen**. Deshalb trennen wir:

| Schicht | Frage | Unsere Regel |
|---------|-------|--------------|
| **Speicher** | Wie sieht ein Datensatz in der Datenbank aus? | existierende JSON-/Textmodelle, feldgenau (JSContact, JSCalendar, GeoJSON, …) |
| **Übertragung** | Wie reden Programme miteinander? | Envelope: AS2/ActivityPub; Cap'n Proto intern (ADR 0021), JSON-LD außen — **beides abgeleitete Projektionen** des kanonischen Standardmodells (Beschluss 4) |
| **Vokabular** | Wie heißen die Felder nach außen? | ein Kanon intern, Mapping-Tabelle pro Zielsystem |

Regel Nr. 1: **Ein Feld, ein Owner.** `name` gehört zur Ressource, nicht zum Modul. Kein Modul bekommt ein `crmContactName`.

## Belegte Standards pro Datenbereich

### Kontakte, Personen, Organisationen

| Standard | Beleg | Abdeckung |
|----------|-------|-----------|
| **vCard Format Specification, RFC 6350** | ✅ | Datenaustausch. Geprüfte Eigenschaftsnamen: `FN`, `N`, `NICKNAME`, `PHOTO`, `BDAY`, `ANNIVERSARY`, `GENDER`, `ADR`, `TEL`, `EMAIL`, `IMPP`, `LANG`, `TZ`, `GEO`, `TITLE`, `ROLE`, `LOGO`, `ORG`, `MEMBER`, `RELATED`, `CATEGORIES`, `NOTE`, `PRODID`, `REV`, `SOUND`, `UID`, `CLIENTPIDMAP`, `URL`, `VERSION`, `KEY`, `FBURL`, `CALADRURI`, `CALURI`, `KIND`, `SOURCE`, `BEGIN`/`END`, `XML` |
| **jCard: The JSON Format for vCard, RFC 7095** | ✅ | JSON-Form von vCard |
| **xCard: vCard XML Representation, RFC 6351** | ✅ | XML-Form (nicht CardDAV — siehe Korrekturliste) |
| **CardDAV, RFC 6352** | ✅ | Zugriff/Sync auf Kontaktordner |
| **JSContact: A JSON Representation of Contact Data, RFC 9553** | ✅ | **der interessanteste Fund**: ein modernes, reines JSON-Kontaktmodell. `Card` mit `@type`, `version`, `uid`, `name`, `nicknames`, `organizations`, `titles`, `emails`, `onlineServices`, `phones`, `preferredLanguages`, `calendars`, `schedulingAddresses`, `addresses`, `cryptoKeys`, `directories`, `links`, `media`, `localizations`, `anniversaries`, `keywords`, `notes`, `personalInfo` |
| **vCard Format Extensions for JSContact, RFC 9554** | ✅ | offizielle Brücke JSContact ↔ vCard, damit ist die Wahl „JSContact als Speicher“ anschlussfähig |

`name` ist bei JSContact **kein String**, sondern ein Objekt `Name` mit `components[]` (`kind` = `title`, `given`, `given2`, `surname`, `surname2`, `credential`, `generation`, `separator`), plus `full`, `isOrdered`, `defaultSeparator`, `sortAs`, `phonetic`. Das ist deutlich besser als `firstName`/`lastName` — es deckt chinesische, spanische und isländische Namen ab, ohne dass wir ein Feld erfinden müssen.

**`lifecycle` (lead/prospect/customer/churned) aus unserem CRM existiert in vCard 4.0 nicht** (❌ belegt: Begriff kommt in RFC 6350 nirgends vor). Das ist eine echte Lücke — siehe „Was wir erfinden müssen“.

### Kalender, Termine, Teilnehmer, Aufgaben

| Standard | Beleg | Abdeckung |
|----------|-------|-----------|
| **iCalendar, RFC 5545** | ✅ | Kernformat; `RRULE` ist bereits hier enthalten |
| **jCal: The JSON Format for iCalendar, RFC 7265** | ✅ | JSON-Form von iCalendar |
| **JSCalendar: A JSON Representation of Calendar Data, RFC 8984** | ✅ | **zweiter Schlüsselfund**. Objekttypen `Event`, `Task`, `Group`. Geprüfte Eigenschaften: `@type`, `uid`, `relatedTo`, `prodId`, `created`, `updated`, `sequence`, `method`, `title`, `description`, `descriptionContentType`, `showWithoutTime`, `locations`, `virtualLocations`, `links`, `locale`, `keywords`, `categories`, `color`, `recurrenceId`, `recurrenceRules`, `excludedRecurrenceRules`, `recurrenceOverrides`, `excluded`, `priority`, `freeBusyStatus`, `privacy`, `replyTo`, `sentBy`, `participants`, `requestStatus`, `useDefaultAlerts`, `alerts`, `localizations`, `timeZone`, `timeZones`; Event: `start`, `duration`, `status`; Task: `due`, `start`, `estimatedDuration`, `percentComplete`, `progress`, `progressUpdated` |
| **Participant-Modell in RFC 8984** | ✅ | `name`, `email`, `description`, `sendTo` (`imip`, `other`), `kind` (`individual`, `group`, `location`, `resource`), `roles` (Pflicht, mindestens eine: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact`), `locationId`, `language`, `participationStatus` (`needs-action`, `accepted`, `declined`, `tentative`, `delegated`), `participationComment`, `expectReply`, `scheduleAgent`, `scheduleForceSend` |
| **iTIP, RFC 5546** | ✅ | Einladungsprotokoll (Anfrage/Antwort/Zurückziehen) |
| **CalDAV Scheduling Extensions, RFC 6638** | ✅ | Kalender-Serverintegration |
| **Calendar Collection Synchronization (CalDAV SYNC), RFC 6578** | ✅ | Sync-Mechanismus — unser Feld `syncToken` hat damit einen Beleg |
| **Event Publishing Extensions to iCalendar, RFC 9073** | ✅ | neue Eigenschaften `STYLED-DESCRIPTION` (Rich-Text-Beschreibung, `VALUE=TEXT` oder `VALUE=URI`, `FMTTYPE`, `DERIVED`) und `STRUCTURED-DATA` (beliebige strukturierte Daten an einem Termin, z. B. `application/ld+json`) |
| **„VALARM" Extensions for iCalendar, RFC 9074** | ✅ | unsere `reminders` |
| **Parameter Value Encoding in iCalendar and vCard, RFC 6868** | ✅ | Escape-Regeln, die beide Formate gemeinsam haben |

JSCalendar ist für uns spannender als jCal: jCal ist die JSON-Hülle **über der iCalendar-Grammatik** (Eigenschaftslisten mit Parametern), JSCalendar ist ein echtes Objektmodell. Für eine Datenbank wäre JSCalendar die Arbeitsrepräsentation, jCal/iCalendar der Export.

Achtung Namenskonflikt, den **die Standards selbst** haben: JSCalendar benutzt `title` für den Anzeigenamen, JSContact benutzt `name` (als Objekt), schema.org benutzt `name`, AS2 benutzt `name`. Das lässt sich nicht auflösen, indem wir „den einen Standard“ wählen — es lässt sich nur durch eine Regel lösen (siehe `mappings.md`).

### Aktivitäten, Benachrichtigungen, Webhooks

| Standard | Beleg | Abdeckung |
|----------|-------|-----------|
| **Activity Streams 2.0 Core + Vocabulary (W3C Recommendation 2017)** | ✅ (Status korrigiert 2026-11-05) | `@context: "https://www.w3.org/ns/activitystreams"`; `id` ist ein **absoluter IRI** (Core §4.1); relative IRIs sollen nicht verwendet werden (§2.2); Medientyp `application/activity+json` ist in Core §8.1 bei der IANA registriert; Sprach-Varianten über `nameMap`, `contentMap`, `summaryMap`; `Link`-Objekte mit `href`, `mediaType`, `width`, `height` |
| **AS2 enthält den Typ `Hashtag` nicht** | ❌ belegt | in Core und Vocabulary kommt der Begriff nirgends vor. Mastodon definiert `Hashtag` als Unterart von `Link` und verweist dabei auf `activitystreams#Hashtag` — eine Erweiterung, nicht der Kern |
| **schema.org hat keinen Typ `Hashtag`** | ❌ belegt | `schema.org/Hashtag` liefert HTTP 404 |
| **AS2 ist kein RFC** | ❌ belegt | RFC 9332 ist „Dual-Queue Coupled Active Queue Management (AQM) …" — hat nichts mit ActivityStreams zu tun. Wer AS2 zitiert, zitiert den W3C-Report |
| **WebFinger, RFC 7033** | ✅ | Auffinden von Akteuren über `acct:` / E-Mail |
| **W3C Web Annotation Model** | ✅ | Motive u. a. `classifying`, `tagging`, `commenting`, `describing`, `editing`, `bookmarking`; Selektoren `TextQuoteSelector`, `TextPositionSelector`, `RangeSelector`; Struktur `body` / `target`. **Das ist der richtige Standard für „einem Textteil ein Tag geben“, ohne den Text umzuschreiben** |
| **AS2 `Profile` + `describes`** | ✅ 2026-11-05 | „describes another object, usually an actor“ — **Envelope-Typ für Kontakt-Cards** (ADR 0020): eine Karte ist *meine Beschreibung* jemandes, `describes` zeigt auf den Schauspieler/DID dieser Person |
| **AS2 `Relationship` (`subject`, `object`, `relationship`)** | ✅ 2026-11-05 | Envelope für Beglaubigungen und für bestätigte „dieselbe Person“-Verknüpfungen. AS2 selbst hat **keine** „same as“-Eigenschaft (✅ geprüft) |
| **JMAP, RFC 8620 (Grundlage) und RFC 8621 (Mail)** | ✅ | Referenz dafür, wie man JSON-Ressourcen sauber adressiert, patcht und synchronisiert |

### Orte, Dateien, API-Querschnitt

| Standard | Beleg | Abdeckung |
|----------|-------|-----------|
| **The GeoJSON Format, RFC 7946** | ✅ | Geometrien |
| **`geo:`-URI, RFC 5870** | ✅ | wird in JSContact `Address.coordinates` vorgeschrieben |
| **Language Tags, RFC 5646** | ✅ | wird in JSContact/JSCalendar für `language`/`locale` verwendet |
| **Addr-spec, RFC 5322 §3.4.1** | ✅ | JSCalendar `Participant.email` muss diesem Format folgen |
| **Web Linking, RFC 8288** | ✅ | `Link`-Header, Pagination |
| **Problem Details for HTTP APIs, RFC 9457** | ✅ | unser Fehlerblock in `api.md` ist eine Variante davon |
| **JSON Patch, RFC 6902** | ✅ | teilweise Ändern; JSContact und JSCalendar definieren beide ein eigenes Patch-Objekt (`PatchObject` in RFC 9553, Pfade wie `participants/<id>/participationStatus` in RFC 8984) |

### Weitere Quellen, deren Erreichbarkeit geprüft ist (HTTP 200)

| Quelle | Geprüfte URL | Status |
|--------|--------------|--------|
| ODRL License Vocabulary (rechtestrukturierte Aussagen) | `https://www.w3.org/TR/odrl-model/` | ✅ URL geprüft, **Inhalt nicht gelesen** |
| W3C Organization Ontology (Teams, Hierarchie, Rollen) | `https://www.w3.org/TR/vocab-org/`, `https://www.w3.org/ns/org` | ✅ URL geprüft, **Inhalt nicht gelesen** |
| LD Vocabulary: Personal Information (Feldnamen für Personen) | `https://www.w3.org/TR/ldp/` | ✅ URL geprüft, **Inhalt nicht gelesen** |
| JSON-LD 1.1 | `https://www.w3.org/TR/json-ld11/` | ✅ URL geprüft |
| Activity Streams 2.0 Core / Vocabulary | `https://www.w3.org/TR/activitystreams-core/`, `https://www.w3.org/TR/activitystreams-vocabulary/` | ✅ Inhalt gelesen |
| Web Annotation Model | `https://www.w3.org/TR/annotation-model/` | ✅ Inhalt gelesen |

## Namensgebung: was die Standards wirklich sagen

Belegt am 2026-10-31 direkt bei schema.org:

| Begriff | Beleg | Definition |
|---------|-------|-----------|
| `name` | ✅ | `Thing > Property :: name`, Unterproperty von `rdfs:label`; als äquivalent gelistet: `cmns-txt:hasName`, `dct:title`, `og:title` |
| `headline` | ✅ | `Thing > Property :: headline`, „Headline of the article", wird auf `CreativeWork` verwendet |
| `Article` | ✅ | `Thing > CreativeWork > Article` |

Für einen Text/Dokument gilt also bereits heute: **`name` ist der allgemeine Anzeigename, `headline` ist speziell die Schlagzeile eines Werks.** Zwei verschiedene Dinge — das sollten wir beim Überschriften-Thema auseinanderhalten.

## Was wir erfinden müssen (bisherige Bestandsaufnahme)

| Lücke | Stand |
|-------|-------|
| `Contact.lifecycle` (lead/prospect/customer/churned) | ❌ nicht in vCard 4.0; Ersatz bisher nicht gefunden → **echte Lücke** |
| Board/Projektstruktur (Board → Liste → Task → Relationen, WBS) | ⚠️ Kandidaten (W6C XML Schema, MSPDI, PMI WBS) sind **nicht belegt**. Erst nachprüfen, dann entscheiden |
| Whiteboard: Formen, Layer, Z-Reihenfolge als abfragbares Modell | ⚠️ InkML ist als alter W3C-Beitrag gefunden; **kein Nachfolge-Dokument gefunden** — meine frühere Aussage zu einem „Ink Annotation Module" war unbelegt und wird zurückgezogen |
| ERP: Rechnung, Bestellung, Artikel, Beträge | ⚠️ EN 16931 / CII / XRechnung / Peppol / GS1 / ISO 4217 / IBAN **in dieser Runde nicht nachgesehen**. Vor Verwendung einzeln belegen |
| „Überschrift im Text wird zum `name` der Ressource" | ❌ kein Standard gefunden, der das festlegt. Es gibt aber Bausteine: Web Annotation (`classifying`, `RangeSelector`), AS2 `name`/`nameMap`, schema.org `headline`. Die **Regel** müssten wir selbst festlegen |

## Korrekturliste

Fehler aus dem bisherigen Gespräch, damit sie nicht in eine Datei wandern:

| Falsch gesagt | Richtig (belegt) |
|---------------|------------------|
| „jCard = RFC 9073, jCal = RFC 9074" | **jCard = RFC 7095, jCal = RFC 7265**. RFC 9073 = Event Publishing Extensions, RFC 9074 = VALARM Extensions |
| „AS2 = RFC 9332" | AS2 hat **kein** RFC. RFC 9332 = Dual-Queue Coupled AQM |
| „vCard 4.0 (RFC 6350/6351)" implying CardDAV | RFC 6351 = **xCard**. CardDAV = **RFC 6352** |
| „RRULE-Erweiterung RFC 7953" | RFC 7953 = **Calendar Availability**. RRULE ist Teil von RFC 5545 |
| schema.org-Version „16.0" | frei erfundene Zahl. Geprüft: schema.org nennt auf den abgerufenen Seiten „V30.1 \| 2026-09-16" |
| „W3C bringt gerade ein Ink Annotation Module" | unbelegt, zurückgezogen |
| „E-Rechnung: Empfang seit 2025, Ausstellung 2027/2028" | in dieser Runde **nicht nachgesehen** — als Frist nicht verwenden |
| „ActivityPub signiert mit `Authorization: Signature`, Referenz `w3id.org/security/httpsig`" | diese Referenz liefert **HTTP 404**. **Gelöst 2026-11-05:** HTTP Message Signatures **RFC 9421** (Feb 2024, ✅); Objekt-Proofs **FEP-8b32** (Entwurf, Data Integrity `eddsa-jcs-2022`, ✅); Schlüssel als `Multikey` nach **FEP-521a** (final 2025-06-14, ✅). Mastodon prüft RFC 9421 seit 4.5.0 (✅). Details: `temp/research/contacts-identity-standards.md` |

## Beschlüsse (2026-11-01)

| Nr. | Beschluss |
|-----|-----------|
| 1 | **Kanonisches Payload pro Domäne:** Kontakte → JSContact (RFC 9553/9554), Termine und Aufgaben → JSCalendar (RFC 8984, deckt `Event` **und** `Task`), Orte/Adressen → GeoJSON + JSContact `Address` (+ ISO 19160, ✅ URL geprüft), Nachrichten → AS2 `Note`/`Article`, Profil → AS2-`Actor`-Projektion auf JSContact. |
| 2 | **Envelope für jeden Austausch: ActivityStreams 2 + ActivityPub.** Änderungen nach außen sind `Create`/`Update`/`Delete` auf typisierten Objekten; das Domänen-Payload trägt das Objekt als Erweiterung. `to`/`cc`/`bto`/`bcc` sind Offenlegungssteuerung (sie entscheiden, **wo Kopien landen**) — aber **keine Zugriffskontrolle**; Autorisierung wird pro Ressource getrennt durchgesetzt. |
| 3 | **IDs:** intern **UUIDv7, RFC 9562** (zeitlich sortierbarer Standard, ✅; ersetzt ULID am 2026-11-05, ADR 0027) — extern absoluter IRI `https://<instanz>/<domaene>/<uuid>` (AS2 Core §4.1 verlangt absolute IRIs — ✅ belegt). Der IRI ist der auflösbare Handle, das UUIDv7 die stabile Identität (Host-Migration bleibt möglich, dezentraler Betrieb inklusive). |
| 4 | **Quelle der Wahrheit ist das belegte Standardmodell** (JSContact, JSCalendar, …). Cap'n Proto nutzen wir intern (ADR 0021), JSON-LD/AS2 außen — beide als daraus generierte Projektionen. (Korrigiert die frühere Richtung „protobuf als einzige Quelle“.) |
| 5 | **Erweitern statt erfinden:** erst die Extension-Punkte des Standards nutzen (z. B. `extensions` bei JSContact für `lifecycle` — ⚠️ Mechanismus noch belegen), erst wenn es die nicht gibt, eigene Specs entwerfen. |

**Noch offen (bewusst nicht entschieden):**

1. **`name`-Regel:** Ein Pflichtfeld `name` für alles Benennbare, `title`/`headline`/`displayName` nur als Export-Alias?
   *Vorschlag 2026-11-05 (ADR 0030):* die Inhaltsstandards behalten ihr eigenes Feld (`title` in JSCalendar,
   `name.full` in JSContact, Betreff bei Mail); der **AS2-Envelope hat immer `name`**, daraus abgeleitet.
   Nichts wird umbenannt; Programm-übergreifende Ansichten lesen nur den Envelope.
2. **Publikationspfade für eigene Specs:** W3C-Community-Groups (AS2-Verwandtschaft: Social Web Incubator CG) vs. IETF-Datatracker — pro Spec einzeln zu wählen.

Die frühere offene Entscheidung „Reichweite“ ist mit Beschluss 1+4 beantwortet: die Standards gelten **bis in die Datenbank** (Arbeitsrepräsentation), Dateiformate sind Export.

## AS2-Abbildung pro Domäne (ADR 0014, 0020)

Jedes gespeicherte Objekt = **AS2-Envelope** (`id`, `type`, `attributedTo`, `to`/`cc`/`bto`/`bcc`/`audience`,
`published`, `updated`, `context`) + **Domänen-Inhalt** + **Aktivitätsprotokoll** (`Create`, `Update`, …).

| Domäne | Inhaltsstandard | AS2-Envelope-Typ | Stand |
|--------|-----------------|-------------------|-------|
| contacts | JSContact `Card` (RFC 9553) | `Profile` (`describes` → Schauspieler/DID der Person) | ✅ 2026-11-05 |
| identity — eigene Person | DID-Dokument / Controlled Identifier (W3C) | `Person` (Akteur) mit `Multikey` (FEP-521a) | ✅ 2026-11-05 |
| identity — Beglaubigung | VC 2.0 + `eddsa-jcs-2022` (wie RLTP) | `Relationship` | ✅ 2026-11-05 |
| identity — dieselbe Person (Hub-Zuordnung, ADR 0019) | — | `Relationship`, Relation `owl:sameAs` | beschlossen 2026-11-05 (ADR 0029) |
| messages | Chat: MIMI-Inhalt (Entwurf -10); E-Mail: Original-MIME + JMAP-`Email`-Felder; Matrix-Events | `Note` (`context` = Unterhaltung) | ✅ 2026-11-05, siehe [messages/](messages/standards.md) |
| events | **JSCalendar 2.0** (`draft-ietf-calext-jscalendarbis-22`) `Event`/`Task` | `Event`; Protokoll `Invite`/`Accept`/`TentativeAccept`/`Reject` | ✅ 2026-11-05, siehe [events/](events/standards.md) |
| documents | Text: Original + CommonMark/GFM; Blöcke: eigene Spec; Struktur: schema.org `Book`/`Collection`; Annotationen: Web Annotation | `Article`, `Document`, `Collection`/`OrderedCollection`, `Annotation` | ✅ 2026-11-05, siehe [documents/](documents/standards.md) |
| geodata | GeoJSON (JSON-FG 1.0 wo nötig); in Bildern Exif 3.1 + XMP + IPTC 2025.1 | `Place` | ✅ 2026-11-05 |
| projects | JSCalendar 2.0 `Task` + RFC 9253/10051-Semantik; Board: eigene Spec | `Collection` (Board), Task-Envelope; ForgeFed `TicketDependency` | ✅ 2026-11-05 |
| profile | JSContact (Selbst-Card) | `Profile` (`describes` → ich selbst) | ✅ 2026-11-05 |
| login | OIDC / WebAuthn L3 / SCIM; Föderation: OpenID Federation 1.0 (ADR 0035) | `Person`-Akteur, WebFinger | ✅ 2026-11-05 |

## Lücken → eigene Spezifikationen (ADR 0014)

| Lücke | Beleg | Kandidat |
|-------|-------|----------|
| Zusammenführen/Aliasierung zweier Karten derselben Person | ❌ keiner in RFC 9553/9554/9555/9610/9982/10050 (✅ geprüft 2026-11-05) | Hub-Matching-Spec (ADR 0019) |
| `Contact.lifecycle` | ❌ in vCard/JSContact; Mechanismus ✅ (RFC 9553 §1.8.1) | Anbieter-Eigenschaft `freesynergy.net:lifecycle` (ADR 0028), später CRM-Spec |
| Markierung sensibler Daten (DSGVO Art. 9) | ⚠️ W3C DPV-Kandidat, ungeprüft | ADR 0029 |
| Board-/Projektstruktur | ❌ | Spec-Kandidat Nr. 3 |
| Web of Trust | ❌ in Standardisierungsgremien | mit RLTP mitgestalten; Trust-Mark-Profil für OpenID Federation |
| Task-Relationen „blocks"/„duplicates" in JSCalendar | ❌ | Relations-Vokabular (OpenProject-Set als Referenz) |
| Profilfeld → DPV-Kategorietabelle, Einwilligungs-Nachweis | ❌ | ADR 0029 |
| WebFinger-Link-Profil (Akteur, OIDC-Issuer, DID) | ❌ | Discovery-Spec |

## Domänen-Verzeichnisse

Jede Datendomäne hat ein Verzeichnis mit `index.md`, `description.md`, `technical.md`, `standards.md`, `examples.md` (Festlegung 2026-11-02, siehe [requirements.md → §4](requirements.md)); jeder Standard darin zusätzlich ein Unterverzeichnis mit `description.md` + `storage.md` (Schema analog zu Komponenten):

| Domäne | Verzeichnis |
|--------|-------------|
| Kontaktdaten | [contacts/](contacts/index.md) |
| Nachrichten | [messages/](messages/index.md) |
| Termine | [events/](events/index.md) |
| Geodaten | [geodata/](geodata/index.md) |
| Login / Konten | [login/](login/index.md) |
| Identität (Web of Trust) | [identity/](identity/index.md) |
| Profil | [profile/](profile/index.md) |
| Dokumente | [documents/](documents/index.md) |
| Projekte | [projects/](projects/index.md) |

## Nachrecherche 2026-11-02 — Belege stehen vollständig hier, nicht erneut herunterladen

> **Regel (ausdrückliche Anweisung 2026-11-02):** Alles, was hier abgerufen und aufgeschrieben wurde, ist im Dokument vollständig festgehalten. **Es muss nicht erneut aus dem Web geladen werden.** Nachrecherchieren nur, wenn ein Eintrag ausdrücklich mit ⚠️ als ungeprüft markiert ist.

### Login: OIDC, OAuth, WebAuthn (am 2026-11-02 direkt abgerufen)

| Standard | Beleg | Was belegt ist (Zitat/Auszug, damit kein Nachladen nötig ist) |
|----------|-------|---------------------------------------------------------------|
| **OpenID Connect Core 1.0, incorporating errata set 2** | ✅ abgerufen 2026-11-02 bei `openid.net/specs/openid-connect-core-1_0.html` | „OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It enables Clients to verify the identity of the End-User based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User.“ Autoren: Sakimura, Bradley, Jones, de Medeiros, Mortimore; final mit errata set 2, **15.12.2023**. Kernstücke: ID Token, Authorization Code Flow, Token Endpoint, ID-Token-Validierung, Claims über den End-User. → **⚠️ auf ✅ gezogen** |
| **The OAuth 2.0 Authorization Framework, RFC 6749** | ✅ abgerufen 2026-11-02 bei `rfc-editor.org/rfc/rfc6749` | Oktober 2012, Proposed Standard, obsoletes RFC 5849 (OAuth 1.0). Der RFC-Editor vermerkt Aktualisierungen durch **RFC 8252** (Native Apps), **RFC 8996** (Deprecating TLS 1.0/1.1) und **RFC 9700** (Best Current Practices für OAuth-Sicherheit). → **⚠️ auf ✅ gezogen** |
| **Web Authentication: An API for accessing Public Key Credentials – Level 2 (WebAuthn)** | ✅ abgerufen 2026-11-02 bei `w3.org/TR/webauthn-2/` | W3C Recommendation **08.04.2021**. Zitat Abstract: „This specification defines an API enabling the creation and use of strong, attested, scoped, public key-based credentials by web applications, for the purpose of strongly authenticating users.“ Credentials sind pro Relying Party scoped. **Neu in unser Login-Register aufgenommen.** |
| **SCIM, RFC 7643/7644** | ⚠️ **weiterhin ungeprüft** (Abruf am 2026-11-02 zeitlich abgebrochen) | Nicht nachgeladen auf Anweisung. Vor Verwendung belegen. |

### Identität / Web of Trust: Antons Repo gesichtet (abgerufen 2026-11-02, `github.com/real-life-org/web-of-trust`)

Faktenstand (vollständig aufgeschrieben, **nicht erneut herunterladen**):

- Selbstbeschreibung: „A decentralized trust infrastructure for real-life communities. People meet in person, verify each other's identity via QR code, and build reputation through attestations over time. No central server sees your data. Everything is end-to-end encrypted and stored locally.“
- **Grundsatz: Verification ≠ Trust.** Verifikation bestätigt nur „das ist wirklich diese Person“ (persönliches Treffen + QR-Scan). Vertrauen entsteht erst durch **Attestations über die Zeit**. Das deckt exakt unsere vorläufige Regel 1 in [identity/index.md](identity/index.md) (Beglaubigungen sind eigene Objekte).
- **Protokoll: „WoT Spec“ v0.1.0-draft** — kombiniert **W3C Verifiable Credentials**, **DIDComm v2.1**, **Ed25519** und **ECIES**.
- Identitätsschlüssel: **BIP39-Mnemonic** (12 Wörter) → HKDF-Master-Key → **Ed25519** (Signatur) + **X25519** (Key Agreement); DID-Methode **`did:key`** (W3C DIDs).
- Verschlüsselung: AES-256-GCM (CRDT-Updates, Gruppeninhalte), X25519-ECIES asymmetrisch, GroupKeys; Relays sehen nur Chiffretext.
- Architektur: CRDT-basiert (Yjs default, Automerge-Alternative); Dienste `wot-relay` (WebSocket, ACK+Outbox), `wot-vault` (verschlüsseltes Backup), `wot-profiles` (öffentliche Profil-Auffindbarkeit, JWS-signiert); Autorisierung **UCAN-inspiriert**, offline-verifizierbar.
- Generation 2 (dieses Repo, ~2044 Commits am 2026-11-02) hat einen Nachfolger: **Real Life Trust Protocol (RLTP), Gen 3**, in `real-life-org/trust-protocol`. Fixes laufen Richtung Gen 3.
- **Unsere Andockpunkte:** Attestation ↔ AS2-`Relationship`-Objekt; `did:key`/Ed25519 ↔ `publicKey` am Actor; `wot-profiles` ↔ unsere `profile/`-Projektion; RLTP beobachten.
- **Folge für das Register:** W3C **DID Core** und **VC Data Model** sind durch Antons Spec belegt *zitiert*.
- **Nachtrag 2026-11-05 (✅):** DID Core 1.0 = W3C Recommendation 2022-07-19 (DID 1.1 ist Candidate Recommendation, 2026-03-05); **VC Data Model 2.0, Data Integrity 1.0, EdDSA-Cryptosuites, Controlled Identifiers 1.0** = Recommendations 2025-05-15. **RLTP Gen 3** (`real-life-org/trust-protocol`, letzter Commit 2026-11-05, Bibliothek 0.12.0, Editor's Drafts): Ed25519 `did:key` mit **eigenen Kennungen je Beziehung**, Credentials **VC 2.0 + `eddsa-jcs-2022`**, Transport nicht festgelegt (erster Adapter: ToIP TSP über Mediator). Gen 2 (`web-of-trust`) ist weiter in Produktion, nicht archiviert.

### Projekte: Standardsuche 2026-11-02 (Suchergebnisse, Titelbeleg — nicht im Volltext gelesen)

| Kandidat | Beleg | Einordnung |
|----------|-------|------------|
| **ISO 21502:2020 „Project, programme and portfolio management — Guidance on project management“** (ISO/TC 258) | ✅ Existenz belegt (ISO-OBP-Register Nr. 74947, TC-258-Seite) | **Prozess-Leitfaden, kein Datenformat.** Für uns als Vokabular-/Rollenreferenz nützlich, nicht als Speichermodell. |
| **MSPDI — Microsoft Office Project 2007 XML Data Interchange Schema (`mspdi_pj12.xsd`)** | ✅ Existenz belegt (Microsoft-Learn-Doku zu Task-Elementen, Kalendern; Dauern in Zehntelsekunden) | **De-facto-Austauschformat**, kein offener Standardisierungsgremium-Standard. Import/Export-Target-Kandidat. |
| **W6C XML Schema** | ⚠️ weiterhin unbelegt (in der Suche nicht aufgetaucht) | Nicht weiter verwenden, bis belegt. |
| **JSON-Xchange für Boards/Tasks (RFC/W3C)** | ❌ erneut nichts gefunden | Unser **Spec-Kandidat Nr. 3 bleibt bestehen**; Basis bleibt JSCalendar-`Task` (✅). |

**Ergebnis für offene Frage 6.1:** Einen offenen ISO/DIN/RFC/W3C-**Datenstandard** für Projekt-/Board-Strukturen gibt es nicht; ISO 21502 ist Prozessführung, MSPDI ist proprietärer De-facto-Export. → eigene Spec, mit JSCalendar-`Task` als Task-Objekt.

## Siehe auch

- [Datenmodelle](models.md)
- [Standardfelder](fields.md)
- [Datenformate](formats.md)
- [Feld-Mappings](mappings.md)
- [Konventionen](conventions.md)
- [Daten-API](api.md)
