# Ant Media Server - Features

## Overview

AMS is the most feature-rich open-source-based streaming platform in this category: receivers, transcoding, packaging, recording, tokens, cluster and a panel — everything automatable through one REST API.

## Main features

### 1. Reception and delivery

- **Input**: RTMP, RTSP (IP cameras), SRT, WebRTC (broadcast), MP4 upload
- **Output**: WebRTC (ultra low latency), HLS, adaptive/ABR-HLS, DASH (enterprise)
- Broadcast types: live stream, IP camera, stream source, playlist

### 2. Adaptive multi-bitrate (enterprise)

- a transcoding profile with several tiers (e.g. 240p–1080p, H.264 + AAC)
- automatic rendition switching in the HLS master
- GPU encoding for high viewer numbers

### 3. Security and access

- **Publish/play tokens** (time-limited tokens per stream)
- **JWT security** (enterprise) for players and the API
- IP filter for REST calls
- RTMPS/HTTPS through uploaded certificates

### 4. Recording and VoD

- recording running streams (mp4), VoD library in the panel
- VoD upload with a processing pipeline (preview image, play list)
- playlists for A/B rotation and jingle sequence (enterprise)

### 5. Scaling

- **cluster** with origin/edge nodes over Redis
- autoscaling in AWS/Azure/GCP (AMIs/marketplace images)
- monitoring through the panel dashboard and REST statistics

### 6. Forwarding and integration

- **restreaming** to several social targets at the same time (enterprise)
- webhooks for stream events
- SDKs: web (WebSocket/WebRTC), Android, iOS, Flutter (partly enterprise)

## Editors and companion tools

| Tool | Purpose |
|------|---------|
| Web panel | streams, VoD, settings, dashboard |
| REST v2 (Swagger) | automate the panel functions (`antmedia.io/rest`) |
| the panel's own test player | check the WebRTC connection |
| Admin CLI (`antmedia-service`) | start/stop the service, status |

## What the Ant Media Server does NOT do

- **No picture mixer / no scenes** — mixing has to be done by OBS or a studio tool (❌)
- **Community version without adaptive transcoding** — multi-bitrate is enterprise (❌)
- **No DRM** in the open sense (Widevine/FairPlay not included; tokens yes, licences no) (❌)
- **No chat and no viewer profiles** (❌)
- **No ad insertion** (no server-side ad tearing) (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| OBS Studio | RTMP/SRT/WebRTC ingest into the `live` app |
| hls.js / video.js / VLC | HLS and DASH playback |
| Redis | cluster state |
| Cloud marketplaces | ready-made images (AWS, Azure, GCP) |
| your own apps | REST v2 + SDKs for panels and automation |
