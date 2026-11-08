# Pulse - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `pulse` | Name der Animation |
| `minScale` | number | `1` | Größe am Anfang des Zyklus |
| `maxScale` | number | `1.06` | Größe an der Spitze |
| `minOpacity` | number | `1` | Deckkraft im Startzustand |
| `maxOpacity` | number | `0.65` | Deckkraft an der Spitze |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1200` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | gleichmäßiges Anschwellen und Abnehmen |
| `iterationCount` | number \| `infinite` | `infinite` | endlos, solange der Status aktiv ist |
| `direction` | string | `alternate` | Spitze und Tal wechseln sich ab, ohne Sprung |
| `playState` | string | `running` | `paused`, solange das Element nicht sichtbar ist |

## Zyklusattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `dauerProZyklus` | number | `1200` | Länge eines vollen Zyklus in ms |
| `waveform` | string | `sinusoidal` | `sinusoidal`, `linear` oder `triangle` |
| `haloRadius` | number | `0` | ein zusätzlicher ausstrahlender Ring in px (0 = aus) |
| `haloFarbe` | string | `accent` | Farbe des Rings |
| `pauseWhenHidden` | boolean | `true` | pausieren außerhalb des Viewports |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `maxCyclesPerView` | number | `3` | beendet die endlose Schleife nach n Zyklen |
