# Search Field (Suchfeld mit Filter)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `text-input` |
| **Varianten** | `Simple`, `Filter`, `Auto-complete` |
| **Zustände** | `open`, `loading`, `no-results` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `fade-in`, `expand`, `highlight` |
| **Verwandt** | `combobox`, `command`, `text-input`, `select` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die frühere Komponente `search-input` ist als Variante in `search-field` aufgegangen: `simple`, `autocomplete`, `filter`.

## Beschreibung
Ein Search Field ist ein Suchfeld mit Filtermöglichkeiten.

## Verwendungszweck

- Suche
- Filter
- Schnellsuche

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Einfache Suche |
| **Filter** | Mit Filtern |
| **Auto-complete** | Mit Vorschlägen |

## Features

- Filter
- Auto-complete
- Recent Searches

## Abgrenzung

- **Nicht verwechseln mit** [combobox](../combobox/): das Suchfeld verändert eine Ansicht oder
  liefert Ergebnisse, die Combobox schreibt einen Wert in ein Formularfeld.
- **Nicht verwechseln mit** [command](../../navigation/command/): die Befehlspalette startet
  Aktionen und ist ein vollflächiges Overlay, das Suchfeld filtert Inhalte einer Ansicht.
- **Nicht verwechseln mit** [text-input](../text-input/): ohne Such-Icon, ohne Leeren-Knopf und
  ohne Sofortauslösung ist es einfach ein Textfeld.

## Best Practices

- Eingabe gebündelt auswerten (200–300 ms), nicht bei jedem Zeichen neu laden.
- Ergebniszahl sichtbar machen ("12 Treffer"), leeres Ergebnis als `no-results` beschriften.
- Leeren mit Clear-Knopf **und** `Esc`; Filterstellungen bleiben beim Zurückkehren erhalten.
- Auf Mobil volle Breite und Suchtastatur; die Suchfeldhöhe bleibt mindestens 44 px.
- Gesuchte Begriffe merken, aber das Feld nicht vorbelegen – der Nutzer soll wissen, warum
  die Liste gefiltert ist.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Combobox](../combobox/) — Wert auswählen statt filtern
- [Command](../../navigation/command/) — Befehle starten
- [Basiskomponente](../../basics/base/)
