# media (Medien)

Band [widgets](../) – kennt seine Inhalte beim Bauen.

Elemente, die Medien wiedergeben oder darstellen. `media-player` ist die Elternklasse von `audio` und `video`.

## Elemente

- [**audio**](./audio/) – Ein Audio-Element spielt Audiodateien in verschiedenen Formaten ab.
- [**video**](./video/) – Ein Video-Element spielt Videos in verschiedenen Formaten ab.
- [**media-player**](./media-player/) – Ein Media Player spielt Videos und Audio ab.
- [**call-controls**](./call-controls/) – Anrufsteuerungen sind die Bedienleiste eines Anrufs: Mikrofon, Kamera, Bildschirmfreigabe und Auflegen.
- [**carousel**](./carousel/) – Ein Carousel zeigt Inhalte nacheinander an einer Stelle: eine Folie ist sichtbar, die anderen stehen bereit, gewechselt wird per Knopf, Wischen oder automatisch.
- [**gallery**](./gallery/) – Eine Galerie ist ein Container-Element, das mehrere Bilder in einem Raster oder in einer Diashow zeigt.

## Steckbriefe

| Komponente | Erbt von | Varianten | Rolle | Status |
|------------|----------|-----------|-------|--------|
| [audio](./audio/) | `base`, `media-player` | `einzeln`, `playlist`, `kompakt` | - | dokumentiert |
| [video](./video/) | `base`, `media-player` | `einzeln`, `hintergrund`, `live` | - | dokumentiert |
| [media-player](./media-player/) | `base` | `einzeln`, `playlist`, `steuerung` | - | dokumentiert |
| [call-controls](./call-controls/) | `base` | `bar`, `compact` | - | Skizze |
| [carousel](./carousel/) | `base`, `gallery` | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` | - | dokumentiert |
| [gallery](./gallery/) | `base` | `raster`, `mosaik`, `zeile` | - | dokumentiert |

## Siehe auch

- [Komponenten-Übersicht](../../index.md)
- [Band widgets](../)
- [Basiskomponente](../../primitives/basics/base.md)
