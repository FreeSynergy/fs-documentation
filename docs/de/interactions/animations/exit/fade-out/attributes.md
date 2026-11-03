# Fade Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start des Ausblendens ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Ausblenden ausgeführt |
| `onElementHidden` | function | - | Meldet, dass das Element ausgeblendet wurde |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `200` | Ausblenddauer in ms |
| `timingFunction` | string | `ease-in` | Ausgänge wirken mit Beschleunigung natürlicher |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (unsichtbar) nach Ende beibehalten |

## Deckkraft-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `fromOpacity` | number | `1` | Ausgangsdeckkraft (1 = voll sichtbar) |
| `toOpacity` | number | `0` | Zieldeckkraft (0 = unsichtbar) |
| `removeOnEnd` | boolean | `false` | Element nach dem Ausblenden aus dem DOM entfernen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `aria-hidden` | string | - | Wird nach Ende automatisch auf `true` gesetzt |
