# media (Medien)

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

## Elemente

- [**audio**](./audio/) – Ein Audio-Element wiedergibt Audiodateien in verschiedenen Formaten.
- [**carousel**](./carousel/) – Ein Karussell zeigt Inhalte nacheinander an einer Stelle: eine Folie sichtbar, die anderen bereit, gewechselt per Knopf, Wisch oder automatisch.
- [**gallery**](./gallery/) – Eine Gallery ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer Slideshow anzeigt.
- [**icon**](./icon/) – Ein Icon ist ein symbolisches Grafikelement, das eine Funktion oder ein Objekt visuell repräsentiert.
- [**image**](./image/) – Ein Bild-Element zeigt Grafiken, Fotos oder andere visuelle Inhalte an.
- [**media-player**](./media-player/) – Ein Media Player wiedergibt Videos und Audios.
- [**video**](./video/) – Ein Video-Element wiedergibt Videos in verschiedenen Formaten.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [audio](./audio/) | `base`, `media-player` | `einzeln`, `playlist`, `kompakt` | - | dokumentiert |
| [carousel](./carousel/) | `base`, `gallery` | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` | - | dokumentiert |
| [gallery](./gallery/) | `base` | `raster`, `mosaik`, `zeile` | - | dokumentiert |
| [icon](./icon/) | `base` | `outline`, `gefüllt`, `animiert` | - | dokumentiert |
| [image](./image/) | `base` | `einfach`, `vignette`, `hintergrund` | - | dokumentiert |
| [media-player](./media-player/) | `base` | `einzeln`, `playlist`, `steuerung` | - | dokumentiert |
| [video](./video/) | `base`, `media-player` | `einzeln`, `hintergrund`, `live` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../index.md)
- [Basiskomponente](../basics/base/)
