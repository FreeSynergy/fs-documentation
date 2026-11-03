# Pop Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `pop-out` | Name der Animation |
| `mirrorOf` | string | `pop-in` | Name der Gegenanimation |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem Verschwinden ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `200` | Dauer in ms |
| `timingFunction` | string | `cubic-bezier(.36,0,.66,-.56)` | kurzes Ausholen, dann beschleunigt hinaus |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | unsichtbaren Endzustand beibehalten |

## Größen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `fromScale` | number | `1` | Ausgangsgröße |
| `toScale` | number | `0` | Zielgröße |
| `anticipation` | number | `1.04` | Ausholen vor dem Schrumpfen |
| `origin` | string | `center` | Bezugspunkt: `center`, `top`, `bottom-left` … |
| `toOpacity` | number | `0` | Zieldeckkraft |
| `removeAfterEnd` | boolean | `true` | Element nach dem Ende aus dem Layout nehmen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | `instant` (sofort entfernen) oder `short-fade` |
