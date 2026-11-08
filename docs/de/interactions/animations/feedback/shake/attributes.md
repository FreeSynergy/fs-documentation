# Shake - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `shake` | Name der Animation |
| `amplitude` | number | `8` | Auslenkung in px aus der Ruheposition |
| `cycles` | number | `3` | Anzahl der Hin- und Her-Bewegungen innerhalb eines Durchlaufs |
| `achse` | string | `x` | `x` (waagerecht), `y` (senkrecht), `rotate` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Gesamtdauer in ms |
| `timingFunction` | string | `ease-in-out` | weiche Umkehr an den Wendepunkten |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `iterationCount` | number | `1` | die Rückmeldung läuft einmal, nicht endlos |
| `fillMode` | string | `none` | das Element endet immer in der Ruheposition |

## Amplitudenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `decay` | boolean | `true` | die Auslenkung klingt pro Zyklus ab |
| `decayFactor` | number | `0.7` | Verhältnis aufeinanderfolgender Amplituden |
| `waveform` | string | `sinusoidal` | `sinusoidal` oder `linear` (ruckartig) |
| `richtung` | string | `beide` | `beide`, `links zuerst`, `rechts zuerst` |
| `interruptible` | boolean | `true` | ein neues Shake ersetzt das laufende |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `announceError` | boolean | `true` | Fehler zusätzlich als Text/ARIA melden |
