# Glow - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `glowColor` | string | `accent` | Farbe des Scheins |
| `glowIntensity` | number | `1.0` | Helligkeit des Scheins (0.0–2.0) |
| `glowSpread` | number | `12` | Radius des Scheins in px |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1500` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | sanftes Anschwellen und Abnehmen |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, solange der Status aktiv ist |
| `direction` | string | `alternate` | der Schein schwillt an und wieder ab |

## Glow-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aktiv` | boolean | `false` | Leuchten einschalten (z. B. bei Auswahl) |
| `pulsierend` | boolean | `true` | der Schein atmet in der Schleife; `false` = konstantes Leuchten |
| `glowForm` | string | `kontur` | `kontur` folgt der Form des Elements, `rechteckig` rendert schneller |
| `glowEbene` | string | `hinter` | Schein hinter oder über dem Inhalt zeichnen |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
