# Apple Mail iOS 26 — API

**No public API** ⚠️ — Apple Mail is a closed client. It is a *consumer* of standard protocols,
which is exactly why it can sit on top of any mail server.

## Protocols
- IMAP for reading, SMTP for sending ⚠️ (account dialog accepts any address ✅; IMAP accounts seen in
  macOS 10.12 ✅)
- Exchange ActiveSync for Microsoft accounts ⚠️
- iCloud Mail is IMAP-based ⚠️

## Core endpoints / methods
- None public ⚠️. Automation on the Mac via AppleScript/Shortcuts ⚠️; Mail extensions (MailKit) on
  macOS ⚠️.

## Authentication
- Password or provider sign-in (OAuth for Google/Microsoft) ⚠️; the "choose from a list" link in the
  add-account dialog leads to the provider list ✅.

## Rate limits
- Not applicable (client) ⚠️.

## SDKs and client libraries
- None ⚠️. Relevant for us only through the standards: see
  [messages standards](../../../../../../data/messages/standards.md).
