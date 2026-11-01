# Context Menu (Rechtsklick-Menü)

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base`, `menu` |
| **Varianten** | `Standard`, `Long Press`, `Overflow Menu` |
| **Zustände** | `open`, `sub-open` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `pop-in`, `fade-out` |
| **Verwandt** | `menu`, `toolbar`, `popover`, `select` |
| **Status** | dokumentiert |

## Beschreibung
Ein Context Menu (Kontextmenü) wird durch Rechtsklick oder lange Touch-Aktion geöffnet und bietet kontextbezogene Optionen.

## Verwendungszweck

- Kontextbezogene Aktionen anzeigen
- Weniger wichtige Funktionen verstecken
- Schneller Zugriff auf Aktionen für ausgewählte Elemente

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Standard** | Rechtsklick-Menü (Desktop) |
| **Long Press** | Lange Touch-Aktion (Mobile) |
| **Overflow Menu** | Drei-Punkte-Menü |

## Features

- Positionierung am Mauszeiger (Desktop)
- Scrollen (bei vielen Optionen)
- Keyboard-Navigation
- Accessibility (Barrierefreiheit)

## Abgrenzung

- **Nicht verwechseln mit** [menu](../../navigation/menu/): ein Menü hängt an einer
  Navigationsleiste und führt meist zu Ansichten; das Kontextmenü ruft Aktionen für das
  Objekt am Zeiger auf.
- **Nicht verwechseln mit** [toolbar](../../navigation/toolbar/): die Toolbar zeigt Aktionen
  dauerhaft, das Kontextmenü nur auf Zuruf (`long-press`, Rechtsklick).
- **Nicht verwechseln mit** [popover](../popover/): ein Popover trägt Inhalt oder ein Formular,
  das Kontextmenü ausschließlich eine Aktionsliste.
- **Nicht verwechseln mit** [select](../../fields/select/): hier wird ein Feldwert gesetzt,
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

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Menu](../../navigation/menu/) — Elternklasse
- [Popover](../popover/) — Inhalt statt Aktionsliste
- [Basiskomponente](../../basics/base/)
