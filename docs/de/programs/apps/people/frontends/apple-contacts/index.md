# Apple Contacts

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

> Kategorie: [people](../../index.md) · Typ: Kontaktverwaltung (iPhone, iPad, Mac, Apple Watch) · Anbieter: Apple · Lizenz: proprietär

## Was es ist

Apple Contacts ist das Adressbuch, das in Apples Betriebssysteme eingebaut ist. Es synchronisiert Kontakte zwischen Geräten und mit hinzugefügten Konten, bietet eine Karte „Ich“ für die eigenen Angaben und tauscht Kontaktdaten zwischen nahen Geräten aus.

## Bemerkenswerte Ideen

Warum dieses Programm hier dokumentiert ist (ADR 0013):

- **NameDrop**: Zwei Geräte, die dicht aneinandergehalten werden, tauschen Kontaktdaten aus. Die Person wählt, welche Angaben gesendet werden; nach Apples Beschreibung werden nur Name, eine gewählte Telefonnummer oder E-Mail-Adresse und das Kontakt-Poster gesendet, nicht Wohnadresse oder Geburtstag. Es sendet neue Kontaktdaten und aktualisiert keinen vorhandenen Kontakt. Für uns relevant als Beispiel für den persönlichen Austausch von Kontakten ohne Tippen und mit bewusster Auswahl der Felder.
- **Eigene Karte („Ich“)**: das Teilen basiert auf einer Karte, die die Person steuert und bearbeitet.
- **Duplikate zusammenführen oder ausblenden** gehört zur selben App.

## Dokumentierte Versionen

| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ aus Hilfeseiten und einem Sicherheitsleitfaden von Apple; kein Gerät geprüft. iOS 17 führte NameDrop ein; Leitfäden in den Versionen 17, 18, 26, 27 existieren |

## Verwendete Protokolle und Standards

Standards für Kontaktdaten: [data/people](../../../../../data/people/index.md). NameDrop ist Teil von AirDrop (apple-intern, kein offener Standard bekannt; offen).

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
| https://support.apple.com/guide/personal-safety/ips97e16d3b1/web ✅ | Apple-Leitfaden (was NameDrop teilt, wie man abbricht) | 2026-11-10 |
| https://support.apple.com/guide/iphone/add-and-use-contact-information-iph3d3da1b3c/ios ✅ | Apple-iPhone-Benutzerhandbuch, Abschnitt Kontakte (nur Themenliste) | 2026-11-10 |
| https://support.apple.com/guide/iphone/namedrop-iphone-share-contact-info-iph1b6c664b7/ios ⚠️ | NameDrop-Artikel; Text nicht lesbar, nur der Titel | 2026-11-10 |
| https://support.apple.com/en-ca/guide/watch/apd46c6e11cf ⚠️ | Apple-Watch-Leitfaden, nur über ein Suchergebnis gesehen | 2026-11-10 |
