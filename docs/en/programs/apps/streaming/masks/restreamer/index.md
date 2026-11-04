# Restreamer Documentation

## Overview

The (Docker) Restreamer is a complete package for your own video reception and distribution: nginx + nginx-rtmp-module + Node.js web UI. It accepts RTMP/push streams, plays them in the browser (HLS/WebRTC) and passes them on to targets such as YouTube or Twitch.

## File structure

- [menu.md](menu.md) - Web UI areas, settings, logs
- [features.md](features.md) - Push/pull, player, multi-target, what the Restreamer does NOT do
- [description.md](description.md) - How it differs from MediaMTX, nginx-rtmp and Restream (SaaS)
- [structure.md](structure.md) - Web UI masks, player embedding
- [shortcuts.md](shortcuts.md) - Shortcuts (the web UI has none) and the CLI alternative
- [api.md](api.md) - `restreamer-cli`, config file, hooks, RTMP/HTTP endpoints
