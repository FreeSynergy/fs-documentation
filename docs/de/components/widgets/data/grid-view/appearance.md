# Grid View - Aussehen

## Grundlayout
Grid View ist eine Karten/Raster-Darstellung von Elementen.

```
┌──────────┬──────────┬──────────┐
│          │          │          │
│  Karte 1 │  Karte 2 │  Karte 3 │
│          │          │          │
├──────────┼──────────┼──────────┤
│          │          │          │
│  Karte 4 │  Karte 5 │  Karte 6 │
│          │          │          │
└──────────┴──────────┴──────────┘
```

## Varianten
| Variant | Beschreibung |
|---------|--------------|
| **Fixed Grid** | Feste Spaltenanzahl |
| **Responsive Grid** | Anpassbare Spalten |
| **Masonry Grid** | Unregelmäßige Karten |

| Spalten | Beschreibung |
|---------|--------------|
| **1** | Ein Spalte |
| **2** | Zwei Spalten |
| **3** | Drei Spalten |
| **4** | Vier Spalten |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Kleine Grids |
| Medium | 300px | Standard |
| Large | 400px | Große Grids |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Card** | Hell | Karten-Hintergrund |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktiver Karte |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `transform` | Leichte Hebung |
| `border` | Rand leuchtet auf |

## Reaktiv

- **Responsive Grid** rechnet mit Mindestkartenbreite: 3 Spalten ab 900 px, 2 ab 600 px,
  1 darunter; **Fixed Grid** behält die Spaltenzahl und skaliert die Karten.
- **Masonry Grid** füllt die kürzeste Spalte; auf schmalen Bildschirmen wird sie einspaltig.
- Neue Karten erscheinen mit `stagger`, beim Umsortieren per `drag` wandern die Nachbarn
  in die Lücke (`reorder`).
