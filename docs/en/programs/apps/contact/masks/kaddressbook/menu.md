# KAddressBook - Menu Items

## Menu bar (standalone program; identical as a module in Kontact)

| Menu | Entries (selection) |
|------|---------------------|
| **File** | New → contact / distribution list; import/export assistant; print; quit |
| **Edit** | Edit contact, copy/cut/paste, delete contact, find/replace |
| **View** | Columns on/off, quick-selection bar, address-book browser on/off, choose display theme |
| **Address Book** | New address book (folder/CardDAV/LDAP/…), address-book properties, save all as vCard |
| **Tools** | Import/export, print cards (business-card layouts), "synchronise contacts" interface (Akonadi agent status) |
| **Settings** | Manage Akonadi resources, shortcuts, Configure KDE PIM |
| **Help** | Handbook, About |

## Import/export assistant

| Format | Direction |
|--------|-----------|
| vCard (.vcf) | Import + export (single/multiple) |
| LDIF / LDAP | Import + export |
| CSV/LDIF (KABC-CSV) | Import |
| GMX/WebDAV export (outdated) | Export |
| ABCZ, LDIF-Bord | Depending on version |

## Right click on a contact

Edit · Copy · Delete · Save as vCard · Add to distribution list · Show details

## Address-book browser (left)

- Akonadi folder tree: personal folders, CardDAV/IMAP/LDAP resources
- Right click: properties, sync now, offline behaviour

## Menus by role

| Role | Effect |
|------|--------|
| Local user | All menus |
| LDAP folder (read-only) | Create/edit menus greyed out |
| CardDAV share (read) | Same as read-only |
