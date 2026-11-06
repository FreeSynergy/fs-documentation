# MediaMTX

> Category: [streaming](../../index.md)

## What it is

MediaMTX (formerly `rtsp-simple-server`) is a lean live media router in **Go**: one binary, one YAML file, and the server accepts streams and delivers them over RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS, MPEG-TS, RTP and MoQ. It does not transcode, but muxes/remuxes and distributes. Stack: Go, MIT licence, configuration via `mediamtx.yml`, control via the control API (port 9997).

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
