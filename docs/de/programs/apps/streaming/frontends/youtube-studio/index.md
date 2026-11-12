# YouTube Studio

> Kategorie: [streaming](../../index.md) · Typ: Verwaltungsbereich für Urheber mit Live-Kontrollraum (SaaS) · Anbieter: Google (YouTube) · Lizenz: proprietär

## Was es ist
YouTube Studio ist der Verwaltungsbereich für Kanalinhaber auf YouTube. Für Live-Übertragungen enthält er den Live-Kontrollraum, ein Dashboard, das während der laufenden Übertragung den Zustand des Streams und Echtzeit-Zahlen zeigt, und einen Analysebereich für die Zahlen danach.

## Bemerkenswerte Ideen
- **Live-Kontrollraum** — Stream-Zustand und Zuschauerzahlen auf einem Bildschirm während der Übertragung; ein Vorbild für die Betreiberansicht unseres Streaming-Programms (ADR 0013).
- **Echtzeit- gegenüber verarbeiteten Auswertungen** — Live-Zahlen (gleichzeitige und höchste Zuschauerzahl) werden sofort angezeigt; die endgültigen Zahlen kommen später und können abweichen, weil sie verarbeitet werden. Relevant dafür, wie wir Zahlen als vorläufig kennzeichnen.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Verwendete Protokolle und Standards
Einspeisung per RTMP(S) oder andere Encoder-Protokolle: offen (hier nicht geprüft). Siehe [Anforderungen Streaming](../../requirements.md).

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
| https://support.google.com/youtube/answer/2853833 | offizielle Hilfeseite ✅ (über Suchzusammenfassung) | 2026-11-10 |
| https://studio.youtube.com | Anmeldung erforderlich, nicht lesbar ⚠️ | 2026-11-10 |
