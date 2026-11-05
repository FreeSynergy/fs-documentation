# Wowza Streaming Engine

> Category: [streaming](../../index.md)

## What it is

Wowza Streaming Engine is a **commercial media server** for live and on-demand video: it accepts streams (RTMP, RTSP, SRT, MP4 upload), shapes them with the built-in transcoder into multi-bitrate ladders and delivers them as HLS, low-latency HLS, CMAF, MPEG-DASH, Smooth and progressive. It is managed through the **Wowza Streaming Engine Manager** (port 8088) and the **REST Server API v2** (port 8087); configuration is done in XML files. Requires a licence, single licence per instance, Windows or Linux (JVM-based).

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->
