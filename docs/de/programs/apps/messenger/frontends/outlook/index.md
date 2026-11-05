# Outlook - Dokumentation

> Kategorie: [messenger](../../index.md)

## Übersicht

Outlook ist der beliebteste E-Mail-Client von Microsoft, Teil von Microsoft 365.

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Review 2026-11-05

- **Gesehene Version:** keine — keine Datei unter `latest/` nennt eine Produktversion; der Text
  beschreibt einen ungenannten neueren Stand. Geprüft am 2026-11-05 (Doku-Stand von Commit
  `3fe3d7d1`) beim Erarbeiten der [Anforderungen](../../requirements.md). Der Ordner `latest/` wird
  nach der Nachrecherche auf die echte Version umbenannt (`temp/frontend-versions-missing.txt`).
- **Qualität:** dünn; teils allgemein. Aus dem Produkt bekannte Funktionen, die hier **fehlen**:
  Reaktionen, Threads, später senden, Snooze, Senden rückgängig machen, Wischaktionen (wo das
- Als **Referenz-Frontend** im Suite-Kontext (Microsoft 365) geplant, siehe ADR 0038; braucht Nachrecherche mit Screenshots.
- **Fähigkeiten, die dieses Frontend zeigt** (aus der Spalte *Gesehen in* der Anforderungen,
  ⚠️ = nur aus dem Produkt bekannt):
  - Pflicht:
  - `account.add`, `account.remove`, `account.edit`
  - `conversation.list`
  - `conversation.move`, `mailbox.create`
  - `conversation.open`, `message.open`
  - `message.send`
  - `message.send`, `key.discover`
  - `message.reply` ⚠️
  - `message.forward`
  - `message.delete`
  - `message.flag` ⚠️
  - `message.read`
  - `message.search`
  - `attachment.add`, `attachment.save`
  - `message.compose`
  - `draft.save`, `draft.list`
  - `group.create`, `group.invite`, `group.leave`
  - `contact.lookup`
  - `rule.create`, `rule.run`
  - Kür:
  - `Emoji in Text einfügen`
  - `message.label`
  - `message.junk`
  - `message.schedule` ⚠️
  - `conversation.snooze` ⚠️
  - `Signaturen an Mails`
  - `Nachricht drucken`
  - `Kalendereinladungen vor Ort beantworten (annehmen / a`

## Dokumentierte Versionen

<!-- gen:versions (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Beschreibung und Abgrenzung |
| [features.md](latest/features.md) | Editor-Funktionen und Features |
| [layout.md](latest/layout.md) | UI/UX und Struktur |
| [menus.md](latest/menus.md) | Alle Menüpunkte |
| [shortcuts.md](latest/shortcuts.md) | Alle Tastatur-Shortcuts |
| [api.md](latest/api.md) | API-Dokumentation (REST, GraphQL, etc.) |
| [themes/index.md](latest/themes/index.md) | Themes: Farben, Typografie, Abstände — was sich nachbauen lässt |
<!-- /gen:versions -->
