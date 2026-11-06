# HTML View (HTML-Ansicht) - Aussehen

## Grundlayout

```
┌─────────────────────────────────────────┐
│ ⓘ Remote content blocked  [ Load ]      │
├─────────────────────────────────────────┤
│ Heading                                 │
│ Body text with a [link]                 │
│ ▢ (blocked image)                       │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **sanitised** | inaktiver Inhalt, blockierte Bilder als Platzhalter |
| **remote-allowed** | wie zuvor, mit geladenen Bildern |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `medium` | auto | passt sich dem Inhalt an |
| `full` | 100% | Lesebereich |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Standard | an das Theme angepasst, Mailfarben begrenzt ⚠️ |
| Blockiert | Platzhalterrahmen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `underline` | Links unterstrichen |
| `tooltip` | tatsächliches Linkziel |

## Reaktiv

- Der Inhalt wird auf die Breite skaliert; breite Tabellen scrollen horizontal.
- Feste Pixelbreiten aus der Quelle werden nicht übernommen.
