# Bounce In - Aussehen

## Grundlayout

Das Element trifft von außen oder aus kleiner Skalierung ein, schießt über die Endposition hinaus und pendelt federnd zur Ruhe ein.

## Visueller Verlauf (Skalen-Bounce)

```
┌────────────────────────────────────────────┐
│   0 ms    [▫]          scale 0.5 (Einflug)  │
│ 220 ms    [██████]     scale 1.12 (drüber)  │
│ 360 ms    [████]       scale 0.94 (zurück)  │
│ 500 ms    [█████]      scale 1.00 (Ruhe)    │
└────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Pop** | Startet bei `startScale: 0` und poppt auf |
| **Drop** | Fällt von oben ein (`dropHeight` größer 0) und federt beim Aufprall |
| **Slide-Bounce** | Kommt von der Seite und federt in die Endposition |
| **Soft** | Nur 1 Rückfederung mit geringem Overshoot (6–8 %) |

## Dauer

- Typisch: 400–700 ms
- Standardwert: 500 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Bounce Out](../../exit/bounce-out/description.md)
- [Slide In](../slide-in/description.md)
