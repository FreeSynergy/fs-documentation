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
| [latest](latest/description.md) | 0/7 |

### latest

| Datei | Inhalt |
|------|----------|

⚠️ Fehlende Pflichtdateien: `description.md`, `features.md`, `layout.md`, `menus.md`, `shortcuts.md`, `api.md`, `themes/index.md`
<!-- /gen:versions -->
