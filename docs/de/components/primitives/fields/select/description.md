# Select

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `simple`, `multi-select`, `searchable`, `custom` |
| **Zustände** | `open`, `no-results` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `combobox`, `radio-group`, `tags-input`, `context-menu` |
| **Status** | dokumentiert |

## Beschreibung
Eine Auswahlliste: das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.

## Verwendungszweck

- Auswählen
- Filter
- Kategorien

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **simple** | Einfache Liste |
| **multi-select** | Mehrfachauswahl |
| **searchable** | Mit Suche |
| **custom** | Angepasst |

## Features

- Suche
- Mehrfachauswahl
- Anpassbar

## Abgrenzung

- **Nicht verwechseln mit** [combobox](../combobox/): hier kann nur gewählt werden, was die Liste
  bietet; die Combobox erlaubt zusätzlich freien Text (Planabschnitt 4, Zeile 5).
- **Nicht verwechseln mit** [context-menu](../../../widgets/overlays/context-menu/): ein Kontextmenü ruft
  Aktionen auf, diese Liste setzt einen Feldwert.
- **Nicht verwechseln mit** dem nativen Select: `native-select` ist eine Variante, die das
  System-Overlay des Betriebssystems verwendet.
- Unterhalb von sieben Optionen ist [radio-group](../radio-group/) meist die schnellere Bedienung.

## Best Practices

- Ab etwa acht Optionen `select` verwenden, darunter eine Radio-Gruppe.
- Als Platzhalterzeile eine Option mit `disabled` anbieten ("Bitte wählen"), niemals eine
  falsche Option "--".
- Lange Listen gliedern (`optgroup`) und ab 20 Optionen durchsuchbar machen.
- Mehrfachauswahl als Chips zeigen und zählen; "Alle" ausdrücklich anbieten.
- Nur vorauswählen, wenn das wirklich die erwartete Antwort ist.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Combobox](../combobox/) — Liste mit freiem Text
- [Radio Group](../radio-group/) — kurze Optionslisten
- [Basiskomponente](../../basics/base.md)
