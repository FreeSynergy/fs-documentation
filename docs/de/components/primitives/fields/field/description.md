# Field (Feld-Wrapper)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `vertikal`, `horizontal`, `inline` |
| **Zustände** | `error` (Fehlermeldung unter dem Feld) |
| **Gesten** | `tap` (Label fokussiert das Feld) |
| **Animationen** | `expand` |
| **Verwandt** | `label`, `search-field`, `text-input`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Field ist der Wrapper um ein Eingabefeld: Er verbindet Beschriftung,
Hilfetext, Fehlermeldung und Pflicht-Markierung zu einer barrierefreien
Einheit. Das eigentliche Feld bleibt eine eigene Komponente.

## Verwendungszweck

- Barrierefreier Rahmen um jedes Eingabefeld
- Hilfetext und Fehler an der richtigen Stelle anzeigen
- Konsistente Abstände und Labelposition in Formularen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vertikal** | Label über dem Feld (Standard) |
| **horizontal** | Label links neben dem Feld (dichte Formulare) |
| **inline** | nur Label, ohne Hilfetext (z. B. in Werkzeugleisten) |

## Features

- Fehler- und Hilfetext mit eigenem Zeilenplatz (nichts überlagert)
- Pflicht-Markierung mit Text, nicht nur Sternchen
- Zeichenzähler (`counter`) für Textfelder
- Verknüpfung von Label und Fehlertext über `id`/`aria-describedby`

## Abgrenzung

- **Nicht verwechseln mit** [label](../../basics/label/): das Label ist nur die
  Beschriftung; das Field ergänzt Hilfe, Fehler und Abstand.

- **Nicht verwechseln mit** [search-field](../search-field/): das ist
  eine komplette Eingabekomponente, kein Wrapper.

- **Nicht verwechseln mit** [description-list](../../data/description-list/): Label-Wert-Paare
  in Detailansichten, ohne Eingabe.
- **Nicht verwechseln mit** [input-group](../input-group/): die Gruppe sitzt im Feld neben
  dem Wert, dieser Wrapper außerhalb (Label, Hilfe, Fehler).

## Best Practices

- Jedes Feld braucht ein sichtbares Label – ein `placeholder` ersetzt es nicht.
- Fehlermeldung konkret benennen („Datum liegt in der Vergangenheit“).
- Fehler zusätzlich durch Icon und Text kennzeichnen, nicht nur durch Farbe.
- Hilfetext nur, wenn er echte Entscheidungen hilft.

## Siehe auch

- [Label](../../basics/label/)
- [Text Input](../text-input/)
- [Basiskomponente](../../basics/base/)
- [Standardisierte Daten](../../data/)
