# GNOME Contacts - Description

## What the program does

GNOME Contacts is GNOME's own contact manager: a lean GTK surface on top of the Evolution Data Server. Contacts are maintained locally and via online accounts (Google, CardDAV, LDAP) and shared with all GNOME apps.

## Advantages

- **Minimal and fast**: one window, no menu bar at all, usable immediately
- **EDS backend**: one source for GNOME Shell search, mail clients, calendars
- **Standard tooling**: vCard import/export, online accounts without vendor lock-in

## Differentiation

| System | Difference |
|--------|------------|
| **KAddressBook** | The KDE counterpart with Akonadi, broader import formats and a wider variety of field types; GNOME Contacts is reduced far more radically. |
| **Evolution** | A full PIM suite (mail/calendar/tasks) on the same EDS; Contacts is only the contact part. |
| **Nextcloud Contacts** | A web server with sharing; GNOME Contacts is a desktop client and can access exactly that (online account). |

## Technical details

- **Backend**: Evolution Data Server (D-Bus services `evolution-source-registry`, -addressbook-registry)
- **Frontend**: GTK 4 / libadwaita, C/Vala
- **Data storage**: EDS caches (`~/.local/share/evolution/addressbook/`), the sync protocols of the sources
- **Authentication**: online-accounts dialog (OAuth2 for Google; Basic for CardDAV), passwords in the GNOME Keyring
- **Platform**: Linux (GNOME), official builds only there
- **Licence**: GPL

## Who it suits

- GNOME users with online accounts or Nextcloud/Fastmail CardDAV
- Environments that need a unified EDS contact base for several apps
- FreeSynergy frontends that recreate reduced contact masks (card + fields + source selection)
