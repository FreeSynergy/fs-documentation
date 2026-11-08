# Fade Out - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn das Ausblenden beginnt |
| `onAnimateEnd` | function | - | Wird ausgeführt, nachdem das Element vollständig ausgeblendet ist |
| `onElementHidden` | function | - | Meldet, dass das Element ausgeblendet wurde |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `200` | Dauer des Ausblendens in ms |
| `timingFunction` | string | `ease-in` | Ausgänge wirken mit Beschleunigung natürlicher |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält den Endzustand (unsichtbar) nach dem Ende |

## Deckkraftattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `fromOpacity` | number | `1` | Startdeckkraft (1 = voll sichtbar) |
| `toOpacity` | number | `0` | Zieldeckkraft (0 = unsichtbar) |
| `removeOnEnd` | boolean | `false` | Element nach dem Ausblenden aus dem DOM entfernen? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `aria-hidden` | string | - | wird nach dem Ende automatisch auf `true` gesetzt |
