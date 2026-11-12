# ActivityWatch

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [history](../../index.md) · Typ: automatischer Aktivitätserfasser · Anbieter: ActivityWatch-Projekt · Lizenz: frei und Open Source (Lizenztext: Open)

## Was es ist
ActivityWatch erfasst, was du auf deinem Computer tust: welches Programm und Fenster vorne ist, ob du an der Tastatur sitzt, welcher Browser-Tab offen ist. Alles wird lokal gespeichert und in einer Weboberfläche angezeigt.

## Bemerkenswerte Ideen
- Watcher speisen "Buckets" mit Ereignissen über eine lokale Schnittstelle. Warum: ein sauberer Ort, um Ereignisse aus anderen Quellen zu importieren.
- Rohdaten in hoher Auflösung, Zusammenfassungen werden auf Abruf durch Abfragen erzeugt. Warum: dieselbe Idee wie unser Digest über rohe Aktivität.
- Daten bleiben standardmäßig auf deinem Rechner; keine Funktion ist hinter einer Bezahlschranke. Warum: dieselbe Haltung wie bei History.
- Kategorisierungsregeln (auch mit regulären Ausdrücken). Warum: die Bedeutung wird später ergänzt, nicht bei der Erfassung.

## Dokumentierte Versionen
| Version | Dokumentiert am | Stand |
|---------|-----------------|-------|
| [latest](latest/description.md) | 2026-11-10 (Release v0.14.1, 2026-10-10) | ✅ |

## Verwendete Protokolle und Standards
HTTP/JSON, Zeitstempel nach RFC 3339.

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://docs.activitywatch.net/en/latest/introduction.html ✅ | offizielle Dokumentation | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/api/rest.html ✅ | offizielle Dokumentation | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/watchers.html ✅ | offizielle Dokumentation | 2026-11-10 |
| https://docs.activitywatch.net/en/latest/features.html ✅ | offizielle Dokumentation | 2026-11-10 |
| https://github.com/ActivityWatch/activitywatch/releases ✅ | Release-Liste | 2026-11-10 |
