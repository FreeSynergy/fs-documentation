# Highlight - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `highlight` | Name der Animation |
| `farbe` | string | `accent` | Leuchtfarbe des Hintergrundes |
| `intensity` | number | `0.35` | Deckkraft im Maximum (0–1) |
| `modus` | string | `background` | `background`, `outline`, `text` oder `border` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `900` | Dauer eines Aufleuchtens in ms |
| `timingFunction` | string | `ease-in-out` | weicher Anstieg und Abklang |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `iterationCount` | number | `1` | meist einmal; 2 für stärkere Aufmerksamkeit |
| `fillMode` | string | `none` | danach gilt wieder die Originalfarbe |

## Farb-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `startFarbe` | string | `transparent` | Ausgangsüberlagerung |
| `endFarbe` | string | `transparent` | Endüberlagerung |
| `anstiegAnteil` | number | `0.25` | Anteil der Dauer bis zum Maximum |
| `radius` | number | `4` | Eckenradius der Leuchtfläche in px |
| `puffer` | number | `8` | Abstand der Leuchtfläche zum Inhalt in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `kontrastCheck` | boolean | `true` | Mindestkontrast beim Aufleuchten erzwingen |
