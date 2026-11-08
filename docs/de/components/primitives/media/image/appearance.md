# Image - Erscheinungsbild

## Grundlayout

Bilder werden in verschiedenen Formen und Größen angezeigt, oft mit Hover-Effekten
und Ladezuständen.

## Varianten

```css
/* rechteckig - Standard */
.image-rectangular {
  border-radius: 4px;
}

/* rund */
.image-circular {
  border-radius: 50%;
}

/* Pille */
.image-pill {
  border-radius: 999px;
}
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| thumbnail | 100px | Listen, Raster |
| small | 200px | Profile, kleine Cards |
| medium | 400px | Cards, Panels |
| large | 600px | hervorgehobene Bilder |
| full | 1920px+ | Hero-Bereiche, Hintergründe |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | das Bild füllt die Zelle, ein leichter Schatten je nach `shadow` |
| `hover` | Zoom oder ein Overlay mit Aktionen, je nach `hoverEffect` |
| `geladen` | Platzhalter in der Grundfarbe, bis das Laden endet |
| `fehler` | Rahmen mit einem Symbol, Ersatzbild, falls eines gesetzt ist |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Bild wächst (1,1-fach) |
| `overlay` | Overlay mit Infos oder Icons |
| `border` | der Rahmen leuchtet auf |
| `opacity` | die Deckkraft ändert sich |

## Responsiv

- `responsive = true` liefert pro Breite eine passende Auflösung. Der Anzeigebereich bleibt
  gleich groß, damit die Seite beim Laden nicht springt.
- In Rastern und Cards hält `fit = cover` das Seitenverhältnis. `fit = contain` fügt auf
  schmalen Bildschirmen Ränder hinzu.
- Hintergrundbilder skalieren mit dem Viewport (`full`). Der Text darüber bleibt bei
  mindestens 4,5:1 Kontrast. Sonst wird ein dunkler Schleier darübergelegt.

## Ladezustand

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

## Varianten des Einpassens

| Modus | Beschreibung | Verwendung |
|-------|--------------|------------|
| `cover` | das Bild füllt den Container, überstehende Bereiche werden abgeschnitten | Hero-Bilder |
| `contain` | das Bild passt ganz in den Container, eventuell mit Rand | Produktbilder |
| `fill` | das Bild wird auf die Containergröße gestreckt | Hintergrundbilder |

## Rahmen und Schatten

| Variante | Beschreibung |
|----------|--------------|
| `default` | kein Rahmen, leichter Schatten |
| `outlined` | leichter Rahmen, kein Schatten |
| `elevated` | starker Schatten, kein Rahmen |
| `rounded` | abgerundete Ecken (8px) |
