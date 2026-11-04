# MediaMTX Documentation

## Overview

MediaMTX (formerly `rtsp-simple-server`) is a lean live media router in **Go**: one binary, one YAML file, and the server accepts streams and delivers them over RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS, MPEG-TS, RTP and MoQ. It does not transcode, but muxes/remuxes and distributes. Stack: Go, MIT licence, configuration via `mediamtx.yml`, control via the control API (port 9997).

## File structure

- [menu.md](menu.md) - Configuration sections, paths, protocol listeners, roles
- [features.md](features.md) - Protocols, auth, recording, hooks, what MediaMTX does NOT do
- [description.md](description.md) - How it differs from nginx-rtmp, MistServer, Ant Media and Restreamer
- [structure.md](structure.md) - Listeners → paths → readers, ports, log and config structure
- [shortcuts.md](shortcuts.md) - Command line and service management (no UI keys)
- [api.md](api.md) - Control API v3 (9997), hooks, metrics, playback server
