# Select (Auswahlliste)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `Simple`, `Multi-select`, `Searchable`, `Custom` |
| **Zustände** | `open`, `no-results` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `expand`, `fade-in` |
| **Verwandt** | `combobox`, `radio-group`, `tags-input`, `context-menu` |
| **Status** | dokumentiert |

## Beschreibung
Eine Auswahlliste: das Feld zeigt den gewählten Wert, die Optionen liegen hinter einem Klick.

## Verwendungszweck

- Auswahl
- Filter
- Kategorien

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Einfache Liste |
| **Multi-select** | Mehrfachauswahl |
| **Searchable** | Mit Suche |
| **Custom** | Benutzerdefiniert |

## Features

- Search
- Multi-select
- Customizable

## Abgrenzung

- **Nicht verwechseln mit** [combobox](../combobox/): hier kann nur gewählt werden, was die Liste
  bietet; die Combobox lässt zusätzlich Freitext zu (Plan Abschnitt 4, Zeile 5).
- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): ein Kontextmenü ruft
  Aktionen auf, diese Liste setzt einen Feldwert.
- **Nicht verwechseln mit** nativer Auswahlliste: `native-select` ist eine Variante, die das
  System-Overlay des Betriebssystems benutzt.
- Unter sieben Optionen ist [radio-group](../radio-group/) meist die schnellere Bedienung.

## Best Practices

- Ab etwa acht Optionen `select`, darunter Radio-Gruppe.
- Gruppe mit `disabled` als Platzhalterzeile anbieten ("Bitte wählen"), nie eine Scheinoption "--".
- Lange Listen gliedern (`Optgroupen`) und ab 20 Optionen durchsuchbar machen.
- Mehrfachauswahl als Chips anzeigen und zählen; "Alle" explizit anbieten.
- Vorauswahl nur, wenn sie wirklich die erwartete Antwort ist.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Combobox](../combobox/) — Liste mit Freitext
- [Radio Group](../radio-group/) — kurze Optionslisten
- [Basiskomponente](../../basics/base/)
