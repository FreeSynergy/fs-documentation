# Apple Mail

> Kategorie: [messenger](../../index.md) · Typ: E-Mail · Anbieter: Apple · Lizenz: proprietär (mit iOS, iPadOS, macOS ausgeliefert)

## Was es ist
Apple Mail ist das Mailprogramm, das auf jedem iPhone, iPad und Mac mitgeliefert wird. Es spricht IMAP und die üblichen Mail-Standards, führt eigene Ordner („Mailboxen“) pro Konto und ergänzt automatische Mailboxen, die Mails über alle Konten hinweg sammeln. Auf dem Telefon ist es um große Titel, Sheets und Wisch-Gesten herum aufgebaut. Es ist unsere Referenz für den Frontend-Typ „größter Gegenspieler / Apple“ (ADR 0038).

## Bemerkenswerte Ideen
Gesehen in Screenshots (✅), sofern nicht mit ⚠️ markiert.

- **Intelligente Mailboxen als konfigurierbare Liste** — Posteingang, VIP, Markiert, Ungelesen, An/Cc, Anhänge, Thread-Benachrichtigungen, Erinnere mich, Nachverfolgen, Später senden, Stummgeschaltete Threads sind keine Ordner, sondern gespeicherte Ansichten; die Person wählt aus, welche erscheinen, und ordnet sie per Ziehen ✅. Für uns: gespeicherte Abfragen über alle Konten, dargestellt wie Ordner.
- **Automatische Kategorien** — der Posteingang ist in Primär, Transaktionen, Updates, Werbung aufgeteilt, mit Chips oben, und ein Erklärungs-Sheet zeigt, wie viele Mails letzte Woche wohin gelandet sind ✅. Zeigt, dass Sortierung erklärt, nicht versteckt werden kann.
- **Mailaktivität schützen** — ein Schalter, der die IP-Adresse verbirgt und entfernte Inhalte privat lädt, damit Absender das Öffnen nicht verfolgen können ✅. Passt zu unserer Regel „kein Tracking standardmäßig“.
- **VIP** — eine Person über die Kontaktkarte als wichtig markieren; VIP-Mails bekommen einen Stern und eine eigene Mailbox ✅.
- **Benachrichtigen / Stummschalten pro Unterhaltung** — über das Langdruck-Menü ✅.
- **Adressen markieren** — jede Adresse hervorheben, die nicht auf den angegebenen Domains endet, als Schutz gegen Senden an Außenstehende ✅.
- **Wisch-Aktionen** — eine Zeile nach links wischen für Mehr / Markieren / Löschen (runde, beschriftete Schaltflächen) ✅.
- **Auswählen und Verschieben als Sheet** — ausgewählte Mails erscheinen als gestapeltes Vorschaubild über der Mailbox-Liste ✅.
- **Erinnere mich und Später senden** — zeitgesteuerte Verarbeitung, dargestellt als Mailboxen und Sortierschlüssel ✅.
- **Farbige Markierungen** — sieben Markierungsfarben, im Aktionsmenü auswählbar ✅.
- **Mailinglisten-Banner mit Abmeldung per Tipp** in der Mail ✅.
- **Suchbereich-Umschalter** (alle Mailboxen / aktuelle Mailbox) mit Top-Treffern zuerst ✅.
- **Nachrichtennavigation** — Pfeiltasten nach oben/unten in einer geöffneten Mail, um zur nächsten/vorherigen zu gelangen ✅.

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [ios-26](ios-26/description.md) | 7/7 |

### ios-26

| Datei | Inhalt |
|------|----------|
| [description.md](ios-26/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es passt |
| [features.md](ios-26/features.md) | Was das Programm kann — und was nicht |
| [layout.md](ios-26/layout.md) | Fensteraufbau, Bereiche, Paneele |
| [menus.md](ios-26/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](ios-26/shortcuts.md) | Tastenkürzel |
| [api.md](ios-26/api.md) | APIs und Protokolle, Authentifizierung, Ratenbegrenzungen |
| [themes/index.md](ios-26/themes/index.md) | Themes: Farben, Typografie, Abstände — was nachgebaut werden kann |
| [interaction.md](ios-26/interaction.md) | Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift) |
| [states.md](ios-26/states.md) | UI-Zustände und Übergänge |
| [dependencies.md](ios-26/dependencies.md) | Welche unserer Komponenten ein Frontend in diesem Stil benötigt |
<!-- /gen:versions -->

## Verwendete Protokolle und Standards
Verweise in `data/` (Protokolle sind keine Frontends): IMAP, SMTP, Exchange ActiveSync ⚠️, S/MIME ⚠️ —
siehe [messages-Standards](../../../../../data/messages/standards.md).

## Quellen
| Quelle | Art | Abgerufen |
|--------|------|-----------|
| Screenshots, vom Projektverantwortlichen gesammelt: iOS 26 auf iPhone 17 Pro, ein iOS-27-Bild, aktuelles macOS Mail, einige macOS-10.12-Bilder (2016) | Screenshots — intern, nicht veröffentlicht (ADR 0038) | 2026-11-05 |
| https://www.cubux.net/5-best-email-clients-for-mac/ | Artikel (Weiterleitungsziel, zusammen mit den Screenshots vermerkt; nicht gelesen) | 2026-11-05 |
