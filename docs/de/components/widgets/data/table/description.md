# Table

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `Simple`, `Data`, `Tree`, `Inline Edit` |
| **Zustände** | `selected`, `bearbeitet` |
| **Gesten** | `tap`, `drag`, `long-press`, `swipe` |
| **Animationen** | `stagger`, `collapse`, `reorder` |
| **Verwandt** | `list-view`, `repeater`, `tree-view`, `description-list`, `pagination` |
| **Status** | dokumentiert |

## Beschreibung
Eine Tabelle ist eine tabellarische Darstellung mit Zeilen und Spalten.

## Verwendungszweck

- Daten anzeigen
- Listen
- Übersichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | statische Zeilen und Spalten ohne Bedienelemente |
| **daten** | Sortierung, Filter, Auswahl und Seitenzahlen |
| **baum** | Zeilen mit Ein- und Ausklappen für verschachtelte Daten |
| **inline-bearbeitung** | Zellen direkt in der Tabelle bearbeiten |

## Features

- Sortierung und Filter pro Spalte
- Zeilenauswahl mit Sammelaktionen
- Spaltenbreite per Ziehen, die erste Spalte kann fixiert werden
- Die Kopfzeile bleibt beim Scrollen stehen

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): eine Tabelle vergleicht Werte in Spalten,
  eine Liste ordnet jede Zeile frei an.
- **Nicht verwechseln mit** [description-list](../description-list/): diese beschreibt ein Objekt,
  die Tabelle viele.
- **Nicht verwechseln mit** [tree-view](../tree-view/): verschachtelte Daten mit navigatorischem
  Charakter gehören dorthin, verschachtelte Datensätze gehören in die Variante `baum`.
- Kopfzeilen-Bedienelemente ersetzen keinen eigenen Filteraufbau ([repeater](../repeater/)).

## Best Practices

- Zahlen rechts, Texte links, Datumsangaben in einem Format; Kopfzeile fett und fixiert.
- Nur sortierbare Spalten mit einem Sortierzeichen markieren; die Sortierung über die Navigation hinweg merken.
- Auswahl über Checkboxen in der ersten Spalte; Sammelaktionen erscheinen erst, wenn etwas
  ausgewählt ist.
- Horizontales Scrollen vermeiden: auf schmalen Bildschirmen Spalten ausblendbar machen oder
  zu Karten wechseln.
- Inline-Bearbeitung braucht klare Ränder und `Esc` als Abbrechen, sonst wirkt die Tabelle leer.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — frei angeordnete Zeilen
- [Tree View](../tree-view/) — Hierarchie statt flacher Liste
- [Basiskomponente](../../../primitives/basics/base.md)
