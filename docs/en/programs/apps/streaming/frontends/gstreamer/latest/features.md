# GStreamer - Features

## Overview

GStreamer is a construction kit: almost everything — capture, transcoding, streaming, playback, recording — arises from combinable elements. It supplies no finished application, but the runtime and the building blocks for one.

## Main features

### 1. Building pipelines

- **Elements and pads**: sources, filters, encoders and sinks are connected via pads with negotiated capabilities (`Caps`)
- **Bins and `decodebin3`**: automatic detection of demuxer/decoder chains
- **Bus and messages**: `EOS`, errors, state changes, latency and tag messages
- **State model**: `NULL` → `READY` → `PAUSED` → `PLAYING` for a controlled start

### 2. Live streaming and low latency

- **WebRTC**: `webrtcbin` with ICE/DTLS/SRTP, WHIP-like integration through your own handlers
- **SRT/RTMP/RTSP/MPEG-TS**: `srtsrc`/`srtsink`, `rtmp2src`/`rtmp2sink`, `rtspsrc`/`rtspclientsink`, `mpegtsmux`, `udpsrc`/`udpsink`
- **Writing and reading HLS/DASH**: `hlssink`, `dashdemux`/`hlssink` combinations, `hlsdemux`
- **`tune=zerolatency`** on encoders, `sync=false` for demo branches

### 3. Editing picture and sound

- **Compositing**: `compositor`, `glvideomixerelement`, overlays, green screen (`gscreenseg`)
- **Scaling/colours**: `scale`, `videoconvert`, `videoflip`, `videobox`, colour metadata
- **Audio**: `audioconvert`, `mixer`, `volume`, `audiofx` elements, loudness chains
- **Text/subtitles**: `subtitleoverlay`, `rsvgoverlay`, `textoverlay`

### 4. Hardware and performance

- **GPU/codec acceleration**: `vaapi*`, `nvcodec` (NVEnc/NVDec), `qsv`, `v4l2*` (embedded), `vulkan`, `glupload`
- **Parallelism**: bins, queues and threads per element; `GST_DEBUG=*:5` for runtime analysis
- **Memory control**: buffer pools, `leaky` queues, `max-size-buffers`

## Editors and companion tools

| Tool | Purpose |
|------|---------|
| `gst-launch-1.0` | test pipelines interactively |
| `gst-inspect-1.0` | documentation of all elements and properties |
| `gst-discoverer-1.0` | media analysis in the terminal |
| `gst-validate-1.0` | quality checking of pipelines |
| GST Editing Services (GES) | timeline/editing library for your own editors |

## Comparing the approaches

| Approach | Strength | Weakness |
|----------|----------|----------|
| `gst-launch-1.0` | fastest pipeline, no code | no dynamic control |
| C API | full control, probes, signals | effort, needs GObject type knowledge |
| `appsrc`/`appsink` | feed your own frames in/out | handle copies and timing yourself |
| GES | timeline, clips, cuts | own interface needed |

## What GStreamer does NOT do

- **No finished GUI** — without your own or a third-party app there is no window (❌)
- **No streaming server out of the box** — `gst-rtsp-server` is a library, not a service (❌)
- **No multi-bitrate packaging** with a master playlist from one source (❌)
- **No scene mixer like OBS** — compositing has to be wired by yourself (❌)
- **No DRM** and no licence-server integration (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| Plugins (base/good/bad/ugly) | C modules, detected at runtime |
| `appsrc`/`appsink` | connection to your own programs (libgstapp) |
| gst-rtsp-server | RTSP endpoints as mount points |
| gst-python (PyGObject), gstreamer-rs | scripting and a modern language binding |
| OBS Studio, Pitivi, Totem | applications based on GStreamer |
