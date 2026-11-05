# FFmpeg - Keyboard shortcuts

FFmpeg is primarily a CLI tool: there are no menu or command shortcuts as in a GUI. Interaction only happens during a running process or in the playback of `ffplay` — which is why the keys are strictly separated per tool.

## ffmpeg (during the run)

| Key | Effect |
|-----|--------|
| `q` / `ESC` | abort the running operation (exit code ≠ 0) |
| `+` / `-` | raise/lower the statistics/log level |
| `c` | switch the frame-based log output |
| `v` | switch the verbosity/frame display |

Note: there are **no** assigned keys for functions such as pause, seek or changing filters — all of that is passed as an argument before the start. In scripts (`-nostdin`, pipe input) even the interactive abort key has no effect.

## ffplay (SDL player window)

| Key | Effect |
|-----|--------|
| `Spacebar` / `p` | pause/resume playback |
| `q` / `ESC` | quit the player |
| `f` | toggle full screen |
| `←` / `→` | 10 s back/forward (seek) |
| `↑` / `↓` | 1 min back/forward |
| `PgUp` / `PgDn` | 10 min back/forward |
| `m` | mute |
| `+` / `-` | volume |
| `w` | waveform display |
| `s` | audio frame statistics |
| `0`–`9` | jump to a percentage mark |
| `a` | switch the audio stream |
| `v` | switch the video stream |
| `r` | switch the subtitle stream |

## ffprobe

No interactive keys — a single invocation, output on stdout, ends with an exit code.

## Starting ffplay and constraining it

| Invocation | Effect |
|------------|--------|
| `ffplay file.mkv` | player window with SDL control |
| `ffplay -nodisp -autoexit file.mp3` | without a window, ends at the file end |
| `ffplay -left / -right / -top / -bottom N` | window position |
| `ffplay rtsp://host/stream` | test network streams directly |

## Shortcuts by role

| Role | relevant keys |
|------|---------------|
| Encoding operations | `q` (abort), `+`/`-` (limit the flood of logs) |
| Quick check | the complete ffplay control (pause, seek, full screen) |
| Automation | none — the invocation parameters replace every key |

## Practical note

Anyone coming from OBS or other GUIs misses shortcuts: FFmpeg moves every "key function" into options — seek becomes `-ss`, pause does not exist (stop the process), volume becomes the `volume` filter. The complete key layout of ffplay is deliberately minimal and only covers playback control; stream cuts, filters or switching encoders are not possible at runtime.

## Cross-references

- Interactive key and hotkey direction: [OBS Studio](../../obs-studio/index.md)
- Server without a keyboard, purely a configuration file: [MediaMTX](../../mediamtx/index.md)
- Pipeline alternatives with their own tooling: [GStreamer](../../gstreamer/index.md)
