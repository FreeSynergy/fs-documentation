# Wiggle - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `wiggle` | Name der Animation |
| `amplitude` | number | `2` | Ausschlag in Grad (bei `achse: rotate`) |
| `achse` | string | `rotate` | `rotate`, `x` oder `y` |
| `pivot` | string | `center` | Drehpunkt der Wippbewegung |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `600` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | weiche Umkehr an den Wendepunkten |
| `iterationCount` | number \| `infinite` | `infinite` | Endlos, solange der Modus aktiv ist |
| `direction` | string | `alternate` | Hin und Her ohne Sprung zurück |
| `playState` | string | `running` | `paused`, wenn das Element unsichtbar ist |

## Amplitude-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `offsetX` | number | `0` | Zusätzliche Verschiebung in px |
| `offsetY` | number | `0` | Zusätzliche Verschiebung in px |
| `phaseOffset` | number | `0` | Phasenversatz pro Element in ms (Gruppen) |
| `decay` | boolean | `false` | Bewegung über die Zeit schwächer werden lassen |
| `stopOnExit` | boolean | `true` | Beim Verlassen des Modus sofort in Ruhelage |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `stateInsteadOfMotion` | boolean | `true` | Modus zusätzlich durch Rahmen/Icon kennzeichnen |
