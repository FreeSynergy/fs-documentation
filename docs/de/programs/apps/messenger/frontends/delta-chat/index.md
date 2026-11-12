# Delta Chat

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [messenger](../../index.md) · Typ: Chat über E-Mail · Anbieter: Delta-Chat-Gemeinschaft · Lizenz: Open Source (Lizenzname offen)

## Was es ist

Delta Chat ist ein Chat-Messenger, dessen Nachrichten als verschlüsselte, E-Mail-artige Nachrichten über Relais („Chatmail“) reisen, oder über ein gewöhnliches E-Mail-Konto, das nur dafür genutzt wird. Kontakte werden per QR-Code oder Einladungslink hinzugefügt; es gibt kein öffentliches Verzeichnis.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **Chat über vorhandene Mail-Infrastruktur**: der Transport ist E-Mail-artig, daher wird kein neues Netz benötigt. Für uns relevant: auch unser Messenger verbindet Mail und Chat in einem Programm (ADR 0018).
- **Verschlüsselung standardmäßig** mit OpenPGP, Schlüsselaustausch über Autocrypt und Secure-Join; die Standardrelais lehnen unverschlüsselte Nachrichten ab. Unverschlüsselte Mail von einem klassischen Konto wird mit einem E-Mail-Symbol markiert.
- **Relais speichern keine Profildaten**: Namen, Bilder und Gruppendaten bleiben auf den Geräten.
- **Kanäle** (einer an viele; Abonnenten können nicht antworten), **webxdc**-Apps im Chat (in einer Sandbox, ohne Internetzugang), mehrere Profile pro Gerät, zweites Gerät per QR-Code, Einzelgespräche per Anruf.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ eine Hilfeseite; keine App geprüft |

## Verwendete Protokolle und Standards

OpenPGP, Autocrypt, E-Mail-Transport. Siehe [Nachrichtenstandards](../../../../../data/messages/standards.md).

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
| https://delta.chat/en/help ✅ | offizielle Hilfe | 2026-11-10 |
