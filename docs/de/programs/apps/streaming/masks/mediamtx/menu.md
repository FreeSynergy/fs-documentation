# MediaMTX - Menüpunkte

## Übersicht

MediaMTX hat **keine Oberfläche**. Bedient wird über die Konfigurationsdatei `mediamtx.yml`, Kommandozeile und Control-API. Die „Menüpunkte" sind die Abschnitte der Konfiguration.

## Konfigurationsabschnitte (`mediamtx.yml`)

| Abschnitt | Inhalt |
|-----------|--------|
| `logLevel`, `logDestinations`, `logStructured` | Loggen (stdout, Datei, syslog; JSONL) |
| `readTimeout`, `writeTimeout`, `writeQueueSize` | Timings und Sende-Queue |
| `authMethod` (`internal`/`http`/`jwt`) + `authInternalUsers` | Nutzer, Aktionen (`publish`, `read`, `playback`, `api`, `metrics`, `pprof`), IP-Listen |
| `rtsp`, `rtmp`, `hls`, `webrtc`, `srt`, `moq` | Protokoll-Listener ein/aus und Adressen |
| `api`, `metrics`, `pprof`, `playback` | Zusatz-Server (9997, 9998, 9999, 9996) |
| `pathDefaults` | Defaults für alle Pfade |
| `paths` | pro Pfad: `source`, `sourceProtocol`, `runOn*`-Hooks, `record`, `recordPath` |
| `runOnConnect`, `runOnDisconnect` | globale Hooks (Umgebungsvariablen `MTX_CONN_TYPE`, `MTX_CONN_ID`) |

## Protokoll-Listener (Default-Ports)

| Protokoll | Adresse | Anmerkung |
|-----------|---------|-----------|
| RTSP | `:8554` | TCP-Handshake, UDP/Multicast optional |
| RTSPS | `:8322` | verschlüsselt |
| RTMP / RTMPS | `:1935` / `:1936` | |
| HLS | `:8888` | `hlsVariant`: `lowLatency`, `fmp4`, `mpegts` |
| WebRTC | `:8889` | WHIP/WHEP; ICE-UDP `:8189` |
| SRT | `:8890` (UDP) | |
| MoQ | `:8892` (HTTP/2+HTTP/3), `:8893` (QUIC) | |
| Control API | `:9997` | `api: yes` nötig |
| Metrics | `:9998` | Prometheus |
| PPROF | `:9999` | Profilberichte |
| Playback | `:9996` | Aufnahmen herunterladen |

## Pfade (Streams)

| Feld | Bedeutung |
|------|-----------|
| `all`, `all_others`, `test1`, RegExp mit `~` | Pfad-Matching |
| `source: publisher` | von Publishern empfangen (Standard) |
| `source: rtsp://…` / `rtmp://…` / `udp+mpegts://…` | Pull von anderer Quelle (Proxy) |
| `sourceOnDemand` | Quelle erst bei Bedarf starten |
| `record: yes` + `recordPath` | Aufnahme (z. B. `/recordings/%path/%Y-%m-%d_%H-%M-%S-%f`) |

## Menüs nach Rolle

| Rolle | Zugriff |
|-------|---------|
| anonym | Pfade je nach `authInternalUsers`-Berechtigung |
| `publish` | Senden an Pfade (Encoder, OBS) |
| `read`/`playback` | Konsumieren und Aufnahmen laden |
| `api` | Control-API, nur localhost oder explizit freigeschaltet |
| Betrieb | Datei `mediamtx.yml`, `systemctl`, Docker-Umgebungsvariablen |
