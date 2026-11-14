# 0085 – Normalisierung an der Grenze: Zeiten und Personen

Status: **Entwurf** (Strategie, 2026-11-14; Nutzerregeln, noch nicht als ADR bestätigt) · baut auf ADR 0014 (Standards zuerst, AS2), 0019 (Hub, Angleichen), 0020 (Speicherformat), 0046 (Speichern ist nicht Exportieren), 0057 (übersetzbare Texte), 0058 (Kontakte sind Profile), 0072 (Blöcke), 0076 (Grundmodell) · ergänzt den Workflow `programm-neu`

## Kontext
- Programme tauschen Daten mit der Welt: iCalendar-Dateien, vCards, Mails, Matrix-Ereignisse, Tabellen. Jedes Fremdformat hat eigene Zeit- und Namensformen. Würden sie ungeprüft nach innen wandern, rechnete jedes Programm anders.
- Bestandsaufnahme (2026-11-14, gelesen; Liste liegt außerhalb des Repos in `/srv/FreeSynergy/.scratch/bestand-zeiten-personen.md`, kein Umbau beschlossen): Die meisten Felder mit einem Menschen sind schon ein Verweis (`owner`, `creator`, `requester`, `updated_by` als Person-IRI oder Akteur in `resources.capnp`, `surveys.capnp`, `groups.capnp`, `texts.capnp`), aber als blanker `String` ohne eigenen Typ. Freie Namen: `add_invitee(name, email)` im Kalender, der Einladungs-Protokolleintrag und eine Kanban-Zuständigkeit in Arbeitszweigen. Zeiten: Kalender und Tasks rechnen nach JSCalendar (`LocalDateTime` plus `timeZone`); die Aufgabe kann ein reines Datum bisher nicht ausdrücken (`fs-tasks-app/src/source/apply.rs:68`); `fs-types::DateTime` kennt Zonen nicht (`Unsupported`).
- ADR 0014: „Gibt es einen Standard, wird er benutzt“; ADR 0020: Namen und Termine liegen **immer** im Fachstandard (JSContact, JSCalendar). ADR 0058: Kontakte sind Profile; `fs-people` besitzt die Personen. Ein Feld mit dem Namen eines Menschen darf daher nicht selbst einen Namen besitzen.

## Nutzerentscheidung (2026-11-14, sinngemäß; im Entwurf als Regeln festgehalten)
1. Import und Export laufen **immer** als Adapter an der Grenze. Innen gilt nur AS2 mit den Fachstandards. **Rein = normalisieren, raus = für das Ziel umwandeln.**
2. **Zeitpunkte** liegen **immer in UTC**. Wo die lokale Bedeutung zählt (Wiederholungen, „um 9 Uhr Berlin“), steht zusätzlich die **IANA-Zonen-Id**. **Ganztägige Daten und Geburtstage** sind ein **Datum ohne Uhrzeit** und werden nie umgerechnet. Die Ausgabe erfolgt in der Zone des Betrachters.
3. **Jedes Feld mit dem Namen eines Menschen ist ein Verweis** auf People (Personen-Id wie ein Fremdschlüssel; AS2 `actor`/`Person`, JSContact oder vCard), nie ein freier Name. **Ausnahme** Buchungen, Rechnungen, Verträge und Ähnliches: Verweis **plus eingefrorener Abzug** (Name, Anschrift … zum Zeitpunkt).

