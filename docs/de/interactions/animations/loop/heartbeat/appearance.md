# Heartbeat - Aussehen

## Grundlayout

Das Element steht still, macht zwei kurze Schläge und bleibt dann für den Rest des Zyklus unverändert.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  ein Zyklus = 1000 ms (72 bpm)                   │
│                                                  │
│  Zeit   0     100    170    240      1000 ms     │
│  Skala  1.00  1.12   1.05   1.09    1.00         │
│         ▁     ▆      ▃      ▅       ▁            │
│         lub   dub    - Ruhephase 450 ms -        │
│                                                  │
│  zwei Schläge pro Zyklus, danach Ruhe            │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | `lub-dub`, 72 bpm, zwei Spitzen mit einer Ruhephase |
| **Verstärkt** | `schlagSkala` 1.25 – ein deutlich sichtbarer Schlag |
| **Ruhig** | 55 bpm, kleine Amplitude für eine dauerhafte Live-Anzeige |
| **Hektisch** | 110 bpm, `pauseAnteil` 0.2 – ein Alarmcharakter |
| **Einmal** | `iterationCount: 1` bei der Bestätigung einer Aktion |

## Dauer

- Typisch: 1000 ms pro Zyklus (Bereich 700–1200 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Pulse](../pulse/description.md)
- [Ripple](../../feedback/ripple/description.md)
