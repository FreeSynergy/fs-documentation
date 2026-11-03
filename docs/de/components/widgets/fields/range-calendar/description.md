# Range Calendar (Bereichskalender)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `date-picker` |
| **Varianten** | `zwei-monate`, `ein-monat` |
| **Zustände** | `open`, `selecting` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `slide-in` |
| **Verwandt** | `date-picker`, `calendar-view`, `table` |
| **Rolle** | `dialog` |
| **Status** | dokumentiert |

## Beschreibung

Der Bereichskalender wählt einen zusammenhängenden Zeitraum. Er zeigt zwei Monate
nebeneinander, damit der Beginn im linken und das Ende im rechten Monat liegen kann.

## Verwendungszweck

- Urlaubs- und Abwesenheitszeiträume
- Berichts- und Filterzeiträume („letzte 30 Tage“)
- Buchungszeiträume für Räume und Ressourcen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zwei-monate** | zwei Monate nebeneinander, Standard im Desktop |
| **ein-monat** | ein Monat, Monatswechsel durch Wischen |

## Features

- Auswahl beginnt mit dem ersten Klick, zweiter Klick setzt das Ende
- Vorhersage des Bereichs, solange der Zeiger wandert
- Voreingestellte Bereiche: heute, 7 Tage, 30 Tage, dieses Quartal
- Tageszähler („14 Tage“) unter dem Raster

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../date-picker/) mit `bereich`: dort sitzt die
  Auswahl an einem Feld, der Bereichskalender ist die eigene Fläche in Filterleisten.
- **Nicht verwechseln mit** [calendar-view](../../data/calendar-view/): die Ansicht zeigt
  Termine, dieser wählt einen Zeitraum.

## Best Practices

- Maximale Länge setzen, wenn Auswertungen sonst zu groß werden.
- Den gewählten Zeitraum als Text anzeigen, nicht nur im Kalender.

## Siehe auch

- [Date Picker](../date-picker/)
- [Calendar View](../../data/calendar-view/)
- [Basiskomponente](../../basics/base/)
