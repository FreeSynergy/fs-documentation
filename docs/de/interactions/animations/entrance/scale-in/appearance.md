# Scale In - Aussehen

## Grundlayout

Das Element bleibt an seiner Position verankert und füllt seinen Layoutplatz von einem einzigen Punkt aus nach außen.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms     70 ms   140 ms    200 ms               │
│                                                  │
│  ·        [───]   [──────]  [────────]           │
│  0 %      35 %    70 %      100 %                │
│                                                  │
│  fester Mittelpunkt, Breite und Höhe wachsen     │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Mitte** | Wachstumspunkt in der Mitte des Elements (Standard) |
| **Auslöser** | Wachstumspunkt am Button; das Menü scheint daraus zu wachsen |
| **Nur Breite** | `axis: x` – die Höhe bleibt derweil gleich |
| **Nur Höhe** | `axis: y` – die Breite bleibt derweil gleich |
| **Mit Einblenden** | die Deckkraft steigt parallel, wirkt weicher |

## Dauer

- Typisch: 200 ms (Bereich 150–300 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Scale Out](../../exit/scale-out/description.md)
- [Expand](../expand/description.md)
