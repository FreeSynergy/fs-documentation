# StreamYard

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [streaming](../../index.md) · Typ: browserbasiertes Live-Studio (SaaS) · Anbieter: StreamYard · Lizenz: proprietär

## Was es ist
StreamYard ist ein Studio für Live-Streaming und Aufnahmen, das im Browser läuft. Die Gastgeberin oder der Gastgeber schickt einen Link, Gäste treten mit Kamera und Mikrofon aus ihrem eigenen Browser bei, und die Gastgeberin oder der Gastgeber stellt alle auf den Bildschirm und sendet an die verbundenen Plattformen.

## Bemerkenswerte Ideen
- **Gäste treten über einen Link bei, ohne Software und standardmäßig ohne Konto** — die Gastgeberin oder der Gastgeber kann optional eine Anmeldung verlangen. Das senkt die Hürde für Interviews; relevant dafür, wie unser Programm Gäste zulässt (ADR 0013).
- **Vom Gastgeber geführtes Studio** — die Gastgeberin oder der Gastgeber bestimmt, wer auf dem Bildschirm ist; Gäste sind keine Bedienenden.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Verwendete Protokolle und Standards
Browser-Aufnahme (WebRTC ist durch Testberichte Dritter nahegelegt ⚠️). Siehe [Anforderungen Streaming](../../requirements.md).

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
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://support.streamyard.com/hc/en-us/articles/4405100913428 | offizielle Hilfe ✅ (über Suchzusammenfassung) | 2026-11-10 |
| https://support.streamyard.com/hc/en-us/articles/360043733751 | offizielle Hilfe, Gäste brauchen keine Anmeldung ✅ (über Suchzusammenfassung) | 2026-11-10 |
| https://support.streamyard.com/hc/en-us/articles/360051855952 | offizielle Hilfe, Telefon-Gäste ✅ (über Suchzusammenfassung) | 2026-11-10 |
| https://streamyard.com/blog/invite-guests-to-stream-for-free | Anbieter-Blog ⚠️ | 2026-11-10 |
