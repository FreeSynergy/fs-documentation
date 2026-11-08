# Cross Fade - Aussehen

## Grundlayout

Zwei Elemente liegen genau übereinander. Die Deckkraft des einen sinkt, während die des anderen steigt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│A 100 %      A/B 70/30     A/B 25/75      B 100 %     │
│                                                      │
│██████       ███▒▒▒▒▒      ▒▒▒▒░░░░       ░░░░░░      │
│                                                      │
│A = altes Element, B = neues; Gesamtdeckkraft ≈ 100 % │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Gleichzeitig** | beide blenden gleichzeitig über (Standard) |
| **Versetzt** | `overlap: 0`, erst ausblenden, dann einblenden |
| **Mit Zoom** | das neue Element skaliert leicht mit (`skalaMit`) |
| **Kurz** | 150–200 ms für Icons und Statusanzeigen |
| **Hart** | ein sofortiger Tausch (reduzierte Bewegung) |

## Dauer

- Typisch: 250–500 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Morph](../morph/description.md)
- [Parallax](../../movement/parallax/description.md)
