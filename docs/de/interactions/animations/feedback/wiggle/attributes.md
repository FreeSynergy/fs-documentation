# Wiggle - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `wiggle` | Name der Animation |
| `amplitude` | number | `2` | Auslenkung in Grad (bei `achse: rotate`) |
| `achse` | string | `rotate` | `rotate`, `x` oder `y` |
| `pivot` | string | `center` | Drehpunkt der Wackelbewegung |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `600` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | weiche Umkehr an den Wendepunkten |
| `iterationCount` | number \| `infinite` | `infinite` | endlos, solange der Modus aktiv ist |
| `direction` | string | `alternate` | Hin und Her ohne Sprung zurück |
| `playState` | string | `running` | `paused`, während das Element unsichtbar ist |

## Amplitudenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `offsetX` | number | `0` | zusätzliche Verschiebung in px |
| `offsetY` | number | `0` | zusätzliche Verschiebung in px |
| `phaseOffset` | number | `0` | Phasenversatz pro Element in ms (Gruppen) |
| `decay` | boolean | `false` | die Bewegung mit der Zeit schwächer werden lassen |
| `stopOnExit` | boolean | `true` | beim Verlassen des Modus direkt in die Ruheposition |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `stateInsteadOfMotion` | boolean | `true` | den Modus zusätzlich mit Umriss/Icon markieren |
