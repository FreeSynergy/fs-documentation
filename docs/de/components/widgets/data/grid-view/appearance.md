# Grid View - Erscheinungsbild

## Grundlayout
Eine Grid View ist eine Karten- bzw. Rasteransicht von Elementen.

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
| Variante | Beschreibung |
|----------|--------------|
| **Fixed Grid** | feste Anzahl an Spalten |
| **Responsive Grid** | anpassbare Spalten |
| **Masonry Grid** | unregelmäßige Karten |

| Spalten | Beschreibung |
|---------|--------------|
| **1** | eine Spalte |
| **2** | zwei Spalten |
| **3** | drei Spalten |
| **4** | vier Spalten |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | kleine Raster |
| medium | 300px | Standard |
| large | 400px | große Raster |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Karte** | hell | Hintergrund der Karte |
| **Hover** | heller | Zustand beim Überfahren |
| **Aktiv** | Primärfarbe | aktive Karte |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | der Schatten wird stärker |
| `transform` | leichtes Anheben |
| `border` | der Rahmen leuchtet auf |

## Responsiv

- **Responsive Grid** rechnet mit einer minimalen Kartenbreite: 3 Spalten ab 900 px, 2 ab
  600 px, darunter 1; **Fixed Grid** behält die Anzahl der Spalten und skaliert die Karten.
- **Masonry Grid** füllt die kürzeste Spalte; auf schmalen Bildschirmen wird es eine Spalte.
- Neue Karten erscheinen mit `stagger`; beim Umsortieren per `drag` rücken die Nachbarn in die
  Lücke (`reorder`).
