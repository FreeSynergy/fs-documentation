# Highlight - Aussehen

## Grundlayout

Ein rechteckiger Farbhintergrund liegt unter dem Inhalt und ändert nur seine Deckkraft.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        225 ms      450 ms      900 ms      │
│  [        ]  [░░░░░░░░]  [▓▓▓▓▓▓▓▓]  [░░░░░░░░]  │
│  0 %         50 %        100 %       20 %        │
│  normal      Anstieg     Maximum     Abklang     │
│                                                  │
│  Fläche leuchtet auf, Position bleibt gleich     │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Hintergrund** | `modus: background` - Standard für Fundstellen |
| **Rahmen** | `modus: outline` - nur die Kontur leuchtet |
| **Doppelt** | `iterationCount: 2` - zwei kurze Pulse |
| **Ausklingend** | `anstiegAnteil` klein, lange Abklingphase |
| **Dauerhaft** | `fillMode: forwards` - bleibt markiert (z. B. Auswahl) |

## Dauer

- Typisch: 900 ms (Bereich 600–1200 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Ripple](../ripple/description.md)
- [Pulse](../../loop/pulse/description.md)
