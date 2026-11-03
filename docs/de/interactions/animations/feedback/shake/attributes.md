# Shake - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `shake` | Name der Animation |
| `amplitude` | number | `8` | Ausschlag in px ab der Ruhelage |
| `cycles` | number | `3` | Anzahl Hin und Her innerhalb eines Durchlaufs |
| `achse` | string | `x` | `x` (horizontal), `y` (vertikal), `rotate` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `400` | Gesamtdauer in ms |
| `timingFunction` | string | `ease-in-out` | weiche Umkehr an den Wendepunkten |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `iterationCount` | number | `1` | Feedback läuft einmal, nicht endlos |
| `fillMode` | string | `none` | Element endet immer in der Ruhelage |

## Amplitude-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `decay` | boolean | `true` | Ausschlag klingt pro Zyklus ab |
| `decayFactor` | number | `0.7` | Verhältnis aufeinanderfolgender Amplituden |
| `waveform` | string | `sinusoidal` | `sinusoidal` oder `linear` (hakelig) |
| `richtung` | string | `beide` | `beide`, `links zuerst`, `rechts zuerst` |
| `interruptible` | boolean | `true` | Neuer Shake ersetzt den laufenden |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `announceError` | boolean | `true` | Fehler zusätzlich als Text/ARIA melden |
