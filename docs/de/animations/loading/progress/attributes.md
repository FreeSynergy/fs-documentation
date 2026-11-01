# Progress - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `wert` | number | `0` | Aktueller Fortschritt |
| `wertMin` | number | `0` | Untergrenze |
| `wertMax` | number | `100` | Obergrenze |
| `indikator` | string | `balken` | `balken`, `ring`, `segmente` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `300` | weiche Übernahme neuer Werte in ms |
| `timingFunction` | string | `ease-out` | Füllung wächst auslaufend |
| `iterationCount` | number \| `infinite` | `1` | `infinite` nur bei unbestimmter Anzeige |

## Progress-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `unbestimmt` | boolean | `false` | laufende Anzeige ohne bekannten Wert |
| `farbe` | string | `accent` | Füllfarbe, optional `success` ab 100 % |
| `beschriftung` | string | `auto` | Prozentwert, eigener Text oder `keine` |
| `dicke` | number | `8` | Balkenstärke bzw. Ringbreite in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
