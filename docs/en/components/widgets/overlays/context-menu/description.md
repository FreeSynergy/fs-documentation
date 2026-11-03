# Context Menu

| Field | Value |
| ------ | ------ |
| **Category** | `overlays` |
| **Inherits from** | `base`, `menu` |
| **Variants** | `Standard`, `Long Press`, `Overflow Menu` |
| **States** | `open`, `sub-open` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `pop-in`, `fade-out` |
| **Related** | `menu`, `toolbar`, `popover`, `select` |
| **State** | documented |

## Description
Ein Context Menu (Kontextmenü) wird durch Rechtsklick oder lange Touch-Aktion geöffnet und bietet kontextbezogene Optionen.

## Purpose

- Kontextbezogene Aktionen anzeigen
- Weniger wichtige Funktionen verstecken
- Schneller Zugriff auf Aktionen für ausgewählte Elemente

## Variants

| Variant | Description |
| --------- | -------------- |
| **Standard** | Rechtsklick-Menü (Desktop) |
| **Long Press** | Lange Touch-Aktion (Mobile) |
| **Overflow Menu** | Drei-Punkte-Menü |

## Features

- Positionierung am Mauszeiger (Desktop)
- Scrollen (bei vielen Optionen)
- Keyboard-Navigation
- Accessibility (Barrierefreiheit)

## Distinction

- **Nicht verwechseln mit** [menu](../../navigation/menu/): ein Menü hängt an einer
  Navigationsleiste und führt meist zu Ansichten; das Kontextmenü ruft Aktionen für das
  Objekt am Zeiger auf.
- **Nicht verwechseln mit** [toolbar](../../navigation/toolbar/): die Toolbar zeigt Aktionen
  dauerhaft, das Kontextmenü nur auf Zuruf (`long-press`, Rechtsklick).
- **Nicht verwechseln mit** [popover](../popover/): ein Popover trägt Inhalt oder ein Formular,
  das Kontextmenü ausschließlich eine Aktionsliste.
- **Nicht verwechseln mit** [select](../../../primitives/fields/select/): hier wird ein Feldwert gesetzt,
  dort eine Aktion ausgeführt.
- Das Overflow-Menü (drei Punkte) ist die Variante für kleine Flächen, keine eigene Komponente.

## Best Practices

- Nur relevante Aktionen anzeigen
- Konsistente Aktionen für gleiche Elemente
- Aktionen mit Icons
- Deaktivierte Aktionen ausgrauen

## Inhalt

- **Actions** - Aktionen (Bearbeiten, Löschen, Teilen)
- **Dividers** - Trennlinien
- **Disabled Items** - Deaktivierte Optionen
- **Icons** - Icons für visuelle Orientierung

## See also

- [overlays – overview](../index.md)
- [Menu](../../navigation/menu/) — Elternklasse
- [Popover](../popover/) — Inhalt statt Aktionsliste
- [Base component](../../../primitives/basics/base.md)
