# Streaming — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Streaming` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Ant Media Server](ant-media-server/index.md) | [latest](ant-media-server/latest/description.md) | Der Ant Media Server (AMS) ist eine Streaming-Plattform auf Java-Basis: Er nimmt RTMP, RTSP, SRT und WebRTC an, liefert WebRTC, HLS und DASH aus, kann transkodieren (Adaptive Multi-Bitrate) und ver… |
| [FFmpeg](ffmpeg/index.md) | [latest](ffmpeg/latest/description.md) | FFmpeg ist die Kommandozeilen-Werkzeugsammlung der FFmpeg-Projekte: `ffmpeg` transcodiert, muxed/demuxed und filtert Medien, `ffprobe` analysiert Dateien maschinenlesbar, `ffplay` spielt sie als ei… |
| [GStreamer](gstreamer/index.md) | [latest](gstreamer/latest/description.md) | GStreamer ist ein Multimedia-Framework in C: Aufnahme, Dekodierung, Filterung, Kodierung und Ausgabe werden als Pipeline aus Elementen (Source → Filter/Codec → Sink) aufgebaut. |
| [MediaMTX](mediamtx/index.md) | [latest](mediamtx/latest/description.md) | MediaMTX (früher `rtsp-simple-server`) ist ein schlanker Live-Media-Router in Go: ein Binary, eine YAML-Datei, und der Server nimmt Streams an und liefert sie über RTSP, RTMP, SRT, WebRTC, HLS/LL-H… |
| [MistServer](mistserver/index.md) | [latest](mistserver/latest/description.md) | MistServer ist ein schlanker, in C++ geschriebener Streaming-Server ohne Transcoding: er nimmt Live-Streams (RTMP, RTSP, SRT, WebRTC/WHIP) und Dateien an und liefert sie über HTTP, HLS, DASH, WebRT… |
| [nginx-rtmp-module](nginx-rtmp-module/index.md) | [latest](nginx-rtmp-module/latest/description.md) | Das nginx-rtmp-module (arut) erweitert nginx um einen RTMP-Server: Es nimmt RTMP-Publishes an, schreibt HLS- und DASH-Streams mit, zeichnet auf und leitet per Relay weiter. |
| [OBS Studio](obs-studio/index.md) | [latest](obs-studio/latest/description.md) | OBS Studio nimmt Bildschirme, Kameras und Audio auf und überträgt sie per RTMP/SRT in Streams; Szenen, Quellen, Filter und Mischer machen daraus ein vollwertiges Produktionswerkzeug. |
| [Restream](restream/index.md) | [latest](restream/latest/description.md) | Restream (restream.io) ist ein Cloud-Multistreaming-Dienst: Ein Encoder-Sendestrom wird angenommen und gleichzeitig an viele Plattformen (YouTube, Twitch, Facebook, LinkedIn, TikTok u. a.) weiterge… |
| [Restreamer](restreamer/index.md) | [latest](restreamer/latest/description.md) | Der (Docker) Restreamer ist ein Komplettpaket für eigenen Videoempfang und -verteilung: nginx + nginx-rtmp-module + Node.js-Webui. |
| [Wowza Streaming Engine](wowza/index.md) | [latest](wowza/latest/description.md) | Wowza Streaming Engine ist ein kommerzieller Medienserver für Live- und On-Demand-Video: Er nimmt Streams (RTMP, RTSP, SRT, MP4-Upload) an, formt sie mit dem eingebauten Transcoder in Multi-Bitrate… |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/streaming/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
