# Rubber Band - Aussehen

## Grundlayout

Der Inhalt liegt plan an der Randkante; beim Ziehen über den Rand entsteht eine gedämpfte Lücke, die nach dem Loslassen wieder zuschnappt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Randlage          Auszug              Zurückfedern    │
│                                                      │
│[Inhalt·····]  ┈┈┈ Rand ┈┈┈       [Inhalt·····]       │
│[···········]  [   Lücke    ]     [···········]       │
│[····Ende···]  [ Inhalt···· ]     [····Ende···]       │
│[···········]  [ folgt Zug  ]     [···········]       │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Vertikal** | Standard für Listen und Artikel |
| **Horizontal** | seitenweise Karussells und Tabellen |
| **Einseitig** | nur oben (z. B. Start für Pull-to-Refresh) |
| **Zäh** | `widerstand: 0.15`, starker Gummiband-Widerstand |
| **Aus** | harte Ränder ohne Auslenkung (reduced motion) |

## Dauer

- Typisch: Rückfederung 300–500 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Elastic](../elastic/description.md)
- [Stagger](../../organization/stagger/description.md)
