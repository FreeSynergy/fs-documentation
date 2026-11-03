# Table (Tabelle)

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
Eine Table ist eine tabellarische Darstellung mit Zeilen und Spalten.

## Verwendungszweck

- Daten anzeigen
- Listen
- Übersichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | statische Zeilen und Spalten ohne Steuerung |
| **daten** | Sortierung, Filter, Auswahl und Seitenzahlen |
| **baum** | Zeilen mit Einklappung für verschachtelte Daten |
| **inline-bearbeitung** | Zellbearbeitung direkt in der Tabelle |

## Features

- Sortierung und Filter je Spalte
- Zeilenauswahl mit Sammelaktionen
- Spaltenbreite per Ziehen, erste Spalte fixierbar
- Kopfzeile bleibt beim Scrollen stehen

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../list-view/): eine Tabelle vergleicht Werte in Spalten,
  eine Liste gestaltet jede Zeile frei.
- **Nicht verwechseln mit** [description-list](../description-list/): die beschreibt ein Objekt,
  die Tabelle viele.
- **Nicht verwechseln mit** [tree-view](../tree-view/): verschachtelte Daten mit Navigations-
  charakter gehören dorthin, verschachtelte Datensätze in die Variante `baum`.
- Kopfzeilen-Steuerung ersetzt keine eigene Filterbaugruppe ([repeater](../repeater/)).

## Best Practices

- Zahlen rechts, Texte links, Datums in einem Format; Kopfzeile fett und fixiert.
- Nur sortierbare Spalten mit Sortiersymbol kennzeichnen, Sortierung über Navigation hinweg merken.
- Auswahl über Kästchen in der ersten Spalte; Sammelaktionen erscheinen erst mit Auswahl.
- Quer-Scrollen vermeiden: auf schmalen Bildschirmen Spalten auswählbar machen oder in Karten
  übergehen.
- Inline-Bearbeitung mit deutlichen Grenzen und `Esc` als Abbruch, sonst wirkt die Tabelle leer.

## Siehe auch

- [data – Übersicht](../index.md)
- [List View](../list-view/) — freie Zeilen
- [Tree View](../tree-view/) — Hierarchie statt flache Liste
- [Basiskomponente](../../basics/base/)
