# FFmpeg - Structure & UI/UX

## The "UI" is the command line

There are no windows, dialogs or menus. The entire user interface consists of the invocation line, the progress display and the exit code. Understanding this structure replaces the control surface.

## Pipeline structure (inner model)

```
Input (demuxer) → decoder → filter graph (libavfilter) → encoder → muxer → output
```

| Stage | What happens | typical options |
|-------|--------------|-----------------|
| Demuxer | read the container (mp4, mkv, ts, HLS) | `-f`, `-i` |
| Decoder | produce raw picture/sound | `-hwaccel`, `-c:v` (input) |
| Filter graph | reshape, mix, draw | `-vf`, `-af`, `-filter_complex` |
| Encoder | re-encode | `-c:v libx264`, `-crf`, `-preset` |
| Muxer | write into the target container | `-f mp4|mkv|webm|ts|hls|dash|nut` |

Several `-i` inputs are assigned to the outputs through `-map 0:v -map 1:a`-style expressions; pads in the graph get names like `[0:v][1:v]overlay[v]`.

## CLI structure (outer model)

| Element | Convention |
|---------|------------|
| Order | options apply to the **following** file; `-ss` before `-i` is fast, after `-i` it is exact |
| Overrides | the last statement wins; `-y` overwrites existing outputs |
| Special paths | `pipe:0`/`pipe:1` for stdio, `:0`/`:1` as stream selection |
| Self-help | `-h`, `-h full`, `-h filter overlay`, `-h encoder h264_nvenc` |

## Display during the run

| Display | Content |
|---------|---------|
| Banner | version, built-in codecs (suppressible with `-hide_banner`) |
| `-stats` | time, frame count, speed, bitrate, q index |
| Log level | `-loglevel error|warning|info|verbose|debug` |
| `-progress pipe:1` | the same status as `key=value` lines for machines |

## Filter graph notation

- Chaining: `scale=1280:-2,fps=30`
- Several sources: `[0:v][1:v]overlay=x=10:y=10[out]`, addressed with `-map "[out]"`
- Each filter has its own options (`flag=value` pairs); the option list via `-h filter NAME`

## Structure of the project components

| Component | Role |
|-----------|------|
| `ffmpeg` / `ffprobe` / `ffplay` | CLI tools over the same libraries |
| libavformat / libavcodec / libavfilter | mux/demux, codec API, filter graph |
| libswscale / libswresample | image scaling, audio resampling |
| Test suite (`fate`) | reference tests for decoders/filters |

## UX assessment

| Aspect | Assessment |
|--------|------------|
| Onboarding | steep — the syntax and the order of options have to be learned |
| Repeatability | excellent — invocations are scripts |
| Error culture | clear error messages per stage, exit code ≠ 0 on errors |
| Accessibility | text-based, therefore good for logs and automation |
