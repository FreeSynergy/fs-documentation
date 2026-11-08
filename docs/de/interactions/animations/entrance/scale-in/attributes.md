# Scale In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `scale-in` | Name der Animation |
| `startScale` | number | `0` | Startgröße als Faktor (0 = unsichtbar) |
| `endScale` | number | `1` | Zielgröße als Faktor |
| `transformOrigin` | string | `center` | Wachstumspunkt: `center`, `top`, `bottom right` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `200` | Dauer in ms |
| `timingFunction` | string | `ease-out` | Einblendungen meist `ease-out` |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `backwards` | Startzustand (0 %) schon während der Verzögerung zeigen |
| `onAnimateEnd` | function | - | Wird ausgeführt, sobald die Endgröße erreicht ist |

## Achsenattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `axis` | string | `both` | `both`, `x` oder `y` |
| `scaleX` | number | `1` | zusätzlicher Faktor für die Breite |
| `scaleY` | number | `1` | zusätzlicher Faktor für die Höhe |
| `keepSpace` | boolean | `true` | Layoutplatz während der Animation reservieren |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `announceOnEnd` | boolean | `false` | Inhalt erst nach Ende der Animation ansagen |
