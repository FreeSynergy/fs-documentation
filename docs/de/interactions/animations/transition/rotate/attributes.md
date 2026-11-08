# Rotate - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn die Drehung beginnt |
| `onRotate` | function | - | Wird bei jeder Winkeländerung fortlaufend ausgeführt |
| `onAnimateEnd` | function | - | Wird ausgeführt, wenn der Zielwinkel erreicht ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `300` | Dauer der Drehung in ms |
| `timingFunction` | string | `ease-in-out` | ein natürlicher Start und Stopp der Drehung |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | der Zielwinkel bleibt als neuer Zustand |

## Winkelattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `angle` | number | `180` | Zielwinkel in Grad (negativ = gegen den Uhrzeigersinn) |
| `transformOrigin` | string | `center` | Drehpunkt: `center`, `top left`, `50% 100%` … |
| `rotationDirection` | string | `shortest` | `cw`, `ccw` oder `shortest` (die kürzeste Drehrichtung) |
| `stateAngle` | boolean | `true` | Endwinkel als bleibenden Zustand merken (z. B. geöffnet/geschlossen)? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – den Winkel ohne Drehung ändern |
