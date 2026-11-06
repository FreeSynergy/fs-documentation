# FFmpeg

> Category: [streaming](../../index.md)

## What it is

FFmpeg is the command-line tool collection of the FFmpeg projects: `ffmpeg` transcodes, muxes/demuxes and filters media, `ffprobe` analyses files in a machine-readable way, `ffplay` plays them as a simple SDL player. The technology stack is pure C (libavformat, libavcodec, libavfilter, libswscale, libswresample) with build options for x264/x265, AV1, Opus and hardware acceleration (NVENC, QSV, VAAPI, VideoToolbox). FFmpeg is primarily a CLI — there is no graphical surface; operation, automation and integration run through arguments, exit codes and status streams. The core is licensed under LGPL, with a GPL-buildable configuration (and de facto GPL when GPL code such as x264 is compiled in). The current release lines are the 6.x and 7.x series (ffmpeg.org).

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
