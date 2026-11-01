# Collapse - Aussehen

## Grundlayout

Der obere Rand bleibt stehen, die Unterkante wandert nach oben, bis nur noch eine Linie übrig ist.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms            125 ms          250 ms          │
│  ┌────────┐      ┌────────┐      ┌────────┐      │
│  ░░░░░░░░░░      ░░░░░░░░░░      └────────┘      │
│  ░░░░░░░░░░      └────────┘      Höhe = 0        │
│  └────────┘      Höhe 50 %       untere Zeilen   │
│  Höhe 100 %                      rücken nach     │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vertikal** | `dimension: height` - Standard bei Akkordeons |
| **Horizontal** | `dimension: width` - Seitenleiste zieht nach links ein |
| **Beides** | `dimension: both` - Panel schrumpft in beide Richtungen |
| **Gestaffelt** | `staggerChildren` - Kindzeilen nacheinander |
| **Mit Fade** | Inhalt wird zusätzlich ausgedünnt, weicherer Übergang |

## Dauer

- Typisch: 250 ms (Bereich 200–350 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Expand](../../entrance/expand/description.md)
- [Scale Out](../scale-out/description.md)
