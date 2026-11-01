# Zoom Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Verkleinerung ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Verschwinden ausgeführt |
| `onElementHidden` | function | - | Meldet, dass das Element ausgeblendet wurde |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `200` | Dauer der Ausblendung in ms |
| `timingFunction` | string | `ease-in` | Beschleunigtes Schrumpfen wirkt absichtsvoll |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Unsichtbarer Endzustand bleibt erhalten |

## Skalierungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `startScale` | number | `1` | Ausgangsskalierung (volle Größe) |
| `endScale` | number | `0` | Zielskalierung (0 = vollständig geschrumpft) |
| `opacitySync` | boolean | `true` | Deckkraft synchron zur Skalierung ausregeln? |
| `removeOnEnd` | boolean | `false` | Element nach dem Schrumpfen aus dem DOM entfernen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – ohne Skalierung sofort ausblenden |
