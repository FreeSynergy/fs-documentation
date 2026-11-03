# Lift - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `lift` | Name der Animation |
| `onLiftStart` | function | - | Wird beim Anheben ausgeführt |
| `onLiftEnd` | function | - | Wird nach dem Zurücksetzen ausgeführt |
| `ausloeser` | string | `hover` | `hover`, `focus` oder `hover-focus` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `160` | Dauer des Anhebens in ms |
| `timingFunction` | string | `ease-out` | sanft steigen, weich landen |
| `delay` | number | `0` | keine Verzögerung – Reaktion auf Zeiger |
| `fillMode` | string | `forwards` | angehobener Zustand bleibt während des Hover |

## Schatten-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `liftOffsetY` | number | `-2` | Verschiebung nach oben in px (negativ = höher) |
| `shadowSpread` | number | `8` | Schattenreichweite im angehobenen Zustand in px |
| `shadowBlur` | number | `16` | Weichzeichnung des Schattens in px |
| `shadowOpacity` | number | `0.18` | Deckkraft des Schattens (0–1) |
| `surfaceDelta` | number | `0.03` | Aufhellung der Fläche im angehobenen Zustand |
| `nurSchatten` | boolean | `false` | ohne Bewegung, nur Schattenwechsel |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `nurSchatten` | `nurSchatten` oder `rand` (Rahmen statt Höhe) |
