# MistServer Documentation

## Overview

MistServer is a lean streaming server written in C++ without transcoding: it accepts live streams (RTMP, RTSP, SRT, WebRTC/WHIP) and files and delivers them over HTTP, HLS, DASH, WebRTC, RTMP, RTSP and SRT — including a DVR buffer and push outputs. Configuration and surface run through the same JSON API on port `4242`. Licence: GPL-licensed LTS edition ("LTS") and commercial Pro edition.

## File structure

- [menu.md](../../masks/mistserver/menu.md) - Web surface: protocol, streams and push page, roles
- [features.md](../../masks/mistserver/features.md) - Inputs/outputs, DVR, recording, what MistServer does NOT do
- [description.md](../../masks/mistserver/description.md) - How it differs from MediaMTX, nginx-rtmp and Ant Media Server
- [structure.md](../../masks/mistserver/structure.md) - Ports, interfaces, layout of the configuration
- [shortcuts.md](../../masks/mistserver/shortcuts.md) - Command line and service management
- [api.md](../../masks/mistserver/api.md) - JSON API on 4242 (`command` parameter), auth challenge, examples
