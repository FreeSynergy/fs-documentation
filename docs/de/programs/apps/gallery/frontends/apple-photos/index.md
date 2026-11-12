# Apple Fotos

> Kategorie: [gallery](../../index.md) · Typ: Fotobibliothek (Apple-Plattformen) · Anbieter: Apple · Lizenz: proprietär

## Was es ist
Fotos ist die Foto- und Videobibliothek-App von macOS, iOS und iPadOS, synchronisiert über iCloud-Fotos.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, in eigenen Worten.

- Live-Text: Text in einem Foto lässt sich auswählen und bearbeiten; dadurch sind Bilder auch über ihren Text auffindbar. Details über die einzeilige Zusammenfassung des Leitfadens hinaus: offen.
- Album „Duplikate“: wird automatisch erkannt (macOS Ventura oder neuer); der Nutzer führt Gruppen zusammen, ein Original bleibt erhalten, die übrigen gehen in „Zuletzt gelöscht“.
- Erinnerungen, Personen und Haustiere, geteilte Alben.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ teilweise verifiziert, Lücken als „Offen“ markiert |

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
| https://support.apple.com/guide/photos/welcome/mac | offizieller Benutzerleitfaden, Willkommensseite | ✅ 2026-11-10 |
| https://support.apple.com/en-la/guide/photos/pht5a3157c1d/8.0/mac/13.0 | offizieller Leitfaden, Duplikate | ✅ 2026-11-10 |
| https://support.apple.com/guide/photos/live-text-pht5ffdb2a7d/mac | offizielles Leitfaden-Verzeichnis (Live-Text verlinkt, selbst nicht gelesen) | ⚠️ 2026-11-10 |
