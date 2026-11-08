# Pop In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `pop-in` | Name der Animation |
| `onAnimateStart` | function | - | läuft am Anfang |
| `onAnimateEnd` | function | - | läuft, nachdem das Element gelandet ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Dauer in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | schneller Anstieg, weiche Landung |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält den Endzustand (volle Größe) |

## Größenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `fromScale` | number | `0.8` | Startgröße |
| `toScale` | number | `1` | Zielgröße |
| `overshoot` | number | `1.06` | Faktor, über den das Element hinausschießt |
| `bounces` | number | `1` | Anzahl der Nachschwingungen nach dem Überschwingen |
| `origin` | string | `center` | Bezugspunkt: `center`, `top`, `bottom-left` … |
| `fromOpacity` | number | `0` | Start-Deckkraft (0 = vollständig transparent) |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `short-fade` | `instant` (sofort sichtbar) oder `short-fade` |
