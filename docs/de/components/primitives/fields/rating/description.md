# Rating (Bewertung)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Sternbewertung`, `Herzbewertung`, `Zahlenbewertung` |
| **Zustände** | `halb`, `read-only` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `pop-in`, `elastic` |
| **Verwandt** | `slider`, `number-input`, `badge` |
| **Status** | dokumentiert |

## Beschreibung
Eine Bewertung ist eine Beurteilung mit Sternen oder Punkten.

## Verwendungszweck

- Produktbewertungen
- Servicebewertungen
- Sterne

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Sternbewertung** | Sterne |
| **Herzbewertung** | Herzen |
| **Zahlenbewertung** | Zahlen |

## Funktionen

- Maximale Anzahl Sterne (meist 5)
- Nur lesen
- Interaktiv

## Abgrenzung

- **Nicht verwechseln mit** [slider](../slider/): Der Slider ist eine stufenlose Skala ohne
  Wertung. Die Bewertungsleiste ist eine diskrete Beurteilung mit einer Bedeutung pro Stufe.
- **Nicht verwechseln mit** [number-input](../number-input/): Dort gibst du einen Wert ein.
  Hier wählst du eine Stufe.
- Eine reine Anzeige einer bestehenden Bewertung (Anzahl, Durchschnitt) gehört in Listen
  als [Badge](../../feedback/badge/). Die Bewertung zum Lesen zeigt die Verteilung.

## Best Practices

- Fünf Stufen als Standard. Jede Stufe beschriften („1 = schlecht … 5 = sehr gut“).
  Sterne allein sind mehrdeutig.
- Halbe Stufen nur erlauben, wenn die Bewertung sie wirklich braucht.
- In Listen nur lesbar anzeigen und die Anzahl der Bewertungen daneben setzen.
- Tastatur: Pfeiltasten ändern die Stufe. `aria-valuenow` beschreibt den aktuellen Wert.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Slider](../slider/) — stufenlose Skala
- [Badge](../../feedback/badge/) — eine Zahl statt einer Leiste
- [Base-Komponente](../../basics/base.md)
