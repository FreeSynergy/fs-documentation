# Slide Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Ausbewegung ausgeführt |
| `onAnimateEnd` | function | - | Wird beim vollständigen Verlassen der Ansicht ausgeführt |
| `onSlideProgress` | function | - | Meldet den Fortschritt der Bewegung (0–1) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `250` | Dauer der Ausbewegung in ms |
| `timingFunction` | string | `ease-in` | Beschleunigender Ausgang wirkt absichtsvoll |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Element bleibt nach Ende außerhalb der Ansicht |

## Richtungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `direction` | string | `right` | `left`, `right`, `up` (nach oben), `down` (nach unten) |
| `distance` | number \| string | `100%` | Wegstrecke bis außerhalb in px oder Prozent |
| `combineFade` | boolean | `false` | Ausbewegung mit Fade Out der Deckkraft kombinieren? |
| `removeOnEnd` | boolean | `false` | Element nach dem Hinausgleiten aus dem DOM entfernen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – bei reduzierter Bewegung sofort ausblenden |
