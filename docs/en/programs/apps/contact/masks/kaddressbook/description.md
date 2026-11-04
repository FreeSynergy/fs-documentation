# KAddressBook - Description

## What the program does

KAddressBook manages contacts on the KDE desktop. It stores them in Akonadi folders or synchronises them with CardDAV, IMAP and LDAP sources, provides editors, import/export and print layouts, and supplies KMail/Kontact with address suggestions and birthdays.

## Advantages

- **Source-open**: one UI over local folders, CardDAV, LDAP and IMAP folders
- **Format fidelity**: clean vCard/LDIF without proprietary additions
- **Deep desktop integration**: autocomplete, business-card printing, calendar linkage
- **Kontact-capable**: as a module it is the same code as the PIM-suite contact tool

## Differentiation

| System | Difference |
|--------|------------|
| **Thunderbird (contacts)** | Thunderbird maintains its own mSQLite address-book file; KAddressBook works through Akonadi resources and can use the same CardDAV servers as Thunderbird. |
| **Nextcloud Contacts** | Server/web UI; KAddressBook is the desktop client on top of it. |
| **Evolution** | A GNOME PIM suite with its own data server; comparable architecture (EDS ≈ Akonadi), different toolkit. |

## Technical details

- **Backend**: Akonadi (MySQL/SQLite depending on setup), libraries `KPim::Akonadi`, `KABC` (vCard)
- **Frontend**: Qt Widgets, part of KDE Gear; Kontact module or standalone program
- **Language**: C++
- **Authentication**: resource-dependent (CardDAV Basic/app password, LDAP bind), passwords in KWallet
- **Platforms**: Linux/BSD; Windows unofficially
- **Licence**: GPL

## Who it suits

- KDE/Kontact users who want to unify several contact sources
- Migrations (GMX/LDAP/CSV → vCard/CardDAV)
- FreeSynergy skins that recreate desktop contact masks and vCard fields
