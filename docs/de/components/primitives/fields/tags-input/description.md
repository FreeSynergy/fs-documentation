# Tags Input

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
Ein Tags Input ist eine Liste aus Tags/Labels.

## Verwendungszweck

- Hashtags
- Kategorien
- Schlagwörter

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **frei** | ein neuer Tag entsteht aus der Eingabe (Komma oder Enter) |
| **vorschlag** | nur vorhandene Tags, gewählt aus einer Vorschlagsliste |
| **nur-lesbar** | Tags anzeigen, ohne zu löschen oder hinzuzufügen |

## Features

- Auto-complete
- Filter
- Entfernen

## Abgrenzung

- **Nicht verwechseln mit** [badge](../../feedback/badge/): ein Badge zeigt einen Status, ein Tag
  ist bearbeitbarer Inhalt mit einem Lösch-Knopf.
- **Nicht verwechseln mit** [mention-input](../mention-input/): Tags sind freie Begriffe,
  eine Erwähnung verweist auf einen Kontakt.
- **Nicht verwechseln mit** [select](../select/) mit Mehrfachauswahl: dort existiert nur, was die
  Liste bietet; hier entstehen neue Werte aus der Eingabe.

## Best Practices

- Doppelte verhindern (Groß-/Kleinschreibung spielt keine Rolle), stattdessen den vorhandenen Tag hervorheben.
- Backspace in einer leeren Eingabe entfernt den letzten Tag – das ist der schnellste Weg.
- Ein Maximum setzen und anzeigen ("8 von 10"), sonst werden die Einträge unbrauchbar.
- Unerlaubte Zeichen ablehnen und den Grund nennen, nicht stillschweigend entfernen.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Badge](../../feedback/badge/) — Anzeige ohne Bearbeitung
- [Mention Input](../mention-input/) — Kontakte statt Begriffe
- [Basiskomponente](../../basics/base.md)
