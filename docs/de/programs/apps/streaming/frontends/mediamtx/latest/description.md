# MediaMTX - Beschreibung

## Übersicht

MediaMTX ist ein „Ready-to-use live media router": ein einziges Go-Binary, das Videostreams empfangt, aufzeichnet und über praktisch jedes relevante Protokoll wieder aussendet. FreeSynergy nutzt es als Referenz für einen schlanken, konfigurationsgetriebenen Streaming-Knoten.

## Was MediaMTX macht

Ein Encoder (OBS, ffmpeg, Kamera) sendet einen Stream auf einen Pfad. MediaMTX muxed um und liefert denselben Stream an RTSP-Clients, HLS-Player, WebRTC-Browser und SRT-Empfänger gleichzeitig. Zusätzlich proxyt es fremde Quellen, zeichnet auf und meldet Ereignisse per Hooks.

## Vorteile

- **Ein Binary, null Abhängigkeiten**: kein Tomcat, keine Datenbank, kein Build-System
- **Einheitliches Modell**: ein Pfad, viele Protokolle — Port- und Pfadlogik bleiben nachvollziehbar
- **Saubere Sicherheit**: Berechtigungen als (`user`, `action`, `path`, `ips`)-Tupel, optional JWT oder HTTP-Auth
- **Betriebssicher**: Prometheus-Metriken, PPROF, strukturierte Logs, offizielle Docker-Images
- **Moderner Stack**: WebRTC, LL-HLS, SRT und MoQ ohne Zusatz-Addons

## Abgrenzung zu anderen Systemen

### MediaMTX vs. nginx-rtmp-module

- MediaMTX ist ein **eigenständiger Server**; nginx-rtmp ist ein **Modul** in nginx-Konfiguration
- MediaMTX bietet WebRTC, SRT und MoQ; nginx-rtmp nur RTMP, HLS und DASH
- MediaMTX hat eine dokumentierte Control-API; nginx-rtmp arbeitet mit Hook-Skripten

### MediaMTX vs. MistServer

- beide leichtgewichtig und ohne Transcoding; MistServer punktet mit DVR und eingebauter Web-Oberfläche
- MediaMTX punktet mit YAML-Datei, JWT/HTTP-Auth, MoQ und besserer Docker-Tauglichkeit
- MistServer konfiguriert man fast vollständig über die API/Oberfläche, MediaMTX über die Datei

### MediaMTX vs. Ant Media Server / Wowza

- Ant Media und Wowza sind **Plattformen** mit Transcoding, Multi-Bitrate, DRM und Panels
- MediaMTX bewusst schlank: kein Transcoding, keine Renditions, kein Panel — dafür geringe Latenz und einfache Betriebsbarkeit

## Technische Details

- **Backend**: Go, ein Prozess; UDP/TCP-Listener und HTTP-Server im selben Binary
- **Database**: keine — Zustand in `mediamtx.yml` und (optional) API-geänderten Pfaden im RAM
- **Frontend**: keines; HLS/WebRTC-Endpunkte werden von Browser-Playern konsumiert
- **Authentication**: `internal`, `http` oder `jwt`, Aktionen `publish`, `read`, `playback`, `api`, `metrics`, `pprof`
- **Hosting**: Bare-Metal, Docker (`mediamtx`-Image), systemd-Dienst, hinter Reverse-Proxy mit TLS

## Für wen ist MediaMTX geeignet?

- Teams, die einen **eigenen Streaming-Knoten** brauchen, ohne Transcoding-Funktionsumfang
- IoT-/Kamera-Szenarien (RTSP-Quellen proxyen, im Browser abspielen)
- FreeSynergy-Eigenbau: Media-Schiene mit klarer API, deren Logik Skin-Entwickler leicht nachbilden können
- Nicht geeignet, wenn Multi-Bitrate-Renditions, DRM oder Aufzeichnung mit Timeline/Ad-Schnitt gefordert sind
