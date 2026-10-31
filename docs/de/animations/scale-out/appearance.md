# Scale Out - Aussehen

## Grundlayout

Das Element behält seinen Mittelpunkt und zieht sich bis auf einen Punkt zusammen.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms     60 ms   120 ms    180 ms               │
│                                                  │
│  [────────] [─────] [─]     ·                    │
│  100 %      70 %    35 %    0 %                  │
│                                                  │
│  Schrumpfpunkt erreicht, Slot wird freigegeben   │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Mitte** | Schrumpfpunkt in der Elementmitte (Standard) |
| **Zum Auslöser** | Schrumpft in Richtung Korb-, X- oder Menü-Button |
| **Plus Fade** | Deckkraft sinkt mit, verhindert harte Kanten |
| **Nur Breite** | `axis: x` - kollabiert seitlich |
| **Platz bleibt** | `removeAfter: false` - Slot bleibt reserviert |

## Dauer

- Typisch: 180 ms (Bereich 120–250 ms)

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Scale In](../scale-in/description.md)
- [Collapse](../collapse/description.md)
