# Highlight - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `highlight` | Name der Animation |
| `farbe` | string | `accent` | Leuchtfarbe des Hintergrunds |
| `intensity` | number | `0.35` | Deckkraft im Maximum (0–1) |
| `modus` | string | `background` | `background`, `outline`, `text` oder `border` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `900` | Dauer eines Aufleuchtens in ms |
| `timingFunction` | string | `ease-in-out` | sanfter Anstieg und Abklingen |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `iterationCount` | number | `1` | meist einmal; 2 für stärkere Aufmerksamkeit |
| `fillMode` | string | `none` | danach gilt wieder die ursprüngliche Farbe |

## Farbattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `startFarbe` | string | `transparent` | Start-Overlay |
| `endFarbe` | string | `transparent` | End-Overlay |
| `anstiegAnteil` | number | `0.25` | Anteil der Dauer bis zum Maximum |
| `radius` | number | `4` | Eckenradius der leuchtenden Fläche in px |
| `puffer` | number | `8` | Abstand der leuchtenden Fläche zum Inhalt in px |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `kontrastCheck` | boolean | `true` | während des Leuchtens einen Mindestkontrast erzwingen |
