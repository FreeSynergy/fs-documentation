# MistServer Dokumentation

## Übersicht

MistServer ist ein schlanker, in C++ geschriebener Streaming-Server ohne Transcoding: er nimmt Live-Streams (RTMP, RTSP, SRT, WebRTC/WHIP) und Dateien an und liefert sie über HTTP, HLS, DASH, WebRTC, RTMP, RTSP und SRT aus — inklusive DVR-Puffer und Push-Ausgängen. Konfiguration und Oberfläche laufen über dasselbe JSON-API auf Port `4242`. Lizenz: GPL-lizenzierte LTS-Ausgabe („LTS") und kommerzielle Pro-Ausgabe.

## Dateistruktur

- [menu.md](latest/menus.md) - Weboberfläche: Protocol-, Streams- und Push-Seite, Rollen
- [features.md](latest/features.md) - Ein-/Ausgänge, DVR, Aufzeichnung, Was MistServer NICHT kann
- [description.md](latest/description.md) - Abgrenzung zu MediaMTX, nginx-rtmp und Ant Media Server
- [structure.md](latest/layout.md) - Ports, Interfaces, Aufbau der Konfiguration
- [shortcuts.md](latest/shortcuts.md) - Kommandozeile und Dienstverwaltung
- [api.md](latest/api.md) - JSON-API auf 4242 (`command`-Parameter), Auth-Challenge, Beispiele
