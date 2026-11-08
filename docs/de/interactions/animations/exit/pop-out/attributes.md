# Pop Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `pop-out` | Name der Animation |
| `mirrorOf` | string | `pop-in` | Name der Gegenanimation |
| `onAnimateStart` | function | - | läuft am Anfang |
| `onAnimateEnd` | function | - | läuft, nachdem das Element verschwunden ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Dauer in ms |
| `timingFunction` | string | `cubic-bezier(.36,0,.66,-.56)` | eine kurze Vorwegnahme, dann beschleunigt nach außen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält den unsichtbaren Endzustand |

## Größenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `fromScale` | number | `1` | Startgröße |
| `toScale` | number | `0` | Zielgröße |
| `anticipation` | number | `1.04` | Vorwegnahme vor dem Schrumpfen |
| `origin` | string | `center` | Bezugspunkt: `center`, `top`, `bottom-left` … |
| `toOpacity` | number | `0` | Ziel-Deckkraft |
| `removeAfterEnd` | boolean | `true` | Element nach dem Ende aus dem Layout nehmen |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | `instant` (sofort entfernen) oder `short-fade` |
