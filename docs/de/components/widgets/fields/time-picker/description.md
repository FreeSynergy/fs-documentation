# Time Picker (Zeitauswahl)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `date-input` |
| **Varianten** | `liste`, `ziffernblatt` |
| **Zustände** | `open` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in` |
| **Verwandt** | `date-picker`, `date-input`, `calendar-view` |
| **Rolle** | `listbox` |
| **Status** | dokumentiert |

## Beschreibung

Die Zeitauswahl wählt eine Uhrzeit aus einer Liste möglicher Zeiten. Sie folgt dem Raster des Programms (Standard: 15-Minuten-Takt) und verhindert
unpassende Zeiten.

## Verwendungszweck

- Beginn und Ende eines Termins
- Fälligkeiten von Aufgaben
- Zeitraster in Ressourcenplanung und Raumbuchung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **liste** | Liste von Zeiten, Standard |
| **ziffernblatt** | Zeiger auf Stunde und Minute, Touch |

## Features

- Raster aus `step` (5, 10, 15, 30 Minuten)
- Freie Eingabe mit Korrektur auf das Raster
- Belegte Zeiten aus dem Kontext ausblenden
- 12- oder 24-Stunden-Darstellung nach Sprache

## Abgrenzung

- **Nicht verwechseln mit** [date-input](../date-input/) mit `type = "time"`:
  dort wird getippt, hier wird ausgewählt.
- **Nicht verwechseln mit** [range-calendar](../range-calendar/): das wählt Tage,
  nicht Uhrzeiten.

## Best Practices

- Schrittweite zum Anwendungsfall passen: Termin 15 Minuten, Zeiterfassung 6 Minuten.
- Immer beide Richtungen anzeigen (Beginn und Ende) und das Ende automatisch nachziehen.

## Siehe auch

- [Date Picker](../date-picker/)
- [Date Input](../date-input/)
- [Basiskomponente](../../basics/base/)
