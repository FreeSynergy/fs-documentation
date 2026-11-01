# GStreamer - API Dokumentation

## Übersicht

GStreamer ist prozessintern: die „API" ist die **C-Bibliothek** (plus GObject-Introspection-Bindungen). Es gibt **keine REST-API, keine Webhooks und keine Rate Limits** — wer Streams über Netze anbieten will, baut sie mit `gst-rtsp-server` oder als eigene HTTP-Schicht auf einer App-Integrationsfläche.

## Integrationsflächen

| Fläche | Wofür |
|--------|-------|
| C-API (`libgstreamer-1.0`) | Pipelines aufbauen, starten, umbauen |
| `libgstapp` (`appsrc`, `appsink`) | eigene Frames/Puffer ein- und ausspeisen |
| `gst-rtsp-server` | RTSP-Mount-Points als Bibliothek, inkl. Auth-Hooks |
| `libgstvideo` / `libgstaudio` | Format- und Pufferhilfe (Zeit, Plane, Format) |
| GObject-Introspection | Python (PyGObject), JavaScript, Rust (`gstreamer-rs`) |

## Authentifizierung

GStreamer regelt Zugang über die jeweiligen Elemente, nicht zentral:

| Quelle/Senke | Authentifizierung |
|--------------|-------------------|
| `rtspsrc` / `rtspclientsink` | Nutzer/Passwort in der URL, `user-agent` |
| `srtsrc` / `srtsink` | `passphrase` (PSK), `streamid` |
| `httpsrc` | `http-proxy`, Header via `httpconfig`-Eigenschaften |
| `webrtcbin` | Signalling ist Sache der Anwendung; SRTP/DTLS automatisch |

## C-API: Pipeline starten

```c
#include <gst/gst.h>

int main(int argc, char **argv) {
    gst_init(&argc, &argv);
    GError *err = NULL;
    GstElement *pipe = gst_parse_launch(
        "v4l2src ! videoconvert ! x264enc tune=zerolatency bitrate=2000 "
        "! rtspclientsink location=rtsp://localhost:8554/test", &err);
    if (err) { g_printerr("Pipeline: %s\n", err->message); return 1; }

    gst_element_set_state(pipe, GST_STATE_PLAYING);

    GstBus *bus = gst_element_get_bus(pipe);
    GstMessage *msg = gst_bus_poll(bus, GST_MESSAGE_EOS | GST_MESSAGE_ERROR, -1);
    if (msg->type == GST_MESSAGE_ERROR) {
        GError *e = NULL; gchar *d = NULL;
        gst_message_parse_error(msg, &e, &d);
        g_printerr("Fehler: %s\n%s\n", e->message, d);
    }
    gst_element_set_state(pipe, GST_STATE_NULL);
    return 0;
}
```

## Python (PyGObject)

```python
import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst

Gst.init(None)
pipe = Gst.parse_launch(
    "filesrc location=in.mp4 ! decodebin3 ! x264enc ! matroskamux ! "
    "filesink location=out.mkv")
pipe.set_state(Gst.State.PLAYING)

bus = pipe.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE,
                             Gst.MessageType.EOS | Gst.MessageType.ERROR)
pipe.set_state(Gst.State.NULL)
```

## appsrc / appsink (eigene Frames)

```c
GstElement *src = gst_element_factory_make("appsrc", "src");
GstAppSrc *app = GST_APP_SRC(src);
g_object_set(app, "format", GST_FORMAT_TIME, "is-live", TRUE, NULL);
GstBuffer *buf = gst_buffer_new_and_alloc(width * height * 4 /* RGBA */);
gst_app_src_push_buffer(app, buf);
```

## RTSP-Server als Bibliothek

```c
GstRTSPServer *server = gst_rtsp_server_new();
GstRTSPMountPoints *maps = gst_rtsp_server_get_mount_points(server);
GstRTSPMediaFactory *factory = gst_rtsp_media_factory_new();

/* Klammer = Media-Definition; Payloader heißt im Mount-Kontext pay0/pay1 */
gst_rtsp_media_factory_set_launch(factory,
    "( v4l2src ! videoconvert ! x264enc tune=zerolatency key-int-max=30 "
    "! rtph264pay name=pay0 pt=96 )");
gst_rtsp_media_factory_set_shared(factory, TRUE);
gst_rtsp_mount_points_add_factory(maps, "/test", factory);
gst_rtsp_server_attach(server, NULL);   /* GMainLoop laufen lassen */
```

## Build und Einbindung

```bash
pkg-config --cflags --libs gstreamer-1.0 gstreamer-app-1.0
# Rust: cargo add gstreamer gstreamer-app
```

## Debugging und Laufzeitsteuerung

| Mechanismus | Beispiel |
|-------------|----------|
| Log-Level | `GST_DEBUG=2`, `GST_DEBUG=x264enc:5` |
| Kategorien | `GST_DEBUG=*:2,RGB:4` |
| Tracer | `GST_TRACERS=latency gst-launch-1.0 ...` |
| Laufzeit-Statistik | `GST_DEBUG_BIN_TO_STDERR`, `gst_pipeline_get_latency()` |
| Registry | `GST_PLUGIN_PATH`, `gst-inspect-1.0 <element>` |

## Rate Limits und Webhooks

- **Rate Limits**: existieren nicht (kein Dienst, kein Netzwerk-Endpunkt)
- **Webhooks**: existieren nicht; Ereignisbehandlung läuft über den **Bus** (asynchrone Messages) oder über `run-command`-Wrapper der eigenen Anwendung

## SDKs und Client-Bibliotheken

- **C/C++**: `gstreamer-1.0`, `gstreamer-app-1.0`, `gstreamer-rtsp-server-1.0`
- **Python**: PyGObject (`gi.repository.Gst`)
- **Rust**: `gstreamer`, `gstreamer-app`, `gstreamer-rtsp-server`
- **JavaScript**: GObject-Introspection (GJS)
- **Plattform-Wrapper**: GStreamer-Backend in OBS Studio, Pitivi, Totem

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (diese Datei)
