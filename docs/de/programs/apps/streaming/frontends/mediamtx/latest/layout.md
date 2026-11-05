# MediaMTX - Struktur & UI/UX

## Übersicht

MediaMTX wird über Dateien und Ports „bedient". Diese Datei beschreibt die innere Struktur (Listener, Pfade, Leser) und die Anordnung der Konfiguration — die Vorlage für eine Skin-Oberfläche.

## Server-Struktur

### Hauptbereiche

```
┌──────────────────────── MediaMTX (ein Prozess) ────────────────────────┐
│                                                                        │
│  Listener (Eingang)              Pfad (intern)          Listener (Ausgang)
│  ─────────────────────           ──────────────         ─────────────────────
│  RTSP  :8554   ──┐                                        ┌── HLS :8888     │
│  RTMP  :1935   ──┤                                       ├── WebRTC :8889   │
│  SRT   :8890   ──┼──►   path "test1"  ──► Leser-Liste ──┼── RTSP :8554     │
│  WHIP  :8889   ──┘      (Remux, Queue)                   ├── SRT :8890      │
│                                                          └── MoQ :8892/8893 │
│                                                                        │
│  Control-API :9997   Metrics :9998   Playback :9996   PPROF :9999       │
└────────────────────────────────────────────────────────────────────────┘
```

### Eingangsseite

- Publisher verbinden sich mit Protokoll-Listener und melden einen Pfadnamen an
- Alternativ zieht MediaMTX als **Proxy** die Quelle selbst (`source: rtsps://…`)
- `sourceOnDemand` startet die Quelle verzögert (per `runOnDemand`-Kommando)

### Ausgangsseite

- Jeder Leser (`read`) erhält eine Remux-Kette: gemeinsame Kodierung, eigene Container
- HLS: Segment-Größe und -Anzahl konfigurierbar (`hlsSegmentCount`, `hlsVariant`)
- WebRTC: WHEP-Endpunkt pro Pfad; ICE über `webrtcLocalUDPAddress` und optionale STUN/TURN

### Nebenkanäle

- Hooks rufen Shell-Befehle auf, wenn sich Verbindungszustände ändern
- Control-API spiegelt die laufende Konfiguration und erlaubt Laufzeitänderungen
- Aufnahmen landen im Dateisystem und werden über den Playback-Server angeboten

## UI/UX (Übertragung auf eine Skin-Oberfläche)

### Design-Prinzipien

- **Deklarativ**: eine Ansicht zeigt die YAML-Struktur, nicht Formular-Kaskaden
- **Pfad als Zentralobjekt**: alle Protokoll-Angaben hängen an einem Pfad-Eintrag
- **Ports sichtbar machen**: Liste der Listener mit Status (aktiv/inaktiv) ist Kern der Ansicht

### Farbschema und Typografie

- keine eigene UI; Vorschlag: helle Standard-Oberfläche, Ports und Pfade in Monospace
- Status als Badge: `live` (grün), `verfügbar` (grau), `Fehler` (rot)

### Interaktionen

- Pfad anlegen/bearbeiten/löschen über Control-API, nicht über Datei-Roundtrip
- Live-Statistik pro Pfad (Reads, Bytes, Bitrate) aus Control-API/Metrics

## Zugänglichkeit

- Konfiguration ist Text → vollständig vorlesbar und versionierbar (Git)
- Logs strukturiert (JSONL) → gut für Screenreader und Weiterverarbeitung
- Für Browser-Wiedergabe gilt: HLS/WebRTC-Player müssen Untertitel und Tastatursteuerung selbst mitbringen

## Performance

- `writeQueueSize` steuert Durchsatz vs. RAM; `readTimeout`/`writeTimeout` begrenzen hängende Clients
- HLS wird standardmäßig nur bei Bedarf geremuxt (`hlsAlwaysRemux` vermeidet Request-Verzögerung)
- Ein Pfad mit vielen Lesern bleibt cheap, weil nur remuxt, nie transkodiert wird
- `udpMaxPayloadSize`/`udpReadBufferSize` bei Paketverlust in Netzen mit kleinem MTU anpassen
