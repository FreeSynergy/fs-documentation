# List View

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `Simple`, `With Icons`, `With Avatars`, `With Badges`, `With Actions` |
| **Zustände** | `selected`, `leer` |
| **Gesten** | `tap`, `swipe`, `long-press`, `drag` |
| **Animationen** | `stagger`, `collapse`, `reorder` |
| **Verwandt** | `table`, `grid-view`, `tree-view`, `repeater`, `description-list` |
| **Status** | dokumentiert |

## Beschreibung
Eine List View ist eine einfache Listenansicht von Elementen.

## Verwendungszweck

- Listen
- Übersichten
- Kategorien

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Text pro Zeile, optional eine zweite Zeile |
| **icon** | Symbol links, z. B. für den Dateityp |
| **avatar** | Bild links, z. B. für Personen oder Chats |
| **badge** | Status oder Zähler rechts |
| **aktion** | Bedienelemente rechts, bei Hover oder immer sichtbar |

## Features

- Gruppenüberschriften und Trenner
- Mehrfachauswahl mit Zähler
- Nachladen beim Scrollen (Virtualisierung für lange Listen)
- Umbenennen, Verschieben und Umsortieren direkt in der Zeile

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): eine Liste ordnet jede Zeile frei an, eine Tabelle
  vergleicht Werte über Spalten hinweg.
- **Nicht verwechseln mit** [repeater](../repeater/): der Repeater wiederholt eine Vorlage für
  Eingaben, diese Liste zeigt Datensätze.
- **Nicht verwechseln mit** [tree-view](../tree-view/): hierarchische Daten brauchen Ein- und Ausklappen.
- **Nicht verwechseln mit** [description-list](../description-list/): diese beschreibt **ein** Objekt
  in Label-Wert-Paaren, diese zeigt viele Objekte.

## Best Practices

- Zeilen mindestens 44 px hoch; ein Klick auf die Zeile ist die Hauptaktion, weitere Aktionen rechts.
- Eine leere Liste beschriften und anbieten, einen Eintrag anzulegen; nie nur leer lassen.
- Wisch-Aktionen auf dem Smartphone müssen rückgängig zu machen sein.
- Die Auswahl sichtbar zählen und Sammelaktionen (Löschen, Verschieben) erst einblenden, wenn etwas
  ausgewählt ist.

## Siehe auch

- [data – Übersicht](../index.md)
- [Table](../table/) — Vergleich nach Spalten
- [Grid View](../grid-view/) — Karten statt Zeilen
- [Basiskomponente](../../../primitives/basics/base.md)
