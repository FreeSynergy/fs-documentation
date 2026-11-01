# Input Group (Feldgruppe) - Aussehen

## Grundlayout

```
praefix:                 suffix:
┌────┬──────────────┐    ┌──────────────┬────┐
│ €  │              │    │              │ kg │
└────┴──────────────┘    └──────────────┴────┘

mit Action-Button:
┌──────────────────────┬─────┐
│  such…               │ 🔍  │
└──────────────────────┴─────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **praefix** | Element links, gleiche Höhe und Fläche wie das Feld, innere Kante gerade |
| **suffix** | Element rechts, analog |
| **beides** | beide Seiten, Feld in der Mitte |

## Größen

Es gilt das Größen-Raster der Basiskomponente; alle Elemente der Gruppe haben
dieselbe Höhe (28/36/44 px).

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Gruppe wie ein Feld, Elemente auf Feldfläche |
| `focus` | gemeinsamer Fokus-Ring um die ganze Gruppe |
| `disabled` | gesamte Gruppe 40 % Deckkraft |
| `error` | Rand der gesamten Gruppe in Fehlerfarbe |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | ein Ring für die Gruppe, nicht pro Element |
| `tone` | interaktive Elemente (Button/Select) wie Einzelkomponenten |

## Reaktiv

- Auf schmalen Bildschirmen kann das Präfix über dem Feld gesetzt werden
  (z. B. Ländercode), die Gruppe bleibt eine Bedieneinheit.
