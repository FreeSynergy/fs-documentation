# Fade In - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start des Einblendens ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Einblenden ausgeführt |
| `onVisibilityChange` | function | - | Meldet den Sichtbarkeitswechsel (hidden → visible) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `250` | Einblendedauer in ms |
| `timingFunction` | string | `ease-out` | Weicher Start, ruhige Landung |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Endzustand (voll sichtbar) nach Ende beibehalten |

## Deckkraft-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `fromOpacity` | number | `0` | Startdeckkraft (0 = voll transparent) |
| `toOpacity` | number | `1` | Zieldeckkraft (1 = voll sichtbar) |
| `blur` | number | `0` | Weichzeichner in px beim Start, klingt beim Einblenden ab |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` (sofort sichtbar) oder `short-fade` |
