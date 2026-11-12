# F-Droid

> Kategorie: [store](../../index.md)

## Was es ist

F-Droid ist ein von einer Community betriebener Katalog und Installationsclient für freie Android-Apps. Das Projekt baut Apps aus dem Quellcode und veröffentlicht sie in einem Repository; die Client-App durchsucht Repositories und installiert und aktualisiert Apps.

## Bemerkenswerte Ideen

- **Anti-Features**: Eine App, die freie Software ist, aber fragwürdiges Verhalten zeigt, trägt sichtbare Kennzeichen (Werbung, Tracking, nicht freie Abhängigkeiten, nicht freie Netzwerkdienste, bekannte Schwachstelle und andere), damit der Nutzer mit den Fakten vor Augen entscheidet.
- **Reproduzierbare Builds**: Das Projekt strebt an, jede App aus dem Quellcode neu zu bauen und zu prüfen, ob das Ergebnis mit dem signierten Release des Entwicklers übereinstimmt; die App-Seite zeigt den Stand der Reproduzierbarkeit.
- **Mehrere Repositories**: Der Client kann neben dem Hauptrepository weitere Repositories von Dritten hinzufügen.
- Hier als Referenz für ehrliche, kennzeichenbasierte App-Informationen aufgeführt (ADR 0013).

## Quellen

- ✅ F-Droid, Anti-Features: https://f-droid.org/docs/Anti-Features/ (abgerufen 2026-11-10)
- ✅ F-Droid, Reproducible Builds: https://f-droid.org/docs/Reproducible_Builds/ (abgerufen 2026-11-10)
- ⚠️ Spezifikation des Repository-Index: Seite unter der geratenen URL nicht erreichbar; Details in api.md sind offen

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
