# MistServer - Features

## Overview

MistServer specialises in **reception, distribution and recording** without its own picture processing: one input, many outputs, push rules and a DVR buffer per stream.

## Main features

### 1. Inputs (sources)

| Source | Syntax / route |
|--------|----------------|
| Live push | `push://` (RTMP, RTSP, SRT, WebRTC), optionally an IP whitelist or a password |
| SRT listener | `srt://:9876` |
| WHIP | `http://host:8080/webrtc/streamname` |
| File / folder | `/media/example.mp4`, a folder for the VoD selection |
| MPEG-TS over UDP | `tsudp://239.0.0.1:9876/` (multicast, interface selectable) |
| Pull over HTTP | `http://…/index.m3u8` (HLS) |
| Stream keys | a token instead of the stream name in the push target |

### 2. Outputs (protocols)

- HTTP progressive (MP4/FLV/WebM), **HLS**, **DASH**, **WebRTC**
- RTMP, RTSP, SRT as viewer protocols (per activated connector)
- Track selection per protocol (the last compatible track as the default)

### 3. Push and recording

- **Automatic push**: a rule per stream, starts on activity (also time-/variable-controlled)
- **Single push**: start once; no automatic restart on errors
- **Recording** counts as a push to a local path; `.ts`/`.mkv` recommended, MP4 as fMP4
- Several automatic-push rules per stream are possible

### 4. Buffers and security

- the **DVR buffer** is configurable per stream (`DVR` in milliseconds)
- rights only on the API interface (login, challenge hash), the media ports without users
- push access gradable through IP whitelist, password or stream key

## Editors and companion tools

| Tool | Purpose |
|------|---------|
| Web interface (`:4242`) | the protocol, streams and push pages |
| JSON API (`command` parameter) | automate the complete configuration |
| `config.json` / `/etc/mistserver.conf` | direct configuration (the expert route) |
| MistServer statistics (`stats_streams`) | viewer counts and live position |

## What MistServer does NOT do

- **No transcoding, no scaling, no renditions** (❌)
- **No picture mixer, no overlays, no scenes** (❌)
- **No multi-bitrate HLS master** from one source (❌)
- **No DRM and no token-protected playback** (❌)
- **No chat, no social publishers, no viewer management** (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| OBS Studio | push via RTMP/SRT/WebRTC onto a `push://` stream |
| ffmpeg | as a push target or source (`tsudp`, HLS) |
| Docker | official images, ports and volumes configurable |
| Monitoring | the API's statistics commands (`stats_streams`, `clients`) |
