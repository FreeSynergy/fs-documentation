# Scale Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `scale-out` | Name der Animation |
| `startScale` | number | `1` | Startgröße als Faktor |
| `endScale` | number | `0` | Zielgröße als Faktor (0 = verschwindet) |
| `transformOrigin` | string | `center` | Schrumpfpunkt; oft `top right` am Auslöser |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `180` | Dauer in ms (Austritte oft kürzer als Eintritte) |
| `timingFunction` | string | `ease-in` | Austritte meist `ease-in` |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält den Endzustand (0 %) bis zum Entfernen |
| `iterationCount` | number | `1` | Austritte laufen genau einmal |

## Achsenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `axis` | string | `both` | `both`, `x` oder `y` |
| `scaleX` | number | `1` | zusätzlicher Faktor für die Breite |
| `scaleY` | number | `1` | zusätzlicher Faktor für die Höhe |
| `removeAfter` | boolean | `true` | Element nach dem Ende aus dem Layout nehmen |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `removeImmediately` | boolean | `false` | Element sofort ohne Animation entfernen |
