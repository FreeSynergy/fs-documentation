# MediaMTX Dokumentation

> Kategorie: [streaming](../../index.md)

## Übersicht

MediaMTX (früher `rtsp-simple-server`) ist ein schlanker Live-Media-Router in **Go**: ein Binary, eine YAML-Datei, und der Server nimmt Streams an und liefert sie über RTSP, RTMP, SRT, WebRTC, HLS/LL-HLS, MPEG-TS, RTP und MoQ aus. Er transkodiert nicht, sondern mux/remux und verteilt. Stack: Go, MIT-Lizenz, Konfiguration über `mediamtx.yml`, Steuerung über Control-API (Port 9997).

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Dokumentierte Versionen

<!-- gen:versions (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | 0/7 |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastatur-Shortcuts |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
