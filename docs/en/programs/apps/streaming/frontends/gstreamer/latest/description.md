# GStreamer - Description

## Overview

GStreamer is the multimedia foundation framework of the freedesktop environment: it provides decoders, encoders, filters, network elements and a pipeline runtime on which applications and servers are built.

## What GStreamer does

GStreamer decodes, filters, encodes and distributes audio, video and text. Elements are assembled into pipelines that work locally (file, camera, screen) or over networks (RTSP, SRT, RTMP, HLS, WebRTC, MPEG-TS/UDP). Any application that wants to process media can use these building blocks through C, Python or Rust.

## Advantages

- **Modularity**: new codecs or filters are individual plugins, without changing applications
- **Cross-platform**: Linux, Windows, macOS, Android, iOS, embedded (Yocto, Buildroot)
- **Hardware acceleration**: VAAPI, NVENC/NVDEC, QSV, V4L2, Vulkan, OpenGL from one and the same pipeline
- **Modern protocols**: WebRTC, SRT and LL-HLS first class
- **Maintenance and an open licence**: LGPL 2.1, active community, release cycle roughly every six months

## Differentiation from other systems

### GStreamer vs. FFmpeg

- FFmpeg is a **toolkit for command-line jobs** (transcoding, analysis); GStreamer is a **runtime library** for long-running pipelines
- FFmpeg pipelines are static per invocation; GStreamer pipelines can be changed at runtime (attach/detach pads, switch elements on/off)
- Both use the same codec libraries; GStreamer rebuilds them as elements, FFmpeg as encoders/decoders inside the program

### GStreamer vs. OBS Studio

- OBS is a finished production application (scenes, mixer, hotkeys) — GStreamer only supplies the building blocks
- OBS uses its own libobs filters, but a GStreamer plugin for several sources and for WebRTC
- For FreeSynergy skins: rebuild the OBS interface, keep GStreamer as the media rail in the background

### GStreamer vs. MediaMTX / MistServer

- MediaMTX and MistServer are **streaming servers** with configuration and an API; GStreamer is a library from which you can build such a server yourself
- No recording manager, no viewer management, no ports that are "simply there"

## Technical details

- **Backend**: C with GObject/GLib; plugin registry (`~/.cache/gstreamer-1.0`)
- **Data model**: `GstBuffer`, `GstCaps`, pads, bins, bus (asynchronous messages)
- **Frontend**: none — tools (CLI) or the toolkits of the application
- **Authentication**: not its own; for sources such as `rtspsrc` via URL/headers
- **Hosting**: runs inside the application's process, in containers, or as the foundation of your own servers

## Who GStreamer suits

- Teams that want to build **their own media tools** (recorders, streaming nodes, playback)
- Embedded and Linux products with hardware codecs
- Automation in which pipelines have to be rebuilt at runtime
- Less suitable for: quick one-off transcodes (→ FFmpeg) or finished streaming servers (→ MediaMTX, MistServer)
