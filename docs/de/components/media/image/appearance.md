# Bild (Image) - Aussehen

## Grundlayout

Bilder werden in verschiedenen Formen und Größen angezeigt, oft mit Hover-Effekten und Loading-Zuständen.

## Varianten

```css
/* Rectangular (Rechteckig) - Standard */
.image-rectangular {
  border-radius: 4px;
}

/* Circular (Rund) */
.image-circular {
  border-radius: 50%;
}

/* Pill (Pillenform) */
.image-pill {
  border-radius: 999px;
}
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Thumbnail | 100px | Listen, Grids |
| Small | 200px | Profile, kleine Karten |
| Medium | 400px | Cards, Panels |
| Large | 600px | Featured-Images |
| Full | 1920px+ | Hero-Sectionen, Backgrounds |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Bild füllt die Zelle, leichter Schatten je nach `shadow` |
| `hover` | Zoom oder Overlay mit Aktionen, gemäß `hoverEffect` |
| `geladen` | Platzhalter in Grundfarbe bis zum Ladende |
| `fehler` | Rahmen mit Symbol, Rückfallbild falls gesetzt |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich (1.1x) |
| `overlay` | Overlay mit Info/Icons |
| `border` | Rand leuchtet auf |
| `opacity` | Deckkraft ändert sich |

## Reaktiv

- `responsive = true` liefert je Breite eine passende Auflösung; die Anzeigefläche bleibt
  gleich groß, damit die Seite beim Laden nicht springt.
- In Rastern und Karten hält `fit = cover` das Seitenverhältnis, `fit = contain` lässt
  auf schmalen Bildschirmen Rand zu.
- Hintergrundbilder skalieren mit dem Viewport (`Full`), der Text darüber bleibt bei
  mindestens 4,5:1 Kontrast — sonst dunkler Schleier darüber.

## Loading-Zustand

### Skeleton (Platzhalter)

```
┌────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
└────────────────────────┘
```

### Spinner (Ladeanimation)

```
┌────────────────────────┐
│                        │
│      🔄                │
│                        │
└────────────────────────┘
```

## Fit-Mode-Varianten

| Mode | Beschreibung | Verwendung |
|------|-------------|------------|
| `cover` | Bild füllt Container, überschüssiger Bereich abgeschnitten | Hero-Bilder |
| `contain` | Bild passt komplett in Container, eventuell Rand | Produktbilder |
| `fill` | Bild wird gestreckt, um Container zu füllen | Hintergrundbilder |

## Border & Shadow

| Variant | Beschreibung |
|---------|--------------|
| `default` | Kein Rand, leichter Schatten |
| `outlined` | Heller Rand, kein Schatten |
| `elevated` | Starkes Shadow, keine Border |
| `rounded` | Abgerundete Ecken (8px) |
