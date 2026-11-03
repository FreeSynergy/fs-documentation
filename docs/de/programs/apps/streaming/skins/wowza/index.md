# Wowza Streaming Engine Dokumentation

## Übersicht

Wowza Streaming Engine ist ein **kommerzieller Medienserver** für Live- und On-Demand-Video: Er nimmt Streams (RTMP, RTSP, SRT, MP4-Upload) an, formt sie mit dem eingebauten Transcoder in Multi-Bitrate-Leitern und liefert sie als HLS, Low-Latency-HLS, CMAF, MPEG-DASH, Smooth und progressiv aus. Verwaltet wird über den **Wowza Streaming Engine Manager** (Port 8088) und die **REST Server API v2** (Port 8087); konfiguriert wird in XML-Dateien. Lizenzpflichtig, Einzellizenz pro Instanz, Windows oder Linux (JVM-basiert).

## Dateistruktur

- [menu.md](menu.md) - Manager-Menüs: Applications, Streaming Publishers, Connections, Add Application, Restart, Log Viewer; Reiter je Anwendung
- [features.md](features.md) - Protokolle, Transcoding, nDVR/Time Shift, Stream Targets, Sicherheit/DRM, Was Wowza NICHT kann
- [description.md](description.md) - Abgrenzung zu Restreamer, nginx-rtmp, MediaMTX, MistServer und Ant Media
- [structure.md](structure.md) - Manager-Layout, Konfigurationshierarchie (VHost → Anwendung → Stream), Ports
- [shortcuts.md](shortcuts.md) - Manager hat keine Shortcuts; Dienstbefehle und REST-Kurzbefehle
- [api.md](api.md) - REST Server API v2 (Basic Auth), Endpunkte, Beispiele, Module statt Webhooks
