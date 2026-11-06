# Streaming systems

**`FreeSynergy.Streaming` (`fs-streaming`) is planned, no code yet.** See the [design](design.md), the [requirements](requirements.md) and the [roadmap](../roadmap.md).

## Overview

Streaming systems accept live or pre-produced video material, process it (transcoding, recording, packaging) and distribute it to viewers or to foreign platforms. The category covers the whole chain: encoders (OBS), protocol routers (MediaMTX, FFmpeg, GStreamer), media servers (nginx-rtmp, Restreamer, MistServer, Ant Media, Wowza) and cloud multistreaming (Restream).

## Available systems

- **obs-studio** - Scene/encoder software for recording and streaming
- **ffmpeg** - Command-line toolkit for encoding, remixing, RTMP push
- **gstreamer** - Modular multimedia pipeline as a library and CLI
- **mediamtx** - Lean protocol router (RTSP/RTMP/HLS/SRT/WebRTC)
- **nginx-rtmp-module** - RTMP reception and HLS delivery as an nginx module
- **restreamer** - Docker complete package: reception, player, recording, multi-target
- **restream** - Cloud multistreaming service (restream.io) with chat and analytics
- **mistserver** - Light media server with built-in HTTP management
- **ant-media-server** - Professional media server with WebRTC and cluster
- **wowza** - Commercial media server with Manager, REST API and DRM

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (10), by function, nothing copied (ADR 0012/0013):

- [Ant Media Server](frontends/ant-media-server/index.md) — The Ant Media Server (AMS) is a streaming platform based on Java: it accepts RTMP, RTSP, SRT and WebRTC, delivers WebRTC, HLS and DASH, can transcode (adaptive multi-bitrate) and manages streams, r…
- [FFmpeg](frontends/ffmpeg/index.md) — FFmpeg is the command-line tool collection of the FFmpeg projects: `ffmpeg` transcodes, muxes/demuxes and filters media, `ffprobe` analyses files in a machine-readable way, `ffplay` plays them as a…
- [GStreamer](frontends/gstreamer/index.md) — GStreamer is a multimedia framework in C: capture, decoding, filtering, encoding and output are built as a **pipeline of elements** (source → filter/codec → sink).
- [MediaMTX](frontends/mediamtx/index.md) — MediaMTX (formerly `rtsp-simple-server`) is a lean live media router in **Go**: one binary, one YAML file, and the server accepts streams and delivers them over RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS,…
- [MistServer](frontends/mistserver/index.md) — MistServer is a lean streaming server written in C++ without transcoding: it accepts live streams (RTMP, RTSP, SRT, WebRTC/WHIP) and files and delivers them over HTTP, HLS, DASH, WebRTC, RTMP, RTSP…
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) — The nginx-rtmp-module (arut) extends nginx with an RTMP server: it accepts RTMP publishes, writes along HLS and DASH streams, records, and forwards via relay.
- [OBS Studio](frontends/obs-studio/index.md) — OBS Studio records screens, cameras and audio and transmits them via RTMP/SRT into streams; scenes, sources, filters and the mixer turn it into a full-fledged production tool.
- [Restream](frontends/restream/index.md) — Restream (restream.io) is a **cloud multistreaming service**: one encoder stream is accepted and passed on simultaneously to many platforms (YouTube, Twitch, Facebook, LinkedIn, TikTok and others).
- [Restreamer](frontends/restreamer/index.md) — The (Docker) Restreamer is a complete package for your own video reception and distribution: nginx + nginx-rtmp-module + Node.js web UI.
- [Wowza Streaming Engine](frontends/wowza/index.md) — Wowza Streaming Engine is a **commercial media server** for live and on-demand video: it accepts streams (RTMP, RTSP, SRT, MP4 upload), shapes them with the built-in transcoder into multi-bitrate l…

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->

## Frontend documentation

The programs in this category are documented following the wiki schema (seven files per program: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) under `programs/apps/streaming/frontends/<program>/`.

**documented (10 programs):**

- [Ant Media Server](frontends/ant-media-server/index.md) - Ant Media Server
- [FFmpeg](frontends/ffmpeg/index.md) - FFmpeg
- [GStreamer](frontends/gstreamer/index.md) - GStreamer
- [MediaMTX](frontends/mediamtx/index.md) - MediaMTX
- [MistServer](frontends/mistserver/index.md) - MistServer
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) - nginx-rtmp-module
- [OBS Studio](frontends/obs-studio/index.md) - OBS Studio
- [Restream](frontends/restream/index.md) - Restream
- [Restreamer](frontends/restreamer/index.md) - Restreamer
- [Wowza Streaming Engine](frontends/wowza/index.md) - Wowza Streaming Engine

Overview: [Frontend directory](frontends/index.md)

Reference schema: [Wiki frontends](../wiki/frontends/index.md) · [Desktop frontends](../../platform/desktop/frontends/index.md) · [Standardised data](../../../data/api.md)
