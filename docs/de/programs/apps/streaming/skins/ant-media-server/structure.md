# Ant Media Server - Struktur & UI/UX

## Übersicht

AMS ist ein Tomcat-Prozess mit Panel (Ports `5080`/`5443`) und Medienports. Diese Datei beschreibt Panel-Layout, Prozessarchitektur und die Anordnung von Anwendungen und Streams.

## Fenster-Struktur

### Hauptbereiche (Panel)

```
┌───────────────────────────────────── Ant Media Server Panel ─────────────────────────┐
│ Logo │ Application-Wähler (live ▾) │ Admin-Menü (Settings, Cluster, SSL, Logout)     │
├──────────────┬───────────────────────────────────────────────────────────────────────┤
│ Seitenleiste │  Content                                                             │
│              │                                                                       │
│ Home / Apps  │  Stream-Kacheln: Status, Viewer, Bitrate, Aktionen (●/■/🔗/⏺)       │
│ Live Stream  │  „Create New Stream" + Buttons                                      │
│ VoD          │  VoD-Tabelle (Status, Preview, Aktionen)                             │
│ Dashboard    │  Diagramme (CPU, RAM, Throughput, Viewer)                            │
│ Settings     │  Formulare (Security, Restreaming, Cluster)                          │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

### Prozess- und Portstruktur

```
Tomcat (ein JVM-Prozess)
 ├── Panel + REST v2          HTTP :5080   HTTPS :5443
 ├── RTMP Ingest              :1935 (RTMPS konfiguriert)
 ├── RTSP / SRT Ingest        kameraspezifische Ports
 ├── WebRTC Signalling        WebSocket über HTTP/HTTPS
 ├── HLS / DASH Delivery      über HTTP(S)
 └── Cluster (Redis)          Origin ⇄ Edge-Knoten
```

### Anwendung → Stream → Ausgänge

- **Application** (`live`, `WebRTCAppEE`, eigene) ist die oberste Ebene; jede App hat eigene Settings und einen REST-Pfad
- **Stream** (Broadcast) gehört zu genau einer App; Stream-ID ist der Schlüssel für URLs und API
- Pro Stream existieren mehrere Ausgangsformen: `…/streams/<id>.m3u8` (HLS), WebRTC-Play-URL, RTMP-Play

## UI/UX

### Design-Prinzipien

- **Kacheln pro Stream**: Status auf einen Blick, Aktionen direkt an der Kachel
- **App-Kontext zuerst**: fast alles setzt die gewählte Application voraus
- **URL-Auswahl statt Ratewege**: „Copy Stream URLs" zeigt alle Ausvarianten in einem Dialog

### Farbschema

- Panel: hell,blaue Akzente; Status grün (live), rot (Fehler/Offline), grau (Ready/VoD)
- Dashboard-Diagramme in Standard-Materialfarben

### Interaktionen

- Start/Stop als Icon auf der Stream-Kachel
- Aufnahme als zweiter Zustand derselben Kachel
- Token-Dialoge und URL-Dialoge als Modals

## Zugänglichkeit

- Panel ist Standard-Web-UI (Tab-Reihenfolge gegeben, aber nicht ausführlich auditiert)
- Diagramme sind grafisch; Zahlenwerte nur teilweise textlich verfügbar
- Media-Player im Panel (WebRTC-Test) ohne Untertitel-Steuerung

## Performance

- Transcoding frisst CPU — Adaptive Bitrate nur mit ausreichend Kernen/GPU betreiben
- Edge/Origin-Trennung hält Zuschauerlast von Transcoding-Prozessen getrennt
- Aufnahme und VoD-Processing laufen asynchron (Processing-Status in der VoD-Tabelle)
- Redis und Panel-Statistik bei sehr vielen Streams beobachten (Speicher)
