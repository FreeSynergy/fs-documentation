# MediaMTX - Features

## Overview

MediaMTX is a **media router**: it accepts streams (or fetches them) and provides them over all supported protocols — without re-encoding. Configuration, auth and hooks happen declaratively in YAML.

## Main features

### 1. Protocol variety

- **Receiving and sending**: RTSP/RTSPS, RTMP/RTMPS, SRT, WebRTC (WHIP/WHEP), MPEG-TS, RTP/UDP
- **Delivery in the browser**: HLS, low-latency HLS, fMP4 segments, WebRTC
- **MoQ (Media over QUIC)**: natively over QUIC and over WebTransport
- **Conversion only in the container**: remux RTSP→HLS→WebRTC without transcoding

### 2. Paths and forwarding

- a static path list plus `all`/RegExp wildcards
- **Proxy mode**: `source: rtsps://camera:8322/stream` fetches externally and distributes internally
- **Relay**: couple several MediaMTX instances (publish to another instance)
- `sourceOnDemand`, `runOnDemand`: start sources on demand (e.g. an ffmpeg command)

### 3. Security and access

- `authMethod: internal` with users, actions and path patterns
- external HTTP auth (`authHTTPAddress`) or **JWT** (`authJWTJWKS`, claim `mediamtx_permissions`)
- IP/CIDR lists per user, `apiTrustedProxies`, PROXY protocol for RTSP
- Encryption: RTSPS, RTMPS, HTTPS for HLS/WebRTC/API (`*Encryption`, server key/cert)

### 4. Recording and playback

- recording into `fmp4`, `mp4`, `mpeg-ts` (`recordFormat`, `recordPartDuration`, `recordSegmentDuration`)
- **playback server** (`:9996`) lists and serves recordings
- `recordMode: auto|disk|memory`, the deletion age (`recordDeleteAge`) is derived from the filename pattern

### 5. Automation and operation

- **Hooks**: `runOnConnect`, `runOnPublish`, `runOnPublishDone`, `runOnUnpublish`, `runOnReady`, `runOnDemand` (shell commands with `MTX_*` variables)
- **Control API v3** (`:9997`) for paths, connections, retransmission, dynamic paths
- **Metrics** (`:9998`, Prometheus) and **PPROF** (`:9999`)
- structured logs (`logStructured: true` → JSONL), `logDestinations: syslog`

## Editors and tools

| Access | Purpose |
|--------|---------|
| `mediamtx.yml` | central, declarative configuration |
| Control API | changes at runtime (create/delete paths) |
| `MTX_*` environment variables | container configuration without a file |
| `ffprobe`/VLC | external checking of the endpoints |

## What MediaMTX does NOT do

- **No transcoding, no scaling, no watermarks** — the encoding stays unchanged (❌)
- **No multi-bitrate packaging** from one source (no adapter/rendition chain) (❌)
- **No DRM** and no token URLs for HLS (only the auth methods) (❌)
- **No web interface** (only API and YAML) (❌)
- **No chat, no viewer management, no platform publishers** (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| ffmpeg | as a `runOnDemand`/`runOnPublish` hook or an external source |
| OBS Studio | RTMP/SRT/WebRTC publish straight to MediaMTX |
| Prometheus/Grafana | metrics from `:9998` |
| nginx/caddy | TLS and routing in front of HLS/WebRTC/API |
| Docker | official images, config by file or env |
