# MistServer - Funktionen

## Übersicht

MistServer ist spezialisiert auf **Empfang, Verteilung und Aufzeichnung** ohne eigene Bildbearbeitung: Ein Eingang, viele Ausgänge, Push-Regeln und ein DVR-Puffer pro Stream.

## Hauptfunktionen

### 1. Eingänge (Quellen)

| Quelle | Syntax / Weg |
|--------|--------------|
| Live-Push | `push://` (RTMP, RTSP, SRT, WebRTC), optional IP-Whitelist oder Passwort |
| SRT-Listener | `srt://:9876` |
| WHIP | `http://host:8080/webrtc/streamname` |
| Datei / Ordner | `/media/beispiel.mp4`, Ordner für VoD-Auswahl |
| MPEG-TS über UDP | `tsudp://239.0.0.1:9876/` (Multicast, interface-wählbar) |
| Pull über HTTP | `http://…/index.m3u8` (HLS) |
| Stream-Keys | Token statt Streamname im Push-Ziel |

### 2. Ausgänge (Protokolle)

- HTTP progressiv (MP4/FLV/WebM), **HLS**, **DASH**, **WebRTC**
- RTMP, RTSP, SRT als Viewer-Protokolle (je nach aktiviertem Connector)
- Track-Auswahl pro Protokoll (letzte kompatible Spur als Default)

### 3. Push und Aufzeichnung

- **Automatic push**: Regel pro Stream, startet bei Aktivität (auch zeit-/variablen-gesteuert)
- **Single push**: einmalig starten; kein automatischer Neustart bei Fehlern
- **Aufzeichnung** gilt als Push auf lokalen Pfad; `.ts`/`.mkv` empfohlen, MP4 als fMP4
- Mehrere Automatic-push-Regeln pro Stream möglich

### 4. Puffer und Sicherheit

- **DVR-Puffer** pro Stream konfigurierbar (`DVR` in Millisekunden)
- Rechte nur auf der API-Schnittstelle (Login, Challenge-Hash), Media-Ports ohne Nutzer
- Push-Zugriff über IP-Whitelist, Passwort oder Stream-Key abstufbar

## Editoren und Begleitwerkzeuge

| Werkzeug | Zweck |
|----------|-------|
| Weboberfläche (`:4242`) | Protocol-, Streams- und Push-Seite |
| JSON-API (`command`-Parameter) | vollständige Konfiguration automatisieren |
| `config.json` / `/etc/mistserver.conf` | direkte Konfiguration (Expertenweg) |
| MistServer-Statistiken (`stats_streams`) | Viewer-Zahlen und Live-Position |

## Was MistServer NICHT kann

- **Kein Transcoding, keine Skalierung, keine Renditions** (❌)
- **Kein Bildmischer, keine Overlays, keine Szenen** (❌)
- **Kein Multi-Bitrate-HLS-Master** aus einer Quelle (❌)
- **Kein DRM und keine Token-geschützte Wiedergabe** (❌)
- **Kein Chat, keine Social-Publisher, keine Viewer-Verwaltung** (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| OBS Studio | Push per RTMP/SRT/WebRTC auf `push://`-Stream |
| ffmpeg | als Push-Ziel oder Quelle (`tsudp`, HLS) |
| Docker | offizielle Images, Ports und Volumes konfigurierbar |
| Monitoring | Statistik-Kommandos der API (`stats_streams`, `clients`) |
