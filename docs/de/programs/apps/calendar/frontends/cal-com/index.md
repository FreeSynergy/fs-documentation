# Cal.com

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [calendar](../../index.md) · [frontends](../index.md)

## Was es ist

Cal.com ist ein Terminplanungsprodukt: Der Eigentümer legt Termintypen und Verfügbarkeit fest, andere buchen einen Slot über eine öffentliche Seite. Es gibt einen gehosteten Dienst und eine REST-API (v2). ✅ Lizenz der aktuellen Codebasis: Open (siehe unten).

## Bemerkenswerte Ideen

- **Buchungsseiten:** eine öffentliche Seite pro Termintyp; Verfügbarkeit, Puffer, Mindestvorlauf und Slot-Intervalle werden pro Termintyp gesetzt ⚠️ (Suchausschnitt des Hilfe-Index).
- **API mit abgestuftem Zugriff:** Zeitpläne, Termintypen und Buchungen sind API-Ressourcen; OAuth und API-Schlüssel ✅. Warum hier: Dies ist die Referenz für unseren Buchungsteil des Kalenders (ADR 0013).

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

- https://cal.com/docs ✅ 2026-11-10 (Einführung in API v2)
- https://github.com/calcom/cal.com ✅ 2026-11-10 (der Abruf lieferte die Seite des Forks Cal.diy: MIT, Enterprise-Code entfernt; dass das Hauptrepository die Lizenz gewechselt hat, ist NICHT bestätigt)
- Drittanbieter-Blogs zu Lizenz und Self-Hosting ⚠️ nicht für Aussagen verwendet
