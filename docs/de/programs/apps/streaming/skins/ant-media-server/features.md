# Ant Media Server - Funktionen

## Übersicht

AMS ist die funktionsreichste Open-Source-basierte Streaming-Plattform in dieser Kategorie: Empfänger, Transcoding, Packaging, Aufnahme, Tokens, Cluster und ein Panel — alles durch eine REST-API automatisierbar.

## Hauptfunktionen

### 1. Empfassung und Auslieferung

- **Eingang**: RTMP, RTSP (IP-Kameras), SRT, WebRTC (Broadcast), MP4-Upload
- **Ausgang**: WebRTC (Ultra-Low-Latency), HLS, Adaptive/ABR-HLS, DASH (Enterprise)
- Broadcast-Typen: Live Stream, IP Camera, Stream Source, Playlist

### 2. Adaptive Multi-Bitrate (Enterprise)

- Transcoding-Profil mit mehreren Stufen (z. B. 240p–1080p, H.264 + AAC)
- automatische Rendition-Umschaltung im HLS-Master
- GPU-Codierung für hohe Zuschauerzahlen

### 3. Sicherheit und Zugang

- **Publish-/Play-Token** (zeitbegrenzte Tokens pro Stream)
- **JWT-Security** (Enterprise) für Player und API
- IP-Filter für REST-Aufrufe
- RTMPS/HTTPS über hochgeladene Zertifikate

### 4. Aufnahme und VoD

- Aufnahme laufender Streams (mp4), VoD-Bibliothek im Panel
- VoD-Upload mit Processing-Pipeline (Preview-Bild, Play-Liste)
- Playlisten für A/B-Rotation und Jingle-Abfolge (Enterprise)

### 5. Skalierung

- **Cluster** mit Origin/Edge-Knoten über Redis
- Autoscaling in AWS/Azure/GCP (AMIs/Marktplatz-Images)
- Monitoring über Panel-Dashboard und REST-Statistiken

### 6. Weiterleitung und Integration

- **Restreaming** zu mehreren Social-Zielen gleichzeitig (Enterprise)
- Webhooks für Stream-Ereignisse
- SDKs: Web (WebSocket/WebRTC), Android, iOS, Flutter (Enterprise teils)

## Editoren und Begleitwerkzeuge

| Werkzeug | Zweck |
|----------|-------|
| Web-Panel | Streams, VoD, Einstellungen, Dashboard |
| REST v2 (Swagger) | Panel-Funktionen automatisieren (`antmedia.io/rest`) |
| Panel-eigener Test-Player | WebRTC-Verbindung prüfen |
| Admin-CLI (`antmedia-service`) | Dienst starten/stoppen, Status |

## Was der Ant Media Server NICHT kann

- **Kein Bildmischer / keine Szenen** — mischen muss OBS oder ein Studio-Tool (❌)
- **Community-Version ohne Adaptive Transcoding** — Multi-Bitrate ist Enterprise (❌)
- **Kein DRM** im offenen Sinne (Widevine/FairPlay nicht enthalten; Tokens ja, Lizenzen nein) (❌)
- **Kein Chat und keine Viewer-Profile** (❌)
- **Kein Ad-Insertion** (kein Server-side Ad-Tearing) (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| OBS Studio | RTMP/SRT/WebRTC-Ingest auf `live`-App |
| hls.js / video.js / VLC | HLS- und DASH-Wiedergabe |
| Redis | Cluster-Zustand |
| Cloud-Marktplätze | fertige Images (AWS, Azure, GCP) |
| eigene Apps | REST v2 + SDKs für Panels und Automatisierung |
