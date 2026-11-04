# Ant Media Server Documentation

## Overview

The Ant Media Server (AMS) is a streaming platform based on Java: it accepts RTMP, RTSP, SRT and WebRTC, delivers WebRTC, HLS and DASH, can transcode (adaptive multi-bitrate) and manages streams, recordings and clusters through a web panel and a REST API. There is a Community (MIT) and an Enterprise edition.

## File structure

- [menu.md](menu.md) - Web panel: apps, live streaming, VoD, settings, cluster
- [features.md](features.md) - Protocols, adaptive streaming, tokens, restreaming, what AMS does NOT do
- [description.md](description.md) - How it differs from Wowza, MediaMTX and MistServer
- [structure.md](structure.md) - Tomcat layout, application model, ports and panel layout
- [shortcuts.md](shortcuts.md) - Server command line and service management
- [api.md](api.md) - REST v2 (broadcasts, VoD, management), JWT/IP filter, webhooks, SDKs
