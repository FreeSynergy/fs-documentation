# Projekte – Technische Erklärung

## Grundsatz: Struktur schmal, Aufgaben wiederverwendet

- **Task-Daten bleiben JSCalendar-Objekte in `calobj`** (Tabelle aus [events/technical.md](../events/technical.md)). Kein zweites Task-Schema.
- Diese Domäne führt **vier eigene, schmale Modelle** ein (eigene Festlegung, zur Diskussion — Spec-Kandidat Nr. 3): `Project`, `Board`, `List`, `Relation`.

## Speicherperspektive

| Tabelle | Payload | Anmerkung |
|---------|---------|-----------|
| `project` | JSON (eigenes Modell) | Referenzen auf Team und `contacts` |
| `board` | JSON | `project_id` (ULID) |
| `list` | JSON | `board_id`, `position` (sortierbarer Zwischenwert, eigene Festlegung) |
| `task_link` | `task_id` (→ `calobj`), `list_id`, `position` | **Zuordnung** eines Tasks zu genau einer Liste (Board-Ansicht) — der Task selbst bleibt kalendarisch unabhängig |
| `relation` | `from_id`, `to_id`, `kind` (Enum) | Beziehungen zwischen Tasks |

## Schlüssel und Fluss

- Extern: `https://<instanz>/projects/<ulid>` (Beschluss 3).
- Verschieben in einem Board = `Update` auf `task_link` (nicht auf dem Task!) — deshalb ist `task.moved` ein Envelope-Ereignis über die Zuordnung, nicht über die Aufgabe (siehe [index.md](index.md), offener Punkt).
- Meilensteine: JSCalendar-`Event` mit `categories: ["milestone"]` (Nutzung ✅ geprüfter Felder; die Konvention selbst ist eigene Festlegung).

## Projektionen

| Ziel | Projektion |
|------|------------|
| Kalender-Ansicht | Meilensteine + Task-`due` aus `calobj` |
| MSPDI-Export (✅ Existenz) | Board/List-Struktur ↔ MSPDI-Task-Baum; ⚠️ Feldmapping muss noch erstellt werden |
| CRM/ERP-Skins | Projekt als Assoziation zu Contacts |

## Offene technische Punkte

- **Positionierung:** Zwischenwerte (z. B. Lexorank-artig) vs. Versionszähler — keine Regel von außen belegt; eigene Festlegung nötig.
- **WBS-Unterstruktur:** ISO 21502 kennt Work-Breakdown als Konzept (Prozess), kein Datenformat; ob wir `parent_id` an Tasks erlauben (KONFLIKT mit JSCalendar-Kanon!) oder nur über `relation` abbilden, ist **zu entscheiden**. Vorschlag: nur `relation` mit `kind: "parent"`, damit JSCalendar-Payload kanonisch bleibt.
