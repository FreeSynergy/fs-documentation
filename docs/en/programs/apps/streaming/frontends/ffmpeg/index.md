# FFmpeg Documentation

## Overview

FFmpeg is the command-line tool collection of the FFmpeg projects: `ffmpeg` transcodes, muxes/demuxes and filters media, `ffprobe` analyses files in a machine-readable way, `ffplay` plays them as a simple SDL player. The technology stack is pure C (libavformat, libavcodec, libavfilter, libswscale, libswresample) with build options for x264/x265, AV1, Opus and hardware acceleration (NVENC, QSV, VAAPI, VideoToolbox). FFmpeg is primarily a CLI — there is no graphical surface; operation, automation and integration run through arguments, exit codes and status streams. The core is licensed under LGPL, with a GPL-buildable configuration (and de facto GPL when GPL code such as x264 is compiled in). The current release lines are the 6.x and 7.x series (ffmpeg.org).

## File structure

- [menu.md](../../masks/ffmpeg/menu.md) - Tools, options, filter commands (FFmpeg without classic menus)
- [features.md](../../masks/ffmpeg/features.md) - Transcoding, filter graph, containers, hardware, what FFmpeg does NOT do
- [description.md](../../masks/ffmpeg/description.md) - How it differs from OBS, GStreamer, MediaMTX and Restreamer
- [structure.md](../../masks/ffmpeg/structure.md) - Pipeline flow & CLI structure, parameter conventions
- [shortcuts.md](../../masks/ffmpeg/shortcuts.md) - ffplay keyboard control, ffmpeg command-line keys
- [api.md](../../masks/ffmpeg/api.md) - Process API, ffprobe JSON, libav\* libraries, language bindings

## Position in the system

FFmpeg is the underlying engine of many other tools: [OBS Studio](../obs-studio/index.md) uses it for recordings, [MediaMTX](../mediamtx/index.md) and Ant Media Server use it as a backend for ffmpeg-based paths, the [Restreamer](../restreamer/index.md) transcodes with it on request, and [GStreamer](../gstreamer/index.md) is the graphically oriented pipeline alternative with its own API.

| Feature | Value |
|---------|-------|
| Project | FFmpeg projects, ffmpeg.org |
| Language | C (assembly optimisations for common architectures) |
| Tools | `ffmpeg`, `ffprobe`, `ffplay` (`ffserver` discontinued/removed) |
| Current versions | 6.x / 7.x |
| Licence | LGPL (core), GPL-buildable, effectively GPL with x264/x265 |
| Platform | Linux, macOS, Windows, BSD, embedded systems |
