# Drawer

| Field | Value |
| ------ | ------ |
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` |
| **States** | `open`, `peek` |
| **Gestures** | `swipe`, `tap`, `drag` |
| **Animations** | `slide-in`, `slide-out` |
| **Related** | `sidebar`, `modal`, `split-view`, `menu` |
| **State** | documented |

## Description
Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).

## Purpose

- Navigation
- Filter
- Profile

## Variants

| Variant | Position | Description |
| --------- | ---------- | -------------- |
| **Left Drawer** | Links | Links |
| **Right Drawer** | Rechts | Rechts |
| **Bottom Drawer** | Unten | Unten |
| **Full Drawer** | Voll | Vollständig |

!!! info "Einordnung"
    Das in Bibliotheken separate `sheet` ist keine eigene Komponente, sondern der
    Bottom Drawer mit reduzierter Höhe und Griffleiste.

## Features

- Header
- Body
- Footer
- Close
- Dismissible

## Distinction

- **Nicht verwechseln mit** [sidebar](../../navigation/sidebar/): die Seitenleiste gehört
  dauerhaft zum Layout; der Drawer kommt auf Zuruf und überdeckt den Inhalt.
- **Nicht verwechseln mit** [modal](../modal/): das Modal sitzt in der Mitte und will eine
  Entscheidung; der Drawer bringt Navigation oder Filter an den Rand.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover ist klein, an ein Element
  geheftet und erklärt genau dieses.
- Der Bottom Drawer mit Griffleiste ist die `sheet`-Bauform — eine Variante, keine eigene
  Komponente.
- Auf breiter Fläche kann der Drawer dauerhaft offen stehen; dann verhält er sich wie eine
  Seitenleiste, bleibt aber dieselbe Komponente.

## Best Practices

- Clear-Content
- Close-Button
- Accessibility
- Feedback

## See also

- [overlays – overview](../index.md)
- [Sidebar](../../navigation/sidebar/) — dauerhafte Seitenleiste
- [Modal](../modal/) — zentriertes Overlay
- [Base component](../../../primitives/basics/base.md)
