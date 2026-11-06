# Apple Mail iOS 26 — Beschreibung

Dokumentiert am 2026-11-05 anhand von Screenshots (intern, nicht veröffentlicht, ADR 0038): iOS 26 auf einem
iPhone 17 Pro, dazu das aktuelle macOS Mail (gleiche Generation 2026) zum Vergleich, ein Bild mit der Bezeichnung
iOS 27, einige ältere iOS-Screenshots und macOS-10.12-Bilder von 2016 (veraltet, nur kurz erwähnt).

✅ = in einem Screenshot gesehen · ⚠️ = erschlossen oder anderweitig bekannt

## Überblick
Apple Mail unter iOS 26 nutzt Apples durchscheinenden „Glas“-Look: schwebende runde Schaltflächen, eine schwebende Suchkapsel unten, große Titel und kartenförmige Sheets ✅. Der Posteingang wird mit Chips oben in Kategorien sortiert ✅. Aktionen liegen in Wisch-Gesten, Langdruck-Menüs und unteren Sheets statt in Werkzeugleisten ✅.

## Was es macht
- Liest und schreibt Mails für mehrere Konten (iCloud und andere) ✅.
- Sortiert den Posteingang automatisch in Primär, Transaktionen, Updates, Werbung ✅.
- Bietet intelligente Mailboxen (VIP, Markiert, Ungelesen, An/Cc, Anhänge, Erinnere mich, Nachverfolgen, Später senden, Stummgeschaltet, Thread-Benachrichtigungen) neben echten Ordnern ✅.
- Schützt vor Tracking (Mailaktivität schützen) und vor falscher Adressierung (Adressen markieren) ✅.
- Fasst eine Mail auf Anfrage zusammen (Schaltfläche „Zusammenfassen“, Apple Intelligence) ✅.

## Für wen es passt
Menschen, die das Telefon vor allem zum Lesen und Sichten nutzen; Menschen, die möchten, dass die Standardeinstellungen privat sind.

## Abgrenzung

### Apple Mail vs. Outlook
Weniger sichtbare Befehle, mehr Gesten; automatische Kategorien statt Fokussiert/Andere; Datenschutz-Schutz standardmäßig; kein Menüband, keine rechte Lesespalte auf dem Telefon ✅. Outlook bietet reichere Organisation (farbige Kategorien, Regeln, Zurückholen, Offline-Steuerung) ✅ (siehe [Outlook](../../outlook/m365-2026-11/description.md)).

### iOS vs. macOS (aktuell) ✅
Die Mac-Version zeigt dieselben Ideen in drei Spalten: Seitenleiste (Favoriten mit Alle Posteingänge, VIPs, Markiert, Erinnere mich, Alle Entwürfe, Alle gesendet; Intelligente Mailboxen; Konto-Ordner), Liste mit Kategorie-Reitern, Lesebereich mit Zusammenfassen; eine Werkzeugleiste mit Antworten, Archivieren, Löschen, Junk, Verschieben, Markieren, Suche; ein Verfasser mit schwebender Werkzeugleiste ✅. Sie bekommt später vielleicht einen eigenen Versionsordner (`macos-26`).

### Frühere Stände
- Ältere iOS-Version (Look vor 2020): dieselbe bearbeitbare Liste intelligenter Mailboxen existierte (Posteingang, VIP, Markiert, Ungelesen, An/Cc, Anhänge, Benachrichtigungen, Heute) ✅ — die Idee ist langlebig.
- macOS 10.12 (2016): Einstellungen mit Registerkarten (Konten, Junk, Schriften und Farben, Anzeige, Verfassen, Signaturen, Regeln), Aliasse pro Konto und eine Absender-Auswahl ✅ — veraltet.
- Das Bild mit der Bezeichnung **iOS 27** zeigt fünf Telefonbildschirme mit einer unteren Tab-Leiste (Posteingang, Heute, Anhänge, Markiert, Suche), eine Karte „Priorität“ und eine Heute-Ansicht, die Termine und Aufgaben mischt ✅ gesehen, wirkt aber wie ein **Konzept**, nicht wie eine bestätigte Apple-Veröffentlichung ⚠️.

## Technische Details
- Plattformen: iOS, iPadOS, macOS, visionOS ⚠️; keine Web- oder Windows-Version ⚠️.
- Speicherung/Synchronisation: lokale Kopie der IMAP-Mailboxen; Einstellungen werden über iCloud synchronisiert ⚠️.
- Verschlüsselung: S/MIME unterstützt ⚠️; kein eingebautes OpenPGP ⚠️.
- Selbst hosten: Der Client arbeitet mit jedem IMAP-Server ✅ (Kontodialog akzeptiert jede Adresse; ältere Screenshots zeigen einen Nicht-Apple-Anbieter) ✅.
