# Label (Beschriftung) - Aussehen

## Grundlayout

```
ueber-feld:        inline:            versteckt:

Benutzername       Benutzername ─┐    (kein sichtbarer Text,
┌──────────────┐   ┌─────────────┴──┐  aber als Text vorhanden)
│              │   │                │
└──────────────┘   └────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **ueber-feld** | Text über dem Element, Abstand 4–6 px |
| **inline** | Text links, an der Grundlinie des Elements ausgerichtet |
| **versteckt** | unsichtbar (1 px, Clip), im Lesefluss erhalten |
| **pflicht** | Zusatz „*“ in Fehlerfarbe plus Text „erforderlich“ |

## Größen

| Größe | Schrift |
|-------|---------|
| `small` | 12 px |
| `medium` | 14 px |
| `large` | 16 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Text | Primärtext |
| deaktivierte Beziehung | Sekundärtext, 60 % Deckkraft |
| Pflicht-Markierung | Fehlerfarbe |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| – | das Label selbst reagiert nicht; Klick auf das Label fokussiert das Feld |

## Reaktiv

- Zu lange Labels dürfen umbrechen; sie überdecken niemals das Feld.
