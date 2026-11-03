# Cross Fade - Aussehen

## Grundlayout

Zwei Elemente liegen exakt übereinander; die Deckkraft des einen sinkt, während die des anderen steigt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│A 100 %      A/B 70/30     A/B 25/75      B 100 %     │
│                                                      │
│██████       ███▒▒▒▒▒      ▒▒▒▒░░░░       ░░░░░░      │
│                                                      │
│A = altes Element, B = neues; Deckkraft gesamt ≈ 100 %│
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Simultan** | beide überblenden gleichzeitig (Standard) |
| **Versetzt** | `overlap: 0`, erst aus-, dann einblenden |
| **Mit Zoom** | neues Element skaliert leicht mit (`skalaMit`) |
| **Kurz** | 150–200 ms für Icons und Statusanzeigen |
| **Hart** | sofortiger Tausch (reduced motion) |

## Dauer

- Typisch: 250–500 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Morph](../morph/description.md)
- [Parallax](../../movement/parallax/description.md)
