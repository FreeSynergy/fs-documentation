# Sidebar

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `angeheftet`, `ikonenleiste`, `einklappbar` |
| **States** | `geöffnet`, `geschlossen` |
| **Gestures** | `tap`, `drag`, `long-press`, `swipe` |
| **Animations** | `expand`, `collapse`, `slide-in` |
| **Related** | `menu`, `bottom-navigation`, `drawer`, `toolbar`, `tree-view` |
| **State** | documented |

## Description
Die Sidebar ist eine vertikale Navigationssäule, die normalerweise links oder rechts am Rand der Anwendung positioniert ist. Sie bietet schnellen Zugriff auf Hauptfunktionen und wird oft in Desktop-Anwendungen und Messenger verwendet.

## Purpose

- Schneller Zugriff auf Hauptfunktionen
- Organisation von Menüpunkten in Gruppen
- Anzeige von Statusinformationen (z.B. Benutzerprofil, Nachrichtenzähler)

## Variants

| Variant | Description |
| ---------- | -------------- |
| **angeheftet** | dauerhaft am Rand, Contentbereich daneben |
| **ikonenleiste** | schmale Leiste mit Symbolen, Namen erst bei Hover oder Auswahl |
| **einklappbar** | breit mit Namen, per Knopf auf die Ikonenleiste reduziert |

Auf kleinen Bildschirmen wird die Seitenleiste zum [drawer](../../overlays/drawer/),
sie ist dann ein Overlay und rückt den Inhalt nicht mehr.

## Features

- Gruppen mit Köpfen und Trennern
- Zähler oder Status an den Punkten ([badge](../../../primitives/feedback/badge/))
- Profilkopf oben, Einstellungen unten
- durchsuchbar bei vielen Punkten, Tastaturnavigation mit Pfeiltasten

## Distinction

- **Nicht verwechseln mit** [drawer](../../overlays/drawer/): der Drawer überdeckt den Inhalt,
  die Seitenleiste nimmt ihm dauerhaft Platz weg.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): die eine sitzt am Rand,
  die andere am unteren Rand kleiner Bildschirme.
- **Nicht verwechseln mit** [tree-view](../../data/tree-view/): hier stehen Ziele und Aktionen,
  dort beliebige Daten.

## Best Practices

- Wichtiges oben, Gruppen mit Überschrift, höchstens zwei Ebenen.
- Der aktive Punkt ist dauerhaft zu erkennen (Fläche plus Text, nicht nur Farbe).
- Einklappen merkt sich den Zustand; in der Ikonenleiste braucht jeder Punkt einen Tooltip.
- Auf kleinen Bildschirmen als Drawer öffnen und nach der Auswahl wieder schließen.
- Breite per Ziehen ändern nur, wenn die Mindestbreite lesbar bleibt (mindestens 200 px).

## Typische Positionen

- Links (Standard bei LTR-Sprachen)
- Rechts (bei RTL-Sprachen oder spezifischen Layouts)
- Oben (als Horizontale Leiste - dann meist "Topbar" genannt)

## See also

- [navigation – overview](../index.md)
- [Drawer](../../overlays/drawer/) — Seitenleiste als Overlay
- [Menu](../menu/) — Menüpunkte in der Leiste
- [Base component](../../../primitives/basics/base.md)
