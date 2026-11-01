# Badge (Abzeichen) - Aussehen

## Grundlayout

```
┌────────┐   ┌────────┐   ●   ┌╌╌╌╌╌╌╌┐
│  offen │   │   12   │       │ offen  │
└────────┘   └────────┘       └╌╌╌╌╌╌╌┘
   status      counter        dot      outline
```

An einem Element (Zähler über einem Icon):

```
        ┌───┐
        │ 3 │
   ┌────╨───┘
   │  ✉
   └────
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **status** | Fläche mit Statusfarbe, dunkler oder heller Text je nach Farbe |
| **counter** | abgerundete Fläche, Ziffern, min. Höhe wie Schriftgröße |
| **dot** | 8 px Kreis in Statusfarbe |
| **outline** | 1 px Rahmen in Statusfarbe, transparenter Grund |

## Größen

| Größe | Höhe | Schrift |
|-------|------|---------|
| `small` | 16 px | 10 px |
| `medium` | 20 px | 12 px |
| `large` | 24 px | 14 px |

Der `dot` wächst nicht mit: er bleibt 8 px (small/medium) bzw. 10 px (large).

## Farben und Zustände

| Status | Farbe |
|--------|-------|
| `neutral` | grau |
| `info` | Primärfarbe |
| `success` | grün |
| `warning` | orange |
| `error` | rot |

Badges sind reine Anzeige: sie haben keine Hover- und Zustandswechsel außer
einer kurzen Ein-/Ausblend-Animation, wenn sich der Wert ändert.

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tooltip` | optional Kurzerklärung des Status (siehe [tooltip](../../overlays/tooltip/)) |
| – | eigener Hover ist nicht vorgesehen |

## Reaktiv

- Auf schmalen Bildschirmen wird ein Zähler-Badge am Navigationspunkt durch ein
  `dot` ersetzt, wenn der Zahlenwert nicht mehr lesbar ist.
