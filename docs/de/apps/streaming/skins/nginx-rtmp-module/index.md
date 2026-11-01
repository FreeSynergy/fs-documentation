# nginx-rtmp-module Dokumentation

## Übersicht

Das nginx-rtmp-module (arut) erweitert nginx um einen RTMP-Server: Es nimmt RTMP-Publishes an, schreibt HLS- und DASH-Streams mit, zeichnet auf und leitet per Relay weiter. Konfiguration geschieht ausschließlich über `nginx.conf`; Steuerung läuft über HTTP-Hooks und die Statusseite. Geschrieben in C, BSD-lizenziert, seit Jahren ohne wesentliche Weiterentwicklung — WebRTC und SRT fehlen.

## Dateistruktur

- [menu.md](menu.md) - Konfigurationsblöcke (`rtmp`, `application`, `http`), Statusseite, Rollen
- [features.md](features.md) - RTMP/HLS/DASH, Hooks, `exec`, Relay, Was das Modul NICHT kann
- [description.md](description.md) - Abgrenzung zu MediaMTX, MistServer und Restreamer
- [structure.md](structure.md) - nginx-Prozesse, Verzeichnislayout der Ausgabe, Konfigschichten
- [shortcuts.md](shortcuts.md) - nginx-Kommandozeile (`-t`, `-s reload`), keine UI-Tasten
- [api.md](api.md) - HTTP-Hooks (`on_publish`, `on_play`, `on_record_done`), Status-XML, `exec`
