# Range Calendar - Erscheinungsbild

## Grundlayout

```
┌──────────────────────────┬──────────────────────────┐
│  ‹  Oktober 2026         │  November 2026        ›  │
│  Mo Di Mi Do Fr Sa So    │  Mo Di Mi Do Fr Sa So    │
│      1  2  3  4          │              1  2        │
│  5 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     │       ▓▓▓ 7              │
├──────────────────────────┴──────────────────────────┤
│  14 Tage   ·   Heute · 7 Tage · 30 Tage · Quartal   │
└─────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **zwei-monate** | zwei Raster nebeneinander, ein Trenner dazwischen |
| **ein-monat** | ein Raster, Monatswechsel gleitet seitlich |

## Größen

| Größe | Tagesfläche | Breite |
|-------|-------------|--------|
| `small` | 28 px | 520 px |
| `medium` | 36 px | 660 px |
| `large` | 44 px | 800 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Tage neutral |
| `selecting` | der Bereich vom Anfang bis zum Zeiger leicht getönt |
| `active` | Anfang und Ende gefüllt, die Mitte hell |
| `outOfRange` | Tage außerhalb von `min`/`max` ausgegraut |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `bridge` | eine zusammenhängende Fläche über beide Monate |
| `ring` | Fokusring auf Anfang und Ende |

## Responsiv

- Unter 700 px Breite auf `ein-monat` wechseln.
- Monatswechsel per Wischgeste, ohne Schaltflächen.
