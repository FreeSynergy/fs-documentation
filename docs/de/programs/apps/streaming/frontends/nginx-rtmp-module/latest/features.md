# nginx-rtmp-module - Funktionen

## Übersicht

Das Modul macht aus nginx einen RTMP-Empfänger und Verteiler: Publish annehmen, HLS/DASH mitschreiben, aufzeichnen, weiterreichen — alles deklarativ in `nginx.conf`.

## Hauptfunktionen

### 1. RTMP-Empfang und -Verteilung

- RTMP-Publish und -Play auf Port `1935`
- mehrere `application`-Blöcke (z. B. `live`, `vod`, `cam`)
- `interleave`, `wait_key`, `wait_video` für stabile Übertragung
- `drop_idle_publisher` und `timeout` gegen Leerverbindungen

### 2. Packaging

- **HLS**: Segmente + Playlist, `hls_fragment`, `hls_playlist_length`, `hls_nested`, `hls_base_url`
- **DASH**: `dash_path`, `dash_fragment`, `dash_playlist_length`
- Auslieferung über normalen nginx-`http`-Block (CORS, Cache, TLS via nginx)

### 3. Aufzeichnung und VoD

- `record all` / `record video` / `record audio` mit `record_path`
- VoD-Ausspielung über `play <pfad>` im `application`-Block (Media-Set)
- `on_record_done`-Hook für Nachverarbeitung (ffmpeg-Schnitt, Upload)

### 4. Weiterleitung und Cluster

- `pull rtmp://…` als Relay (Eingang von anderer Instanz)
- Ketten von nginx-rtmp-Instanzen für origin/edge-Aufbau

### 5. Automatisierung

- **HTTP-Hooks**: `on_publish`, `on_publish_done`, `on_play`, `on_play_done`, `on_done`, `on_update`, `on_record_done`, `on_drop`
- `on_publish`/`on_play` entscheiden über Zulassung (HTTP-Statuscode)
- **`exec`**: pro Stream ein Prozess (Standard: ffmpeg-Transcoding), Variablen `$(name)`, `$(app)`, `$(addr)`

## Editoren und Werkzeuge

| Werkzeug | Zweck |
|----------|-------|
| `nginx.conf` | einzige Konfigurationsfläche |
| `stat.xsl` | Statusseite im Browser (Streams, Leser, Bitraten) |
| ffmpeg | Transcoding/Aufbereitung via `exec` |
| OBS Studio / ffmpeg | Publisher auf `rtmp://host/live/<name>` |

## Was das Modul NICHT kann

- **Kein WebRTC, kein SRT, kein LL-HLS** (❌)
- **Kein RTMPS/TLS für RTMP** — Verschlüsselung nur für HLS über nginx (❌)
- **Kein Transcoding eingebaut** — ffmpeg muss selbst verdrahtet werden (❌)
- **Keine Multi-Bitrate-Renditions** aus einer Quelle ohne eigene ffmpeg-Kette (❌)
- **Keine DRM, keine Token-URLs** (nur Hook-basierte Prüfung) (❌)
- **Kein aktives Monitoring/Alerting** über die Statusseite hinaus (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| ffmpeg | `exec`/`exec_async`, `on_record_done` |
| hls.js / video.js | Wiedergabe der HLS-Ausgabe |
| Prometheus | Status-XML per Exporter übersetzen |
| Certbot/TLS | HTTPS für HLS im `http`-Block |
