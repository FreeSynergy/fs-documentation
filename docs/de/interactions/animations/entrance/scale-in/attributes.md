# Scale In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `scale-in` | Name der Animation |
| `startScale` | number | `0` | Startgröße als Faktor (0 = unsichtbar) |
| `endScale` | number | `1` | Zielgröße als Faktor |
| `transformOrigin` | string | `center` | Wachstumspunkt: `center`, `top`, `bottom right` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `200` | Dauer in ms |
| `timingFunction` | string | `ease-out` | Eingänge meist `ease-out` |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `backwards` | Startzustand (0 %) schon während des Delays zeigen |
| `onAnimateEnd` | function | - | Wird nach dem Erreichen der Endgröße ausgeführt |

## Achsen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axis` | string | `both` | `both`, `x` oder `y` |
| `scaleX` | number | `1` | Zusätzlicher Faktor für die Breite |
| `scaleY` | number | `1` | Zusätzlicher Faktor für die Höhe |
| `keepSpace` | boolean | `true` | Layout-Platz während der Animation reservieren |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `announceOnEnd` | boolean | `false` | Inhalt erst nach Ende der Animation melden |
