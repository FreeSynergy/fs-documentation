# Nextcloud Contacts - Menu Items

## Main navigation (Nextcloud header)

- App icon "Contacts" on the left of the app bar (order managed by the admin)
- Top bar: search, user menu, admin settings (⚙ → "Contacts administration" depending on version)

## Left column

| Menu item | Description |
|-----------|-------------|
| All contacts | The user's cross-cutting contact list |
| Deleted contacts | Trash bin with restoration |
| Shared address books | Books shared by others |
| Address books (own) | "Personal", "Birthdays & anniversaries", further own ones |
| + New address book | Create a new CardDAV address book |

## Contact detail

- Edit / Done
- Add fields (phone, e-mail, address, organisation, birthday, notes, social media)
- Favourite (star)
- Actions menu: **Call** (Talk/SIP), **Message** (Talk), **Write e-mail** (Mail app), **Save as card** (vCard file), **Delete**

## Sharing menu (per address book)

- Share with users/groups/circles — permissions: read, read/write, editor
- Public link sharing (address-book link, read access)
- Show the CardDAV URL of the book (for external clients)

## Import/export menu

- Import `.vcf` file(s) via drag & drop or the file dialog (duplicate detection)
- Mark contacts → "Download contacts" (`.vcf`)

## Menus by role

| Role | Menu |
|------|------|
| Regular user | Own books, received shares |
| Group admin | Manage shares for their own group |
| Nextcloud admin | "Settings → Contacts": allow circles, system address book (yellow pages), certificate/ColdStore options |
