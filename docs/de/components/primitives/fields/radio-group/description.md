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
Eine Radio Group ist eine Gruppe von Optionsfeldern (Einfachauswahl).

## Verwendungszweck

- Auswahlmöglichkeiten
- Optionen
- Einstellungen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | klassischer Kreis, Beschriftungen untereinander |
| **toggle** | Optionen als aneinanderliegende Buttons (segmentiert) |
| **karte** | Optionen als Karten mit Titel und Beschreibung |

## Funktionen

- Eine Auswahl
- Beschriftungen
- Icons

## Abgrenzung

- **Nicht verwechseln mit** [checkbox](../checkbox/): Hier ist genau eine Option gültig.
  Dort sind mehrere gleichzeitig möglich.
- **Nicht verwechseln mit** [select](../select/): Die Optionen der Radio Group sind alle sichtbar.
  Die Auswahlliste versteckt sie hinter einem Klick.
- **Nicht verwechseln mit** [button-group](../../actions/button-group/): Eine Button-Gruppe löst
  Aktionen aus. Diese Gruppe setzt einen Formularwert.

## Best Practices

- Radio bis etwa sieben Optionen verwenden, darüber `select`.
- Eine Vorauswahl setzen oder „keine Präferenz“ als eigene Option anbieten.
- Die Gruppe als Ganzes beschriften (`fieldset`/`legend`). Die einzelne Option braucht kein eigenes Label.
- Gefährliche Optionen zuletzt anbieten und mit einer Bestätigung absichern.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Checkbox](../checkbox/) — Mehrfachauswahl
- [Select](../select/) — Auswahlliste
- [Base-Komponente](../../basics/base.md)
