# Immich Dokumentation

> Kategorie: [gallery](../../index.md)

## Übersicht

Immich ist eine selbst gehostete Foto- und Video-Verwaltung (Server + Mobile-App): Uploads vom Telefon, Gesichts- und Objekterkennung, Zeitleisten, Alben, geteilte Galerien und eine vollständige REST-API. Stack: NestJS-Server + PostgreSQL + Machine-Learning-Jobs, Frontend Svelte/React, Apps für iOS/Android.

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
| [description.md](latest/description.md) | Abgrenzung zu PhotoPrism, LibrePhotos und Nextcloud Photos |
| [features.md](latest/features.md) | Upload, Suchindex, Freigaben, Was Immich NICHT kann |
| [layout.md](latest/layout.md) | Zeitleisten-Raster, Viewer, Album- und Teilseiten |
| [menus.md](latest/menus.md) | Navigation in Web-App und App, Verwaltungs-Menüs |
| [shortcuts.md](latest/shortcuts.md) | Shortcuts der Web-App |
| [api.md](latest/api.md) | REST `/api`, API-Keys/OAuth2, BullMQ-Jobs, SDKs |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
