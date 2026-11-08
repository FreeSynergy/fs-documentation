# Zoom In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn die Vergrößerung beginnt |
| `onAnimateEnd` | function | - | Wird ausgeführt, wenn die volle Größe erreicht ist |
| `onScaleChange` | function | - | Meldet die aktuelle Skalierung während der Animation |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `250` | Dauer des Einblendens in ms |
| `timingFunction` | string | `ease-out` | bremst sauber bis zur vollen Größe |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | die volle Größe bleibt nach dem Ende erhalten |

## Skalierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `startScale` | number | `0.5` | Startskalierung (muss kleiner als 1 sein) |
| `endScale` | number | `1` | Zielskalierung in X und Y |
| `opacitySync` | boolean | `true` | Deckkraft synchron mit der Skalierung erhöhen? |
| `transformOrigin` | string | `center` | Ursprung der Skalierung (z. B. `center`, `top left`) |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – nur einblenden statt skalieren |
