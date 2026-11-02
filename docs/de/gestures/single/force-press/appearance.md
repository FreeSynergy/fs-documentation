# Force Press - Aussehen

## Grundlayout

Das Element sinkt beim Drücken ein; ab der Peek-Stufe erscheint eine
Vorschau-Karte über dem Element, der Hintergrund dunkelt ab.

```
┌─────────────────────────────────────────┐
│  ┌─────────────┐                        │
│  │  Pop: offen │      ┌───────────┐     │
│  └─────────────┘      │ Peek:     │     │
│        ▲              │ Vorschau  │     │
│   stärker drücken     └───────────┘     │
│  (Hintergrund gedimmt)                 │
└─────────────────────────────────────────┘
```

## Stufen-Feedback

| Stufe | Feedback |
|-------|----------|
| Light Press | Element sinkt 1–2px ein (press-Animation) |
| Peek | Vorschau-Karte wächst aus dem Element, Haptic Tick |
| Pop | Vorschau füllt den Rand, Inhalt dahinter skaliert zurück |

## Vorschau-Größen

| Größe | Anteil des Bildschirms | Verwendung |
|-------|------------------------|------------|
| Small | ~25% | Link-Vorschau, Kurzinfo |
| Large | ~66% | Artikelanriss, Medien-Vorschau |

## Dauer

- Einsinken: 100–150ms
- Peek-Öffnen: 200–300ms
- Pop-Übergang: 300–400ms

## Unterschied zu Long Press

- Force Press: Kraft sichtbar durch Stufen (sinkt ein, Vorschau, öffnet)
- Long Press: Zeit sichtbar durch Countdown/Rückkopplung erst am Ende
