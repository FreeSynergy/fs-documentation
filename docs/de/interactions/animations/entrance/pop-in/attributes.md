# Pop In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `pop-in` | Name der Animation |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem Aufkommen ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `250` | Dauer in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | schneller Anstieg, weiche Landung |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (volle Größe) beibehalten |

## Größen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `fromScale` | number | `0.8` | Startgröße |
| `toScale` | number | `1` | Zielgröße |
| `overshoot` | number | `1.06` | Faktor, über den das Element hinausschießt |
| `bounces` | number | `1` | Anzahl Nachschwingungen nach dem Overshoot |
| `origin` | string | `center` | Bezugspunkt: `center`, `top`, `bottom-left` … |
| `fromOpacity` | number | `0` | Startdeckkraft (0 = voll transparent) |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `short-fade` | `instant` (sofort sichtbar) oder `short-fade` |
