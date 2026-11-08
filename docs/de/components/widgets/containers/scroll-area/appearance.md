# Scroll Area - Erscheinungsbild

## Grundlayout

```
┌──────────────────────────────┐
│ Inhaltszeile 1               │
│ Inhaltszeile 2               │
│ Inhaltszeile 3               │
│ ⋮        ▮                   │  Scrollbalken rechts, blendet im Ruhezustand aus
│ Inhaltszeile n        ▮      │
└──────────────────────────────┘
   Verlauf oben und unten, wenn mehr vorhanden ist
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **vertikal** | Scrollbalken rechts, Verläufe oben und unten |
| **horizontal** | Scrollbalken unten, Verläufe links und rechts |
| **beides** | beide Scrollbalken, die Ecke bleibt frei |

## Größen

| Größe | Breite des Scrollbalkens | Verlauf |
|-------|--------------------------|---------|
| `small` | 6 px | 12 px |
| `medium` | 8 px | 20 px |
| `large` | 12 px | 28 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Scrollbalken verborgen, Verlauf nur bei Bedarf |
| `hover` | Scrollbalken erscheint in neutralem Grau |
| `dragging` | Scrollbalken dunkler, Breite +2 px |
| `atTop` / `atBottom` | der Verlauf auf dieser Seite verschwindet |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `fade` | Verläufe am Rand zeigen, dass mehr Inhalt folgt |
| `ring` | Fokusring, wenn der Bereich per Tastatur bedient werden kann |

## Responsiv

- Auf Touchgeräten erscheint der Scrollbalken nie. Gescrollt wird per Geste.
- Bei reduzierter Bewegung entfallen Verläufe und sanftes Nachziehen.
