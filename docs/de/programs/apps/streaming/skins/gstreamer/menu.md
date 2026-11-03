# GStreamer - Menüpunkte

GStreamer hat **keine eigene Oberfläche**. „Menüpunkte" sind die Werkzeuge, Optionen und Element-Klassen, mit denen man Pipelines baut und prüft.

## Werkzeuge (Ersatz für ein Menü)

| Werkzeug | Inhalt |
|----------|--------|
| `gst-launch-1.0` | Pipeline aus der Shell starten (`-v`, `-e` für Ende-Events) |
| `gst-inspect-1.0` | Elemente, Plugins und Pad-Eigenschaften erklären (`gst-inspect-1.0 webrtcbin`) |
| `gst-typefind-1.0` | Medium/Typ einer Datei ermitteln |
| `gst-discoverer-1.0` | Detail-Analyse: Tracks, Codecs, Dauer, Bitraten |
| `gst-play-1.0` | simplest Abspieler (Playlist, Shell-Steuerung) |
| `gst-validate-1.0` | Laufzeit-Prüfung einer Pipeline (Fehlerberichte, Traces) |
| `gst-capabilities`/`gst-inspect --gst-plugin-path` | Plugin-Registry untersuchen |

## Kommando-Syntax (das „Bedienmenü")

| Symbol | Bedeutung |
|--------|-----------|
| `!` | Element an das vorherige anhängen (Pad-Verbindung) |
| `name=` | Element benennen, um Pads gezielt zu verbinden |
| `.name` | bestimmtes Pad ansprechen (Quell-/Senken-Pad) |
| `tee` / `queue` | Verteilung bzw. Entkopplung von Zweigen |
| `property=value` | Eigenschaft setzen (`x264enc bitrate=2000 tune=zerolatency`) |
| `(` `)` | verzweigte Teilgraphen, z. B. für Split/Merge |

## Typische Element-Familien (Auswahl)

| Familie | Beispiele |
|---------|-----------|
| Quellen | `videotestsrc`, `v4l2src`, `pulsaaudiosrc`, `filesrc`, `appsrc` |
| Netzwerk | `rtspsrc`, `rtspclientsink`, `udpsrc`, `srtsrc`, `rtmp2src`, `webrtcbin` |
| Demux/Mux | `qtdemux`, `matroskademux`, `decodebin3`, `mpegtsmux`, `matroskamux`, `hlssink` |
| Codec | `x264enc`, `vp8enc`, `vp9enc`, `avdec_h264`, `openh264enc`, `opusenc` |
| Filter | `videoconvert`, `scale`, `videoflip`, `compositor`, `audioconvert`, `volume` |
| Senken | `fakesink`, `autovideosink`, `glimagesink`, `filesink`, `appsink` |

## Menüs nach Rolle

| Rolle | Zugriff |
|-------|---------|
| Anwender | `gst-play-1.0`, fertige Apps (Totem, OBS-Plugin) |
| Entwickler | C-/Python-API, `appsrc`/`appsink`, Pad-Probes |
| Betrieb | Plugin-Registry, `GST_PLUGIN_PATH`, `GST_DEBUG`, `gst-inspect-1.0` |
