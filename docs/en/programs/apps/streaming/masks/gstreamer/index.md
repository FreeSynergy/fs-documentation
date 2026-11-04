# GStreamer Documentation

## Overview

GStreamer is a multimedia framework in C: capture, decoding, filtering, encoding and output are built as a **pipeline of elements** (source → filter/codec → sink). Tools such as `gst-launch-1.0` and `gst-inspect-1.0` provide access to the system through the shell, and custom programs use the C API (or Python/Rust bindings). Stack: C + GObject, LGPL 2.1, packages base/good/bad/ugly, WebRTC via `webrtcbin`.

## File structure

- [menu.md](menu.md) - Tools, command syntax, element inspection, roles
- [features.md](features.md) - Elements, containers, hardware, WebRTC, what GStreamer does NOT do
- [description.md](description.md) - How it differs from ffmpeg, OBS Studio, MediaMTX and MistServer
- [structure.md](structure.md) - Pipeline model, pads/caps, bus, states, debugging tools
- [shortcuts.md](shortcuts.md) - Keys in `gst-play-1.0`, options of the CLI tools
- [api.md](api.md) - C API, appsrc/appsink, gst-rtsp-server, bindings, debugging environment
