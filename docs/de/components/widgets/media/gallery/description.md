# Gallery

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base` |
| **Varianten** | `raster`, `mosaik`, `zeile` |
| **Zustände** | `geöffnet`, `geladen` |
| **Gesten** | `tap`, `double-tap`, `swipe`, `pinch`, `drag` |
| **Animationen** | `stagger`, `zoom-in`, `fade-in` |
| **Verwandt** | `image`, `carousel`, `grid-view`, `hover-card` |
| **Status** | dokumentiert |

## Beschreibung
Eine Galerie ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer
Diashow zeigt. Oft bietet sie Interaktionen wie Lightbox, Zoom und Navigation.

## Verwendungszweck

- Fotogalerien zeigen
- Produktbilder präsentieren
- Portfolio-Seiten
- Screenshots zeigen
- Bildgeschichten erzählen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **raster** | gleich große Kacheln in Spalten (Standard) |
| **mosaik** | unterschiedliche Höhen, die Spalten füllen sich nach Höhe |
| **zeile** | eine Reihe, seitlich scrollbar, für wenige Bilder |

Die Abfolge einzelner Bilder ist keine Galerie-Variante mehr, sondern die eigene
Komponente [carousel](../carousel/).

## Features

- Zoom beim Hover (das Bild wächst beim Überfahren)
- Lightbox (ein Klick öffnet die große Ansicht)
- Swipe (Wischen auf dem Smartphone)
- Tastaturnavigation (Pfeiltasten)
- Touch-Gesten
- Lazy Loading (nur sichtbare Bilder laden)
- Filter (Filtern nach Kategorien)

## Abgrenzung

- **Nicht verwechseln mit** [carousel](../carousel/): der Carousel zeigt nacheinander, die
  Galerie nebeneinander (Planabschnitt 4, Zeile 14).
- **Nicht verwechseln mit** [grid-view](../../data/grid-view/): das Raster zeigt beliebige Objekte,
  die Galerie nur Bilder mit Vergrößerung.
- **Nicht verwechseln mit** [image](../../../primitives/media/image/): ein einzelnes Bild ist kein Galerie-Element.
- Die große Ansicht ist ein Overlay wie [popover](../../overlays/popover/), keine eigene Seite.

## Best Practices

- Immer einen `alt`-Text für die Barrierefreiheit angeben
- Lazy Loading für die Leistung
- Responsives Layout für Mobilgeräte
- Schnelle Ladezeiten (optimierte Bilder)
- Klare visuelle Hierarchie

## Navigations-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `images` | array[] | Array mit Bildern |
| `columns` | number | Anzahl der Spalten |
| `autoplay` | boolean | automatische Diashow? |
| `interval` | number | Intervall in ms (bei autoplay) |
| `loop` | boolean | endlose Schleife? |
| `showNavigation` | boolean | Navigation vor/zurück anzeigen? |
| `showThumbnails` | boolean | Vorschaubilder anzeigen? |

## Interaktions-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClickImage` | function | wird beim Klick auf ein Bild ausgeführt |
| `onZoom` | function | wird beim Zoomen ausgeführt |
| `onSwipe` | function | wird beim Wischen ausgeführt |
| `lightBox` | boolean | beim Klick eine Lightbox öffnen? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Bild wird größer |
| `overlay` | Overlay mit Informationen |
| `border` | der Rand leuchtet auf |
| `scale` | das Bild skaliert |

## Siehe auch

- [media – Übersicht](../index.md)
- [Basiskomponente](../../../primitives/basics/base.md)
