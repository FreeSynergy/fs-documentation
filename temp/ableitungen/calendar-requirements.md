# calendar — Pflichtmenge und Kür (abgeleitet, Muster für alle Kategorien)

Abgeleitet am 2026-11-03 aus den **sechs vollständig verifizierten** Kalender-Masken
(`[x]` in `temp/apps-plan.md`): **davical, google-calendar, merkuro, nextcloud-calendar,
outlook-calendar, planner**. Grundlage sind nur deren `features.md` (Belege dort je Datei).
Kategorie eingefroren nach ADR 0006 (6 Masken verifiziert, Schnittmenge steht).

**planner ist der Randfall:** GNOME Planner ist ein Projektplaner mit internen
Arbeitszeitkalendern — kein Kalender-Sync, kein Terminmodell mit Teilnehmern. Er erweitert
die Kür (Ressourcen, Kosten, Gantt), verändert aber die Pflichtmenge nicht.

## a) Pflichtmenge (Schnittmenge — was jedes Kalenderprogramm können muss)

| # | Fähigkeit | davical | google | merkuro | nextcloud | outlook | Begründung der Aufnahme |
|---|-------------|---------|--------|---------|-----------|---------|--------------------------|
| 1 | Kalender anlegen / umbenennen / Farbe / löschen | ✅ | ✅ | ✅ | ✅ (Papierkorb) | ✅ | alle fünf |
| 2 | Termine ansehen: Tag, Woche, Monat, Liste | – (kein UI) | ✅ | ✅ | ✅ | ✅ | alle vier Client-Masken; davical liefert die Daten dafür |
| 3 | Vor / zurück / heute | – | ✅ | ✅ | ✅ | ✅ | wie 2 |
| 4 | Termin anlegen: Titel, Beginn, Ende, ganztägig | ✅ (Client) | ✅ | ✅ | ✅ | ✅ | alle |
| 5 | Zeitzone **je Termin** | ✅ (tz-Service) | ✅ | ✅ | ✅ | ✅ | alle — keine Debatte, Pflicht |
| 6 | Termin bearbeiten (Felder ändern) | ✅ | ✅ | ✅ | ✅ | ✅ | alle |
| 7 | Termin verschieben (Zeit und zwischen Kalendern) | ✅ | ✅ (`events.move`) | ✅ (Drag) | ✅ (Drag) | ✅ | alle |
| 8 | Termin löschen (Serien-Instanz separat) | ✅ | ✅ | ✅ | ✅ | ✅ | alle |
| 9 | Wiederholungsserien mit Ausnahmen | ✅ (RRULE serverseitig) | ✅ | ✅ (RRULE + Exdate) | ✅ | ✅ (`PatternedRecurrence`) | alle |
| 10 | Erinnerung / Alarm pro Termin | ✅ (VALARM) | ✅ | ✅ | ✅ | ✅ | alle |
| 11 | Ort / Raum am Termin | ✅ (Ressourcen) | ✅ | ✅ (Karte optional) | ✅ (Room-Availability) | ✅ (`locations`) | alle |
| 12 | Beschreibung / Notiz am Termin | ✅ | ✅ | ✅ | ✅ | ✅ (Rumpf) | alle |
| 13 | Kategorie / Farbe / Schlagwort | ✅ (ACL-Ordnung) | ✅ | ✅ (Tags) | ✅ (Farbe) | ✅ (`categories`) | alle |
| 14 | Suche über Bestand | ✅ (REPORT) | ✅ (`q`) | 🟡 (nicht verifiziert) | ✅ | ✅ | vier von fünf belegt |
| 15 | Kalender teilen, mit **Rechstufen** | ✅ (RFC 3744 ACL) | ✅ (4 Stufen) | – (Server) | ✅ (Nutzer/Gruppen/Circles) | ✅ (`calendarPermissions`) | alle Server-Masken |
| 16 | Fremden Kalender **abonnieren** | ✅ (`webcal://`, BIND) | ✅ (ICS-Abo) | – | ✅ (WebCal) | – | drei von fünf → Pflicht, weil Abo die Brücke zur Föderation ist |
| 17 | Teilnehmer einladen, RSVP (annehmen/vorläufig/ablehnen) | ✅ (Inbox/Outbox, RFC 6638) | ✅ | ✅ (RSVP anfordern) | ✅ (Buttons im Editor) | ✅ (`accept`/`decline`) | alle |
| 18 | Free/Busy ansehen und veröffentlichen | ✅ (`free-busy-query`) | ✅ | ✅ (Veröffentlichung) | ✅ (Teilnehmer-Belegung) | ✅ (`getSchedule`) | alle |
| 19 | Import / Export (ICS) | ✅ (Skripte) | ✅ | ✅ (Datei/URL) | ✅ (Einstellungen) | 🟡 (Client-Funktion) | vier von fünf |
| 20 | Objekt ist **adressierbar** (Deep Link) | 🟡 (URI je Objekt) | – | ✅ (D-Bus `showIncidenceByUid`) | ✅ (`/object/{uid}`) | – | zwei belegt, aber ohne Adresse kein Sprung aus dem Widget (§14) → **Pflicht aus Architektur** |
| 21 | Aufgaben (VTodo) sichtbar im Kalender | ✅ | 🟡 (separater Dienst) | ✅ | ✅ (Deck/Tasks) | ✅ (To Do separat) | vier von fünf, zwei davon nur Projektion → Pflicht: **sichtbar machen**, eigene Aufgabe ist Kür |
| 22 | Anhang am Termin | – | ✅ | ✅ | ✅ (Files) | ✅ (`attachments`) | vier von fünf |

