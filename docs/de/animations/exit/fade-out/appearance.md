# Fade Out - Aussehen

## Grundlayout

Das Element bleibt an seiner Layout-Position und wird nur über die Deckkraft unsichtbar – eine Layout-Verschiebung findet nicht statt.

## Visueller Verlauf

```
┌────────────────────────────────────────────┐
│   0 ms            100 ms          200 ms   │
│                                            │
│   [Titel]         ░░ Titel ░░  (unsichtbar) │
│   α = 1           α = 0.5        α = 0     │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Weich ausblenden, Element bleibt im DOM |
| **Fast** | 100–150ms für Mikro-Feedback und kleine Elemente |
| **With Remove** | Nach dem Ausblenden aus dem DOM entfernen (`removeOnEnd`) |
| **Blur Fade** | Mit zunehmendem Weichzeichner beim Ausblenden |

## Dauer

- Typisch: 150–300ms
- Standardwert: 200ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Fade In](../../entrance/fade-in/description.md)
- [Zoom Out](../zoom-out/description.md)