4. **Entscheidungen der Strategie (Nutzer, 2026-11-14), Antworten auf die Offen-Fragen:**
   - **Schwebende Zeit** (ohne Zone) wird an der Grenze aufgelöst: Der Importer setzt die Zone der Person (Einstellung, sonst Gerät) und markiert `zone_assumed`; der Export gibt sie mit Zone aus. Eine echte „überall 8 Uhr“-Zeit kommt später als eigener, ausdrücklicher Typ (bleibt offen). Zone des Betrachters: Einstellung der Person, sonst Gerät.
   - **Ausnahme Abzug:** alle Dokumente, die nach der Ausstellung rechtlich oder finanziell gelten: Buchung/Reservierung, Bestellung, Rechnung, Quittung/Spendenbescheinigung, Vertrag, Beschluss/Protokoll, Urkunde/Zeugnis. Regel statt Liste: **ausgestellt = eingefroren**.
   - **Ein Typ** `PersonRef { id, abzug: Option<…> }`; der Abzug ist Teil des Typs.
   - **Bestand** wird einzeln in den Programm-Runden behoben, Reihenfolge: zuerst `fs-types` DateTime UTC-normiert plus Zone (Basis), dann Kalender-Einladungen und Kanban-`assignee` auf `PersonRef`, dann Tasks mit ganztägiger Fälligkeit (als bugfix-Einträge in den Welle-1-Listen).

## Vorschlag (Strategie)
### 1. Adapter an der Grenze
- Jeder **Importer** ist ein Adapter (Ports and Adapters, ADR 0043/0066): Fremdformat lesen, in das innere Modell **normalisieren** (Zeiten nach Regel 2, Namen nach Regel 3), erst dann speichern. Jeder **Exporter** wandelt das innere Modell **für das Ziel** (zum Beispiel iCalendar-Zeitangaben, vCard-Namen) und ist ein eigener Befehl, nicht Speichern (ADR 0046).
- Was beim Normalisieren nicht abbildbar ist, geht nicht still verloren: Der Importer hängt das Original an (Rohwert, Quelle) und meldet den Verlust. Beispiel: Die iCalendar-Fassung eines Eintrags bleibt Byte für Byte erhalten (so macht es `fs-jscalendar` heute, laut dessen README).
- Importer und Exporter haben **Tests mit Fremd-Beispieldateien** und einen Rundlauf (rein, raus, vergleichen). Das gehört in den Workflow `programm-neu` (siehe Folgen).

### 2. Zeiten
| Art | Innen gespeichert | Beispiel |
|---|---|---|
| Zeitpunkt (ein Ereignis ist geschehen oder beginnt) | UTC, RFC 3339 mit `Z` (JSCalendar `UTCDateTime`) | Zeitstempel, `created`, Protokoll |
| Termin mit lokaler Bedeutung | lokale Zeit **und** IANA-Zonen-Id (JSCalendar `LocalDateTime` plus `timeZone`); abgeleiteter UTC-Wert zum Sortieren und Abfragen | „jeden Dienstag 9 Uhr, Europe/Berlin“ |
| Ganztägig, Geburtstag, Stichtag ohne Uhrzeit | Datum `JJJJ-MM-TT` (JSCalendar `showWithoutTime` bzw. reines Datum), **keine Zone, keine Umrechnung** | Neujahr, 14.11. |
| „Schwebende“ Zeit (ohne Zone) | wird an der Grenze **aufgelöst**: Importer setzt die Zone der Person (Einstellung, sonst Gerät) und markiert `zone_assumed`; Export gibt sie mit Zone aus | iCalendar-Zeit ohne `TZID` |
- Warum beides: UTC allein verliert, was der Mensch meinte. Ändern sich die Zonenregeln, verschiebt sich „9 Uhr Berlin“ in UTC; die Zonen-Id bewahrt die Absicht. Belegt ist das im Text von RFC 9557: Eine benannte IANA-Zone bedeutet, dass die zum Zeitpunkt der Auslegung **aktuellen** Regeln gelten sollen.
- Die Ausgabe wandelt zur Zone des Betrachters (Einstellung der Person, sonst Gerät). Die Zonen-Regeln liefert die tz-Datenbank; `fs-jscalendar` nimmt schon die neueste gefundene (System oder gebündelt).
- Rechnen bleibt bei den Eigentümern: Wiederholungen rechnet `fs-calendar` in der Zone des Termins (heute so), nicht in UTC.

