# Ripple - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `ripple` | Name der Animation |
| `wellenUrsprung` | string | `click` | `click` (Berührungspunkt) oder `center` |
| `farbe` | string | `onSurface 0.2` | Füllfarbe der Welle mit Deckkraft |
| `radius` | string \| number | `auto` | Zielradius; `auto` = ganze Fläche erreichen |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `450` | Ausbreitungsdauer einer Welle in ms |
| `timingFunction` | string | `ease-out` | Welle wird beim Wachsen langsamer |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `iterationCount` | number | `1` | Eine Welle pro Interaktion |
| `fillMode` | string | `none` | Welle verschwindet vollständig |

## Wellen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `startRadius` | number | `0` | Startradius in px |
| `spreadDuration` | number | `450` | Zeit bis zum Erreichen des Zielradius |
| `fadeAnteil` | number | `0.6` | Anteil der Dauer, in dem die Welle ausblendet |
| `containInElement` | boolean | `true` | Welle an der Elementkontur beschneiden |
| `maxWellen` | number | `3` | Gleichzeitige Wellen, älteste wird ersetzt |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `focusRipple` | boolean | `true` | Welle auch bei Tastaturfokus auslösen |
