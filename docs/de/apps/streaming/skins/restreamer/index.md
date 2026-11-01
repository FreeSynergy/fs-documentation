# Restreamer Dokumentation

## Übersicht

Der (Docker) Restreamer ist ein Komplettpaket für eigenen Videoempfang und -verteilung: nginx + nginx-rtmp-module + Node.js-Webui. Er nimmt RTMP/Push-Streams an, spielt sie im Browser ab (HLS/WebRTC) und gibt sie an Ziele wie YouTube oder Twitch weiter.

## Dateistruktur

- [menu.md](menu.md) - Webui-Bereiche, Settings, Logs
- [features.md](features.md) - Push/Pull, Player, Multi-Target, Was der Restreamer NICHT kann
- [description.md](description.md) - Abgrenzung zu MediaMTX, nginx-rtmp und Restream (SaaS)
- [structure.md](structure.md) - Webui-Masken, Player-Einbettung
- [shortcuts.md](shortcuts.md) - Shortcuts (Webui hat keine) und CLI-Alternative
- [api.md](api.md) - `restreamer-cli`, Config-Datei, Hooks, RTMP/HTTP-Endpunkte
