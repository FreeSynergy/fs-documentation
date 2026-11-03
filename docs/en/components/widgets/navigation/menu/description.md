# Menu

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `horizontal`, `vertical`, `dropdown`, `menubar`, `hamburger` |
| **States** | `open`, `expanded`, `selected` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `expand`, `collapse`, `fade-in` |
| **Related** | `context-menu`, `breadcrumb`, `tabs`, `bottom-navigation`, `sidebar` |
| **Role** | `menubar` |
| **State** | documented |

!!! info "Standardisierung"
    Die frühere Komponente `hamburger-menu` ist als Variante in `menu` aufgegangen:
    `dropdown`, `menubar`, `hamburger` (eingeklapptes Mobilmenü).

## Description

Ein Menü ist eine geordnete Liste von Menüpunkten, die Aktionen auslösen oder
Ansichten wechseln. Punkte können Untermenüs besitzen. Ein Menü ist der gemeinsame
Oberbau für Leisten, Aufklappmenüs und das Mobilmenü.

## Purpose

- Programmweite Navigation in einer Leiste (`menubar`, `horizontal`)
- Aktionen gebündelt anbieten, ohne die Fläche vollzustellen (`dropdown`)
- Navigation in der Seitenleiste (`vertical`)
- Navigation auf kleinen Bildschirmen (`hamburger`)

## Variants

| Variant | Description |
| ---------- | -------------- |
| **horizontal** | Leiste über dem Inhalt, Standard im Desktop |
| **vertical** | Liste nebeneinander mit Inhalt, in Seitenleisten |
| **dropdown** | Punkte erscheinen erst beim Öffnen |
| **menubar** | mehrere Menüs nebeneinander, je mit Untermenü |
| **hamburger** | eingeklapptes Menü mit Icon, Mobile und schmale Fenster |

## Features

- Untermenüs mit beliebigem Tiefgang
- Tastaturnavigation (Pfeiltasten, `Esc`, Pfeiltaste nach rechts öffnet Unteremenü)
- Gruppen und Trennlinien zwischen Punkten (`separator`)
- Symbole und Beschriftungen einzeln schaltbar
- Öffnet und schließt mit Animation; Klick außerhalb schließt

## Distinction

- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): das Kontextmenü gehört zum
  angeklickten Objekt und erscheint an der Zeigerposition (andere ARIA-Rolle).
- **Nicht verwechseln mit** [tabs](../tabs/): Reiter wechseln innerhalb einer Ansicht,
  ein Menü wechselt Adressen oder führt Aktionen aus.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): feste
  Hauptbereiche auf Mobilgeräten, immer sichtbar.

## Best Practices

- Höchstens sieben Punkte pro Ebene; mehr gruppieren.
- Zerstörerische Aktionen nicht im Hauptmenü, sondern im Kontext des Objekts.
- Auf Mobilgeräten das Menü nicht doppelt anbieten (Hamburger *oder* Seitenleiste).
- Menüpunkte mit Verb beginnen; für den aktiven Punkt `aria-current` bzw. `activeItem`.

## See also

- [navigation – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
