# KAddressBook - Features

## Main features

### Contacts and folders
- vCard 3.0/4.0 with all KDE field types (phones, e-mail, addresses, birthdays, organisations, images)
- Several address-book sources in parallel: local folders (Akonadi), CardDAV, IMAP, LDAP, Akonadi Network Contacts
- Distribution lists (as vCard groups), quick-selection bar, favourited contacts

### Editing
- Full-fledged detail editor with tabs (General, Addresses, Relationships, Notes)
- Bulk editing (assigning categories/delete marks)
- Duplicate check via a "similarity" assistant

### Input and output
- Import/export assistant: vCard, LDIF, CSV/TSV, GMX, WebDAV
- Business-card/label printing (layouts, vCard renderer)
- QR business cards (newer versions, `kabc-export` helpers)

### Integration
- Birthday/anniversary calendar in the KDE PIM calendar, generated from contacts
- Autocomplete in KMail/Kontact; the address-book window in KMail is KAddressBook

## What KAddressBook does NOT do

- **No server**: contacts live in Akonadi databases or in the resources — no network endpoint of its own
- **No CRM** (no activities, no relationships beyond persons — Monica)
- **No web/mobile surface** (desktop only; mobile KDE devices via Plasma Mobile in its infancy)
- **No end-to-end encryption** of the folders (only full-disk/Ceph encryption of the operating system)
- **No team sharing** — sharing has to happen via CardDAV servers

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| CardDAV server (Nextcloud, Baïkal) | Akonadi resource "CardDAV" |
| LDAP/Active Directory | Akonadi LDAP resource |
| Google/calendar sync | Akonadi Google resource |
| KMail/Kontact | Embedded module |
| `kabc`/`akonadi-console` | CLI/debug access to the database |
