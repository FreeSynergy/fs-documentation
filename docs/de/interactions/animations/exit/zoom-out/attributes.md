# Zoom Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | läuft, wenn das Schrumpfen beginnt |
| `onAnimateEnd` | function | - | läuft, sobald das Element vollständig verschwunden ist |
| `onElementHidden` | function | - | meldet, dass das Element ausgeblendet wurde |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Dauer des Ausblendens in ms |
| `timingFunction` | string | `ease-in` | ein beschleunigtes Schrumpfen wirkt bewusst |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | der unsichtbare Endzustand bleibt erhalten |

## Skalierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `startScale` | number | `1` | Startskalierung (volle Größe) |
| `endScale` | number | `0` | Zielskalierung (0 = vollständig geschrumpft) |
| `opacitySync` | boolean | `true` | Deckkraft synchron zur Skalierung ausblenden? |
| `removeOnEnd` | boolean | `false` | Element nach dem Schrumpfen aus dem DOM entfernen? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – sofort ausblenden ohne Skalierung |
