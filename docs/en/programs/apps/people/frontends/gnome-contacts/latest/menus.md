# GNOME Contacts - Menu Items

## Overview

GNOME Contacts has **no menu bar** — everything hangs off the HeaderBar and the context menus (⋮).

## Main menu (⋮ top right)

| Entry | Description |
|-------|-------------|
| New Contact | Create an empty card |
| Import… | Import a vCard file |
| Export… | All contacts as `.vcf` |
| Merge Contacts | Merge duplicates |
| Print | Print the contact list |
| Help / Keyboard Shortcuts / About | Standard GNOME items |

## Contact view

- Edit switch (the "Edit" toggle): all fields inline; "+" adds field types (phone, e-mail, address, birthday, note, website, relationship)
- Header action menu of the contact: **Delete**, **Save contact as vCard**, **Merge with…**
- Photo via drag&drop into the portrait

## Sources (primary/secondary address books)

- The source is chosen in the "Address" field of the card
- Account sources come from **GNOME Online Accounts** (Google, ownCloud/Nextcloud CardDAV, LDAP via EDS)

## Menus by role

No accounts/roles — access follows from the EDS sources (writable/read-only, e.g. LDAP = read-only).
