# MistServer Dokumentation

> Kategorie: [streaming](../../index.md)

## Übersicht

MistServer ist ein schlanker, in C++ geschriebener Streaming-Server ohne Transcoding: er nimmt Live-Streams (RTMP, RTSP, SRT, WebRTC/WHIP) und Dateien an und liefert sie über HTTP, HLS, DASH, WebRTC, RTMP, RTSP und SRT aus — inklusive DVR-Puffer und Push-Ausgängen. Konfiguration und Oberfläche laufen über dasselbe JSON-API auf Port `4242`. Lizenz: GPL-lizenzierte LTS-Ausgabe („LTS") und kommerzielle Pro-Ausgabe.

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
