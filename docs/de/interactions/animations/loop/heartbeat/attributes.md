# Heartbeat - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `heartbeat` | Name der Animation |
| `schlagAbfolge` | string | `lub-dub` | Muster pro Zyklus: `lub-dub`, `dub-lub` |
| `schlagSkala` | number | `1.12` | maximale Größe des ersten Schlags |
| `dauerProZyklus` | number | `1000` | Länge eines Zyklus in ms (60 bpm = 1000 ms) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1000` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-out` | schneller Anstieg, weiche Rückkehr |
| `iterationCount` | number \| `infinite` | `infinite` | endlos, solange der Status live ist |
| `keyframes` | array | - | eigene Stützpunkte (ersetzt das Standardmuster) |
| `playState` | string | `running` | `paused` außerhalb des sichtbaren Bereichs |

## Rhythmusattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `bpm` | number | `72` | Herzfrequenz; daraus wird `dauerProZyklus` abgeleitet |
| `zweiterSchlag` | number | `0.8` | Stärke des zweiten Schlags relativ zum ersten |
| `schlagAbstand` | number | `140` | Abstand zwischen den beiden Schlägen in ms |
| `pauseAnteil` | number | `0.45` | Anteil der Ruhephase am Zyklus (0–1) |
| `haloFarbe` | string | `danger` | ein optionaler roter Halo |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `maxDauer` | number | `10000` | nach dieser Zeit in ms endet die endlose Schleife |
