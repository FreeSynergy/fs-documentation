# Zoom In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Vergrößerung ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Erreichen der vollen Größe ausgeführt |
| `onScaleChange` | function | - | Meldet die aktuelle Skalierung während der Animation |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `250` | Dauer der Einblendung in ms |
| `timingFunction` | string | `ease-out` | Bremst zur vollen Größe sauber ab |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Volle Größe bleibt nach Ende erhalten |

## Skalierungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `startScale` | number | `0.5` | Ausgangsskalierung (muss kleiner als 1 sein) |
| `endScale` | number | `1` | Zielskalierung in X und Y |
| `opacitySync` | boolean | `true` | Deckkraft synchron zur Skalierung hochregeln? |
| `transformOrigin` | string | `center` | Ursprung der Skalierung (z. B. `center`, `top left`) |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – nur einblenden statt skalieren |
