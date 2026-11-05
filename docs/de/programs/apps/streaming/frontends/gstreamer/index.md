# GStreamer Dokumentation

> Kategorie: [streaming](../../index.md)

## Übersicht

GStreamer ist ein Multimedia-Framework in C: Aufnahme, Dekodierung, Filterung, Kodierung und Ausgabe werden als **Pipeline aus Elementen** (Source → Filter/Codec → Sink) aufgebaut. Werkzeuge wie `gst-launch-1.0` und `gst-inspect-1.0` erschließen das System über die Shell, eigene Programme nutzen die C-API (oder Python/Rust-Bindungen). Stack: C + GObject, LGPL 2.1, Pakete base/good/bad/ugly, WebRTC über `webrtcbin`.

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
