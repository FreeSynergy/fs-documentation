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

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (10), nach Funktionen, nichts kopiert (ADR 0012/0013):

- [Ant Media Server](frontends/ant-media-server/index.md) — Der Ant Media Server (AMS) ist eine Streaming-Plattform auf Java-Basis: Er nimmt RTMP, RTSP, SRT und WebRTC an, liefert WebRTC, HLS und DASH aus, kann transkodieren (Adaptive Multi-Bitrate) und ver…
- [FFmpeg](frontends/ffmpeg/index.md) — FFmpeg ist die Kommandozeilen-Werkzeugsammlung der FFmpeg-Projekte: `ffmpeg` transcodiert, muxed/demuxed und filtert Medien, `ffprobe` analysiert Dateien maschinenlesbar, `ffplay` spielt sie als ei…
- [GStreamer](frontends/gstreamer/index.md) — GStreamer ist ein Multimedia-Framework in C: Aufnahme, Dekodierung, Filterung, Kodierung und Ausgabe werden als Pipeline aus Elementen (Source → Filter/Codec → Sink) aufgebaut.
- [MediaMTX](frontends/mediamtx/index.md) — MediaMTX (früher `rtsp-simple-server`) ist ein schlanker Live-Media-Router in Go: ein Binary, eine YAML-Datei, und der Server nimmt Streams an und liefert sie über RTSP, RTMP, SRT, WebRTC, HLS/LL-H…
- [MistServer](frontends/mistserver/index.md) — MistServer ist ein schlanker, in C++ geschriebener Streaming-Server ohne Transcoding: er nimmt Live-Streams (RTMP, RTSP, SRT, WebRTC/WHIP) und Dateien an und liefert sie über HTTP, HLS, DASH, WebRT…
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) — Das nginx-rtmp-module (arut) erweitert nginx um einen RTMP-Server: Es nimmt RTMP-Publishes an, schreibt HLS- und DASH-Streams mit, zeichnet auf und leitet per Relay weiter.
- [OBS Studio](frontends/obs-studio/index.md) — OBS Studio nimmt Bildschirme, Kameras und Audio auf und überträgt sie per RTMP/SRT in Streams; Szenen, Quellen, Filter und Mischer machen daraus ein vollwertiges Produktionswerkzeug.
- [Restream](frontends/restream/index.md) — Restream (restream.io) ist ein Cloud-Multistreaming-Dienst: Ein Encoder-Sendestrom wird angenommen und gleichzeitig an viele Plattformen (YouTube, Twitch, Facebook, LinkedIn, TikTok u.
- [Restreamer](frontends/restreamer/index.md) — Der (Docker) Restreamer ist ein Komplettpaket für eigenen Videoempfang und -verteilung: nginx + nginx-rtmp-module + Node.js-Webui.
- [Wowza Streaming Engine](frontends/wowza/index.md) — Wowza Streaming Engine ist ein kommerzieller Medienserver für Live- und On-Demand-Video: Er nimmt Streams (RTMP, RTSP, SRT, MP4-Upload) an, formt sie mit dem eingebauten Transcoder in Multi-Bitrate…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
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
