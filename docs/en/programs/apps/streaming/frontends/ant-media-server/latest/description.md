# Ant Media Server - Description

## Overview

The Ant Media Server is a fully grown streaming platform: a Java/Tomcat process with RTMP, RTSP, SRT and WebRTC reception, built-in transcoding and multi-bitrate packaging, a panel and a REST API. A free community edition and a paid enterprise edition.

## What the Ant Media Server does

Streams are received through applications (`live`, `WebRTCAppEE`, your own). The server transcodes into several tiers where needed, packages into HLS/WebRTC/DASH, records and provides playlists. Cluster nodes (origin/edge) scale the viewer load. Everything the panel shows can be called through REST.

## Advantages

- **Everything from one source**: ingest, transcoding, packaging, recording, tokens, cluster
- **Ultra low latency** via WebRTC with SDKs for web, Android, iOS
- **Automatable**: complete REST v2 coverage (broadcasts, VoD, management, cluster)
- **Production-ready**: cloud images, Redis cluster, monitoring, commercial support
- **Free to start**: the community edition under the MIT licence

## Differentiation from other systems

### Ant Media Server vs. Wowza Streaming Engine

- both are platforms with a panel and transcoding; Wowza is commercial with licence fees, AMS has a free base
- Wowza scores with RIST, broader DRM support and its add-on ecosystem
- AMS scores with WebRTC SDKs, cloud scaling and free REST API coverage

### Ant Media Server vs. MediaMTX

- MediaMTX is deliberately lean (Go, no transcoding, YAML, control API)
- AMS brings transcoding, tokens, a VoD library and a panel — considerably more complexity and resource demand
- For FreeSynergy skins: MediaMTX as the simple node, AMS as the platform template

### Ant Media Server vs. MistServer

- MistServer without transcoding, but tiny and entirely API-driven
- AMS is heavier (Java, Tomcat), but with adaptive bitrate and cluster
- The licence models differ markedly (GPL vs. MIT/enterprise)

## Technical details

- **Backend**: Java (servlet container Tomcat), ingest media library based on FFmpeg, in-memory statistics
- **Database**: Derby/PostgreSQL for app metadata, Redis for cluster state
- **Frontend**: web panel (JavaScript) on `5080`/`5443`
- **Authentication**: panel login, REST via IP filter or JWT, media through publish/play tokens
- **Hosting**: bare metal, Docker, VMs, AWS/Azure/GCP marketplace images, Kubernetes-capable

## Who the Ant Media Server suits

- Teams that want to operate a **complete streaming platform** (transcoding + packaging + tokens + cluster) themselves
- WebRTC products with very low latency (video apps, events, auctions)
- FreeSynergy architectures that need a reference for "streaming as a platform"
- Less suitable as a side component on small hardware — for that MediaMTX/MistServer
