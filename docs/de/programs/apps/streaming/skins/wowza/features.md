# Wowza Streaming Engine - Funktionen

## Hauptfunktionen

- **Breiter Eingang**: RTMP/RTMPS, RTSP, SRT (ab 4.6), MP4-/Progressive-Upload, HTTP-Pull von Fremd-Quellen (HTTP Publisher)
- **Breiter Ausgang**: HLS, Low-Latency-HLS, CMAF/Chunked CMAF, MPEG-DASH, Smooth Streaming, progressives MP4, RTMP-Play; WebRTC je nach Version/Modul (⚠)
- **Live Transcoder**: Multi-Bitrate-Leitern, Audio-Remixing, Watermarking; Vorlagen in `TranscoderTemplates.xml`
- **nDVR und Time Shift**: Live-Aufzeichnung mit Sprung zurück ins laufende Programm
- **Stream Targets**: paralleles Restreaming an externe RTMP-Ziele (YouTube, Twitch, andere Server)
- **Publisher Control**: Einspeiser einzeln freigeben oder blockieren, auch im laufenden Betrieb
- **Sicherheit**: Hash-Key-/Token-Authentifizierung für Play und Publish, eigene Auth-Module, IP-Filter
- **DRM** (Add-on): Widevine, FairPlay, PlayReady für HLS/DASH
- **Skalierung**: Live Repeater (Origin/Edge-Kette) und Load Balancer Add-on für große Zuschauerzahlen
- **Erweiterbarkeit**: Java-Modul-API, Hooks in den Stream-Lebenszyklus (publish, play, close …)

## Was Wowza NICHT kann

- **Kein eingebauter CDN** — Verteilung über eigene Edge-Kette oder externen CDN (❌ integriert)
- **Kein Player-Portal / keine Upload-Website** für Endnutzer (❌, nur Wiedergabe-URLs)
- **Kein Chat, keine Community-, keine Analytics-Dashboards** über Log Viewer hinaus (❌)
- **Keine Mandantenfähigkeit** — pro Instanz ein Verwaltungsmodell (❌)
- **Keine automatische Plattform-Anbindung mit Login** (kein OAuth zu YouTube/Twitch wie bei SaaS-Diensten) (❌)
- **Kostenpflichtig**: Lizenz pro Instanz, kein freier Funktionsstamm (❌ Open Source)

## Editoren

| Editor | Wo | Zweck |
|--------|----|-------|
| Properties-Masken | Manager | Einstellungen ohne XML-Handarbeit |
| XML-Dateien | `conf/` der Instanz | vollständige Konfiguration (maßgeblich) |
| Transcoder-Vorlagen | XML/Manager | Bitrate-Leitern definieren |

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Add-ons | DRM, Load Balancer, Publisher Control u. a. (im Aboumfang je nach Lizenz) |
| Java-Module | eigene Authentifizierung, Event-Verarbeitung, Routing |
| OBS/ffmpeg als Einspeiser | Standard-RTMP/SRT-Push |
| Player | JW Player, Video.js, hls.js u. a. über die HLS-/DASH-URLs |
