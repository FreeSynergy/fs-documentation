# Gallery - Erscheinungsbild

## Grundlayout

Galerien zeigen Bilder in verschiedenen Anordnungen: als Raster, Carousel oder Kachelansicht.

## Varianten

### Raster (`raster`)

```
┌──────────┬──────────┬──────────┐
│  🖼️    │  🖼️    │  🖼️    │
│ Bild 1 │ Bild 2 │ Bild 3 │
├──────────┼──────────┼──────────┤
│  🖼️    │  🖼️    │  🖼️    │
│ Bild 4 │ Bild 5 │ Bild 6 │
└──────────┴──────────┴──────────┘
```

### Masonry (unregelmäßig)

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

### Zeile (`zeile`)

```
┌────────┬────────┬────────┬────────┐
│  🖼️  │  🖼️  │  🖼️  │  🖼️ ▶ │
└────────┴────────┴────────┴────────┘
```

Die Abfolge einzelner Bilder übernimmt der [carousel](../carousel/).

### Lightbox (große Ansicht)

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
| Thumbnail | 100px | Listen, Raster |
| Small | 200px | Karten, kleine Galerien |
| Medium | 400px | Standard-Galerien |
| Large | 600px | hervorgehobene Galerien |
| Full | 800px+ | Galerien als Blickfang |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Kachel ohne Rand, das Bild füllt die Zelle |
| `hover` | leichte Vergrößerung, eine halbtransparente Leiste mit Aktionen |
| `selected` | 2 px Rand in der Primärfarbe |
| `geöffnet` | Hintergrund abdunkeln, Bild in der Lightbox zentriert |
| `geladen` | Platzhalter (`skeleton`), bis das Bild da ist |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Bild wird größer (1,1-fach) |
| `overlay` | Overlay mit Informationen/Icons |
| `border` | der Rand leuchtet auf |
| `scale` | das Bild skaliert leicht |

## Responsiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | volle Galerie mit Navigation |
| Tablet (480–768px) | 2 Spalten, kompakt |
| Mobil (<480px) | 1 Spalte, Carousel |

## Gestaltung des Overlays

```
┌────────────────────────┐
│  🖼️                  │
│  Overlay             │
│  [🔍] [ℹ️] [❤️]       │
└────────────────────────┘
```

## Navigationsknöpfe

| Knopf | Icon | Funktion |
|-------|------|----------|
| Zurück | ⏮️ | vorheriges Bild |
| Weiter | ⏭️ | nächstes Bild |
| Schließen | ✕ | Galerie schließen |
| Vollbild | ⛶ | Vollbild |
| Teilen | 🔗 | teilen |
