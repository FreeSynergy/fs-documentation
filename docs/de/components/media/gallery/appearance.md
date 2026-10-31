# Gallery - Aussehen

## Grundlayout

Galerien zeigen Bilder in verschiedenen Layouts an: Raster, Karussell oder Kachelansicht.

## Layout-Varianten

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

### Carousel (Slideshow)
```
┌─────────────────────────────────────┐
│ [◀]   🖼️   [▶]                     │
│          Bild 1                     │
└─────────────────────────────────────┘
```

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

## Größe-Varianten

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Thumbnail | 100px | Listen, Grids |
| Small | 200px | Cards, kleine Galerien |
| Medium | 400px | Standard-Galerien |
| Large | 600px | Featured-Galerien |
| Full | 800px+ | Hero-Galerien |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich (1.1x) |
| `overlay` | Overlay mit Info/Icons |
| `border` | Rand leuchtet auf |
| `scale` | Bild skaliert leicht |

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

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Galerie mit Navigation |
| Tablet (480-768px) | 2 Spalten, kompakt |
| Mobile (<480px) | 1 Spalte, Carousel |
