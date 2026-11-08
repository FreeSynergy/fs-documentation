# Drawer

| Feld | Wert |
|------|------|
| **Kategorie** | `overlays` |
| **Erbt von** | `base` |
| **Varianten** | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` |
| **Zustände** | `open`, `peek` |
| **Gesten** | `swipe`, `tap`, `drag` |
| **Animationen** | `slide-in`, `slide-out` |
| **Verwandt** | `sidebar`, `modal`, `split-view`, `menu` |
| **Status** | dokumentiert |

## Beschreibung
Ein Drawer ist ein seitliches Overlay-Fenster (einklappbar).

## Verwendungszweck

- Navigation
- Filter
- Profile

## Varianten

| Variante | Position | Beschreibung |
|----------|----------|--------------|
| **Left Drawer** | links | links |
| **Right Drawer** | rechts | rechts |
| **Bottom Drawer** | unten | unten |
| **Full Drawer** | vollständig | Vollbild |

!!! info "Einordnung"
    Das `sheet`, in Bibliotheken getrennt geführt, ist keine eigene Komponente, sondern der untere
    Drawer mit reduzierter Höhe und einem Griff.

## Funktionen

- Kopfbereich
- Inhalt
- Fußbereich
- Schließen
- Wegwischbar

## Abgrenzung

- **Nicht verwechseln mit** [sidebar](../../navigation/sidebar/): die Seitenleiste gehört dauerhaft
  zum Layout; der Drawer kommt auf Abruf und legt sich über den Inhalt.
- **Nicht verwechseln mit** [modal](../modal/): das Modal steht in der Mitte und verlangt eine Entscheidung;
  der Drawer bringt Navigation oder Filter an den Rand.
- **Nicht verwechseln mit** [popover](../popover/): ein Popover ist klein, hängt an einem Element und
  erklärt genau dieses Element.
- Der untere Drawer mit Griff ist die Form `sheet` — eine Variante, keine eigene Komponente.
- Auf einer breiten Fläche kann der Drawer dauerhaft offen bleiben; er verhält sich dann wie eine
  Seitenleiste, bleibt aber dieselbe Komponente.

## Best Practices

- Klarer Inhalt
- Schließen-Schaltfläche
- Barrierefreiheit
- Rückmeldung

## Siehe auch

- [overlays – Übersicht](../index.md)
- [Sidebar](../../navigation/sidebar/) — dauerhafte Seitenleiste
- [Modal](../modal/) — zentriertes Overlay
- [Basiskomponente](../../../primitives/basics/base.md)
