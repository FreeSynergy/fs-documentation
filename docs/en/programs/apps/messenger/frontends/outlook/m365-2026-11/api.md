# Outlook m365-2026-11 — API

Nothing here was seen in the screenshots; everything is ⚠️ (known from Microsoft's public
documentation, to be verified and stored with source and date, ADR 0013).

## Protocols
- **Microsoft Graph** (REST/JSON) — mail, calendar, contacts, to-do in one API ⚠️
- Exchange Web Services (EWS) — older, being retired ⚠️
- IMAP/POP3/SMTP for Microsoft 365 mailboxes ⚠️; IMAP is also what Outlook uses for foreign accounts ✅
  (the add-account dialog names IMAP)
- Exchange ActiveSync for phones ⚠️ ("mobile devices" settings page seen ✅)

## Core endpoints / methods
- Graph `/me/messages`, `/me/mailFolders`, `/me/sendMail`, `/me/events` ⚠️
- Flags, categories, pinned and focused/other classification are message properties in Graph ⚠️
- Schedule send and recall: whether Graph exposes them is open ⚠️

## Authentication
- OAuth 2.0 via Microsoft Entra ID ⚠️; for Gmail/Yahoo/iCloud the add-account dialog uses the
  provider's sign-in ✅ (dialog seen, flow not seen)

## Rate limits
- Graph throttling per app and mailbox ⚠️ — values to be fetched.

## SDKs and client libraries
- Microsoft Graph SDKs ⚠️. For us irrelevant: we connect through JMAP/IMAP connectors
  (see [messages standards](../../../../../../data/messages/standards.md)).
