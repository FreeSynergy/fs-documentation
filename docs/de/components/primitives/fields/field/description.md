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

Ein Field ist der Wrapper um ein Eingabefeld. Er verbindet Beschriftung,
Hilfetext, Fehlermeldung und Pflicht-Markierung zu einer barrierefreien
Einheit. Das eigentliche Feld bleibt eine eigene Komponente.

## Verwendungszweck

- Ein barrierefreier Rahmen um jedes Eingabefeld
- Hilfetext und Fehler an der richtigen Stelle anzeigen
- Konsistente Abstände und Labelposition in Formularen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vertikal** | Label über dem Feld (Standard) |
| **horizontal** | Label links neben dem Feld (dichte Formulare) |
| **inline** | nur das Label, ohne Hilfetext (z. B. in Werkzeugleisten) |

## Funktionen

- Fehler- und Hilfetext bekommen eigene Zeilen. Nichts überlappt.
- Pflichtfelder werden mit Text markiert, nicht nur mit einem Sternchen.
- Zeichenzähler (`counter`) für Textfelder
- Label und Fehlertext sind über `id`/`aria-describedby` verknüpft

## Abgrenzung

- **Nicht verwechseln mit** [label](../../basics/label/): Das Label ist nur
  die Beschriftung. Das Field ergänzt Hilfetext, Fehler und Abstände.

- **Nicht verwechseln mit** [search-field](../search-field/): Das ist
  eine vollständige Eingabekomponente, kein Wrapper.

- **Nicht verwechseln mit** [description-list](../../../widgets/data/description-list/): Wertepaare
  in Detailansichten, ohne Eingabe.
- **Nicht verwechseln mit** [input-group](../input-group/): Die Gruppe sitzt im Feld
  neben dem Wert, dieser Wrapper außen (Label, Hilfe, Fehler).

## Best Practices

- Jedes Feld braucht ein sichtbares Label. Ein `placeholder` ersetzt es nicht.
- Benenne die Fehlermeldung konkret („Das Datum liegt in der Vergangenheit“).
- Markiere Fehler zusätzlich mit Icon und Text, nicht nur mit Farbe.
- Hilfetext nur, wenn er bei Entscheidungen wirklich hilft.

## Siehe auch

- [Label](../../basics/label/)
- [Text Input](../text-input/)
- [Base-Komponente](../../basics/base.md)
- [Standardisierte Daten](../../../widgets/data/)
