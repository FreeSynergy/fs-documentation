# Restreamer - Funktionen

## Hauptfunktionen

- **Push-Eingang**: RTMP(S) mit Push-Key, alternativ RTSP/SRT-Eingang in neuen Versionen
- **Browser-Player** mit HLS und (optional) WebRTC, Einbettungs-Snippet, Direktdownload der Segmente
- **Restreaming**: gleichzeitiges Weiterleiten an mehrere RTMP-Ziele (Multi-Target)
- **Aufzeichnung** in Segmente (Standard: 2-Minuten-Intervalle) auf Volume, optional Transcoding per ffmpeg
- **Snippets/Tools**: Vorschaubild generieren, Statistik, Support-Logpaket
- **Einfacher Betrieb**: ein Docker-Image, Konfiguration über UI oder `restreamer-cli`

## Was der Restreamer NICHT kann

- **Kein Bildmischer / keine Szenen** — er leitet weiter, was ankommt (❌)
- **Keine Plattform-APIs** (kein automatisches YouTube-Upload-Management, kein Chat) (❌)
- **Kein adaptives Multi-Bitrate-Packaging** (nur eine HLS-Variante; kein HLS-Master mit mehreren Stufen) (❌)
- **Kein DRM und keine Token-geschützte HLS-Auslieferung** out of the box (❌)
- **Kein Monitoring/Alerting** über Logs hinaus (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| ffmpeg | integriert für Transcoding/Aufnahme |
| nginx-rtmp-module | Basis des Empfangs, Direktiven konfigurierbar |
| `restreamer-cli` | offizielle Kommandozeile für Settings und Hooks |
| Hooks | `on_publish`, `on_publish_done`, `on_record_done` per Script/HTTP |
| Storage | Docker-Volume `statistics` und `records` |
