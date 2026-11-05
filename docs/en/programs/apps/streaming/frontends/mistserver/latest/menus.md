# MistServer - Menu items

## Overview

MistServer is operated through a built-in web interface on port `4242`; this is only a client of the same JSON API. The interface has three core pages.

## Protocol page

| Element | Content |
|---------|---------|
| Activate default protocols | set HTTP, HTTPS, RTMP, RTSP, SRT, WebRTC on their standard ports |
| Add a connector | choose protocol/port (HTTP 8080, HTTPS 4433, RTMP 1935, RTSP 5554, SRT 8889/udp, WebRTC 18203/udp) |
| Remove a connector | deactivate the listener |
| Stream keys | a token per stream instead of the stream name in the push path |

## Streams page

| Element | Content |
|---------|---------|
| Streams list | blue = active but not created, white = configured |
| Right-click on a stream | open the stream page, delete, create |
| Create a new stream | `Stream name` + `Source` (file, folder, `push://`, `srt://:port`, `tsudp://ip:port`, `http://…m3u8`) |
| Show the push protocols | below the source field: the RTMP, SRT, RTSP, WebRTC and WHIP target addresses |
| Tracks | inspect the video/audio/data tracks of a stream |

## Push page

| Element | Content |
|---------|---------|
| Automatic push | rule: push/record automatically on stream activity (or time/variable) |
| Single push | start a one-off push immediately |
| Target type | RTMP, SRT, RTSP, WebRTC or a local file (recording) |
| Track selection | which video/audio track is pushed (default: the last compatible one) |
| Variables | substitutions for stream name, time, date in the target |

## Menus by role

| Role | Access |
|------|--------|
| localhost | full access without login (automatic detection) |
| Admin (user) | after login all three pages, all API commands |
| First start without an account | the `NOACC` state: create a local account through the API/interface |
| Viewer | only the media ports (not 4242) |
