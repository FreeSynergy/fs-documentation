# GStreamer Dokumentation

## Übersicht

GStreamer ist ein Multimedia-Framework in C: Aufnahme, Dekodierung, Filterung, Kodierung und Ausgabe werden als **Pipeline aus Elementen** (Source → Filter/Codec → Sink) aufgebaut. Werkzeuge wie `gst-launch-1.0` und `gst-inspect-1.0` erschließen das System über die Shell, eigene Programme nutzen die C-API (oder Python/Rust-Bindungen). Stack: C + GObject, LGPL 2.1, Pakete base/good/bad/ugly, WebRTC über `webrtcbin`.

## Dateistruktur

- [menu.md](menu.md) - Werkzeuge, Kommando-Syntax, Element-Inspektion, Rollen
- [features.md](features.md) - Elemente, Container, Hardware, WebRTC, Was GStreamer NICHT kann
- [description.md](description.md) - Abgrenzung zu ffmpeg, OBS Studio, MediaMTX und MistServer
- [structure.md](structure.md) - Pipeline-Modell, Pads/Caps, Bus, Zustände, Debug-Werkzeuge
- [shortcuts.md](shortcuts.md) - Tasten in `gst-play-1.0`, Optionen der CLI-Werkzeuge
- [api.md](api.md) - C-API, appsrc/appsink, gst-rtsp-server, Bindungen, Debug-Umgebung
