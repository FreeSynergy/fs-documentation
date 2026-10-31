# Fade In - Aussehen

## Grundlayout

Das Element bleibt exakt an seiner Layout-Position und wird ausschließlich über die Deckkraft sichtbar – ohne Bewegung und ohne Größenänderung.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms            125 ms          250 ms   │
│                                            │
│  (unsichtbar)     ░░ Titel ░░     [Titel]  │
│    α = 0          α = 0.5         α = 1    │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Weich von 0 auf 1 geblendet (250ms) |
| **Fast** | 100–150ms für Hover, Tooltip, Mikro-Feedback |
| **Soft** | 350–400ms mit `ease-out` für Overlays und Modals |
| **Blur Fade** | Blende kombiniert mit abklingendem Weichzeichner |

## Dauer

- Typisch: 150–400ms
- Standardwert: 250ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Fade Out](../fade-out/description.md)
- [Slide In](../slide-in/description.md)
