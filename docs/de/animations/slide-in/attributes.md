# Slide In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Einbewegung ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Erreichen der Endposition ausgeführt |
| `onSlideProgress` | function | - | Meldet den Fortschritt der Bewegung (0–1) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `300` | Dauer der Einbewegung in ms |
| `timingFunction` | string | `ease-out` | Endphase abbremsen, wirkt greifbar |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `backwards` | Element bleibt vor dem Start außerhalb der Ansicht |

## Richtungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `direction` | string | `left` | `left`, `right`, `up` (von unten), `down` (von oben) |
| `distance` | number \| string | `100%` | Startversatz in px oder Prozent der Elementgröße |
| `combineFade` | boolean | `true` | Einbewegung mit Fade In der Deckkraft kombinieren? |
| `edge` | string | `viewport` | Bezugsrahmen der Außenposition: `viewport` oder Parent-Element |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `fade` – bei reduzierter Bewegung nur einblenden |
