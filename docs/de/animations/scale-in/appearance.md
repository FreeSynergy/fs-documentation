# Scale In - Aussehen

## Grundlayout

Das Element bleibt an seiner Position verankert und füllt seinen Layout-Slot von einem Punkt aus auf.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms     70 ms   140 ms    200 ms               │
│                                                  │
│  ·        [───]   [──────]  [────────]           │
│  0 %      35 %    70 %      100 %                │
│                                                  │
│  Fixer Mittelpunkt, Breite und Höhe wachsen      │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Mitte** | Wachstumspunkt in der Elementmitte (Standard) |
| **Auslöser** | Wachstumspunkt am Button; Menü scheint herauszuwachsen |
| **Nur Breite** | `axis: x` - Höhe bleibt währenddessen konstant |
| **Nur Höhe** | `axis: y` - Breite bleibt währenddessen konstant |
| **Plus Fade** | Deckkraft steigt parallel, wirkt weicher |

## Dauer

- Typisch: 200 ms (Bereich 150–300 ms)

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Scale Out](../scale-out/description.md)
- [Expand](../expand/description.md)
