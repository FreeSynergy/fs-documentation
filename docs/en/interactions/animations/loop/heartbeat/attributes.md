# Heartbeat - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `heartbeat` | Name of the animation |
| `schlagAbfolge` | string | `lub-dub` | pattern per cycle: `lub-dub`, `dub-lub` |
| `schlagSkala` | number | `1.12` | maximum size of the first beat |
| `dauerProZyklus` | number | `1000` | cycle length in ms (60 bpm = 1000 ms) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1000` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-out` | fast rise, soft return |
| `iterationCount` | number \| `infinite` | `infinite` | endless, for as long as the status is live |
| `keyframes` | array | - | own support points (overrides the default pattern) |
| `playState` | string | `running` | `paused` outside the visible area |

## Rhythm attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `bpm` | number | `72` | heart rate; derives `dauerProZyklus` from it |
| `zweiterSchlag` | number | `0.8` | strength of the second beat relative to the first |
| `schlagAbstand` | number | `140` | distance between the two beats in ms |
| `pauseAnteil` | number | `0.45` | share of the rest phase in the cycle (0–1) |
| `haloFarbe` | string | `danger` | an optional red halo |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `maxDauer` | number | `10000` | after this time in ms the endless loop ends |
