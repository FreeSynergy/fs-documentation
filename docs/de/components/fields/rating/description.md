# Rating (Bewertung)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Star Rating`, `Heart Rating`, `Number Rating` |
| **Zustände** | `halb`, `read-only` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `pop-in`, `elastic` |
| **Verwandt** | `slider`, `number-input`, `badge` |
| **Status** | dokumentiert |

## Beschreibung
Ein Rating ist eine Sterne- oder Punktebewertung.

## Verwendungszweck

- Produktbewertung
- Service-Bewertung
- Sterne

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Star Rating** | Sterne |
| **Heart Rating** | Herzen |
| **Number Rating** | Zahlen |

## Features

- Max Stars (meist 5)
- Read-only
- Interactive

## Abgrenzung

- **Nicht verwechseln mit** [slider](../slider/): der Regler ist eine kontinuierliche Skala ohne
  Werturteil, der Rating-Streifen ist eine diskrete Bewertung mit Bedeutung pro Stufe.
- **Nicht verwechseln mit** [number-input](../number-input/): dort gibt man einen Wert ein,
  hier wählt man eine Stufe.
- Reine Anzeige einer vorhandenen Bewertung (Anzahl, Durchschnitt) gehört als
  [badge](../../feedback/badge/) in Listen – das read-only-Rating zeigt die Verteilung.

## Best Practices

- Fünf Stufen als Standard; jede Stufe beschriften ("1 = schlecht … 5 = sehr gut"),
  Sterne allein sind mehrdeutig.
- Halbe Schritte nur zulassen, wenn die Auswertung sie wirklich braucht.
- In Listen read-only darstellen und Anzahl der Bewertungen daneben stellen.
- Tastatur: Pfeiltasten ändern die Stufe, `aria-valuenow` beschreibt den aktuellen Wert.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Slider](../slider/) — kontinuierliche Skala
- [Badge](../../feedback/badge/) — Zahl statt Streifen
- [Basiskomponente](../../basics/base/)
