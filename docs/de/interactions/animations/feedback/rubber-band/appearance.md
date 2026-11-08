# Rubber Band - Erscheinungsbild

## Grundaufbau

Der Inhalt liegt bündig am Rand. Wird über den Rand hinaus gezogen, entsteht ein gedämpfter
Abstand, der sich nach dem Loslassen wieder schließt.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────┐
│Randposition      herausziehen     zurückfedern        │
│                                                      │
│[Inhalt·····]  ┈┈┈ Rand ┈┈┈       [Inhalt·····]       │
│[············]  [    Abstand  ]    [············]       │
│[····Ende····]  [ Inhalt··· ]     [····Ende····]      │
│[············]  [ folgt dem Zug]  [············]       │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Vertikal** | der Standard für Listen und Artikel |
| **Horizontal** | blätternde Karussells und Tabellen |
| **Einseitig** | nur oben (z. B. der Anfang von Zum-Aktualisieren-Ziehen) |
| **Straff** | `widerstand: 0.15`, starker Gummibandwiderstand |
| **Aus** | harte Ränder ohne jede Auslenkung (reduzierte Bewegung) |

## Dauer

- Typisch: Zurückfedern 300–500 ms

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Elastic](../elastic/description.md)
- [Stagger](../../organization/stagger/description.md)
