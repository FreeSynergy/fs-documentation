# Tree View

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
Eine Tree View ist eine hierarchische Verzeichnisstruktur mit Ein- und Ausklappen.

## Verwendungszweck

- Dateiverzeichnisse
- Kategorien
- Organigramme

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Namen mit einem Dreieck zum Ein- und Ausklappen |
| **icon** | Symbol nach Objekttyp (Ordner, Datei, Kategorie) |
| **kästchen** | Mehrfachauswahl, übergeordneter Knoten halb markiert bei Teilauswahl |
| **verschiebbar** | Knoten per Ziehen neu einhängen |

## Funktionen

- Ein- und Ausklappen
- Auswahl per Checkbox
- Drag and Drop
- Suche

## Abgrenzung

- **Nicht verwechseln mit** [menu](../../navigation/menu/): ein Menü löst Aktionen aus,
  dieser Baum zeigt eine Datenstruktur.
- **Nicht verwechseln mit** [table](../table/) in der Variante `baum`: dort gehören Spalten und
  Vergleichswerte dazu, hier nur die Hierarchie.
- **Nicht verwechseln mit** [list-view](../list-view/): die Liste ist flach.
- **Nicht verwechseln mit** [table-of-contents](../table-of-contents/): das Inhaltsverzeichnis springt
  innerhalb eines Textes.

## Best Practices

- Pfeil zum Auf- und Zuklappen, Klick auf den Namen zum Auswählen — nicht beides an derselben Stelle.
- Die Checkbox des übergeordneten Knotens zeigt den gemischten Zustand, nie einfach angehakt.
- Die Suche öffnet den Pfad zum Treffer automatisch und markiert den Treffer.
- Beim Verschieben ist das Ziel klar sichtbar und lässt sich rückgängig machen.
- Mehr als fünf Ebenen brauchen Einrückungslinien, sonst ist die Struktur nicht mehr erkennbar.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — flache Daten
- [Menu](../../navigation/menu/) — Aktionen statt Struktur
- [Basiskomponente](../../../primitives/basics/base.md)
