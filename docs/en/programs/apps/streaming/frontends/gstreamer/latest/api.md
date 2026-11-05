# GStreamer - API documentation

## Overview

GStreamer is process-internal: the "API" is the **C library** (plus GObject introspection bindings). There is **no REST API, no webhooks and no rate limits** — anyone who wants to offer streams over networks builds them with `gst-rtsp-server` or as their own HTTP layer on an app integration surface.

## Integration surfaces

| Surface | For what |
|---------|----------|
| C API (`libgstreamer-1.0`) | build, start and rebuild pipelines |
| `libgstapp` (`appsrc`, `appsink`) | feed your own frames/buffers in and out |
| `gst-rtsp-server` | RTSP mount points as a library, incl. auth hooks |
| `libgstvideo` / `libgstaudio` | format and buffer helpers (time, planes, format) |
| GObject introspection | Python (PyGObject), JavaScript, Rust (`gstreamer-rs`) |

## Authentication

GStreamer regulates access through the respective elements, not centrally:

| Source/sink | Authentication |
|-------------|----------------|
| `rtspsrc` / `rtspclientsink` | user/password in the URL, `user-agent` |
| `srtsrc` / `srtsink` | `passphrase` (PSK), `streamid` |
| `httpsrc` | `http-proxy`, headers via `httpconfig` properties |
| `webrtcbin` | signalling is the application's job; SRTP/DTLS automatic |

## C API: starting a pipeline

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
        g_printerr("Error: %s\n%s\n", e->message, d);
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

## appsrc / appsink (your own frames)

```c
GstElement *src = gst_element_factory_make("appsrc", "src");
GstAppSrc *app = GST_APP_SRC(src);
g_object_set(app, "format", GST_FORMAT_TIME, "is-live", TRUE, NULL);
GstBuffer *buf = gst_buffer_new_and_alloc(width * height * 4 /* RGBA */);
gst_app_src_push_buffer(app, buf);
```

## RTSP server as a library

```c
GstRTSPServer *server = gst_rtsp_server_new();
GstRTSPMountPoints *maps = gst_rtsp_server_get_mount_points(server);
GstRTSPMediaFactory *factory = gst_rtsp_media_factory_new();

/* Brackets = media definition; in the mount context the payloader is called pay0/pay1 */
gst_rtsp_media_factory_set_launch(factory,
    "( v4l2src ! videoconvert ! x264enc tune=zerolatency key-int-max=30 "
    "! rtph264pay name=pay0 pt=96 )");
gst_rtsp_media_factory_set_shared(factory, TRUE);
gst_rtsp_mount_points_add_factory(maps, "/test", factory);
gst_rtsp_server_attach(server, NULL);   /* let the GMainLoop run */
```

## Build and inclusion

```bash
pkg-config --cflags --libs gstreamer-1.0 gstreamer-app-1.0
# Rust: cargo add gstreamer gstreamer-app
```

## Debugging and runtime control

| Mechanism | Example |
|-----------|---------|
| Log level | `GST_DEBUG=2`, `GST_DEBUG=x264enc:5` |
| Categories | `GST_DEBUG=*:2,RGB:4` |
| Tracer | `GST_TRACERS=latency gst-launch-1.0 ...` |
| Runtime statistics | `GST_DEBUG_BIN_TO_STDERR`, `gst_pipeline_get_latency()` |
| Registry | `GST_PLUGIN_PATH`, `gst-inspect-1.0 <element>` |

## Rate limits and webhooks

- **Rate limits**: do not exist (no service, no network endpoint)
- **Webhooks**: do not exist; event handling runs over the **bus** (asynchronous messages) or over `run-command` wrappers of your own application

## SDKs and client libraries

- **C/C++**: `gstreamer-1.0`, `gstreamer-app-1.0`, `gstreamer-rtsp-server-1.0`
- **Python**: PyGObject (`gi.repository.Gst`)
- **Rust**: `gstreamer`, `gstreamer-app`, `gstreamer-rtsp-server`
- **JavaScript**: GObject introspection (GJS)
- **Platform wrappers**: the GStreamer backend in OBS Studio, Pitivi, Totem

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
