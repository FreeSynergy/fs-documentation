# Time Picker

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

Der Time Picker wählt eine Uhrzeit aus einer Liste möglicher Zeiten. Er folgt dem
Raster des Programms (Standard: Schritte von 15 Minuten) und verhindert ungeeignete Zeiten.

## Verwendungszweck

- Beginn und Ende eines Termins
- Fälligkeiten von Aufgaben
- Zeitraster in der Ressourcenplanung und bei der Raumbuchung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **liste** | Liste der Uhrzeiten, Standard |
| **ziffernblatt** | Zeiger für Stunde und Minute, für Touch |

## Funktionen

- Raster aus `step` (5, 10, 15, 30 Minuten)
- Freie Eingabe mit Korrektur auf das Raster
- Belegte Uhrzeiten aus dem Kontext ausblenden
- 12- oder 24-Stunden-Anzeige je nach Sprache

## Abgrenzung

- **Nicht verwechseln mit** [date-input](../../../primitives/fields/date-input/) mit `type = "time"`:
  dort tippst du, hier wählst du aus.
- **Nicht verwechseln mit** [range-calendar](../range-calendar/): dieser wählt Tage,
  keine Uhrzeiten.

## Best Practices

- Passe die Schrittweite an den Anwendungsfall an: Termin 15 Minuten, Zeiterfassung 6 Minuten.
- Zeig immer beide Richtungen (Anfang und Ende) und zieh das Ende automatisch mit.

## Siehe auch

- [Date Picker](../date-picker/)
- [Date Input](../../../primitives/fields/date-input/)
- [Basiskomponente](../../../primitives/basics/base.md)
