# GStreamer - Beschreibung

## Übersicht

GStreamer ist das Multimedia-Unterbau-Framework des freedesktop-Umfelds: Es stellt Decoder, Encoder, Filter, Netzwerk-Elemente und eine Pipeline-Laufzeit bereit, auf der Anwendungen und Server aufsetzen.

## Was GStreamer macht

GStreamer dekodiert, filtert, kodiert und verteilt Audio, Video und Text. Aus Elementen werden Pipelines gebaut, die lokal (Datei, Kamera, Bildschirm) oder über Netzwerke (RTSP, SRT, RTMP, HLS, WebRTC, MPEG-TS/UDP) arbeiten. Jede Anwendung, die Medien verarbeiten will, kann diese Bausteine über C, Python oder Rust nutzen.

## Vorteile

- **Modularität**: neue Codecs oder Filter sind einzelne Plugins, ohne Anwendungen zu ändern
- **Plattformübergreifend**: Linux, Windows, macOS, Android, iOS, Embedded (Yocto, Buildroot)
- **Hardware-Beschleunigung**: VAAPI, NVENC/NVDEC, QSV, V4L2, Vulkan, OpenGL aus ein und derselben Pipeline
- **Zeitgemäße Protokolle**: WebRTC, SRT und LL-HLS aus erster Hand
- **Wartung und Offene Lizenz**: LGPL 2.1, aktive Community, Release-Zyklus etwa alle sechs Monate

## Abgrenzung zu anderen Systemen

### GStreamer vs. FFmpeg

- FFmpeg ist ein **Werkzeugkasten für Kommandozeilen-Jobs** (Transcoding, Analyse); GStreamer ist eine **Laufzeit-Bibliothek** für lang laufende Pipelines
- FFmpeg-Pipelines sind pro Aufruf statisch; GStreamer-Pipelines sind zur Laufzeit änderbar (Pads an-/abhängen, Elemente zum-/abschalten)
- Beide nutzen dieselben Codec-Bibliotheken; GStreamer baut sie als Elemente nach, FFmpeg als Encoder/Dekoder im Programm

### GStreamer vs. OBS Studio

- OBS ist eine fertige Produktionsanwendung (Szenen, Mischer, Hotkeys) — GStreamer liefert nur die Bausteine
- OBS nutzt eigene libobs-Filter, aber für etliche Quellen und WebRTC ein GStreamer-Plugin
- Für FreeSynergy-Skins gilt: OBS-Oberfläche nachbilden, GStreamer als Medienschiene im Hintergrund

### GStreamer vs. MediaMTX / MistServer

- MediaMTX und MistServer sind **Streaming-Server** mit Konfiguration und API; GStreamer ist eine Bibliothek, aus der man sich so einen Server selbst bauen kann
- Kein Aufnahmemanager, keine Viewer-Verwaltung, keine Ports, die „einfach da sind"

## Technische Details

- **Backend**: C mit GObject/GLib; Plugin-Registry (`~/.cache/gstreamer-1.0`)
- **Datenmodell**: `GstBuffer`, `GstCaps`, Pads, Bins, Bus (asynchrone Messages)
- **Frontend**: keines — Werkzeuge (CLI) oder Toolkits der Anwendung
- **Authentication**: keine eigene; bei Quellen wie `rtspsrc` über URL/Headers
- **Hosting**: läuft im Prozess der Anwendung, in Containern oder als Grundlage eigener Server

## Für wen ist GStreamer geeignet?

- Teams, die **eigene Medien-Tools** (Recorder, Streaming-Knoten, Wiedergabe) bauen wollen
- Embedded- und Linux-Produkte mit Hardware-Codecs
- Automatisierung, in der Pipelines zur Laufzeit umgebaut werden müssen
- Weniger geeignet für: schnelle Einmal-Transcodes (→ FFmpeg) oder fertige Streaming-Server (→ MediaMTX, MistServer)
