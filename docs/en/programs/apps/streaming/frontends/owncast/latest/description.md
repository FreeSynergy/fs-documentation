# Owncast - Description

## What the program does
Owncast runs a personal live-streaming site. The streamer points broadcasting software (the README names OBS, Streamlabs and Restream as examples) at the server; viewers watch in the browser and chat. An admin area configures the server.

## Advantages
- Self-hosted, MIT licence, one binary stack with ffmpeg.
- Chat included; no separate service.
- Optional fediverse following.

## Differentiation
| System | Difference |
|--------|------------|
| PeerTube | Platform for many users with uploads and federation of videos; Owncast is a single-streamer server. |
| MediaMTX, nginx-rtmp-module | Media routers without chat or viewer page. |

## Technical details
Backend Go (README asks for a recent Go version, a C compiler and ffmpeg); frontend React. Storage options: Open.
