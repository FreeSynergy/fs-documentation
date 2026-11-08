# Badge - Erscheinungsbild

## Grundlayout

```
┌────────┐   ┌────────┐   ●   ┌╌╌╌╌╌╌╌┐
│  offen │   │   12   │       │  offen │
└────────┘   └────────┘       └╌╌╌╌╌╌╌┘
   Status      Zähler        Punkt    Umriss
```

Auf einem Element (eine Zahl über einem Icon):

```
        ┌───┐
        │ 3 │
   ┌────╨───┘
   │  ✉
   └────
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **status** | Fläche in der Statusfarbe, dunkler oder heller Text je nach Farbe |
| **counter** | abgerundete Fläche mit Ziffern, Mindesthöhe gleich der Schriftgröße |
| **dot** | Kreis mit 8 px in der Statusfarbe |
| **outline** | 1 px Rahmen in der Statusfarbe, transparenter Hintergrund |

## Größen

| Größe | Höhe | Schrift |
|-------|------|---------|
| `small` | 16 px | 10 px |
| `medium` | 20 px | 12 px |
| `large` | 24 px | 14 px |

Der `dot` wächst nicht mit. Er bleibt bei 8 px (small/medium) bzw. 10 px (large).

## Farben und Zustände

| Status | Farbe |
|--------|-------|
| `neutral` | grau |
| `info` | Primärfarbe |
| `success` | grün |
| `warning` | orange |
| `error` | rot |

Badges dienen nur der Anzeige. Abgesehen von einer kurzen Ein- und Ausblendanimation,
wenn sich der Wert ändert, gibt es keine Hover- oder Zustandsänderungen.

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | optionale kurze Erklärung des Status (siehe [tooltip](../../../widgets/overlays/tooltip/)) |
| – | ein eigener Hover ist nicht vorgesehen |

## Responsiv

- Auf schmalen Bildschirmen wird ein Zähler-Badge an einem Navigationspunkt durch einen
  `dot` ersetzt, wenn die Zahl nicht mehr lesbar ist.
