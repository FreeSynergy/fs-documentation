# Signal

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: Chat · Anbieter: Signal (unabhängige gemeinnützige Organisation, 501(c)(3)) · Lizenz: Open-Source-Protokoll; Client-Lizenzen offen

## Was es ist

Signal ist ein privater Messenger für Text, Sprachnachrichten, Fotos, Videos, Dateien, Sprach- und Videoanrufe sowie Gruppenchats. Er wird laut Anbieter durch Zuschüsse und Spenden finanziert und enthält keine Werbung und keine Tracker.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Referenz für das Protokoll**: Ende-zu-Ende-Verschlüsselung auf dem offenen Signal-Protokoll. Die Dokumentation nennt X3DH, PQXDH (Schlüsselvereinbarung, die gegen Quantencomputer schützt), Double Ratchet, Sesame (Sitzungen über mehrere Geräte), ML-KEM Braid, XEdDSA/VXEdDSA. Für uns relevant: der Maßstab dafür, was „standardmäßig verschlüsselt“ bedeutet (ADR 0018); unsere Wahl von MLS (RFC 9420) unterscheidet sich davon.
- **Sticker-Pakete**, die jede Person erstellen und teilen kann, verschlüsselt.
- Finanzierung ohne Werbung und Tracking, passend zu ADR 0016.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ Startseite und Protokollseite des Anbieters; die Funktionsseite lieferte 404 |

## Verwendete Protokolle und Standards

Signal-Protokoll (eigenes). Brücken von Matrix existieren (Brückenliste). Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| https://signal.org/ ✅ | Startseite des Anbieters | 2026-11-10 |
| https://signal.org/docs/ ✅ | Index der Protokolldokumentation | 2026-11-10 |
| https://matrix.org/ecosystem/bridges/ ✅ | Liste der Matrix-Brücken (Signal erscheint) | 2026-11-10 |
