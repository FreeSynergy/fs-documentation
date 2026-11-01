# Range Calendar (Bereichskalender) - Aussehen

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

| Variante | Aussehen |
|----------|----------|
| **zwei-monate** | zwei Raster nebeneinander, Trennlinie dazwischen |
| **ein-monat** | ein Raster, Monatswechsel seitlich |

## Größen

| Größe | Tagfläche | Breite |
|-------|-----------|--------|
| `small` | 28 px | 520 px |
| `medium` | 36 px | 660 px |
| `large` | 44 px | 800 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Tage neutral |
| `selecting` | Bereich vom Beginn bis zum Zeiger hell unterlegt |
| `active` | Beginn und Ende gefüllt, Mitte hell |
| `outOfRange` | Tage außerhalb von `min`/`max` ausgegraut |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `bridge` | zusammenhängende Fläche über beide Monate hinweg |
| `ring` | Fokusring auf Beginn und Ende |

## Reaktiv

- Unter 700 px Breite auf `ein-monat` umschalten.
- Monatswechsel per Wischgeste, ohne Knöpfe.
