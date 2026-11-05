# Restreamer - Description

## What the program does

The Restreamer is a ready-made media server in a container: it receives a stream (typically
from OBS over RTMP), shows it in its own player, records it in segments and passes it on to
any number of RTMP targets.

## Advantages

- **up and running in minutes**: one container, one UI, no hand-building
- **your own domain, your own player** instead of platform pressure
- **multi-target** for streaming to several targets at the same time
- **recording included** (ffmpeg segments), without extra tools

## Differentiation

| System | Difference |
|--------|------------|
| **nginx + nginx-rtmp-module** | the same base, but without a web UI and without CLI comfort. |
| **MediaMTX** | lean protocol router (RTSP/SRT/HLS/WebRTC), no web UI with a multi-target assistant. |
| **Restream (SaaS)** | commercial service with chat, targets, analytics; the Restreamer runs on your own hardware. |
| **Wowza / MistServer / Ant Media** | professional servers with scaling and DRM, considerably more complex. |

## Technical details

- **Base**: Alpine image with nginx, nginx-rtmp-module, Node.js (web UI), ffmpeg
- **Ports**: 1935 (RTMP), 8080 (HTTP player/web UI), 8081 (HTTPS) — configurable
- **Input**: RTMP `rtmp://host:1935/live/stream?key=<pushKey>`
- **Output**: HLS `…/hls/stream.m3u8`, MP4 original, RTMP restream targets
- **Persistence**: volumes `/opt/restreamer/var/media`, `/var/statistics`
- **Licence**: MIT (datarhei/restreamer)

## Who it suits

- your own live-stream infrastructure without programming effort
- FreeSynergy streaming frontends with the model input / target / segment
- talks and meetings that are to be recorded and distributed at the same time
