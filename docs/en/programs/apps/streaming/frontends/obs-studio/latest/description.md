# OBS Studio - Description

## What the program does

OBS builds a scene out of sources (windows, camera, audio, files), switches between
scenes and delivers the result as a recording or a live stream to a platform. It is the
mixing desk and the encoder in one.

## Advantages

- **free and open source** (GPLv2), Windows/macOS/Linux
- **extremely flexible**: every source has filters, every scene has transitions, every channel has filters
- **controllable from outside** via obs-websocket — ideal for automation and frontend connection
- **huge community**: guides, plugins, scene collections

## Differentiation

| System | Difference |
|--------|------------|
| **Restreamer / MediaMTX / nginx-rtmp** | server-side recording and forwarding; OBS is the client side with picture mixing. |
| **Restream (SaaS)** | multi-streaming and chat bundling in the browser; OBS supplies the audio/video, Restream distributes it. |
| **GStreamer / ffmpeg** | programming tools without a UI; OBS is the GUI over them. |
| **vMix / StreamYard** | commercial; vMix Windows only, StreamYard browser-based without local recording quality. |

## Technical details

- **Core**: libobs (C/C++), graphics via DirectX/OpenGL/Metal, audio via PulseAudio/WASAPI/CoreAudio
- **Encoders**: x264, AV1 (SVT-AV1), NVENC, AMF, QSV, VideoToolbox
- **Profiles/scenes**: JSON-like collections (`~/.config/obs-studio`), portable
- **Remote control**: obs-websocket 5 (JSON over WebSocket, password authentication)
- **Formats**: output up to 4096×2160, 60 fps and higher, multiple audio tracks
- **Licence**: GPLv2+

## Who it suits

- solo production of recordings and streams (talk, gaming, training)
- FreeSynergy streaming frontends with the model scene / source / encoder / target
- automated recording chains over WebSocket (e.g. started from the FreeSynergy calendar)
