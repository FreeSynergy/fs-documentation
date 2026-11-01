# Field (Feld-Wrapper) - Aussehen

## Grundlayout

```
vertikal:                     horizontal:

Benutzername *                Benutzername *
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
└────────────────────────┘    └────────────────────────┘
Melde dich mit deiner          (Feld rechts vom Label)
E-Mail-Adresse an
```

Fehlerzustand:

```
E-Mail *
┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
│ ✕  fehlerhafte@doma   │
└╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
⚠ Diese E-Mail ist nicht gültig.
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **vertikal** | Label über dem Feld, Hilfetext unter dem Feld |
| **horizontal** | Label mit fester Breite links, Feld rechts |
| **inline** | Label und Feld in einer Zeile, kein Hilfetext |

## Größen

| Größe | Label-Schrift | Hilfetext |
|-------|---------------|-----------|
| `small` | 12 px | 11 px |
| `medium` | 14 px | 12 px |
| `large` | 16 px | 14 px |

Das umschlossene Feld behält seine eigene Größe.

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Label | Primärtext |
| Pflicht-Markierung `*` | Fehlerfarbe |
| Hilfetext | Sekundärtext |
| Fehlerzustand | Feldrand und Text in Fehlerfarbe |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `expand` | Hilfetext/Fehler blendet ein, der Block wächst sauber nach |
| – | Hover gehört zum Feld, nicht zum Wrapper |

## Reaktiv

- Unterhalb einer schmalen Breite wechselt `horizontal` automatisch auf
  `vertikal`.
