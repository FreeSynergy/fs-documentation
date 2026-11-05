# GStreamer - Keyboard shortcuts

## Overview

GStreamer is a framework without a window of its own — there are **no global shortcuts**. Keys exist only in the bundled tools (`gst-play-1.0`) and in applications built on GStreamer.

## gst-play-1.0 (playback in the terminal)

| Key | Purpose |
|-----|---------|
| `SPACE` | pause / resume |
| `→` / `←` | 5 seconds forward/back |
| `PAGE UP` / `PAGE DOWN` | one chapter respectively a larger jump |
| `+` / `-` | raise / lower the volume |
| `M` | mute |
| `N` / `P` | next / previous title |
| `S` | print the current position |
| `Q` | quit |

## gst-launch-1.0

| Key | Purpose |
|-----|---------|
| `Ctrl+C` | stop the pipeline (EOS is sent) |
| `r` (newer versions) | restart the pipeline when started with `--repeat` |

## Your own applications (recommendation for a skin implementation)

This assignment is a **suggestion**, not a GStreamer decision — it follows the convention of other media players:

| Shortcut | Purpose |
|----------|---------|
| `Space` | play/pause |
| `Ctrl+Shift+P` | rebuild the pipeline (change the source) |
| `Del` | remove the active sink branch |
| `F5` | force `PLAYING` / start the pipeline |
| `F6` | set `PAUSED` |

## Mac variants

| Windows/Linux | Mac | Note |
|---------------|-----|------|
| `Ctrl+C` | `Cmd+C` in the terminal | abort; in a terminal `Ctrl+C` also works on macOS |
| `Alt` combinations | `Option` | only in GTK/Qt interfaces |

## Summary

- In short: **GStreamer itself has no shortcuts**; `gst-play-1.0` offers the usual transport control in the terminal
- All keys in a FreeSynergy interface have to be defined by yourself and documented in this file
- For automation shortcuts are irrelevant — there `GST_DEBUG`, bus handlers and `run-command` hooks count
