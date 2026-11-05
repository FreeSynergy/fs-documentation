# Ant Media Server - Menüpunkte

## Übersicht

Der AMS hat ein **Web-Panel** (Standard-Ports: HTTP `5080`, HTTPS `5443`). Fast jede Panel-Aktion hat ein Gegenstück in der REST-API (`/rest/v2/…`).

## Hauptmenüpunkte

### 1. Apps / Application-Verwaltung

- **Funktion**: Anwendungen anlegen und verwalten (`live`, `WebRTCAppEE`, eigene App-Namen)
- **Details**:
  - neue Application erstellen (RTMP-Streaming-App, WebRTC-App)
  - Application-Einstellungen (Aufnahme, Transcoding, Token-Sicherheit)
  - App löschen / REST-Basispfad einer App ansehen

### 2. Live Streaming

- **Funktion**: Streams anlegen, starten, stoppen, beobachten
- **Details**:
  - „Create New Stream" (Broadcast-Typen: Live Stream, IP Camera, Stream Source, List)
  - Stream-Liste mit Status, Viewer-Zahl, Bitrate, Laufzeit
  - „Copy Stream URLs" (RTMP/Eingang, HLS/WebRTC/Player-Ausgänge)
  - „Join the Stream" (Test-Player im Panel)
  - Aufnahme starten/stoppen, Dashboard-Diagramme

### 3. VoD

- **Funktion**: Aufnahmen und hochgeladene Videos verwalten
- **Details**: Upload, Liste mit Status (Processing/Ready), Löschen, Direktlinks

### 4. Dashboard / Statistiken

- CPU, RAM, Netzwerk, aktive Streams, Viewer-Zahlen, Bitrate-Verlauf

### 5. Settings

| Bereich | Inhalt |
|---------|--------|
| General | Server-Name, Ports, RTMP-Port |
| Advanced | Data-Settings, Aufnahme-Defaults, Logging |
| Security | IP-Filter für REST, Play/Publish-Token, JWT |
| Restreaming | Ziele (YouTube, Twitch, …) und Weiterleitung |
| Cluster / Redis | Cluster-Modus, Edge/Origin-Knoten |
| SSL-Zertifikate | PEM/PFX hochladen |

## Kontext-Menüs

| Objekt | Aktionen |
|--------|----------|
| Stream-Kachel | Start, Stop, Löschen, URLs kopieren, Aufnahme, Statistiken |
| VoD-Eintrag | Abspielen, Download, Löschen, Umbenennen |
| Application | Einstellungen, REST-Pfad, Löschen |

## Menüs nach Benutzerrolle

| Rolle | Zugriff |
|-------|---------|
| Admin (Panel-Login) | alle Menüpunkte, Settings, Cluster |
| API-Nutzer | REST v2 je App, gesichert über IP-Filter oder JWT |
| Zuschauer | nur Media-Endpunkte (HLS/WebRTC-Player), kein Panel |
| Publisher | RTMP/SRT/WebRTC-Ingest mit Stream-ID (und Token, wenn aktiviert) |
