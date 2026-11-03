# Gallery - Aussehen

## Grundlayout

Galerien zeigen Bilder in verschiedenen Layouts an: Raster, Karussell oder Kachelansicht.

## Varianten

### Grid (Raster)

```
┌──────────┬──────────┬──────────┐
│  🖼️    │  🖼️    │  🖼️    │
│ Bild 1 │ Bild 2 │ Bild 3 │
├──────────┼──────────┼──────────┤
│  🖼️    │  🖼️    │  🖼️    │
│ Bild 4 │ Bild 5 │ Bild 6 │
└──────────┴──────────┴──────────┘
```

### Masonry (Unregelmäßig)

```
┌──────────┬──────────┐
│  🖼️    │  🖼️    │
│ Bild 1 │ Bild 2 │
│        │        │
│        │        │
├──────────┼──────────┤
│  🖼️    │  🖼️    │
│ Bild 3 │ Bild 4 │
│        │        │
│        │        │
│        └──────────┤
│        │  🖼️    │
│        │ Bild 5 │
└──────────┴──────────┘
```

### Zeile

```
┌────────┬────────┬────────┬────────┐
│  🖼️  │  🖼️  │  🖼️  │  🖼️ ▶ │
└────────┴────────┴────────┴────────┘
```

Die Abfolge einzelner Bilder übernimmt [carousel](../carousel/).

### Lightbox (Großansicht)

```
┌─────────────────────────────────────┐
│ [✕]                                 │
│                                     │
│        🖼️                          │
│                                     │
│   [◀]          [▶]                  │
│                                     │
└─────────────────────────────────────┘
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Thumbnail | 100px | Listen, Grids |
| Small | 200px | Cards, kleine Galerien |
| Medium | 400px | Standard-Galerien |
| Large | 600px | Featured-Galerien |
| Full | 800px+ | Hero-Galerien |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Kachel ohne Rand, Bild füllt die Zelle |
| `hover` | leichter Zoom, halbtransparente Leiste mit Aktionen |
| `selected` | 2 px Rand in Primärfarbe |
| `geöffnet` | Hintergrund abdunkeln, Bild zentriert in der Lightbox |
| `geladen` | Platzhalter (`skeleton`), bis das Bild da ist |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich (1.1x) |
| `overlay` | Overlay mit Info/Icons |
| `border` | Rand leuchtet auf |
| `scale` | Bild skaliert leicht |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Galerie mit Navigation |
| Tablet (480-768px) | 2 Spalten, kompakt |
| Mobile (<480px) | 1 Spalte, Carousel |

## Overlay-Styling

```
┌────────────────────────┐
│  🖼️                  │
│  overlay             │
│  [🔍] [ℹ️] [❤️]       │
└────────────────────────┘
```

## Navigation-Buttons

| Button | Icon | Funktion |
|--------|------|----------|
| Prev | ⏮️ | Vorheriges Bild |
| Next | ⏭️ | Nächstes Bild |
| Close | ✕ | Galerie schließen |
| Fullscreen | ⛶ | Vollbild |
| Share | 🔗 | Teilen |
