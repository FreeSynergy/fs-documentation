# Slide Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | läuft, wenn die Austrittsbewegung beginnt |
| `onAnimateEnd` | function | - | läuft, wenn der Bereich vollständig verlassen ist |
| `onSlideProgress` | function | - | meldet den Fortschritt der Bewegung (0–1) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Dauer der Austrittsbewegung in ms |
| `timingFunction` | string | `ease-in` | ein beschleunigter Austritt wirkt bewusst |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | das Element bleibt nach dem Ende außerhalb des Bereichs |

## Richtungsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `direction` | string | `right` | `left`, `right`, `up` (nach oben), `down` (nach unten) |
| `distance` | number \| string | `100%` | zurückgelegte Strecke bis außerhalb, in px oder Prozent |
| `combineFade` | boolean | `false` | Austrittsbewegung mit einem Ausblenden der Deckkraft kombinieren? |
| `removeOnEnd` | boolean | `false` | Element nach dem Hinausgleiten aus dem DOM entfernen? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – bei reduzierter Bewegung sofort ausblenden |
