# Spin - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn die Drehung beginnt |
| `onCycle` | function | - | Wird nach jeder vollen Umdrehung ausgeführt |
| `onAnimateEnd` | function | - | Wird ausgeführt, wenn die Drehung stoppt |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1000` | Dauer einer Umdrehung in ms |
| `timingFunction` | string | `linear` | gleichmäßiges Tempo ohne Ruckeln |
| `iterationCount` | number \| `infinite` | `infinite` | endlose Schleife bis zum Stoppen |
| `playState` | string | `running` | `running` oder `paused` (z. B. bei einem Tab-Wechsel) |

## Drehattribute (fortlaufendes Drehen)

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `spinDirection` | string | `cw` | `cw` = im Uhrzeigersinn, `ccw` = gegen den Uhrzeigersinn |
| `arcSweep` | number | `270` | sichtbarer Bogen in Grad (360 = volle Scheibe) |
| `pauseWhenHidden` | boolean | `true` | Drehung pausieren, wenn das Element nicht sichtbar ist? |
| `stopOnTaskEnd` | boolean | `true` | Drehung automatisch beenden, wenn die Aufgabe endet? |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text, z. B. "Laden" |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `role` | string | - | `status` – gibt den Fortschritt zusätzlich als Text aus |
