# Description List (Beschreibungsliste)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `zweispaltig`, `gestapelt`, `inline` |
| **Zustände** | `empty` |
| **Gesten** | `tap` |
| **Animationen** | `fade-in` |
| **Verwandt** | `table`, `field`, `card` |
| **Rolle** | `list` |
| **Status** | dokumentiert |

## Beschreibung

Eine Beschreibungsliste zeigt Wertpaare aus Bezeichnung und Wert — die Detailansicht
eines Datensatzes. Sie ist lesen optimiert und nicht zum Bearbeiten gedacht.

## Verwendungszweck

- Detailansicht eines Kontakts, eines Termins oder einer Aufgabe
- Metadaten unter einem Dokument oder Bild
- Vergleichende Blöcke in Übersichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zweispaltig** | Bezeichnung links, Wert rechts (Desktop) |
| **gestapelt** | Bezeichnung über dem Wert (schmale Fläche) |
| **inline** | Paare im Textfluss, durch Trennzeichen getrennt |

## Features

- Werte dürfen eigene Bausteine enthalten: [avatar](../avatar/),
  [badge](../../feedback/badge/), [link](../../basics/link/), [tag](../../fields/tags-input/)
- Fehlende Werte bleiben als Platzhalter sichtbar oder werden ausgeblendet
- Gruppen mit Zwischenüberschriften für lange Detailansichten
- Kopieren eines Wertes über ein Icon pro Zeile

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): eine Tabelle vergleicht viele Datensätze
  nach gleichen Feldern, die Beschreibungsliste zeigt ein Objekt.
- **Nicht verwechseln mit** [field](../../fields/field/): Felder bearbeiten Werte,
  diese Liste stellt sie dar.

## Best Practices

- Reihenfolge nach Lesbarkeit, nicht nach Datenbankspalten.
- Leere Werte ausblenden, außer sie sind aussagekräftig („keine Frist“).
- Höchstens zwei Spalten; mehr wird unruhig.

## Siehe auch

- [Table](../table/)
- [Field](../../fields/field/)
- [Basiskomponente](../../basics/base/)
