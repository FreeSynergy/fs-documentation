# Restreamer - Beschreibung

## Was das Programm macht

Der Restreamer ist ein fertiger Medienserver im Container: Er empfängt einen Stream (typisch von OBS per RTMP), zeigt ihn im eigenen Player, zeichnet ihn in Segmente auf und gibt ihn an beliebig viele RTMP-Ziele weiter.

## Vorteile

- **in Minuten einsatzbereit**: ein Container, eine Oberfläche, kein Handbau
- **eigene Domain, eigener Player** statt Plattformzwang
- **Multi-Target** für gleichzeitiges Streaming zu mehreren Zielen
- **Aufzeichnung inklusive** (ffmpeg-Segmente), ohne Zusatztools

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **nginx + nginx-rtmp-module** | dieselbe Basis, aber ohne Weboberfläche und ohne CLI-Komfort. |
| **MediaMTX** | schlanker Protokoll-Router (RTSP/SRT/HLS/WebRTC), keine Weboberfläche mit Multi-Target-Assistenten. |
| **Restream (SaaS)** | kommerzieller Dienst mit Chat, Zielen, Analytik; der Restreamer läuft auf eigener Hardware. |
| **Wowza / MistServer / Ant Media** | professionelle Server mit Skalierung und DRM, deutlich komplexer. |

## Technische Details

- **Basis**: Alpine-Image mit nginx, nginx-rtmp-module, Node.js (Webui), ffmpeg
- **Ports**: 1935 (RTMP), 8080 (HTTP-Player/Webui), 8081 (HTTPS) — konfigurierbar
- **Eingang**: RTMP `rtmp://host:1935/live/stream?key=<pushKey>`
- **Ausgang**: HLS `…/hls/stream.m3u8`, MP4-Original, RTMP-Restream-Ziele
- **Persistence**: Volumes `/opt/restreamer/var/media`, `/var/statistics`
- **Lizenz**: MIT (datarhei/restreamer)

## Für wen geeignet

- Eigene Livestream-Infrastruktur ohne Programmieraufwand
- FreeSynergy-Streaming-Skins mit Modell Eingang / Ziel / Segment
- Vorträge und Meetings, die gleichzeitig aufgenommen und verteilt werden sollen
