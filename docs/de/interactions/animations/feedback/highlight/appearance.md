# Highlight - Erscheinungsbild

## Grundaufbau

Ein rechteckiger farbiger Hintergrund liegt unter dem Inhalt und ändert nur seine Deckkraft.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        225 ms      450 ms      900 ms      │
│  [        ]  [░░░░░░░░]  [▓▓▓▓▓▓▓▓]  [░░░░░░░░]  │
│  0 %         50 %        100 %       20 %        │
│  normal      Anstieg     Maximum     Abklingen   │
│                                                  │
│  die Fläche leuchtet auf, die Position bleibt    │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Hintergrund** | `modus: background` – der Standard für gefundene Stellen |
| **Umriss** | `modus: outline` – nur die Kontur leuchtet |
| **Zweimal** | `iterationCount: 2` – zwei kurze Impulse |
| **Abklingend** | `anstiegAnteil` klein, eine lange Abklingphase |
| **Dauerhaft** | `fillMode: forwards` – bleibt markiert (z. B. eine Auswahl) |

## Dauer

- Typisch: 900 ms (Bereich 600–1200 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Ripple](../ripple/description.md)
- [Pulse](../../loop/pulse/description.md)
