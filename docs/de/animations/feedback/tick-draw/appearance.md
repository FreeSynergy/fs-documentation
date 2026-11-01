# Tick Draw - Aussehen

## Grundlayout

Der Haken sitzt in einer vorbereiteten Fläche (Kreis oder Kästchen) und wird als durchgehender Strich aufgebaut: erst der kurze nach unten führende Schenkel, dann der lange nach oben rechts. Die Dicke bleibt während des Zeichnens gleich.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms        150 ms        320 ms        550 ms      │
│                                                      │
│   ( )         ( )          ( /          ( ✓ )        │
│  leer      Kreis sichtbar  Schenkel     fertig      │
│             α = 1          wird gezeichnet           │
│                                                      │
│  Kreis: 200 ms  ·  Strich: 400 ms, von links nach    │
│  rechts oben, ohne abzusetzen                        │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Kreis erscheint, dann Haken in 400 ms |
| **Nur Strich** | `hintergrund: none` – Haken zeichnet sich direkt auf der Fläche |
| **Kasten** | `hintergrund: flaeche` – passt zu Kontrollkästchen |
| **Betont** | `nachziehen: 1.5` – Strich schießt am Ende minimal über das Ziel |

## Dauer

- Typisch: 300–500 ms für den Strich, plus 150–250 ms Vorlauf
- Standardwert: 400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Ripple](../ripple/description.md)
- [Highlight](../highlight/description.md)
- [Checkbox](../../../components/fields/checkbox/description.md)
