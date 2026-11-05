# GStreamer - Structure & UI/UX

## Overview

GStreamer has no window. "Structure" here means the build of a pipeline and the places where a program (or a skin) intervenes: the element chain, pads, bus and state machine.

## Model of a pipeline

### Main areas

```
Source            Filter / conversion          Encoding           Sink
┌───────────┐     ┌──────────────────────┐      ┌───────────┐   ┌────────────────┐
│ v4l2src   │ --> │ videoconvert → scale │ -->  │ x264enc   │-> │ rtspclientsink │
└───────────┘     └──────────────────────┘      └───────────┘   └────────────────┘
      │           Pads negotiate caps            properties        │
      └── Bus: EOS / error / tags / latency ────────────────────────┘
```

### Elements

- **Source**: delivers buffers (`filesrc`, `v4l2src`, `appsrc`, `udpsrc`)
- **Filter**: changes data (`scale`, `videoconvert`, `audioconvert`)
- **Codec**: `x264enc`, `avdec_h264`, `opusenc` — mostly from base/good/bad/ugly
- **Sink**: consumes buffers (`fakesink`, `autovideosink`, `filesink`, `appsink`)
- **Muxer/demuxer**: `matroskamux`, `qtdemux`, `hlssink`
- **Bins**: `decodebin3` (automatic), `tee` + `queue` (branching)

### State machine

```
NULL → READY → PAUSED → PLAYING
```

On a `PAUSED` start, buffers are filled up to the sync point; `PLAYING` releases them.

## UI structure of your own apps (reference)

```
┌───────────────────────────────────────────────┐
│ Title bar / transport (play, pause, stop)     │
├───────────────────────────────────────────────┤
│ Video/sink area (autovideosink, gtksink)      │
├───────────────────────────────────────────────┤
│ Status: position, codec, bitrate, latency     │
└───────────────────────────────────────────────┘
```

## UI/UX

### Design principles

- **Explicit instead of magical**: pads and caps are negotiated visibly — error messages name the element and the pad
- **Errors travel over the bus**: applications react to `ERROR`/`WARNING`/`EOS`, not to exit codes
- **No global defaults**: each pipeline carries its own properties

### Interactions

- `sync=false` for preview branches (faster, but irregular)
- **Seek/snapshot**: through `GstStream` events or `gst_element_send_event`, not through keys
- **Dynamic rebuilding**: attach/detach pads at runtime (hotplug, track switching)

## Accessibility

- No interface of its own → accessibility hangs on the app's toolkit (GTK/Qt)
- Text and subtitle elements (`subtitleoverlay`) provide the basis for captions
- Debug output is machine-readable and easy to filter (`GST_DEBUG_CATEGORY`)

## Performance

- Buffer pools avoid copies between elements
- Queues with `max-size-buffers` limit latency and RAM
- Hardware elements (`vaapipostproc`, `nvv4l2decoder`) keep frames in GPU memory
- `GST_TRACERS` (e.g. `latency`, `schedtime`) for measurements during operation
