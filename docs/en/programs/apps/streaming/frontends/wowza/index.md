# Wowza Streaming Engine Documentation

## Overview

Wowza Streaming Engine is a **commercial media server** for live and on-demand video: it accepts streams (RTMP, RTSP, SRT, MP4 upload), shapes them with the built-in transcoder into multi-bitrate ladders and delivers them as HLS, low-latency HLS, CMAF, MPEG-DASH, Smooth and progressive. It is managed through the **Wowza Streaming Engine Manager** (port 8088) and the **REST Server API v2** (port 8087); configuration is done in XML files. Requires a licence, single licence per instance, Windows or Linux (JVM-based).

## File structure

- [menus.md](latest/menus.md) - Manager menus: Applications, Streaming Publishers, Connections, Add Application, Restart, Log Viewer; tabs per application
- [features.md](latest/features.md) - Protocols, transcoding, nDVR/time shift, stream targets, security/DRM, what Wowza does NOT do
- [description.md](latest/description.md) - How it differs from Restreamer, nginx-rtmp, MediaMTX, MistServer and Ant Media
- [layout.md](latest/layout.md) - Manager layout, configuration hierarchy (VHost → application → stream), ports
- [shortcuts.md](latest/shortcuts.md) - the Manager has no shortcuts; service commands and REST shortcuts
- [api.md](latest/api.md) - REST Server API v2 (Basic auth), endpoints, examples, modules instead of webhooks
