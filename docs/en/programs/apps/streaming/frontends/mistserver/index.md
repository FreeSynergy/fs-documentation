# MistServer

> Category: [streaming](../../index.md)

## What it is

MistServer is a lean streaming server written in C++ without transcoding: it accepts live streams (RTMP, RTSP, SRT, WebRTC/WHIP) and files and delivers them over HTTP, HLS, DASH, WebRTC, RTMP, RTSP and SRT — including a DVR buffer and push outputs. Configuration and surface run through the same JSON API on port `4242`. Licence: GPL-licensed LTS edition ("LTS") and commercial Pro edition.

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
