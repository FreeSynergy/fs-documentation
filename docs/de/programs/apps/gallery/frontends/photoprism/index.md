# PhotoPrism Dokumentation

> Kategorie: [gallery](../../index.md)

## Übersicht

PhotoPrism indexiert eine vorhandene Fotosammlung, erkennt Inhalte und Gesichter und präsentiert sie als durchsuchbare Web-Galerie mit Alben und Freigaben. Stack: Go-Backend (Plus-Variante mit erweiterter KI), Vue-Frontend, MariaDB/SQLite, Index auf eigenem Ordner.

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
| [description.md](latest/description.md) | Abgrenzung zu Immich, LibrePhotos und Piwigo |
| [features.md](latest/features.md) | Indexierung, Labels, Gesichter, Alben, Was PhotoPrism NICHT kann |
| [layout.md](latest/layout.md) | Suchleiste, Mosaik, Detail-Panel, Ordneransicht |
| [menus.md](latest/menus.md) | Hauptnavigation, Ordner-/Alben-Menüs, Einstellungen, Admin |
| [shortcuts.md](latest/shortcuts.md) | Shortcuts von Suche und Viewer |
| [api.md](latest/api.md) | REST `/api/v1`, Basic/Bearer, Batch-Index, Webhooks |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
