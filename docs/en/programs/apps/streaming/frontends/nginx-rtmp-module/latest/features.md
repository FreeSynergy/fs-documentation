# nginx-rtmp-module - Features

## Overview

The module turns nginx into an RTMP receiver and distributor: accept publishing, write along HLS/DASH, record, pass on — all declaratively in `nginx.conf`.

## Main features

### 1. RTMP reception and distribution

- RTMP publish and play on port `1935`
- several `application` blocks (e.g. `live`, `vod`, `cam`)
- `interleave`, `wait_key`, `wait_video` for a stable transmission
- `drop_idle_publisher` and `timeout` against empty connections

### 2. Packaging

- **HLS**: segments + playlist, `hls_fragment`, `hls_playlist_length`, `hls_nested`, `hls_base_url`
- **DASH**: `dash_path`, `dash_fragment`, `dash_playlist_length`
- Delivery through the normal nginx `http` block (CORS, cache, TLS via nginx)

### 3. Recording and VoD

- `record all` / `record video` / `record audio` with `record_path`
- VoD playback through `play <path>` in the `application` block (media set)
- the `on_record_done` hook for post-processing (ffmpeg cutting, upload)

### 4. Forwarding and cluster

- `pull rtmp://…` as a relay (input from another instance)
- chains of nginx-rtmp instances for an origin/edge build

### 5. Automation

- **HTTP hooks**: `on_publish`, `on_publish_done`, `on_play`, `on_play_done`, `on_done`, `on_update`, `on_record_done`, `on_drop`
- `on_publish`/`on_play` decide on admission (HTTP status code)
- **`exec`**: one process per stream (standard: ffmpeg transcoding), variables `$(name)`, `$(app)`, `$(addr)`

## Editors and tools

| Tool | Purpose |
|------|---------|
| `nginx.conf` | the only configuration surface |
| `stat.xsl` | status page in the browser (streams, readers, bitrates) |
| ffmpeg | transcoding/preparation via `exec` |
| OBS Studio / ffmpeg | publishers onto `rtmp://host/live/<name>` |

## What the module does NOT do

- **No WebRTC, no SRT, no LL-HLS** (❌)
- **No RTMPS/TLS for RTMP** — encryption only for HLS through nginx (❌)
- **No built-in transcoding** — ffmpeg has to be wired by yourself (❌)
- **No multi-bitrate renditions** from one source without your own ffmpeg chain (❌)
- **No DRM, no token URLs** (only hook-based checking) (❌)
- **No active monitoring/alerting** beyond the status page (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| ffmpeg | `exec`/`exec_async`, `on_record_done` |
| hls.js / video.js | playback of the HLS output |
| Prometheus | translate the status XML with an exporter |
| Certbot/TLS | HTTPS for HLS in the `http` block |
