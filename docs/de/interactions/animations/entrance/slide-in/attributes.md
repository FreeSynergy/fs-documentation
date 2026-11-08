# Slide In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn die Bewegung beginnt |
| `onAnimateEnd` | function | - | Wird ausgeführt, wenn die Endposition erreicht ist |
| `onSlideProgress` | function | - | Meldet den Fortschritt der Bewegung (0–1) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `300` | Dauer der Bewegung in ms |
| `timingFunction` | string | `ease-out` | Abbremsen in der Endphase, wirkt greifbar |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `backwards` | Das Element bleibt vor dem Start außerhalb der Ansicht |

## Richtungsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `direction` | string | `left` | `left`, `right`, `up` (von unten), `down` (von oben) |
| `distance` | number \| string | `100%` | Startversatz in px oder Prozent der Elementgröße |
| `combineFade` | boolean | `true` | Bewegung mit einem Einblenden der Deckkraft kombinieren? |
| `edge` | string | `viewport` | Bezugsrahmen der Außenposition: `viewport` oder das übergeordnete Element |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – bei reduzierter Bewegung nur einblenden |
