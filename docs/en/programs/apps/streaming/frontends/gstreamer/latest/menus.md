# GStreamer - Menu items

GStreamer has **no interface of its own**. "Menu items" are the tools, options and element classes with which you build and check pipelines.

## Tools (the stand-in for a menu)

| Tool | Content |
|------|---------|
| `gst-launch-1.0` | start a pipeline from the shell (`-v`, `-e` for end events) |
| `gst-inspect-1.0` | explain elements, plugins and pad properties (`gst-inspect-1.0 webrtcbin`) |
| `gst-typefind-1.0` | determine the medium/type of a file |
| `gst-discoverer-1.0` | detailed analysis: tracks, codecs, duration, bitrates |
| `gst-play-1.0` | the simplest player (playlist, shell control) |
| `gst-validate-1.0` | runtime checking of a pipeline (error reports, traces) |
| `gst-capabilities`/`gst-inspect --gst-plugin-path` | inspect the plugin registry |

## Command syntax (the "control menu")

| Symbol | Meaning |
|--------|---------|
| `!` | append the element to the previous one (pad connection) |
| `name=` | name the element in order to connect pads deliberately |
| `.name` | address a specific pad (source/sink pad) |
| `tee` / `queue` | distribution respectively decoupling of branches |
| `property=value` | set a property (`x264enc bitrate=2000 tune=zerolatency`) |
| `(` `)` | branched subgraphs, e.g. for split/merge |

## Typical element families (a selection)

| Family | Examples |
|--------|----------|
| Sources | `videotestsrc`, `v4l2src`, `pulsaaudiosrc`, `filesrc`, `appsrc` |
| Network | `rtspsrc`, `rtspclientsink`, `udpsrc`, `srtsrc`, `rtmp2src`, `webrtcbin` |
| Demux/mux | `qtdemux`, `matroskademux`, `decodebin3`, `mpegtsmux`, `matroskamux`, `hlssink` |
| Codec | `x264enc`, `vp8enc`, `vp9enc`, `avdec_h264`, `openh264enc`, `opusenc` |
| Filter | `videoconvert`, `scale`, `videoflip`, `compositor`, `audioconvert`, `volume` |
| Sinks | `fakesink`, `autovideosink`, `glimagesink`, `filesink`, `appsink` |

## Menus by role

| Role | Access |
|------|--------|
| User | `gst-play-1.0`, finished apps (Totem, the OBS plugin) |
| Developer | C/Python API, `appsrc`/`appsink`, pad probes |
| Operations | plugin registry, `GST_PLUGIN_PATH`, `GST_DEBUG`, `gst-inspect-1.0` |
