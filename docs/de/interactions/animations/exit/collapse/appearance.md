# Collapse - Aussehen

## Grundlayout

Die obere Kante bleibt stehen. Die untere Kante wandert nach oben, bis nur noch eine Linie übrig ist.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms            125 ms          250 ms          │
│  ┌────────┐      ┌────────┐      ┌────────┐      │
│  ░░░░░░░░░░      ░░░░░░░░░░      └────────┘      │
│  ░░░░░░░░░░      └────────┘      Höhe = 0       │
│  └────────┘      Höhe 50 %       untere Zeilen   │
│  Höhe 100 %                      rücken nach oben│
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vertikal** | `dimension: height` – der Standard für Akkordeons |
| **Horizontal** | `dimension: width` – die Seitenleiste fährt nach links zurück |
| **Beides** | `dimension: both` – das Panel schrumpft in beide Richtungen |
| **Versetzt** | `staggerChildren` – Kindzeilen nacheinander |
| **Mit Einblenden** | der Inhalt wird zusätzlich ausgeblendet, ein weicherer Übergang |

## Dauer

- Typisch: 250 ms (Bereich 200–350 ms)

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Expand](../../entrance/expand/description.md)
- [Scale Out](../scale-out/description.md)
