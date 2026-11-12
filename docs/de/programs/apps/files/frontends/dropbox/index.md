# Dropbox

> Kategorie: [files](../../index.md) · [frontends](../index.md)

## Was es ist

Dropbox ist ein kommerzieller Cloud-Speicherdienst mit Web-, Desktop- und Mobil-Clients sowie einer Entwickler-API. ✅ (Hilfecenter; Liste der Clients: offen.)

## Bemerkenswerte Ideen

- **Dateianfragen:** der Eigentümer bittet andere, Dateien zu senden. Der Absender braucht kein Konto; die Dateien landen in einem gewählten Ordner, standardmäßig privat ✅. Optionen: Titel, Beschreibung, Benennungskonvention, Passwort, Frist mit oder ohne verspätete Uploads (kostenpflichtige Tarife) ✅. Limit pro Datei: 2 GB in den Basistarifen, 250 GB in den kostenpflichtigen ✅. Uploads zählen auf den Speicher des Eigentümers ✅.
- Warum hier: ein Weg, Dateien nur zu empfangen, ist der Fall hinter „Nur-Ablage-Ordner“ in unseren Freigaberollen (ADR 0013).

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

- https://help.dropbox.com/share/create-file-request ✅ 2026-11-10
- https://help.dropbox.com/share/received-file-request ⚠️ 2026-11-10 (nur Suchergebnis)
- https://dropbox.tech/developers/streamline-file-collection-with-the-file-request-api ⚠️ 2026-11-10 (nur Suchergebnis; eine API für Dateianfragen existiert)
