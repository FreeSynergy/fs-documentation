# Radio Group (Optionsgruppe)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `einzeln`, `toggle`, `karte` |
| **Zustände** | `checked` |
| **Gesten** | `tap` |
| **Animationen** | `press`, `highlight` |
| **Verwandt** | `checkbox`, `select`, `button-group`, `field` |
| **Status** | dokumentiert |

## Beschreibung
Eine Radio Group ist eine Gruppe von Optionsfeldern (einzelfach).

## Verwendungszweck

- Auswahlmöglichkeiten
- Optionen
- Einstellungen

## Features

- One Selection
- Labels
- Icons

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | Klassischer Kreis mit Label untereinander |
| **toggle** | Optionen als aneinandergrenzende Knöpfe (segmentiert) |
| **karte** | Optionen als Karten mit Titel und Beschreibung |

## Abgrenzung

- **Nicht verwechseln mit** [checkbox](../checkbox/): hier ist genau eine Option gültig,
  dort sind mehrere gleichzeitig möglich.
- **Nicht verwechseln mit** [select](../select/): Radio-Optionen sind alle sichtbar,
  die Auswahlliste versteckt sie hinter einem Klick.
- **Nicht verwechseln mit** [button-group](../../actions/button-group/): eine Knopfgruppe löst
  Aktionen aus, diese Gruppe setzt einen Formularwert.

## Best Practices

- Bis etwa sieben Optionen Radio verwenden, darüber `select`.
- Vorauswahl setzen oder ausdrücklich "keine Angabe" als eigene Option vorsehen.
- Gruppe als Ganzes beschriften (`fieldset`/`legend`) — die einzelne Option braucht kein Label.
- Gefährliche Optionen zuletzt und mit Bestätigung anbieten.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Checkbox](../checkbox/) — Mehrfachauswahl
- [Select](../select/) — Auswahlliste
- [Basiskomponente](../../basics/base/)
