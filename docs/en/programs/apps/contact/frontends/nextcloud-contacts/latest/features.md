# Nextcloud Contacts - Features

## Main features

### Contact management
- vCard 3.0 fields: names, phone, e-mail, addresses, organisations, birthday/anniversary, notes, social media, photos
- Favourites, "recently in contact", pools for reused fields (key-value)
- Duplicate detection on import, mergeable

### Address books and circles
- Several CardDAV address books per user
- Shares with users/groups/circles at three permission levels
- "Yellow system address book" (all Nextcloud users as contacts) — controlled by the admin
- Circles (teams): shared contacts, group birthday calendar

### Synchronisation
- CardDAV (RFC 6352) with Thunderbird, iOS, Android (DAVx⁵), GNOME
- Full/delta sync via sync token/COLLECTION-REPORT

### Import/export
- `.vcf` import (multiple files), vCard export of single/all contacts
- Merging imported with existing contacts

## What Nextcloud Contacts does NOT do

- **No CRM** (no activity history, no task relationship to persons — for that Monica/OCS-CRM)
- **No field templates/group fields** beyond the standard vCard
- **No LDAP replication** of personal contacts (LDAP is only read for accounts / "yellow pages")
- **No e-mail tracking** (opens/clicks) and no double-opt-in features
- **No REST administration API of its own** for contacts — the route is CardDAV, or OCS for shares

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| Talk | "Message" button, status display |
| Mail | Autocomplete from the contacts, images |
| Calendar | Birthday calendar "Personal birthdays" (generated from contacts) |
| Circles/Teams | Shared address books, team favourites |
| DAVx⁵/Thunderbird | CardDAV with privacy/sync filters |
| OCC CLI | `occ contacts:add`, `occ user:resetpassword` etc. (admin level) |
