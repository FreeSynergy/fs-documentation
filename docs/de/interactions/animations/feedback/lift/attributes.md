# Lift - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `lift` | Name der Animation |
| `onLiftStart` | function | - | läuft, wenn das Element angehoben wird |
| `onLiftEnd` | function | - | läuft nach dem Zurücksetzen |
| `ausloeser` | string | `hover` | `hover`, `focus` oder `hover-focus` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `160` | Dauer des Anhebens in ms |
| `timingFunction` | string | `ease-out` | sanft anheben, weich landen |
| `delay` | number | `0` | keine Verzögerung – eine Reaktion auf den Zeiger |
| `fillMode` | string | `forwards` | der angehobene Zustand bleibt während des Hovers |

## Schattenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `liftOffsetY` | number | `-2` | Verschiebung nach oben in px (negativ = höher) |
| `shadowSpread` | number | `8` | Reichweite des Schattens im angehobenen Zustand in px |
| `shadowBlur` | number | `16` | Weichzeichnung des Schattens in px |
| `shadowOpacity` | number | `0.18` | Deckkraft des Schattens (0–1) |
| `surfaceDelta` | number | `0.03` | Aufhellung der Fläche im angehobenen Zustand |
| `nurSchatten` | boolean | `false` | ohne Bewegung, nur der Schatten ändert sich |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `nurSchatten` | `nurSchatten` oder `rand` (Umriss statt Höhe) |
