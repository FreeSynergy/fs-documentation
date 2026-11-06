# Apple Mail iOS 26 — API

**Keine öffentliche API** ⚠️ — Apple Mail ist ein geschlossener Client. Es ist ein *Konsument* von Standardprotokollen, und genau deshalb kann es auf jedem Mailserver aufsetzen.

## Protokolle
- IMAP zum Lesen, SMTP zum Senden ⚠️ (Kontodialog akzeptiert jede Adresse ✅; IMAP-Konten in macOS 10.12 gesehen ✅)
- Exchange ActiveSync für Microsoft-Konten ⚠️
- iCloud Mail basiert auf IMAP ⚠️

## Zentrale Endpunkte / Methoden
- Keine öffentlichen ⚠️. Automatisierung auf dem Mac über AppleScript/Kurzbefehle ⚠️; Mail-Erweiterungen (MailKit) auf macOS ⚠️.

## Authentifizierung
- Passwort oder Anmeldung beim Anbieter (OAuth für Google/Microsoft) ⚠️; der Link „aus einer Liste wählen“ im Dialog zum Hinzufügen eines Kontos führt zur Anbieterliste ✅.

## Ratenbegrenzungen
- Nicht anwendbar (Client) ⚠️.

## SDKs und Client-Bibliotheken
- Keine ⚠️. Für uns nur über die Standards relevant: siehe [messages-Standards](../../../../../../data/messages/standards.md).
