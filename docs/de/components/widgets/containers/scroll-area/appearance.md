# Scroll Area (Laufbereich) - Aussehen

## Grundlayout

```
┌──────────────────────────────┐
│ Inhalt Zeile 1               │
│ Inhalt Zeile 2               │
│ Inhalt Zeile 3               │
│ ⋮        ▮                   │  Leiste rechts, blendet bei Ruhe aus
│ Inhalt Zeile n        ▮      │
└──────────────────────────────┘
   Verlauf oben und unten, wenn es weitergeht
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **vertikal** | Leiste rechts, Verläufe oben und unten |
| **horizontal** | Leiste unten, Verläufe links und rechts |
| **beides** | beide Leisten, Ecken ausgespart |

## Größen

| Größe | Leistenbreite | Verlauf |
|-------|---------------|---------|
| `small` | 6 px | 12 px |
| `medium` | 8 px | 20 px |
| `large` | 12 px | 28 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Leiste ausgeblendet, Verlauf nur bei Bedarf |
| `hover` | Leiste erscheint in neutralem Grauton |
| `dragging` | Leiste dunkler, Breite +2 px |
| `atTop` / `atBottom` | Verlauf der betreffenden Seite verschwindet |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `fade` | Verläufe an den Rändern signalisieren weiteren Inhalt |
| `ring` | Fokus-Ring, wenn der Bereich über Tastatur bedienbar ist |

## Reaktiv

- Auf Touch-Geräten erscheint die Leiste nie; gelaufen wird per Geste.
- Bei reduced Motion entfallen Verläufe und sanftes Nachziehen.
