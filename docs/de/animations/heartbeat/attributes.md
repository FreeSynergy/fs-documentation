# Heartbeat - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `heartbeat` | Name der Animation |
| `schlagAbfolge` | string | `lub-dub` | Muster pro Zyklus: `lub-dub`, `dub-lub` |
| `schlagSkala` | number | `1.12` | Maximale Größe des ersten Schlags |
| `dauerProZyklus` | number | `1000` | Zykluslänge in ms (60 bpm = 1000 ms) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1000` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-out` | schneller Anstieg, weiches Zurückgehen |
| `iterationCount` | number \| `infinite` | `infinite` | Endlos, solange der Status Live ist |
| `keyframes` | array | - | Eigene Stützstellen (Überschreibt das Standardmuster) |
| `playState` | string | `running` | `paused` außerhalb des Sichtbereichs |

## Rhythmus-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `bpm` | number | `72` | Herzfrequenz; leitet `dauerProZyklus` ab |
| `zweiterSchlag` | number | `0.8` | Stärke des zweiten Schlags relativ zum ersten |
| `schlagAbstand` | number | `140` | Abstand der beiden Schläge in ms |
| `pauseAnteil` | number | `0.45` | Anteil der Ruhephase am Zyklus (0–1) |
| `haloFarbe` | string | `danger` | optionaler roter Heiligenschein |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `maxDauer` | number | `10000` | Nach dieser Zeit in ms endet die Endlosschleife |
