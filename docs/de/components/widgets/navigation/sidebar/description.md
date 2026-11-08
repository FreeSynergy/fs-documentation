# Sidebar

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `angeheftet`, `ikonenleiste`, `einklappbar` |
| **Zustände** | `geöffnet`, `geschlossen` |
| **Gesten** | `tap`, `drag`, `long-press`, `swipe` |
| **Animationen** | `expand`, `collapse`, `slide-in` |
| **Verwandt** | `menu`, `bottom-navigation`, `drawer`, `toolbar`, `tree-view` |
| **Status** | dokumentiert |

## Beschreibung
Die Sidebar ist eine vertikale Navigationsspalte, meist am linken oder rechten Rand der
Anwendung. Sie bietet schnellen Zugriff auf die wichtigsten Funktionen und wird oft in
Desktop-Anwendungen und Messengern verwendet.

## Zweck

- Schneller Zugriff auf die wichtigsten Funktionen
- Menüpunkte in Gruppen ordnen
- Statusinformationen zeigen (z. B. Benutzerprofil, Nachrichtenzähler)

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **angeheftet** | dauerhaft am Rand, daneben der Inhaltsbereich |
| **ikonenleiste** | schmale Leiste mit Icons, Namen nur bei Hover oder Auswahl |
| **einklappbar** | breit mit Namen, per Knopf auf die Icon-Leiste reduzierbar |

Auf kleinen Bildschirmen wird die Sidebar zum [drawer](../../overlays/drawer/). Sie ist dann
ein Overlay und schiebt den Inhalt nicht mehr zur Seite.

## Funktionen

- Gruppen mit Überschriften und Trennlinien
- Zähler oder Status an den Punkten ([badge](../../../primitives/feedback/badge/))
- Profilkopf oben, Einstellungen unten
- Durchsuchbar bei vielen Punkten, Tastaturnavigation mit den Pfeiltasten

## Abgrenzung

- **Nicht verwechseln mit** [drawer](../../overlays/drawer/): Der Drawer legt sich über den Inhalt,
  die Sidebar nimmt ihm dauerhaft Platz weg.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): Das eine sitzt am Rand,
  das andere am unteren Rand kleiner Bildschirme.
- **Nicht verwechseln mit** [tree-view](../../data/tree-view/): Hier stehen Ziele und Aktionen,
  dort beliebige Daten.

## Best Practices

- Wichtiges oben, Gruppen mit Überschrift, höchstens zwei Ebenen.
- Der aktive Punkt ist dauerhaft erkennbar (Fläche und Text, nicht nur Farbe).
- Das Einklappen merkt sich den Zustand; in der Icon-Leiste braucht jeder Punkt einen Tooltip.
- Auf kleinen Bildschirmen als Drawer öffnen und nach der Auswahl wieder schließen.
- Die Breite nur durch Ziehen ändern, wenn die Mindestbreite lesbar bleibt (mindestens 200 px).

## Typische Positionen

- Links (Standard bei Sprachen mit Leserichtung von links nach rechts)
- Rechts (für Sprachen mit Leserichtung von rechts nach links oder bestimmte Layouts)
- Oben (als horizontale Leiste — dann meist „Topbar“ genannt)

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Drawer](../../overlays/drawer/) — Sidebar als Overlay
- [Menu](../menu/) — Menüpunkte in der Leiste
- [Base-Komponente](../../../primitives/basics/base.md)
