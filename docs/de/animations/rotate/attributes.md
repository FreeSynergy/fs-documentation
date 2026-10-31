# Rotate - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Drehung ausgeführt |
| `onRotate` | function | - | Wird bei jeder Winkeländerung fortlaufend ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Erreichen des Zielwinkels ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `300` | Dauer der Drehung in ms |
| `timingFunction` | string | `ease-in-out` | Natürlicher Drehstart und Drehstopp |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Zielwinkel bleibt als neuer Zustand stehen |

## Winkel-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `angle` | number | `180` | Zielwinkel in Grad (negativ = gegen den Uhrzeigersinn) |
| `transformOrigin` | string | `center` | Drehpunkt: `center`, `top left`, `50% 100%` … |
| `rotationDirection` | string | `shortest` | `cw`, `ccw` oder `shortest` (kürzeste Drehrichtung) |
| `stateAngle` | boolean | `true` | Endwinkel als dauerhaften Zustand merken (z. B. auf-/zugeklappt)? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – Winkel ohne Drehung wechseln |
