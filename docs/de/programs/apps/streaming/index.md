# Streaming-Systeme

## Übersicht

Streaming-Systeme nehmen Live- oder vorproduziertes Videomaterial an, verarbeiten es (Transcoding, Aufzeichnung, Packaging) und verteilen es an Zuschauer oder an fremde Plattformen. Die Kategorie deckt die ganze Kette ab: Encoder (OBS), Protokoll-Router (MediaMTX, FFmpeg, GStreamer), Medienserver (nginx-rtmp, Restreamer, MistServer, Ant Media, Wowza) und Cloud-Multistreaming (Restream).

## Verfügbare Systeme

- **obs-studio** - Szenen-/Encoder-Software für Aufnahme und Streaming
- **ffmpeg** - Kommandozeilen-Toolkit für Kodierung, Remixing, RTMP-Push
- **gstreamer** - modulare Multimedia-Pipeline als Bibliothek und CLI
- **mediamtx** - schlanker Protokoll-Router (RTSP/RTMP/HLS/SRT/WebRTC)
- **nginx-rtmp-module** - RTMP-Empfang und HLS-Auslieferung als nginx-Modul
- **restreamer** - Docker-Komplettpaket: Empfang, Player, Aufzeichnung, Multi-Target
- **restream** - Cloud-Multistreaming-Dienst (restream.io) mit Chat und Analytik
- **mistserver** - leichter Medienserver mit eingebautem HTTP-Management
- **ant-media-server** - professioneller Medienserver mit WebRTC und Cluster
- **wowza** - kommerzieller Medienserver mit Manager, REST API und DRM

## Skin-Dokumentation

Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter `programs/apps/streaming/masks/<programm>/`.

**dokumentiert (10 Programme):**

- [Ant Media Server](frontends/ant-media-server/index.md) - Ant Media Server
- [FFmpeg](frontends/ffmpeg/index.md) - FFmpeg
- [GStreamer](frontends/gstreamer/index.md) - GStreamer
- [MediaMTX](frontends/mediamtx/index.md) - MediaMTX
- [MistServer](frontends/mistserver/index.md) - MistServer
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) - nginx-rtmp-module
- [OBS Studio](frontends/obs-studio/index.md) - OBS Studio
- [Restream](frontends/restream/index.md) - Restream
- [Restreamer](frontends/restreamer/index.md) - Restreamer
- [Wowza Streaming Engine](frontends/wowza/index.md) - Wowza Streaming Engine

Übersicht: [Skin-Verzeichnis](frontends/index.md)

Referenzschema: [Wiki-Skins](../wiki/frontends/index.md) · [Desktop-Skins](../../platform/desktop/frontends/index.md) · [Standardisierte Daten](../../../data/api.md)

## Masken-Dokumentation

Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter `programs/apps/streaming/masks/<programm>/`.

**dokumentiert (10 Programme):**

- [Ant Media Server](frontends/ant-media-server/index.md) - Ant Media Server
- [FFmpeg](frontends/ffmpeg/index.md) - FFmpeg
- [GStreamer](frontends/gstreamer/index.md) - GStreamer
- [MediaMTX](frontends/mediamtx/index.md) - MediaMTX
- [MistServer](frontends/mistserver/index.md) - MistServer
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) - nginx-rtmp-module
- [OBS Studio](frontends/obs-studio/index.md) - OBS Studio
- [Restream](frontends/restream/index.md) - Restream
- [Restreamer](frontends/restreamer/index.md) - Restreamer
- [Wowza Streaming Engine](frontends/wowza/index.md) - Wowza Streaming Engine

Übersicht: [Masken-Verzeichnis](frontends/index.md)

Referenzschema: [Wiki-Masken](../wiki/frontends/index.md) · [Desktop-Masken](../../platform/desktop/frontends/index.md) · [Standardisierte Daten](../../../data/api.md)
