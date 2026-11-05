# media

Band [widgets](../) – knows its contents when it is built.

Elements that play or show media. `media-player` is the parent class of `audio`
and `video`.

## Elements

- [**audio**](./audio/) – An audio element plays audio files in various formats.
- [**call-controls**](./call-controls/) – Call controls are the control bar of a call: microphone, camera, screen sharing, hang up.
- [**carousel**](./carousel/) – A carousel shows contents one after another in a single place: one slide visible, the others ready, switched by button, swipe or automatically.
- [**gallery**](./gallery/) – A gallery is a container element that shows several images in a grid or in a slideshow.
- [**media-player**](./media-player/) – A media player plays videos and audio.
- [**video**](./video/) – A video element plays videos in various formats.

## Profiles

| Component | Inherits from | Variants | Role | Status |
|-----------|---------------|----------|------|--------|
| [audio](./audio/) | `base`, `media-player` | `einzeln`, `playlist`, `kompakt` | - | documented |
| [call-controls](./call-controls/) | `base` | `bar`, `compact` | - | skeleton |
| [carousel](./carousel/) | `base`, `gallery` | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` | - | documented |
| [gallery](./gallery/) | `base` | `raster`, `mosaik`, `zeile` | - | documented |
| [media-player](./media-player/) | `base` | `einzeln`, `playlist`, `steuerung` | - | documented |
| [video](./video/) | `base`, `media-player` | `einzeln`, `hintergrund`, `live` | - | documented |

## See also

- [Component overview](../../index.md)
- [Band widgets](../)
- [Base component](../../primitives/basics/base.md)
