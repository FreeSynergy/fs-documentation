# Gallery (Bildergalerie)

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
Eine Gallery ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer Slideshow anzeigt. Sie bietet oft Interaktionen wie Lightbox, Zoom und Navigation.

## Verwendungszweck

- Foto-Galerien anzeigen
- Produkt-Bilder präsentieren
- Portfolio-Seiten
- Screenshots zeigen
- Bildergeschichten erzählen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **raster** | gleich große Kacheln in Spalten (Standard) |
| **mosaik** | unterschiedliche Höhen, Spalten füllen sich nach Höhe |
| **zeile** | eine Reihe seitlich scrollbar, für wenige Bilder |

Die Abfolge einzelner Bilder ist keine Galerie-Variante mehr, sondern die eigene Komponente
[carousel](../carousel/).

## Features

- Hover-Zoom (Bild vergrößert sich beim Hover)
- Lightbox (Klick öffnet Grossansicht)
- Swipe (Touch-Swipe auf Mobile)
- Keyboard-Navigation (Pfeiltasten)
- Touch-Gesten
- Lazy Loading (nur sichtbare Bilder laden)
- Filter (nach Kategorien filtern)

## Best Practices

- Immer `alt`-Text für Barrierefreiheit
- Lazy Loading für Performance
- Responsives Layout für Mobile
- Schnelle Ladezeiten (optimierte Bilder)
- Clear-Visual-Hierarchy

## Abgrenzung

- **Nicht verwechseln mit** [carousel](../carousel/): das Karussell zeigt nacheinander,
  die Galerie nebeneinander (Plan Abschnitt 4, Zeile 14).
- **Nicht verwechseln mit** [grid-view](../../data/grid-view/): das Raster zeigt beliebige Objekte,
  die Galerie ausschließlich Bilder samt Vergrößerung.
- **Nicht verwechseln mit** [image](../image/): ein einzelnes Bild ist kein Galeriemember.
- Die Großansicht ist ein Overlay wie [popover](../../overlays/popover/), keine eigene Seite.

## Navigation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `images` | array[] | Array von Bildern |
| `columns` | number | Anzahl Spalten |
| `autoplay` | boolean | Automatische Slideshow? |
| `interval` | number | Intervall in ms (bei autoplay) |
| `loop` | boolean | Endlosschleife? |
| `showNavigation` | boolean | Vor/Zurück-Navigation anzeigen? |
| `showThumbnails` | boolean | Vorschaubilder anzeigen? |

## Interaktions-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClickImage` | function | Wird beim Klick auf Bild ausgeführt |
| `onZoom` | function | Wird beim Zoom ausgeführt |
| `onSwipe` | function | Wird beim Swipe ausgeführt |
| `lightBox` | boolean | Lightbox beim Klick öffnen? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich |
| `overlay` | Overlay mit Info |
| `border` | Rand leuchtet auf |
| `scale` | Bild skaliert |

## Siehe auch

- [media – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
