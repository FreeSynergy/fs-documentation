# Owncast

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [streaming](../../index.md) · Typ: selbst gehosteter Server für Live-Video und Chat · Anbieter: Owncast-Projekt · Lizenz: MIT

## Was es ist
Owncast ist ein Server für eine einzelne Streamerin oder einen einzelnen Streamer: Er nimmt einen Stream aus einer Sendesoftware über RTMP an, liefert ihn im Browser an Zuschauende aus und bietet einen eingebauten Webchat. Er ist in Go geschrieben, hat einen React-Webclient und nutzt ffmpeg.

## Bemerkenswerte Ideen
- **Modell einer Person, ein Server** — ein kleiner, vollständiger Stack (Video, Chat, Administration, Verzeichniseintrag) statt einer Plattform; passt zu unserem Ziel des Selbsthostings (ADR 0013).
- **Der Server ist ein Akteur im Fediverse** — er ist ein einzelnes Konto vom Typ Service; Konten kompatibler Dienste können ihm folgen. Föderation ist eine optionale soziale Schicht, nicht der Kern.
- **Plugins in JavaScript oder Python und Web-APIs** für Bots, Einblendungen und Integrationen.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
RTMP-Eingang; ActivityPub, WebFinger, HTTP-Signaturen, NodeInfo für die Föderation. Siehe [Datenstandards](../../../../../data/standards.md).

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen geeignet |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastaturkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://owncast.online/docs/ | offizielle Dokumentation ✅ | 2026-11-10 |
| https://github.com/owncast/owncast | Quell-README ✅ | 2026-11-10 |
| https://owncast.online/docs/api/activitypub | offizielle Dokumentation ✅ (über Suchzusammenfassung) | 2026-11-10 |
| https://owncast.online/dev-docs/activitypub-and-federation-engineering-reference | offizielle Entwicklerdokumentation ✅ (über Suchzusammenfassung) | 2026-11-10 |
