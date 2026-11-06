# 0050 – Ein Standard, ein Programm, eine Schnittstelle; `fs-contacts` heißt `fs-people`

Status: akzeptiert (2026-11-06) · ergänzt ADR 0014, 0045, 0049 · Abgrenzung der Standards: Vorschlag

## Entscheidung (Nutzer)
1. **Jedes Programm kümmert sich um die Standards, für die es geschaffen wurde. Ein Programm je Standard, damit es einen
   Point of Truth gibt. Jeder Standard hat eine eigene Schnittstelle, über die andere Programme zugreifen. IMMER.**
2. **`Task` steht für sich allein.** `fs-tasks` besitzt ihn. `fs-calendar` besitzt `Event` und bindet Aufgaben nur über die
   Schnittstelle von `fs-tasks` ein, ohne eigenes Task-Modell.
3. **`fs-contacts` heißt jetzt `fs-people`.** (Nutzer: „Ich mag es nicht, aber es umschreibt es wohl am besten.“)
   Repo, Verzeichnis und Crate `fs-people-core` sind umbenannt, die alte URL leitet weiter.

## Vorschlag zur Abgrenzung (offen)
Die Regel braucht eine Antwort auf zwei Fälle:
- **Ein Standard mit mehreren Objekten:** JSCalendar definiert `Event` und `Task`, und die Entscheidung oben teilt ihn auf
  zwei Programme. Also gilt die Regel je **Objektart** eines Standards, nicht je Dokument.
- **Querschnittsstandards:** AS2 ist die Hülle aller Objekte (ADR 0020) und das Aktivitätsprotokoll, kann also nicht
  einem Fachprogramm gehören. Vorschlag: Die Hülle gehört `fs-store`; `Group` gehört `fs-groups`, `Question` `fs-surveys`.
  JSContact kennt auch Gruppen-Karten: Sie gehören zu `fs-people` als Karte, die Mitgliedschaft und Rechte zu `fs-groups`.

## Entscheidung (Opus, 2026-11-06, auf Rückfrage von freesynergy-32; Nutzer kann ändern)
Gemeinsame **Typen** eines Standards dürfen in einer reinen Bibliothek liegen, zum Beispiel `fs-jscalendar` (Zeit, Zone,
Teilnehmer, Wiederholung, ICS). Sie hat keine Daten, keine Speicherung, keine Schnittstelle und ist kein Programm: Der Point
of Truth bleibt beim Besitzer. Sonst stünde Kopieren gegen ADR 0043. Importierte `Task`-Daten leitet `fs-calendar` immer an
`fs-tasks` weiter, in jedem Format.

## Vorschlag: Personen und Rollen (Frage des Nutzers, wartet auf Antwort)
Ein Programm `fs-people`, statt Contacts und People. Der Nutzer denkt an Vererbung: Person als Elternklasse, Kontakt, Kunde, User
als Ableitungen. Vorschlag: gleicher Gedanke, aber als **Person mit mehreren Rollen**, weil dieselbe Person zugleich Kontakt,
Kunde und User sein kann, was Vererbung nicht abbildet. Jede Rolle hat ihren Standard (JSContact, SCIM `User`, Kunde: Lücke).

## Folgen
- Der Schnittstellen-Katalog nennt je Thema den Besitzer.
- `fs-calendar` hat sein Task-Modell an `fs-tasks` abgegeben (erledigt: fs-tasks 0.1.0, fs-calendar 0.2.0). Offen: Wo liegen die Verträge (`fs-interfaces`, ADR 0045)?
- Doku-Verzeichnisse `programs/apps/contact/` und `data/contacts/` heißen noch wie vorher; Umbenennung folgt.
