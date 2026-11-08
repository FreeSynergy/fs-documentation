# Context Menu

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
Ein Kontextmenü wird per Rechtsklick oder durch eine lange Berührung geöffnet und bietet kontextbezogene Optionen an.

## Verwendungszweck

- Anzeige kontextbezogener Aktionen
- Ausblenden weniger wichtiger Funktionen
- Schneller Zugriff auf Aktionen für ausgewählte Elemente

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | Rechtsklick-Menü (Desktop) |
| **Long Press** | lange Berührung (Mobil) |
| **Overflow Menu** | Menü mit drei Punkten |

## Funktionen

- Positionierung am Mauszeiger (Desktop)
- Scrollen (bei vielen Optionen)
- Tastaturnavigation
- Barrierefreiheit

## Abgrenzung

- **Nicht verwechseln mit** [menu](../../navigation/menu/): ein Menü hängt an einer Navigationsleiste und
  führt meist zu Ansichten; das Kontextmenü löst Aktionen für das Objekt am Zeiger aus.
- **Nicht verwechseln mit** [toolbar](../../navigation/toolbar/): die Werkzeugleiste zeigt Aktionen
  dauerhaft, das Kontextmenü nur auf Abruf (`long-press`, Rechtsklick).
- **Nicht verwechseln mit** [popover](../popover/): ein Popover trägt Inhalte oder ein Formular, das
  Kontextmenü ausschließlich eine Aktionsliste.
- **Nicht verwechseln mit** [select](../../../primitives/fields/select/): hier wird ein Feldwert gesetzt,
  dort wird eine Aktion ausgeführt.
- Das Überlaufmenü (drei Punkte) ist die Variante für kleine Flächen, keine eigene Komponente.

## Best Practices

- Zeig nur relevante Aktionen
- Gleiche Aktionen für gleichartige Elemente
- Aktionen mit Icons
- Deaktivierte Aktionen ausgrauen

## Inhalt

- **Aktionen** - Aktionen (bearbeiten, löschen, teilen)
- **Trenner** - Trennlinien
- **Deaktivierte Einträge** - deaktivierte Optionen
- **Icons** - Icons zur visuellen Orientierung

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Menu](../../navigation/menu/) — Elternklasse
- [Popover](../popover/) — Inhalte statt Aktionsliste
- [Basiskomponente](../../../primitives/basics/base.md)
