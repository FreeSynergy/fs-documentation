# FFmpeg - API documentation

## No REST API

FFmpeg offers **no** HTTP/REST interface, no endpoints, no authentication, no rate limits and no webhooks — and it cannot, because it is not a daemon and not a server but a process you start, watch, and which ends with an exit code. `ffserver` (the former HTTP stream server) was discontinued and removed from the builds. "Integration" therefore means: control the process, read the status streams, link the libraries.

## Integration surface 1: process invocation

| Surface | Detail |
|---------|--------|
| Invocation | `ffmpeg [options] -i IN [options] OUT` |
| Exit code | `0` success, `≠ 0` error (e.g. 1 general error, 69 etc. depending on the build) |
| stdout/stderr | human statistics on stderr; use `-progress` for machines |
| Signals | `SIGINT`/`q` abort, SIGPIPE at the end of a pipe |
| Lock stdin | `-nostdin` prevents keyboard interference in pipelines |

## Integration surface 2: `-progress pipe:1` (status stream)

```
ffmpeg -nostdin -progress pipe:1 -i in.mp4 -c:v libx264 out.mp4
```

| Field (example) | Meaning |
|-----------------|---------|
| `frame=`, `fps=`, `bitrate=` | encode progress |
| `out_time_us=`, `out_time_ms=` | processed time (microseconds) |
| `progress=` | `continue` up to `end` |

One line per update, `key=value` — the de-facto "streaming API" for progress in web interfaces and workers.

## Integration surface 3: `ffprobe -of json` (machine API)

```
ffprobe -v quiet -print_format json -show_streams -show_format file.mkv
```

| Area | returned |
|------|----------|
| `streams[]` | codec, resolution, framerate, channel count, timeline |
| `format` | container, duration, bitrate, tags |
| Formats | json, csv, xml, ini (`-of`/`-print_format`) |

This makes ffprobe a complete read API without a library dependency — ideal for skin and web-interface tools that display metadata.

## Integration surface 4: the libav\* libraries (C)

| Library | Task |
|---------|------|
| libavformat | muxers/demuxers, protocols |
| libavcodec | encode/decode |
| libavfilter | filter graph programmatically |
| libswscale / libswresample | scaling, audio conversion |
| libavutil | buffers, time base, hashing |

Bound via `pkg-config libavformat libavcodec libavfilter`; version/API guarantees follow the release branches (6.x/7.x).

## Language bindings and wrappers

| Language binding | Approach |
|------------------|----------|
| ffmpeg-python | Python command builder around `ffmpeg`/`ffprobe` |
| Python `subprocess` | direct call + `-progress` parsing (the standard route) |
| fluent-ffmpeg / ffmpeg-static | Node.js builders respectively bundled binaries |
| JavaCV / JavaCPP (bytedeco) | Java binding of the libav\* C API |
| MediaMTX, Ant Media Server | use FFmpeg as a process backend (remux/recording) |

| Property | FFmpeg process API |
|----------|--------------------|
| Rate limits | none — locally limited by CPU/GPU |
| Webhooks | none — replaced by exit code and `-progress end` |
| Auth | none — filesystem/process permissions suffice |
| Parallelism | as many processes as the hardware allows |

## Command-builder pattern

```python
cmd = ["ffmpeg", "-nostdin", "-hide_banner",
       "-ss", "00:01:00", "-t", "60",
       "-i", src, "-vf", "scale=1280:-2",
       "-c:v", "libx264", "-crf", "23", dst]
```

Rule: pass the arguments as a list (no shell string), tap `-progress pipe:1`, evaluate the exit code — that is the complete "API" of FFmpeg.

## See also

- [index.md](../index.md) - overview and file structure
- [menus.md](menus.md) - tools, options, filter commands
- [features.md](features.md) - features and limits
- [description.md](description.md) - classification and differentiation
- [layout.md](layout.md) - pipeline and CLI structure
- [shortcuts.md](shortcuts.md) - keyboard control of ffmpeg and ffplay
