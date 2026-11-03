# Pulse - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `pulse` | Name der Animation |
| `minScale` | number | `1` | Größe am Zyklusbeginn |
| `maxScale` | number | `1.06` | Größe am Peak |
| `minOpacity` | number | `1` | Deckkraft am Ausgangszustand |
| `maxOpacity` | number | `0.65` | Deckkraft am Peak |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1200` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | gleichmäßiges An- und Abschwellen |
| `iterationCount` | number \| `infinite` | `infinite` | Endlos, solange der Status aktiv ist |
| `direction` | string | `alternate` | Peak und Tal im Wechsel, ohne Sprung |
| `playState` | string | `running` | `paused`, wenn das Element nicht sichtbar ist |

## Zyklus-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `dauerProZyklus` | number | `1200` | Länge eines vollständigen Zyklus in ms |
| `waveform` | string | `sinusoidal` | `sinusoidal`, `linear` oder `triangle` |
| `haloRadius` | number | `0` | Zusätzlicher Ausstrahl-Ring in px (0 = aus) |
| `haloFarbe` | string | `accent` | Farbe des Rings |
| `pauseWhenHidden` | boolean | `true` | Pausieren außerhalb des Viewports |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `maxCyclesPerView` | number | `3` | Endlosschleife nach n Zyklen beenden |
