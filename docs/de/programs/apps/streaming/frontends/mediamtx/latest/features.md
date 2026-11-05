# MediaMTX - Funktionen

## Übersicht

MediaMTX ist ein **Media-Router**: er nimmt Streams entgegen (oder holt sie sich) und stellt sie über alle unterstützten Protokolle bereit — ohne Umkodierung. Konfiguration, Auth und Hooks geschehen deklarativ in YAML.

## Hauptfunktionen

### 1. Protokoll-Vielfalt

- **Empfang und Versand**: RTSP/RTSPS, RTMP/RTMPS, SRT, WebRTC (WHIP/WHEP), MPEG-TS, RTP/UDP
- **Auslieferung im Browser**: HLS, Low-Latency-HLS, fMP4-Segmente, WebRTC
- **MoQ (Media over QUIC)**: nativ über QUIC und über WebTransport
- **Konvertierung nur im Container**: Remux RTSP→HLS→WebRTC ohne Transcoding

### 2. Pfade und Weiterleitung

- statische Pfadliste plus `all`/RegExp-Platzhalter
- **Proxy-Modus**: `source: rtsps://kamera:8322/stream` holt extern ab und verteilt intern
- **Relay**: mehrere MediaMTX-Instanzen koppeln (Publish an andere Instanz)
- `sourceOnDemand`, `runOnDemand`: Quellen bei Bedarf starten (z. B. ffmpeg-Kommando)

### 3. Sicherheit und Zugriffe

- `authMethod: internal` mit Benutzern, Aktionen und Pfad-Mustern
- externe HTTP-Auth (`authHTTPAddress`) oder **JWT** (`authJWTJWKS`, Claim `mediamtx_permissions`)
- IP-/CIDR-Listen pro Nutzer, `apiTrustedProxies`, PROXY-Protocol für RTSP
- Verschlüsselung: RTSPS, RTMPS, HTTPS für HLS/WebRTC/API (`*Encryption`, Server-Key/Cert)

### 4. Aufnahme und Wiedergabe

- Aufnahme in `fmp4`, `mp4`, `mpeg-ts` (`recordFormat`, `recordPartDuration`, `recordSegmentDuration`)
- **Playback-Server** (`:9996`) listet und liefert Aufnahmen
- `recordMode: auto|disk|memory`, Altersfreigabe über Dateinamen-Muster

### 5. Automatisierung und Betrieb

- **Hooks**: `runOnConnect`, `runOnPublish`, `runOnPublishDone`, `runOnUnpublish`, `runOnReady`, `runOnDemand` (Shell-Befehle mit `MTX_*`-Variablen)
- **Control API v3** (`:9997`) für Pfade, Connections, Retransmission, dynamische Pfade
- **Metrics** (`:9998`, Prometheus) und **PPROF** (`:9999`)
- strukturierte Logs (`logStructured: true` → JSONL), `logDestinations: syslog`

## Editoren und Werkzeuge

| Zugang | Zweck |
|--------|-------|
| `mediamtx.yml` | zentrale, deklarative Konfiguration |
| Control API | Änderungen zur Laufzeit (Pfade anlegen/löschen) |
| `MTX_*`-Umgebungsvariablen | Container-Konfiguration ohne Datei |
| `ffprobe`/VLC | externe Prüfung der Endpunkte |

## Was MediaMTX NICHT kann

- **Kein Transcoding, keine Skalierung, keine Wasserzeichen** — Codierung bleibt unverändert (❌)
- **Kein Multi-Bitrate-Packaging** aus einer Quelle (keine Adapter-/Rendition-Kette) (❌)
- **Keine DRM** und keine Token-URLs für HLS (nur Auth-Methoden) (❌)
- **Keine Weboberfläche** (nur API und YAML) (❌)
- **Kein Chat, keine Viewer-Verwaltung, keine Plattform-Publisher** (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| ffmpeg | als `runOnDemand`/`runOnPublish`-Hook oder externe Quelle |
| OBS Studio | RTMP/SRT/WebRTC-Publish direkt an MediaMTX |
| Prometheus/Grafana | Metriken von `:9998` |
| nginx/caddy | TLS und Routing vor HLS/WebRTC/API |
| Docker | offizielle Images, Config per Datei oder Env |
