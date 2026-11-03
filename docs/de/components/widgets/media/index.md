# media (Medien)

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

## Elemente

- [**audio**](./audio/) – Ein Audio-Element wiedergibt Audiodateien in verschiedenen Formaten.
- [**video**](./video/) – Ein Video-Element wiedergibt Videos in verschiedenen Formaten.
- [**media-player**](./media-player/) – Ein Media Player wiedergibt Videos und Audios.
- [**carousel**](./carousel/) – Ein Karussell zeigt Inhalte nacheinander an einer Stelle: eine Folie sichtbar, die anderen bereit, gewechselt per Knopf, Wisch oder automatisch.
- [**gallery**](./gallery/) – Eine Gallery ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer Slideshow anzeigt.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [audio](./audio/) | `base`, `media-player` | `einzeln`, `playlist`, `kompakt` | - | dokumentiert |
| [video](./video/) | `base`, `media-player` | `einzeln`, `hintergrund`, `live` | - | dokumentiert |
| [media-player](./media-player/) | `base` | `einzeln`, `playlist`, `steuerung` | - | dokumentiert |
| [carousel](./carousel/) | `base`, `gallery` | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` | - | dokumentiert |
| [gallery](./gallery/) | `base` | `raster`, `mosaik`, `zeile` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band widgets](../)
- [Basiskomponente](../../primitives/basics/base.md)
