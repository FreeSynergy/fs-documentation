# Streaming — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Streaming` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Ant Media Server](ant-media-server/index.md) | [latest](ant-media-server/latest/description.md) | The Ant Media Server (AMS) is a streaming platform based on Java: it accepts RTMP, RTSP, SRT and WebRTC, delivers WebRTC, HLS and DASH, can transcode (adaptive multi-bitrate) and manages streams, r… |
| [Ecamm Live](ecamm-live/index.md) | [latest](ecamm-live/latest/description.md) | Ecamm Live is a live-streaming and recording studio for the Mac. |
| [FFmpeg](ffmpeg/index.md) | [latest](ffmpeg/latest/description.md) | FFmpeg is the command-line tool collection of the FFmpeg projects: `ffmpeg` transcodes, muxes/demuxes and filters media, `ffprobe` analyses files in a machine-readable way, `ffplay` plays them as a… |
| [GStreamer](gstreamer/index.md) | [latest](gstreamer/latest/description.md) | GStreamer is a multimedia framework in C: capture, decoding, filtering, encoding and output are built as a **pipeline of elements** (source → filter/codec → sink). |
| [MediaMTX](mediamtx/index.md) | [latest](mediamtx/latest/description.md) | MediaMTX (formerly `rtsp-simple-server`) is a lean live media router in **Go**: one binary, one YAML file, and the server accepts streams and delivers them over RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS,… |
| [MistServer](mistserver/index.md) | [latest](mistserver/latest/description.md) | MistServer is a lean streaming server written in C++ without transcoding: it accepts live streams (RTMP, RTSP, SRT, WebRTC/WHIP) and files and delivers them over HTTP, HLS, DASH, WebRTC, RTMP, RTSP… |
| [nginx-rtmp-module](nginx-rtmp-module/index.md) | [latest](nginx-rtmp-module/latest/description.md) | The nginx-rtmp-module (arut) extends nginx with an RTMP server: it accepts RTMP publishes, writes along HLS and DASH streams, records, and forwards via relay. |
| [OBS Studio](obs-studio/index.md) | [latest](obs-studio/latest/description.md) | OBS Studio records screens, cameras and audio and transmits them via RTMP/SRT into streams; scenes, sources, filters and the mixer turn it into a full-fledged production tool. |
| [Owncast](owncast/index.md) | [latest](owncast/latest/description.md) | Owncast is a server for one streamer: it takes a stream from broadcasting software over RTMP, serves it to viewers in the browser and offers a built-in web chat. |
| [PeerTube](peertube/index.md) | [latest](peertube/latest/description.md) | PeerTube is free software for hosting videos and live streams. |
| [Restream](restream/index.md) | [latest](restream/latest/description.md) | Restream (restream.io) is a **cloud multistreaming service**: one encoder stream is accepted and passed on simultaneously to many platforms (YouTube, Twitch, Facebook, LinkedIn, TikTok and others). |
| [Restreamer](restreamer/index.md) | [latest](restreamer/latest/description.md) | The (Docker) Restreamer is a complete package for your own video reception and distribution: nginx + nginx-rtmp-module + Node.js web UI. |
| [StreamYard](streamyard/index.md) | [latest](streamyard/latest/description.md) | StreamYard is a live-streaming and recording studio that runs in the browser. |
| [Wowza Streaming Engine](wowza/index.md) | [latest](wowza/latest/description.md) | Wowza Streaming Engine is a **commercial media server** for live and on-demand video: it accepts streams (RTMP, RTSP, SRT, MP4 upload), shapes them with the built-in transcoder into multi-bitrate l… |
| [YouTube Studio](youtube-studio/index.md) | [latest](youtube-studio/latest/description.md) | YouTube Studio is the management area for channel owners on YouTube. |

## File set per program (ADR 0012)

```
programs/apps/streaming/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
