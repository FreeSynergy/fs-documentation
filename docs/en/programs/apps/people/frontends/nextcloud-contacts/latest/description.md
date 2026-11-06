# Nextcloud Contacts - Description

## What the program does

Nextcloud Contacts manages personal and shared address books within a Nextcloud instance. Contacts are vCards in the server database, reachable via the web frontend and any CardDAV client. Sharing, circles and the linkage with Mail/Talk/Calendar make it the contact backbone of the suite.

## Advantages

- **One account, all devices**: CardDAV sync out of the box
- **GDPR-friendly**: the data stays on your own instance
- **Suite integration**: mail autocomplete, Talk chat buttons, birthday calendar
- **Standard formats**: import/export is pure vCard, no vendor lock-in

## Differentiation

| System | Difference |
|--------|------------|
| **KAddressBook (KDE)** | A desktop program with Akonadi; Nextcloud Contacts is the server with a web UI. Both can hang off the same CardDAV. |
| **Monica** | A personal CRM with activities and relationships; Nextcloud Contacts only stores contact data. |
| **GNOME Contacts** | A local GTK client on the Evolution Data Server; it accesses CardDAV itself (including Nextcloud) — client vs. server. |

## Technical details

- **Backend**: PHP (Nextcloud app `contacts`), vCard parser `sabre/vobject`
- **Database**: the Nextcloud main DB (tables `oc_cards`, `oc_cards_addressbook`)
- **Frontend**: Vue 3, Team dialog components
- **Authentication**: Nextcloud session/app passwords; CardDAV Basic over TLS
- **Hosting**: on any Nextcloud instance (app can be enabled)
- **Licence**: AGPL

## Who it suits

- Nextcloud users as a central contact store
- Families/teams with CalDAV/CardDAV clients on all devices
- FreeSynergy contact scenarios that want to recreate vCard/CardDAV frontends with sharing
