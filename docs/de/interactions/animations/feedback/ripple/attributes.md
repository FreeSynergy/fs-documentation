# Ripple - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `ripple` | Name der Animation |
| `wellenUrsprung` | string | `click` | `click` (Berührungspunkt) oder `center` |
| `farbe` | string | `onSurface 0.2` | Füllfarbe der Welle mit Deckkraft |
| `radius` | string \| number | `auto` | Zielradius; `auto` = gesamte Fläche erreichen |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `450` | Ausbreitungsdauer einer Welle in ms |
| `timingFunction` | string | `ease-out` | die Welle verlangsamt sich beim Wachsen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `iterationCount` | number | `1` | eine Welle pro Interaktion |
| `fillMode` | string | `none` | die Welle verschwindet vollständig |

## Wellenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `startRadius` | number | `0` | Startradius in px |
| `spreadDuration` | number | `450` | Zeit bis zum Erreichen des Zielradius |
| `fadeAnteil` | number | `0.6` | Anteil der Dauer, in dem die Welle ausblendet |
| `containInElement` | boolean | `true` | Welle an der Elementkontur abschneiden |
| `maxWellen` | number | `3` | gleichzeitige Wellen, die älteste wird ersetzt |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `focusRipple` | boolean | `true` | Welle auch bei Tastaturfokus auslösen |
