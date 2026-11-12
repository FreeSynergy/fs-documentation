# PeerTube

> Kategorie: [streaming](../../index.md) · Typ: föderierte Videoplattform mit Live-Streaming · Anbieter: Framasoft und Mitwirkende · Lizenz: AGPL-3.0

## Was es ist
PeerTube ist freie Software zum Hosten von Videos und Live-Streams. Jede Installation (eine Instanz) ist unabhängig; Instanzen können einander über ActivityPub folgen, sodass Videos über sie hinweg auffindbar sind. Zuschauende können sich über WebRTC gegenseitig die Last abnehmen.

## Bemerkenswerte Ideen
- **Föderation von Videos über ActivityPub** — Kanäle können von Mastodon und anderer Fediverse-Software oder per RSS abonniert werden (ADR 0013).
- **Peer-to-peer-Auslieferung** — Zuschauende entlasten den Server, indem sie den Stream untereinander teilen.
- **Redundanz zwischen Instanzen** — Instanzen können die Videos anderer zwischenspeichern.
- **Plugins und Themes**; der Web-Client kann ersetzt werden.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Verwendete Protokolle und Standards
ActivityPub, WebRTC, HLS ⚠️ (auf den gelesenen Seiten nicht genannt), REST mit OpenAPI 3. Siehe [Datenstandards](../../../../../data/standards.md).

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
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Ratenlimits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://github.com/Chocobozzz/PeerTube | Quell-README ✅ | 2026-11-10 |
| https://docs.joinpeertube.org/ | offizielle Dokumentation ✅ | 2026-11-10 |
