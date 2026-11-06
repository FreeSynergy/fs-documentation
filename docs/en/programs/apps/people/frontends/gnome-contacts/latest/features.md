# GNOME Contacts - Features

## Main features

### Contacts
- vCard fields: name, phone, e-mail, address, birthday/anniversary, note, website, relationships (parents, children, partner, siblings)
- Photos (drag&drop), favourites via a "star" are not present — instead a "frequent contacts" sort order
- Link/split cards (`Link contacts`, `Unlink`)

### Sources via Evolution Data Server (EDS)
- Local address books ("Personal")
- GNOME online accounts: Google contacts, CalDAV/CardDAV (Nextcloud, Fastmail …)
- LDAP address books (read-only)
- Offline persistence + re-sync through EDS

### Maintenance
- Duplicate detection and merging
- vCard import/export (single and batch)
- Printing (address lists)

## What GNOME Contacts does NOT do

- **No distribution lists** as their own cards (creating/managing mailing lists)
- **No tags/categories** (only field types and relationships)
- **No CRM** (no activities — Monica)
- **No server component/API of its own** (EDS is client-side; sharing runs over CardDAV servers)
- **No field templates/custom fields**

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| GNOME Shell | Contacts/search result in the overview |
| GNOME Online Accounts | Account → EDS source automatically |
| Geary/Evolution Mail | Autocomplete from EDS |
| `abook`/`khal` | Use the same EDS catalogues |
