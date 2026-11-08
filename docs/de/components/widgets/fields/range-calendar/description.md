# Range Calendar

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

Der Range Calendar wählt einen zusammenhängenden Zeitraum. Er zeigt zwei Monate
nebeneinander, damit der Anfang im linken und das Ende im rechten Monat liegen kann.

## Verwendungszweck

- Urlaubs- und Abwesenheitszeiträume
- Berichts- und Filterzeiträume („letzte 30 Tage“)
- Buchungszeiträume für Räume und Ressourcen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zwei-monate** | zwei Monate nebeneinander, Standard am Desktop |
| **ein-monat** | ein Monat, Monatswechsel per Wischen |

## Funktionen

- Die Auswahl beginnt mit dem ersten Klick, der zweite Klick setzt das Ende
- Vorschau des Zeitraums, während sich der Zeiger bewegt
- Schnellauswahl (`presets`): heute, 7 Tage, 30 Tage, dieses Quartal
- Tageszähler („14 Tage“) unter dem Raster

## Abgrenzung

- **Nicht verwechseln mit** [date-picker](../date-picker/) mit `bereich`: dort sitzt die
  Auswahl an einem Feld, der Range Calendar ist eine eigene Fläche in Filterleisten.
- **Nicht verwechseln mit** [calendar-view](../../data/calendar-view/): die Ansicht zeigt
  Termine, dieser Wähler wählt einen Zeitraum.

## Best Practices

- Setze eine maximale Länge, wenn Auswertungen sonst zu groß würden.
- Zeig den gewählten Zeitraum als Text, nicht nur im Kalender.

## Siehe auch

- [Date Picker](../date-picker/)
- [Calendar View](../../data/calendar-view/)
- [Basiskomponente](../../../primitives/basics/base.md)
