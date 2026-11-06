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

## Folgen
- Der Schnittstellen-Katalog nennt je Thema den Besitzer.
- `fs-calendar-core` gibt sein Task-Modell an `fs-tasks` ab. Offen: Wo liegen die Verträge (`fs-interfaces`, ADR 0045)?
- Doku-Verzeichnisse `programs/apps/contact/` und `data/contacts/` heißen noch wie vorher; Umbenennung folgt.
