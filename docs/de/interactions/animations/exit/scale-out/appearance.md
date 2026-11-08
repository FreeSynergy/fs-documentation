# Scale Out - Erscheinungsbild

## Grundaufbau

Das Element behält seinen Mittelpunkt und zieht sich auf einen einzigen Punkt zusammen.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  0 ms     60 ms   120 ms    180 ms               │
│                                                  │
│  [────────] [─────] [─]     ·                    │
│  100 %      70 %    35 %    0 %                  │
│                                                  │
│  Schrumpfpunkt erreicht, der Platz wird frei     │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Mitte** | Schrumpfpunkt in der Mitte des Elements (Standard) |
| **Zum Auslöser** | schrumpft zum Warenkorb-, X- oder Menüknopf hin |
| **Mit Fade** | die Deckkraft sinkt mit, verhindert harte Kanten |
| **Nur Breite** | `axis: x` – fällt seitlich zusammen |
| **Platz bleibt** | `removeAfter: false` – der Platz bleibt reserviert |

## Dauer

- Typisch: 180 ms (Bereich 120–250 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Scale In](../../entrance/scale-in/description.md)
- [Collapse](../collapse/description.md)
