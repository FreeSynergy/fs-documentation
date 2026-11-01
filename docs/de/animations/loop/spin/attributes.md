# Spin - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Drehung ausgeführt |
| `onCycle` | function | - | Wird nach jeder vollständigen Umdrehung ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Stoppen der Drehung ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1000` | Dauer einer Umdrehung in ms |
| `timingFunction` | string | `linear` | Gleichmäßige Geschwindigkeit ohne Ruckeln |
| `iterationCount` | number \| `infinite` | `infinite` | Endlosschleife bis zum Stop |
| `playState` | string | `running` | `running` oder `paused` (z. B. bei Tab-Wechsel) |

## Dreh-Attribute (Dauerbetrieb)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `spinDirection` | string | `cw` | `cw` = Uhrzeigersinn, `ccw` = gegen den Uhrzeigersinn |
| `arcSweep` | number | `270` | Sichtbarer Bogen in Grad (360 = volle Scheibe) |
| `pauseWhenHidden` | boolean | `true` | Drehung pausieren, wenn das Element nicht sichtbar ist? |
| `stopOnTaskEnd` | boolean | `true` | Drehung automatisch beenden, wenn die Aufgabe endet? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text, z. B. „Wird geladen“ |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `role` | string | - | `status` – Fortschritt zusätzlich als Text ausgeben |
