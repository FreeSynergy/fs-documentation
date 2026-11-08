# Fade In - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | läuft, wenn das Einblenden beginnt |
| `onAnimateEnd` | function | - | läuft, nachdem das Element vollständig sichtbar ist |
| `onVisibilityChange` | function | - | meldet die Sichtbarkeitsänderung (versteckt → sichtbar) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Dauer des Einblendens in ms |
| `timingFunction` | string | `ease-out` | sanfter Start, ruhige Landung |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | hält den Endzustand (vollständig sichtbar) nach dem Ende |

## Deckkraft-Attribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `fromOpacity` | number | `0` | Start-Deckkraft (0 = vollständig transparent) |
| `toOpacity` | number | `1` | Ziel-Deckkraft (1 = vollständig sichtbar) |
| `blur` | number | `0` | Unschärfe in px am Start, klingt beim Einblenden ab |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` (sofort sichtbar) oder `short-fade` |
