# Radial Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `radial-out` | Name der Animation |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem letzten Punkt ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `220` | Dauer pro Ring in ms |
| `timingFunction` | string | `cubic-bezier(.2,.8,.3,1)` | zügiger Start, weiche Landung |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (Ringposition) beibehalten |

## Radial-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `origin` | string | `anchor` | Ausgangspunkt: Ankermitte (`center`, `fab`, Zeiger …) |
| `fromRadius` | number | `0` | Startabstand vom Anker (0 = Kernmitte) |
| `fromScale` | number | `0` | Startgröße der Punkte |
| `toScale` | number | `1` | Endgröße |
| `overshoot` | number | `1` | Faktor über die Ringposition hinaus (1 = ohne) |
| `staggerStep` | number | `18` | Versatz zwischen Punkten in ms |
| `ringStep` | number | `80` | Versatz zwischen Ringen in ms |
| `order` | string | `angle` | Reihenfolge: `angle`, `inside-out`, `random` |
| `fadePoints` | boolean | `true` | Punkte zusätzlich einblenden? |
| `mirrorOf` | string | `radial-in` | Name der Gegenanimation |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `fade-in` | `instant` (sofort sichtbar) oder `fade-in` |
