# Tags Input (Tags-Feld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `text-input` |
| **Varianten** | `frei`, `vorschlag`, `nur-lesbar` |
| **Zustände** | `open`, `error` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `pop-in`, `collapse` |
| **Verwandt** | `mention-input`, `combobox`, `badge`, `select` |
| **Status** | dokumentiert |

## Beschreibung
Ein Tags Input ist eine Liste von Tags/Etiketten.

## Verwendungszweck

- Hashtags
- Kategorien
- Schlagworte

## Features

- Auto-complete
- Filter
- Remove

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **frei** | neuer Tag entsteht aus der Eingabe (Komma oder Enter) |
| **vorschlag** | nur vorhandene Tags, Auswahl aus Vorschlagsliste |
| **nur-lesbar** | Tags anzeigen ohne Löschen und Ergänzen |

## Abgrenzung

- **Nicht verwechseln mit** [badge](../../feedback/badge/): ein Badge zeigt einen Status, ein Tag
  ist editierbarer Inhalt mit Löschen-Knopf.
- **Nicht verwechseln mit** [mention-input](../mention-input/): Tags sind freie Begriffe,
  eine Erwähnung zeigt auf einen Kontakt.
- **Nicht verwechseln mit** [select](../select/) mit Mehrfachauswahl: dort gibt es nur, was die
  Liste bietet; hier entstehen neue Werte aus der Eingabe.

## Best Practices

- Duplikate verhindern (Groß-/Kleinschreibung egal), stattdessen den vorhandenen Tag hervorheben.
- Rücktaste in leerer Eingabe entfernt den letzten Tag – das ist der schnellste Weg.
- Höchstzahl setzen und anzeigen ("8 von 10"), sonst werden Datensätze unbrauchbar.
- Verbotene Zeichen ablehnen und begründen, nicht still entfernen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Badge](../../feedback/badge/) — Anzeige ohne Bearbeitung
- [Mention Input](../mention-input/) — Kontakte statt Begriffe
- [Basiskomponente](../../basics/base/)
