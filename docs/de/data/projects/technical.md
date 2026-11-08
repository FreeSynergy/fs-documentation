# Projekte – technische Erklärung

## Prinzip: Struktur schmal, Aufgaben wiederverwendet

- **Aufgabendaten bleiben JSCalendar-Objekte in `calobj`** (Tabelle aus [events/technical.md](../events/technical.md)). Kein zweites Aufgabenschema.
- Diese Domäne führt **vier eigene, schmale Modelle** ein (unsere eigene Entscheidung, zur Diskussion offen — Spezifikationskandidat Nr. 3): `Project`, `Board`, `List`, `Relation`.

## Speicher-Sicht

| Tabelle | Nutzlast | Hinweis |
|-------|----------|---------|
| `project` | JSON (eigenes Modell) | Verweise auf das Team und `contacts` |
| `board` | JSON | `project_id` (UUIDv7) |
| `list` | JSON | `board_id`, `position` (sortierbarer Zwischenwert, unsere eigene Entscheidung) |
| `task_link` | `task_id` (→ `calobj`), `list_id`, `position` | **Zuordnung** einer Aufgabe zu genau einer Liste (Board-Ansicht) — die Aufgabe selbst bleibt kalendarisch unabhängig |
| `relation` | `from_id`, `to_id`, `kind` (Enum) | Beziehungen zwischen Aufgaben |

## Schlüssel und Ablauf

- Nach außen: `https://<instance>/projects/<uuid>` (Entscheidung 3).
- Verschieben innerhalb eines Boards = `Update` auf `task_link` (nicht auf der Aufgabe!) — deshalb ist `task.moved` ein Umschlag-Ereignis über die Zuordnung, nicht über die Aufgabe (siehe [index.md](index.md), offener Punkt).
- Meilensteine: JSCalendar-`Event` mit `categories: ["milestone"]` (nutzt ✅ geprüfte Felder; die Konvention selbst ist unsere Entscheidung).

## Projektionen

| Ziel | Projektion |
|--------|------------|
| Kalenderansicht | Meilensteine + Aufgaben-`due` aus `calobj` |
| MSPDI-Export (✅ Existenz) | Board-/Listenstruktur ↔ MSPDI-Aufgabenbaum; ⚠️ Feldzuordnung noch zu erstellen |
| CRM-/ERP-Frontends | Projekt als Zuordnung zu Kontakten |

## Offene technische Punkte

- **Positionierung:** Zwischenwerte (z. B. LexoRank-artig) gegenüber einem Versionszähler — keine externe Regel belegt; braucht eine eigene Entscheidung.
- **PSP-Unterstruktur:** ISO 21502 kennt die Arbeitsaufteilung als Konzept (Prozess), nicht als Datenformat. Ob wir `parent_id` an Aufgaben zulassen (KONFLIKT mit dem JSCalendar-Kanon!) oder sie nur über `relation` abbilden, **ist noch zu entscheiden**. Vorschlag: nur `relation` mit `kind: "parent"`, damit die JSCalendar-Nutzlast kanonisch bleibt.
