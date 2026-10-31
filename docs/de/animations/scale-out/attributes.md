# Scale Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `scale-out` | Name der Animation |
| `startScale` | number | `1` | Ausgangsgröße als Faktor |
| `endScale` | number | `0` | Zielgröße als Faktor (0 = verschwindet) |
| `transformOrigin` | string | `center` | Schrumpfpunkt; oft `top right` beim Auslöser |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `180` | Dauer in ms (Ausgänge gern kürzer als Eingänge) |
| `timingFunction` | string | `ease-in` | Ausgänge meist `ease-in` |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (0 %) bis zum Entfernen halten |
| `iterationCount` | number | `1` | Ausgänge laufen genau einmal |

## Achsen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axis` | string | `both` | `both`, `x` oder `y` |
| `scaleX` | number | `1` | Zusätzlicher Faktor für die Breite |
| `scaleY` | number | `1` | Zusätzlicher Faktor für die Höhe |
| `removeAfter` | boolean | `true` | Element nach dem Ende aus dem Layout entfernen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `removeImmediately` | boolean | `false` | Element ohne Animation sofort entfernen |
