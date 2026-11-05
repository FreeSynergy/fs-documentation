# KAddressBook - API Documentation

## Overview

KAddressBook is a client — it provides **no API**. Programming targets the KDE libraries (`KABC` for vCards, the Akonadi server via D-Bus/IPC) and the resource protocols (CardDAV, LDAP, IMAP). A FreeSynergy skin therefore attaches to **Akonadi exports or the underlying server APIs**, not to the program itself.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| KABC / KPim APIs (C++) | Read/write contacts programmatically | official (library) |
| Akonadi-control / D-Bus | Manage the resources, test access | semi-public |
| CardDAV/LDAP/IMAP of the resources | Actual data transfer | standard protocols |
| vCard/LDIF/CSV files | Exchange format | official |
| REST API | — | ❌ Not present |

## Authentication

None of its own — resource logic: CardDAV Basic with an app password, LDAP bind DN, IMAP OAuth; all in **KWallet**.

## KABC core (C++)

```cpp
KABC::Addressee a;
a.setFormattedName(QStringLiteral("Andrea Berg"));
a.insertEmail(QStringLiteral("andrea@example.org"), true);
KABC::AddressBook *book = KABC::standardAddressBook();
book->insertAddressee(a);
book->save();   // writes into the Akonadi database
```

- `KABC::AddressBook` aggregates all Akonadi contact folders
- `KPim::Mime`/`KTp` supplement vCard/iPIM handling

## CLI levers

| Tool | Purpose |
|------|---------|
| `akonadi-console` | Graphical view of the collection structure |
| `akonadi-control --help` | Manage agents/folders |
| `kabc-export` (newer versions) | Pull folders out as vCard files |

## Example: the vCard exchange route

1. Address book → "Save all as vCard" → `.vcf` batch
2. Map the batch with any vCard tool/REST converter
3. Re-import via the import assistant with a duplicate check

## Rate limits

Only relevant for the resource servers (the CardDAV/LDAP limits of the server).

## Skin note

The vCard field vocabulary is the common language ([fields.md](../../../../../../data/fields.md), [Contact model](../../../../../../data/models.md)); a "KAddressBook skin" recreates list/tree/editor and reads `.vcf` batches or CardDAV.
