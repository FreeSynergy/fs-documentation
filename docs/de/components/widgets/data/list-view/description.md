# List View (Listenansicht)

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
| **einfach** | Text pro Zeile, optional Zweitzeile |
| **icon** | Symbol links, z. B. Dateityp |
| **avatar** | Bild links, z. B. Personen oder Chats |
| **badge** | Status oder Zähler rechts |
| **aktion** | Bedienelemente rechts, sichtbar bei Hover oder immer |

## Features

- Gruppenköpfe und Trenner
- Mehrfachauswahl mit Zähler
- Nachladen beim Scrollen (Virtualisierung lange Listen)
- Umbenennen, Verschieben und Umsortieren direkt in der Zeile

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): eine Liste gestaltet jede Zeile frei, eine Tabelle
  vergleicht Werte über Spalten.
- **Nicht verwechseln mit** [repeater](../repeater/): der Repeater wiederholt ein Template für
  Eingaben, diese Liste zeigt Datensätze.
- **Nicht verwechseln mit** [tree-view](../tree-view/): hierarchische Daten brauchen Einklappung.
- **Nicht verwechseln mit** [description-list](../description-list/): die beschreibt **ein** Objekt
  in Label-Wert-Paaren, diese zeigt viele Objekte.

## Best Practices

- Zeilen mindestens 44 px hoch; der Zeilenklick ist die Hauptaktion, weitere Aktionen rechts.
- Leere Liste beschriften und zum Anlegen anbieten, nie nur leer lassen.
- Wischaktionen auf Mobil rückgängig machen können.
- Auswahl sichtbar zählen und Sammelaktionen (Löschen, Verschieben) erst bei Auswahl einblenden.

## Siehe auch

- [data – Übersicht](../index.md)
- [Table](../table/) — Spaltenvergleich
- [Grid View](../grid-view/) — Karten statt Zeilen
- [Basiskomponente](../../basics/base/)
