# Tree View (Baumansicht)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `Simple`, `With Icons`, `With Checkboxes`, `Draggable` |
| **Zustände** | `checked`, `halbausgewählt`, `geöffnet` |
| **Gesten** | `tap`, `double-tap`, `drag`, `long-press` |
| **Animationen** | `expand`, `collapse`, `reorder` |
| **Verwandt** | `list-view`, `table`, `menu`, `table-of-contents`, `sidebar` |
| **Status** | dokumentiert |

## Beschreibung
Ein Tree View ist eine hierarchische Verzeichnisstruktur mit Ein-/Ausklappen.

## Verwendungszweck

- Dateiverzeichnis
- Kategorien
- Organigramm

## Features

- Expand/Collapse
- Checkbox Selection
- Drag-and-Drop
- Search

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Namen mit Einklapp-Dreieck |
| **icon** | Symbol nach Objekttyp (Ordner, Datei, Kategorie) |
| **kästchen** | Mehrfachauswahl, Elternknoten halbiert bei Teilauswahl |
| **verschiebbar** | Knoten per Ziehen umhängen |

## Abgrenzung

- **Nicht verwechseln mit** [menu](../../navigation/menu/): ein Menü ruft Aktionen auf,
  dieser Baum zeigt eine Datenstruktur.
- **Nicht verwechseln mit** [table](../table/) in der Variante `baum`: dort gehören Spalten und
  Vergleichswerte dazu, hier nur die Hierarchie.
- **Nicht verwechseln mit** [list-view](../list-view/): die Liste ist flach.
- **Nicht verwechseln mit** [table-of-contents](../table-of-contents/): das Verzeichnis springt
  innerhalb eines Textes.

## Best Practices

- Pfeil zum Auf-/Zuklappen, Klick auf den Namen zum Auswählen – nicht beides am selben Ort.
- Elternkästchen zeigt den gemischten Zustand, nie einfach nur angehakt.
- Suche klappt den Pfad zum Treffer automatisch auf und markiert den Treffer.
- Verschieben zeigt das Ziel deutlich an und lässt sich rückgängig machen.
- Mehr als fünf Ebenen brauchen Einzugslinien, sonst ist die Struktur nicht mehr erkennbar.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — flache Daten
- [Menu](../../navigation/menu/) — Aktionen statt Struktur
- [Basiskomponente](../../basics/base/)
