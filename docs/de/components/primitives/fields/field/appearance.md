# Feld – Erscheinungsbild

## Grundlayout

```
vertikal:                     horizontal:

Username *                    Username *
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
└────────────────────────┘    └────────────────────────┘
Mit deiner E-Mail-Adresse     (Feld rechts neben dem Label)
anmelden
```

Fehlerzustand:

```
Email *
┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
│ ✕  broken@doma.in     │
└╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
⚠ Diese E-Mail-Adresse ist ungültig.
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **vertikal** | Label über dem Feld, Hilfetext unter dem Feld |
| **horizontal** | Label mit fester Breite links, Feld rechts |
| **inline** | Label und Feld in einer Zeile, kein Hilfetext |

## Größen

| Größe | Label-Schrift | Hilfetext |
|------|------------|-----------|
| `small` | 12 px | 11 px |
| `medium` | 14 px | 12 px |
| `large` | 16 px | 14 px |

Das eingeschlossene Feld behält seine eigene Größe.

## Farben und Zustände

| Teil | Farbe |
|------|------|
| Label | Primärtext |
| Pflichtkennzeichnung `*` | Fehlerfarbe |
| Hilfetext | Sekundärtext |
| Fehlerzustand | Feldrahmen und Text in der Fehlerfarbe |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `expand` | Hilfetext/Fehler blendet ein, der Block wächst sauber nach unten |
| – | Hover gehört zum Feld, nicht zur Hülle |

## Responsiv

- Unterhalb einer schmalen Breite wechselt `horizontal` automatisch zu `vertikal`.
