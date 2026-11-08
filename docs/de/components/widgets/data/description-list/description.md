# Description List

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

Eine Description List zeigt Paare aus Label und Wert — die Detailansicht eines
Datensatzes. Sie ist auf das Lesen optimiert, nicht auf das Bearbeiten.

## Verwendungszweck

- Detailansicht eines Kontakts, eines Termins oder einer Aufgabe
- Metadaten unter einem Dokument oder Bild
- Vergleichende Blöcke in Übersichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zweispaltig** | Label links, Wert rechts (Desktop) |
| **gestapelt** | Label über dem Wert (schmale Fläche) |
| **inline** | Paare im Textfluss, getrennt durch Trennzeichen |

## Funktionen

- Werte können eigene Bausteine enthalten: [avatar](../avatar/),
  [badge](../../../primitives/feedback/badge/), [link](../../../primitives/basics/link/), [tag](../../../primitives/fields/tags-input/)
- Fehlende Werte bleiben als Platzhalter sichtbar oder werden ausgeblendet
- Gruppen mit Zwischenüberschriften für lange Detailansichten
- Kopieren eines Werts über ein Symbol pro Zeile

## Abgrenzung

- **Nicht verwechseln mit** [table](../table/): eine Tabelle vergleicht viele Datensätze
  anhand der gleichen Felder, die Description List zeigt ein Objekt.
- **Nicht verwechseln mit** [field](../../../primitives/fields/field/): Felder bearbeiten Werte,
  diese Liste stellt sie dar.

## Best Practices

- Ordne nach Lesbarkeit, nicht nach Datenbankspalten.
- Blende leere Werte aus, außer sie haben eine Bedeutung („kein Fälligkeitsdatum“).
- Höchstens zwei Spalten; mehr wird unübersichtlich.

## Siehe auch

- [Table](../table/)
- [Field](../../../primitives/fields/field/)
- [Basiskomponente](../../../primitives/basics/base.md)
