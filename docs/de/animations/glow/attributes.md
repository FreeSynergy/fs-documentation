# Glow - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `glowColor` | string | `accent` | Farbe des Leuchtens |
| `glowIntensity` | number | `1.0` | Helligkeit des Scheins (0.0–2.0) |
| `glowSpread` | number | `12` | Radius des Scheins in px |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1500` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | weiches An- und Abschwellen |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, solange der Status aktiv ist |
| `direction` | string | `alternate` | Schein schwillt an und wieder ab |

## Glow-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aktiv` | boolean | `false` | Glow einschalten (z. B. bei Auswahl) |
| `pulsierend` | boolean | `true` | Schein atmet im Loop; `false` = konstantes Leuchten |
| `glowForm` | string | `kontur` | `kontur` folgt der Elementform, `rechteckig` rendert schneller |
| `glowEbene` | string | `hinter` | Schein hinter oder über dem Inhalt zeichnen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
