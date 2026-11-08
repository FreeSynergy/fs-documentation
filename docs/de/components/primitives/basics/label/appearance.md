# Label – Erscheinungsbild

## Grundlayout

```
ueber-feld:        inline:            versteckt:

Username           Username ─┐        (kein sichtbarer Text,
┌──────────────┐   ┌─────────────┴──┐  aber als Text vorhanden)
│              │   │                │
└──────────────┘   └────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **ueber-feld** | Text über dem Element, Abstand 4–6 px |
| **inline** | Text links, an der Grundlinie des Elements ausgerichtet |
| **versteckt** | unsichtbar (1 px, abgeschnitten), bleibt im Lesefluss erhalten |
| **pflicht** | zusätzliches „*“ in der Fehlerfarbe plus der Text „Pflichtfeld“ |

## Größen

| Größe | Schrift |
|------|------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 16 px |

## Farben und Zustände

| Teil | Farbe |
|------|------|
| Text | Primärtext |
| deaktivierte Beziehung | Sekundärtext, 60 % Deckkraft |
| Pflichtkennzeichnung | Fehlerfarbe |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| – | das Label selbst reagiert nicht; ein Klick auf das Label fokussiert das Feld |

## Responsiv

- Zu lange Labels dürfen umbrechen; sie überdecken nie das Feld.
