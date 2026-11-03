# Popover

| Field | Value |
| ------ | ------ |
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `inhalt`, `aktionen`, `formular` |
| **States** | `open` |
| **Gestures** | `tap` |
| **Animations** | `expand`, `fade-in` |
| **Related** | `tooltip`, `modal`, `select`, `context-menu`, `base` |
| **State** | documented |

## Description

Ein Popover ist ein kleines Overlay mit interaktivem Inhalt: Aktionen, eine
Vorschau oder ein kurzes Formular. Es ist an ein Auslöser-Element gedockt,
übernimmt aber – anders als ein Modal – nicht den ganzen Bildschirm.

## Purpose

- Sekundäraktionen an einem Eintrag (mehr-Menü mit Buttons)
- Schnelleingaben ohne Seitenwechsel (Datum setzen, Label zuweisen)
- Detailvorschau zu einem Eintrag (Kurzfassung vor dem Öffnen)

## Variants

| Variant | Description |
| ---------- | -------------- |
| **inhalt** | Text, Bilder oder Vorschau, keine Formulareingabe |
| **aktionen** | Liste von Aktionen (Abgrenzung zu context-menu: fester Auslöser) |
| **formular** | kleines Formular, z. B. Datum oder Farbe setzen |

## Features

- Fokus wandert in das Popover und nach dem Schließen zum Auslöser zurück
- Schließen per Klick außerhalb, Escape oder Aktion im Popover
- Andockposition wie beim [tooltip](../tooltip/)

## Distinction

- **Nicht verwechseln mit** [tooltip](../tooltip/): Tooltip = nur Text, nie
  interaktiv.

- **Nicht verwechseln mit** [modal](../modal/): ein Modal blockiert
  und zentriert; ein Popover bleibt am Auslöser und lässt das Übrige bedienbar.

- **Nicht verwechseln mit** [dropdown](../../../primitives/fields/select/): ein Dropdown
  wählt einen Wert aus einer Liste, ein Popover trägt beliebigen Inhalt.

- **Nicht verwechseln mit** [context-menu](../context-menu/): das
  Kontextmenü folgt dem Rechtsklick, ein Popover einem festen Auslöser.

## Best Practices

- Escape und Klick außerhalb müssen schließen; Fokus kehrt zum Auslöser zurück.
- `aria-expanded` am Auslöser ist Pflicht.
- Kein voller Dialog-Ersatz: für mehr als ~5 Eingabefelder ein `modal` verwenden.

## See also

- [Tooltip](../tooltip/)
- [Modal](../modal/)
- [Context Menu](../context-menu/)
- [Base component](../../../primitives/basics/base.md)
