# gethomepage (Bibliothek)

> Kategorie: [desktop](../../index.md)

## Was es ist

`gethomepage` bezeichnet die **API-Bibliotheksschicht** des Projekts `gethomepage/homepage`: die Service-Clients, Proxy-Handler, Konfigurationsleser und Hilfsfunktionen, die die YAML-Einträge in `services.yaml` in echte HTTP-Aufrufe an Sonarr, Pi-hole, Proxmox, Docker oder Kubernetes umsetzen. Die Bibliothek hat **keine eigene Benutzeroberfläche** – Bedienung und Konfiguration laufen über das Dashboard.

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastenkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
