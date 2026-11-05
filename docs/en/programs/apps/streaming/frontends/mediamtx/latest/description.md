# MediaMTX - Description

## Overview

MediaMTX is a "ready-to-use live media router": a single Go binary that receives video streams, records them and re-emits them over practically every relevant protocol. FreeSynergy uses it as the reference for a lean, configuration-driven streaming node.

## What MediaMTX does

An encoder (OBS, ffmpeg, camera) sends a stream to a path. MediaMTX remuxes and delivers that same stream to RTSP clients, HLS players, WebRTC browsers and SRT receivers at the same time. In addition it proxies third-party sources, records, and reports events through hooks.

## Advantages

- **One binary, zero dependencies**: no Tomcat, no database, no build system
- **A uniform model**: one path, many protocols — the port and path logic stays comprehensible
- **Clean security**: permissions as (`user`, `action`, `path`, `ips`) tuples, optionally JWT or HTTP auth
- **Operationally sound**: Prometheus metrics, PPROF, structured logs, official Docker images
- **Modern stack**: WebRTC, LL-HLS, SRT and MoQ without add-on extras

## Differentiation from other systems

### MediaMTX vs. nginx-rtmp-module

- MediaMTX is a **stand-alone server**; nginx-rtmp is a **module** inside nginx configuration
- MediaMTX offers WebRTC, SRT and MoQ; nginx-rtmp only RTMP, HLS and DASH
- MediaMTX has a documented control API; nginx-rtmp works with hook scripts

### MediaMTX vs. MistServer

- both are lightweight and without transcoding; MistServer scores with DVR and a built-in web interface
- MediaMTX scores with the YAML file, JWT/HTTP auth, MoQ and better Docker suitability
- You configure MistServer almost entirely through the API/interface, MediaMTX through the file

### MediaMTX vs. Ant Media Server / Wowza

- Ant Media and Wowza are **platforms** with transcoding, multi-bitrate, DRM and panels
- MediaMTX is deliberately lean: no transcoding, no renditions, no panel — but low latency and easy operability

## Technical details

- **Backend**: Go, one process; UDP/TCP listeners and the HTTP server in the same binary
- **Database**: none — state in `mediamtx.yml` and (optionally) API-changed paths in RAM
- **Frontend**: none; the HLS/WebRTC endpoints are consumed by browser players
- **Authentication**: `internal`, `http` or `jwt`, actions `publish`, `read`, `playback`, `api`, `metrics`, `pprof`
- **Hosting**: bare metal, Docker (`mediamtx` image), systemd service, behind a reverse proxy with TLS

## Who MediaMTX suits

- Teams that need a **streaming node of their own** without transcoding features
- IoT/camera scenarios (proxy RTSP sources, play them in the browser)
- FreeSynergy own-build: a media rail with a clear API whose logic skin developers can easily reproduce
- Not suitable when multi-bitrate renditions, DRM or recording with a timeline/ad cutter are required
