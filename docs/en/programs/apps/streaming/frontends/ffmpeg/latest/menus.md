# FFmpeg - Menu items

FFmpeg has no menus — it is a pure command-line collection. Instead of a menu bar and dialogs there are tools, option switches and filter commands. "Menu items" here are therefore the invocation variants.

## Tools (instead of an application menu)

| Tool | Purpose |
|------|---------|
| `ffmpeg` | transcoding, muxing/demuxing, filtering, stream selection |
| `ffprobe` | analysis of streams/formats, output as json/csv/xml |
| `ffplay` | simple SDL player for quick checks |
| `ffserver` | stream server — discontinued and removed from the builds |
| `ffmpeg -h` / `-help` | built-in self-help by topic (`-h encoder`, `-h filter`, `-h muxer`) |

## Invocation structure

```
ffmpeg [global options] [input options] -i INPUT ... [output options] OUTPUT
```

| Area | typical options |
|------|-----------------|
| Global | `-hide_banner`, `-loglevel`, `-y`/`-n`, `-stats`, `-progress` |
| Input | `-ss` (seek), `-t`/`-to` (duration), `-f` (force format), `-i` |
| Stream selection | `-map`, `-vn`, `-an`, `-sn`, `-map_metadata` |
| Codec | `-c copy`, `-c:v libx264`, `-c:a aac`, `-b:a 128k` |
| Quality | `-crf`, `-b:v`, `-preset`, `-tune`, `-pix_fmt` |

## Option topics (instead of submenus)

| Topic block | Examples |
|-------------|----------|
| Video | `-vf`, `-r`, `-s WxH`, `-g`, `-profile`, `-level` |
| Audio | `-af`, `-ar`, `-ac`, `-channel_layout` |
| Muxer/container | `-f mp4|mkv|webm|ts|hls|dash|nut`, `-movflags` |
| Network | `-rtsp_transport`, timeout options, SRT parameters |
| Hardware | `-hwaccel`, `-hwaccel_output_format`, encoders such as `h264_nvenc` |

## Filter commands (libavfilter)

The filter graph is FFmpeg's actual "control menu" — short commands, chained with `,` and wired through `-filter_complex` with named pads.

| Filter | Task |
|--------|------|
| `scale` | scaling, aspect handling |
| `crop` / `pad` | trimming, adding borders |
| `overlay` | picture-in-picture, watermark |
| `drawtext` | burned-in text (libfreetype) |
| `concat` | joining sources one after another |
| `fps` | framerate conversion |
| `volume` / `amix` | loudness, multi-channel mixing |
| `loudnorm` | audio normalisation according to EBU R128 |

Example:

```
ffmpeg -i in.mp4 -i logo.png -filter_complex "[0:v][1:v]overlay=W-w-10:10" out.mp4
```

## Menus by role

FFmpeg knows no roles and no user interface — usability arises solely from arguments, shell scripts and wrappers. Team roles (editing, encoding operations, automation) use the same commands; permissions are filesystem permissions.
