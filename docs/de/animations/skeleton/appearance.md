# Skeleton - Aussehen

## Grundlayout

Graue Platzhalterformen (Balken, Kreise, Blöcke) in den Maßen des späteren Inhalts, über die im Loop ein heller Schimmer wandert.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Zyklus 1          Zyklus 2          Zyklus 3          │
│                                                      │
│(●) ▓▓▒▒▒▒▒▒     (●) ▒▓▓▓▒▒▒▒     (●) ▒▒▒▒▒▓▓▓        │
│    ▓▓▓▒▒▒▒         ▒▒▓▓▒▒▒▒         ▒▒▓▓▓▒▒▒         │
│                                                      │
│▓ = Schimmer   ▒ = Grundfläche   ● = Avatar           │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Zeilen** | Textzeilen unterschiedlicher Breite |
| **Liste** | Avatar-Kreis plus zwei Textbalken pro Zeile |
| **Karte** | Bildblock, Titelzeile und zwei Textzeilen |
| **Tabelle** | Kopfzeile plus gleichmäßige Datenzeilen |
| **Statisch** | ohne Schimmer, nur graue Formen (reduced motion) |

## Dauer

- Typisch: 1200–1800 ms pro Zyklus

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Progress](../progress/description.md)
- [Listen-Komponenten](../../components/lists/index.md)
