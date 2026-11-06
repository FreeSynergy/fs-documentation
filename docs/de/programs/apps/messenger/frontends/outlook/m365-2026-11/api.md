# Outlook m365-2026-11 — API

In den Screenshots wurde hier nichts gesehen; alles ist ⚠️ (aus Microsofts öffentlicher Dokumentation bekannt, noch zu prüfen und mit Quelle und Datum zu speichern, ADR 0013).

## Protokolle
- **Microsoft Graph** (REST/JSON) — Mail, Kalender, Kontakte, Aufgaben in einer API ⚠️
- Exchange Web Services (EWS) — älter, wird abgelöst ⚠️
- IMAP/POP3/SMTP für Microsoft-365-Postfächer ⚠️; IMAP nutzt Outlook auch für fremde Konten ✅ (der Dialog „Konto hinzufügen“ nennt IMAP)
- Exchange ActiveSync für Telefone ⚠️ (Einstellungsseite „Mobile Geräte“ gesehen ✅)

## Zentrale Endpunkte / Methoden
- Graph `/me/messages`, `/me/mailFolders`, `/me/sendMail`, `/me/events` ⚠️
- Markierungen, Kategorien, angeheftete Mails sowie die Einstufung Fokussiert/Andere sind Nachrichteneigenschaften in Graph ⚠️
- Ob Graph das Terminieren des Versands und das Zurückrufen anbietet, ist offen ⚠️

## Authentifizierung
- OAuth 2.0 über Microsoft Entra ID ⚠️; für Gmail/Yahoo/iCloud nutzt der Dialog „Konto hinzufügen“ die Anmeldung des Anbieters ✅ (Dialog gesehen, Ablauf nicht gesehen)

## Ratenbegrenzungen
- Graph-Drosselung pro App und Postfach ⚠️ — Werte noch abzurufen.

## SDKs und Client-Bibliotheken
- Microsoft-Graph-SDKs ⚠️. Für uns nicht relevant: Wir verbinden uns über JMAP-/IMAP-Konnektoren (siehe [messages-Standards](../../../../../../data/messages/standards.md)).
