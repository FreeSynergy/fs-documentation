# nginx-rtmp-module Documentation

## Overview

The nginx-rtmp-module (arut) extends nginx with an RTMP server: it accepts RTMP publishes, writes along HLS and DASH streams, records, and forwards via relay. Configuration happens exclusively through `nginx.conf`; control runs through HTTP hooks and the status page. Written in C, BSD-licensed, for years without substantial further development — WebRTC and SRT are missing.

## File structure

- [menu.md](menu.md) - Configuration blocks (`rtmp`, `application`, `http`), status page, roles
- [features.md](features.md) - RTMP/HLS/DASH, hooks, `exec`, relay, what the module does NOT do
- [description.md](description.md) - How it differs from MediaMTX, MistServer and Restreamer
- [structure.md](structure.md) - nginx processes, directory layout of the output, configuration layers
- [shortcuts.md](shortcuts.md) - nginx command line (`-t`, `-s reload`), no UI keys
- [api.md](api.md) - HTTP hooks (`on_publish`, `on_play`, `on_record_done`), status XML, `exec`