**Regel aus §9:** eine Maske, die Punkt 1–22 nicht zeigt, ist kaputt, nicht schlank.

## b) Kür (vereinzelt, bewusst nicht Pflicht)

| Fähigkeit | nur in | Warum Kür |
|-----------|--------|-----------|
| Öffentliche Buchungsseite / Terminplanung per Slot | google (kostenlos), nextcloud (Konfigurationen) | outlook ausgelagert (Bookings-App), merkuro/planner nicht vorhanden |
| Terminumfrage / Wahlvorschläge mit Abstimmung | nextcloud (Proposals), google (Erwähnung) | outlook hat nur Gegen-Vorschläge je Teilnehmer |
| Automatische Zeitvorschläge für Gruppen | outlook (`findMeetingTimes`) | stark an Exchange-Postfach gebunden |
| Konferenz-Schaltung im Termin | google (Meet), nextcloud (Talk) | beide binde ihren eigenen Anbieter ein — passt nicht in ein offenes Modell |
| Räume/Ressourcen mit Buchungs-Workflow | outlook, davical (Principal-Typ `ROOM`) | nextcloud setzt serverseitige CalDAV-Ressourcen voraus |
| Vertretung / Delegation (Assistent ↔ Chef) | davical (`calendar-proxy`), nextcloud (`delegation`) | zwei von fünf — mächtig, aber Rechte-Modell fehlt noch (§8 Lücke) |
| Befristete Zugangs-Tickets ohne Login | davical (MKTICKET/DELTICKET, Draft) | nur Entwurf, kein Standard |
| Papierkorb mit Wiederherstellung | nextcloud | angenehm, nicht grundlegend |
| Feiertage nach Region | merkuro | Länderdaten sind eigener Dienst |
| Journal-Einträge (VJOURNAL) | davical, merkuro | zwei von fünf |
| Ressourcen, Kosten, Gantt, Abhängigkeiten | planner | anderes Domänenmodell (Projekt), nicht Kalender |

## c) Daten, die die Pflichtmenge braucht (Input für §10 / `data/`)

| Für Fähigkeit | Felder / Modell | Pate (Standard) |
|---------------|-----------------|------------------|
| Termin-Kern | `title`, `start`, `duration`, `description`, `color`, `categories` | JSCalendar RFC 8984 ✅ |
| Zeitzone je Termin | `timeZone`, `timeZones` | JSCalendar ✅ |
| Ganztägig | `showWithoutTime` | JSCalendar ✅ |
| Serie + Ausnahmen | `recurrenceRules`, `excludedRecurrenceRules`, `recurrenceOverrides` | JSCalendar ✅ |
| Teilnehmer + RSVP | `participants` mit `roles`, `participationStatus` | JSCalendar ✅ |
| Alarm | `alerts`, `useDefaultAlerts` | JSCalendar + RFC 9074 ✅ |
| Ort / Raum | `locations`, `virtualLocations` + `geodata/` | JSCalendar + GeoJSON ✅ |
| Anhang | `links` / `attachments` | JSCalendar ✅, RFC 9073 `STRUCTURED-DATA` ✅ |
| Abo / Fremdkalender | ICS-Import, `sync-collection` | RFC 5545 ✅, RFC 6578 ✅ |
| Adresse des Objekts | `uid` + Instanz-IRI | AS2 Core §4.1 ✅, Beschluss 3 (ULID + IRI) |
| Rechstufen am Kalender | **fehlt** | kein Pate ⚠️ — Kandidat ODRL (§8/§17), Modell-Lücke (§18 Nr. 17) |

**Ergebnis für die Grundmaske:** die Kalender-Datenseite ist fast vollständig gedeckt. Eine
echte Lücke bleibt **Rechstufen beim Teilen** — genau die Lücke, die §8 in `modelle.md`
benennt.

## d) Übertrag auf die anderen Kategorien

Dieses Blatt ist das **Muster**. Pro Kategorie: 3–5 Masken verifizieren, dann dieselben drei
Tabellen (Pflichtmenge, Kür, Daten mit Pate). Danach: erst **Standards** suchen, die die
Pflichtmenge abbilden, dann **Crates**, dann 2 nicht-OSS + 1 OSS zum Nachbauen (ADR 0006).
