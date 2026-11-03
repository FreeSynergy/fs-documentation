# Dots - Aussehen

## Grundlayout

Drei gleich große Punkte stehen in einer Zeile auf einer Grundlinie und bewegen sich zeitversetzt. Der Indikator ist so hoch wie die umgebende Textzeile und stört den Zeilenfluss nicht.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        200 ms       400 ms       600 ms    │
│                                                  │
│    •           •            •           •        │
│   • •         • •          • ••        • • •     │
│  (ruhig)     P1 hebt     P2 hebt     P3 hebt     │
│                                                  │
│  ein Zyklus = 1400 ms, danach von vorn           │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Heben** | `modus: bounce` – Punkte steigen über die Grundlinie (Standard) |
| **Blinken** | `modus: fade` – Punkte wechseln die Deckkraft, keine Bewegung |
| **Wachsen** | `modus: scale` – Punkte werden größer und kleiner |
| **Zwei Punkte** | `anzahl: 2` für sehr schmale Plätze (Buttons mit Icon) |

## Dauer

- Typisch: 1200–1600 ms pro Zyklus
- Standardwert: 1400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Typing](../typing/description.md)
- [Skeleton](../skeleton/description.md)
- [Progress](../progress/description.md)
