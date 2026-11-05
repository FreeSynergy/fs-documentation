# nginx-rtmp-module Dokumentation

> Kategorie: [streaming](../../index.md)

## Übersicht

Das nginx-rtmp-module (arut) erweitert nginx um einen RTMP-Server: Es nimmt RTMP-Publishes an, schreibt HLS- und DASH-Streams mit, zeichnet auf und leitet per Relay weiter. Konfiguration geschieht ausschließlich über `nginx.conf`; Steuerung läuft über HTTP-Hooks und die Statusseite. Geschrieben in C, BSD-lizenziert, seit Jahren ohne wesentliche Weiterentwicklung — WebRTC und SRT fehlen.

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
