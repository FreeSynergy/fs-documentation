# Syncthing

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [files](../../index.md) · [frontends](../index.md)

## Was es ist

Syncthing ist ein kostenloses Programm, das ausgewählte Ordner direkt zwischen Geräten identisch hält, ohne zentralen Server ✅ (Konzept; die Einstiegsseite sagt es nicht ausdrücklich, siehe Offen). Die Steuerung erfolgt über eine Web-Oberfläche unter `localhost:8384` ✅. Lizenz: offen (nicht gelesen).

## Bemerkenswerte Ideen

- **Gerät zu Gerät:** jedes Gerät hat eine ID, die aus seinem Zertifikat gebildet wird; zwei Geräte verbinden sich nur, wenn jedes die ID des anderen hinzugefügt hat ✅.
- **Ordner werden pro Gerät freigegeben,** bei der Gerätehinzufügung gewählt ✅.
- **Erkennung und Relays:** globale und lokale Erkennung sowie öffentliche Relays, wenn kein direkter Weg besteht; alles standardmäßig aktiv und abschaltbar ✅. Über Relays übertragene Daten bleiben Ende-zu-Ende verschlüsselt ✅.
- **TLS 1.2/1.3** zwischen Geräten; der Fingerabdruck wird gegen die Liste akzeptierter Geräte geprüft ✅.
- **Nicht vertrauenswürdige (verschlüsselte) Geräte** existieren als Dokumentationsthema ✅; Details offen.
- Warum hier: die Referenz für Synchronisation ohne Server (ADR 0013, ADR 0019).

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

- https://docs.syncthing.net/intro/getting-started.html ✅ 2026-11-10
- https://docs.syncthing.net/users/security.html ✅ 2026-11-10
- https://docs.syncthing.net/dev/rest.html ✅ 2026-11-10
