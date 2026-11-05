# MediaMTX Dokumentation

## Übersicht

MediaMTX (früher `rtsp-simple-server`) ist ein schlanker Live-Media-Router in **Go**: ein Binary, eine YAML-Datei, und der Server nimmt Streams an und liefert sie über RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS, MPEG-TS, RTP und MoQ aus. Er transkodiert nicht, sondern mux/remux und verteilt. Stack: Go, MIT-Lizenz, Konfiguration über `mediamtx.yml`, Steuerung über Control-API (Port 9997).

## Dateistruktur

- [menu.md](latest/menus.md) - Konfigurationsabschnitte, Pfade, Protokoll-Listener, Rollen
- [features.md](latest/features.md) - Protokolle, Auth, Aufnahme, Hooks, Was MediaMTX NICHT kann
- [description.md](latest/description.md) - Abgrenzung zu nginx-rtmp, MistServer, Ant Media und Restreamer
- [structure.md](latest/layout.md) - Listener → Pfade → Leser, Ports, Log- und Konfigstruktur
- [shortcuts.md](latest/shortcuts.md) - Kommandozeile und Dienstverwaltung (keine UI-Tasten)
- [api.md](latest/api.md) - Control API v3 (9997), Hooks, Metrics, Playback-Server
