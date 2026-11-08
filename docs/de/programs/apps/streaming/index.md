# Streaming-Systeme

## Kurz gesagt

Streaming nimmt einen Live-Stream entgegen, leitet ihn gleichzeitig an mehrere Ziele weiter und zeichnet ihn auf. Du brauchst keinen Anbieter dazwischen. Es beantwortet die Frage: Wie zeige ich etwas einmal und bringe es überall hin, ohne meinen Stream-Schlüssel an andere weiterzugeben?

**Befehl:** `fs-streaming`, ein Befehl je Programm mit Unterbefehlen ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); Programme werden umgestellt, wenn sie ohnehin angefasst werden, nicht jedes ist es schon).

## Was hier anders ist

- Der Stream wird unverändert weitergegeben, sodass keine Qualität verloren geht und die Maschine wenig Arbeit hat.
- Ein langsames oder totes Ziel bremst weder den Sender noch die anderen Ziele.
- Schlüssel werden als Geheimnisse behandelt. Der Schlüssel, mit dem du sendest, wird nur einmal angezeigt, und nur ein Hash wird gespeichert. Schlüssel tauchen nie in Logs oder Fehlermeldungen auf.
- Fällt der Sender aus, bleiben die Ziele eine Weile verbunden, und der Stream läuft weiter, sobald er zurückkehrt.
- Streaming besitzt seine Schnittstelle selbst, `streaming.capnp` in `fs-interfaces`. Sie ist ein Entwurf und als vorläufig markiert.

## Wo es heute steht

Neuester Tag: `v0.2.0` (Stufe 1 des Entwurfs). Es gibt **noch kein Fenster und noch keinen Server**.

Heute kann es einen RTMP-Stream empfangen und an viele RTMP- oder RTMPS-Ziele senden, den Stream als FLV in einen Ordner aufzeichnen und ein Ziel vor dem Live-Gang prüfen, soweit das im Voraus bekannt sein kann. Es hat 94 Tests mit echten Sockets.

Noch nicht vorhanden: Es wurde nur auf Loopback mit ffmpeg getestet, nie gegen eine echte Streaming-Plattform. Der Empfang ist einfaches RTMP und bleibt standardmäßig auf Loopback. Eine Aufnahme an Files zu übergeben ist nicht gebaut; alles andere im Vertrag wird als „nicht möglich“ gemeldet. Eine Weiterleitungsschleife über eine andere Maschine kann von hier aus nicht erkannt werden.

**Status: Stufe 1 `v0.0.1` in [`fs-streaming`](https://github.com/FreeSynergy/fs-streaming) (weiterleiten und aufzeichnen, nur auf Loopback getestet), noch kein Fenster.** Siehe das [Design](design.md), die [Anforderungen](requirements.md) und den [Gesamtplan](../roadmap.md).

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
- **mistserver** - leichter Medienserver mit eingebauter HTTP-Verwaltung
- **ant-media-server** - professioneller Medienserver mit WebRTC und Cluster
- **wowza** - kommerzieller Medienserver mit Manager, REST API und DRM

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (10), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Ant Media Server](frontends/ant-media-server/index.md) — Der Ant Media Server (AMS) ist eine Streaming-Plattform auf Java-Basis: Er nimmt RTMP, RTSP, SRT und WebRTC an, liefert WebRTC, HLS und DASH aus, kann transkodieren (Adaptive Multi-Bitrate) und verwaltet Streams, r…
- [FFmpeg](frontends/ffmpeg/index.md) — FFmpeg ist die Sammlung von Kommandozeilenwerkzeugen der FFmpeg-Projekte: `ffmpeg` transkodiert, muxt/demuxt und filtert Medien, `ffprobe` analysiert Dateien maschinenlesbar, `ffplay` spielt sie als ei…
- [GStreamer](frontends/gstreamer/index.md) — GStreamer ist ein Multimedia-Framework in C: Aufnahme, Dekodierung, Filterung, Kodierung und Ausgabe werden als **Pipeline aus Elementen** aufgebaut (Quelle → Filter/Codec → Senke).
- [MediaMTX](frontends/mediamtx/index.md) — MediaMTX (früher `rtsp-simple-server`) ist ein schlanker Live-Media-Router in **Go**: ein Binary, eine YAML-Datei, und der Server nimmt Streams an und liefert sie über RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS,…
- [MistServer](frontends/mistserver/index.md) — MistServer ist ein schlanker Streaming-Server in C++ ohne Transcoding: Er nimmt Live-Streams (RTMP, RTSP, SRT, WebRTC/WHIP) und Dateien an und liefert sie über HTTP, HLS, DASH, WebRTC, RTMP, RTSP…
- [nginx-rtmp-module](frontends/nginx-rtmp-module/index.md) — Das nginx-rtmp-module (arut) erweitert nginx um einen RTMP-Server: Es nimmt RTMP-Publishes an, schreibt HLS- und DASH-Streams mit, zeichnet auf und leitet per Relay weiter.
- [OBS Studio](frontends/obs-studio/index.md) — OBS Studio nimmt Bildschirme, Kameras und Audio auf und überträgt sie per RTMP/SRT in Streams; Szenen, Quellen, Filter und der Mixer machen daraus ein vollwertiges Produktionswerkzeug.
- [Restream](frontends/restream/index.md) — Restream (restream.io) ist ein **Cloud-Multistreaming-Dienst**: Ein Encoder-Stream wird angenommen und gleichzeitig an viele Plattformen (YouTube, Twitch, Facebook, LinkedIn, TikTok und andere) weitergegeben.
- [Restreamer](frontends/restreamer/index.md) — Der (Docker-)Restreamer ist ein Komplettpaket für deinen eigenen Videoempfang und deine Videoverteilung: nginx + nginx-rtmp-module + Node.js-Web-UI.
- [Wowza Streaming Engine](frontends/wowza/index.md) — Wowza Streaming Engine ist ein **kommerzieller Medienserver** für Live- und On-Demand-Video: Er nimmt Streams (RTMP, RTSP, SRT, MP4-Upload) an, formt sie mit dem eingebauten Transcoder in Multi-Bitrate-…

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->

## Frontend-Dokumentation

Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter `programs/apps/streaming/frontends/<program>/`.

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

Übersicht: [Frontend-Verzeichnis](frontends/index.md)

Referenzschema: [Wiki-Masken](../wiki/frontends/index.md) · [Desktop-Masken](../../platform/desktop/frontends/index.md) · [Standardisierte Daten](../../../data/api.md)
