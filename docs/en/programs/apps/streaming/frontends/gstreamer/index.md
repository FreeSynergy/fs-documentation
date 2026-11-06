# GStreamer

> Category: [streaming](../../index.md)

## What it is

GStreamer is a multimedia framework in C: capture, decoding, filtering, encoding and output are built as a **pipeline of elements** (source → filter/codec → sink). Tools such as `gst-launch-1.0` and `gst-inspect-1.0` provide access to the system through the shell, and custom programs use the C API (or Python/Rust bindings). Stack: C + GObject, LGPL 2.1, packages base/good/bad/ugly, WebRTC via `webrtcbin`.

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
