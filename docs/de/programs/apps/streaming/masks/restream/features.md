# Restream - Funktionen

## Übersicht

Restream ist ein SaaS-Dienst: Er übernimmt Ingest, Weiterleitung, Chat-Bündelung und Auswertung. FreeSynergy dokumentiert ihn als Referenz für eine plattformübergreifende Multistreaming-Oberfläche.

## Hauptfunktionen

### 1. Multistreaming

- ein Eingang (RTMP/SRT aus OBS, ffmpeg oder direkt aus dem Studio) → viele Ziele
- 30+ Plattformen per Login koppeln: YouTube, Twitch, Facebook, LinkedIn, TikTok, Vimeo u. a.
- Custom-Ziele über RTMP-URL und Key
- Zielanzahl und Parallelität sind planabhängig

### 2. Restream Studio (Browser-Produktion)

- Szenen, Quellen (Kamera, Screen-Sharing, Medien, Browser-Overlay), Layouts
- Overlays, Texte, Bilder, Backdrops
- Gäste per Link; Interview-/Panel-Ansichten
- Proben ohne Senden (Soundcheck, Preview)

### 3. Events und Zeitplan

- geplante Lives mit Countdown/Pre-Roll
- automatische Aufnahme und Übernahme in die Videobibliothek
- Erinnerungen und teilbare Event-Seiten

### 4. Chat und Moderation

- alle Plattform-Chats in einer Ansicht
- Moderatoren-Funktionen, Filter, Spam-Schutz
- Antworten aus einer Konsole heraus

### 5. Analytics

- Viewer-Verlauf, Watch-Time, Interaktionen
- Aufschlüsselung pro Plattform und pro Event
- Export/Berichte je nach Plan

### 6. Video und Einbettung

- VOD-Bibliothek, Uploads, Wiedergabelisten
- eingebetteter Player (Branding nach Plan) für eigene Seiten

## Editoren

| Editor | Zweck |
|--------|-------|
| Restream Studio | vollständige Produktion im Browser |
| externe Encoder | OBS/ffmpeg senden an Restream-Ingest |
| Event-Planer | Zeitplanung, Pre-Rolls |

## Was Restream NICHT kann

- **Kein Selbstbetrieb** — Daten und Infrastruktur liegen beim Anbieter (❌)
- **Kein direkter Zugriff auf Server-Konfiguration** (Ports, Protokolle, Transcoding-Profile) (❌)
- **Keine unbegrenzte Zielanzahl** — Pläne begrenzen Ziele und Streaming-Zeit (❌)
- **Kein DRM und keine private Video-Cloud** im Sinne eines eigenen CDNs (❌)
- **Kein API-Zugang zu allen Dashboard-Funktionen** (Studio-Szenen sind nicht API-steuerbar) (❌)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| OBS Studio / ffmpeg | RTMP/SRT-Ingest laut Dashboard |
| eingebetteter Player | Iframe-Snippet auf eigenen Seiten |
| Chat-Widgets | Chat-Einbettung für Streams |
| REST/WebSocket-APIs | Automatisierung von Zielen, Events, Status |