### 3. Personen
- Ein Feld mit dem Namen eines Menschen hat den Typ **Personen-Verweis** (Personen-Id; in AS2 ein `actor`/`Person`, im Fachstandard JSContact/vCard bei `fs-people`). Ein freier Name ist **kein** erlaubter Feldinhalt.
- **Ausnahme eingefrorener Abzug:** Wo ein Dokument nach der Ausstellung rechtlich oder finanziell gilt (Regel „ausgestellt = eingefroren“; Arten siehe Nutzerentscheidung 4), trägt das Feld den Verweis **und** einen Abzug (Name, Anschrift … wie zum Zeitpunkt). Der Abzug ändert sich nie, auch wenn die Person später umzieht oder den Namen ändert. Wer „aktuell“ will, folgt dem Verweis; wer „damals“ will, liest den Abzug.
- **Gemeinsamer Baustein „Personen-Verweis“** (Muster Strategy: Auswahl und Auflösung hinter einem Trait):
  - **Typ** `PersonRef { id, abzug: Option<…> }` in `fs-interfaces` (ein Basistyp neben `Date`/`DateTime`; Abzug Teil des Typs), damit jedes Programm denselben Typ in seiner Typbeschreibung nennt (ADR 0066: Oberflächen aus der Typbeschreibung).
  - **Auswahlfeld** in `fs-components` (Baustein mit festem Namen, ADR 0074; sucht in People, legt auf Wunsch eine Person an).
  - **Ohne installiertes People:** eine **kleine lokale Ablage im selben Format** (JSContact-Kern: Id, Name, E-Mail), damit der Verweis gültig bleibt. Kein Programm erfindet ein eigenes Namensformat.
  - **Später** gleicht der Hub die lokale Ablage mit People ab (ADR 0019 „Angleichen statt Verschmelzen“); **der Mensch bestätigt** jede Angleichung.
- Importer legen für unbekannte Namen **keinen** freien String an: Sie finden die Person in People (E-Mail, Telefon), schlagen einen Treffer vor (Mensch bestätigt) oder legen sie in der lokalen Ablage an.

## Recherche (Fakten, nur lesend aus den amtlichen Textfassungen, 2026-11-14; nichts übernommen)
Quellen: `https://www.rfc-editor.org/rfc/rfc5545.txt`, `rfc8984.txt`, `rfc9557.txt`, je per GET gelesen, Rohtext außerhalb des Repos.
- **RFC 5545 (iCalendar), §3.3.5:** Es gibt drei Formen für Datum-mit-Uhrzeit: lokale Zeit („floating“), UTC mit `Z` und lokale Zeit mit Zonenverweis über den Parameter `TZID`. Beispiel der Fassung: `TZID=America/New_York:19980119T020000`. Für Termine ohne Uhrzeit gibt es den Werttyp `DATE` (`DTSTART;VALUE=DATE:19971102`).
- **RFC 8984 (JSCalendar):** `UTCDateTime` ist ein RFC-3339-Zeitpunkt mit Versatz `Z` (Abschnitt 1.4.4); `LocalDateTime` hat keine Zone und bekommt sie aus der Eigenschaft `timeZone` des Objekts; fehlt sie, ist die Zeit „floating“ (1.4.5, 4.7.1). `showWithoutTime` (4.2.4) kennzeichnet ganztägige Ereignisse; die Zeit bleibt für Terminkonflikte wichtig, der Kalender darf sie weglassen. Eine Zone ist ein Name der IANA-Zonen-Datenbank oder eine eigene Kennung in `timeZones`.
- **RFC 9557 (Zeitstempel mit Zusatzinformation, erweitert RFC 3339):** erlaubt, an einen Zeitstempel die Zone anzuhängen. Die Fassung unterscheidet **benannte IANA-Zone** (Regeln können sich ändern; gemeint sind die jeweils aktuellen) und **Versatz-Zone** (fester Versatz). Das trägt Entscheidung 2: UTC für den Zeitpunkt, Zonen-Id für die Absicht.
- **JSContact (RFC 9553)** und **vCard**: Personen-Standards, auf die ADR 0020 für Namen verweist; **AS2** kennt `Person`/`actor`. Dieser Entwurf übernimmt davon nur die Zuordnung (Verweis statt Namensfeld), keinen Text.
- **Bestand, belegt aus dem Quelltext:** siehe Kontext. Nicht belegt: ob alle Importer (zum Beispiel iCalendar über `calcard`) heute **jede** Zeit auf UTC/Zonen-Id normieren (nur das README sagt es).

