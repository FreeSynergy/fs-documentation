# LibrePhotos Dokumentation

> Kategorie: [gallery](../../index.md)

## Übersicht

LibrePhotos ist die quelloffene Alternative zu Google Photos: Auto-Backup per App, Gesichts- und Objekterkennung, Zeitleiste, Alben und geteilte Galerien. Stack: Django/Python-Backend, React-Frontend, PostgreSQL, Machine-Learning-Pipeline (CLIP, Face-Recognition).

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
| [description.md](latest/description.md) | Abgrenzung zu Immich und PhotoPrism |
| [features.md](latest/features.md) | Scan-Pipeline, Suche, Teilfunktionen, Was LibrePhotos NICHT kann |
| [layout.md](latest/layout.md) | Zeitleiste, Suche-Overlay, Albumseiten |
| [menus.md](latest/menus.md) | Navigation, Alben-/Personen-Menüs, Administration |
| [shortcuts.md](latest/shortcuts.md) | Shortcuts von Suche und Viewer |
| [api.md](latest/api.md) | REST `/api/...`, Token-Auth, Verwaltungsaufgaben |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