## Folgen
- **Typen:** `fs-interfaces` bekommt den Basistyp `PersonRef` (Abzug Teil des Typs) und erweitert `fs-types::DateTime`/Zeit um UTC-Zeitpunkt, `LocalDateTime` plus Zonen-Id und reines Datum; die heutige Lücke „Zonen sind `Unsupported`“ (`fs-types/src/datetime.rs`) wird geschlossen. Eine Typbeschreibung nennt nur diese Typen für Zeiten und Menschen.
- **Baustein:** `fs-components` bekommt das Auswahlfeld „Personen-Verweis“ mit festem Namen und Stilteilen (ADR 0074); Aufbau wie die Editor-Bausteine (ADR 0084): ein Vertrag, Frontends wählen.
- **Workflow `programm-neu`:** P1 Schritt 5 legt die Formate fest (inklusive Zeit- und Personenregel), ein neuer Schritt 9a in P3 baut Importer und Exporter als Grenz-Adapter mit Tests, P2 Schritt 6 verweist für Zeit- und Personenfelder auf diesen Entwurf. Der Workflow verweist auf einen **Entwurf**; Wortlaut und Zahlen müssen sich ändern, wenn der ADR sich ändert.
- **Bestand:** Die Liste der Stellen mit freien Namen und lokalen Zeiten ist erstellt; Behoben wird einzeln in den Programm-Runden (bugfix-Einträge in `/srv/FreeSynergy/.scratch/plan-dossiers-welle1.md`), Reihenfolge: `fs-types` DateTime UTC plus Zone, dann Kalender-Einladungen und Kanban-`assignee` auf `PersonRef`, dann Tasks ganztägige Fälligkeit.
- **Prüfbar:** Ein Skript kann in Typbeschreibungen Felder mit Namen wie `owner`/`author`/`assignee` vom Typ Text als Verstoß melden; Zeitfelder ohne UTC- oder Zonentyp ebenso (Vorschlag, noch nicht gebaut).

## Alternativen
| Option | Bewertung |
|---|---|
| Nur lokale Zeit speichern | Verworfen: Sortieren, Abfragen und Vergleichen über Zonen hinweg ist falsch oder aufwendig. |
| Nur UTC speichern | Verworfen für Wiederholungen und Termine: „jeden Dienstag 9 Uhr“ verschiebt sich zur Sommerzeit; die Absicht ginge verloren. |
| Ganztägig als 00:00 UTC | Verworfen: In Zonen westlich von UTC fiele das auf den Vortag; ein Geburtstag wäre falsch. |
| Freier Name mit Kopie der Person | Verworfen (Nutzer): Namensänderung kommt nicht an; zwei Wahrheiten. Nur als eingefrorener Abzug zusätzlich zum Verweis, wo das Dokument es verlangt. |
| Jedes Programm normalisiert selbst | Verworfen: Gleiche Fremdformate würden verschieden gelesen; ein Baustein am Rand spart die Kopien. |

## Offen
- Echte „überall 8 Uhr“-Zeit als eigener, ausdrücklicher Typ: später. **[offen]**
- Umgang mit abgelaufenen Zonen-Regeln beim Wiederabgleich gespeicherter Termine nach tz-Updates **[nicht belegt]**.
- Ob die lokale Ablage ohne People denselben Speicher wie `fs-people` nutzt (gleiches Schema, anderes Programm) **[nicht belegt]**.
- Geschlossen am 2026-11-14 (Nutzerentscheidung 4): schwebende Zeit, Typzuschnitt, Abzug-Ausnahme, Zone des Betrachters, Umbau-Reihenfolge.
