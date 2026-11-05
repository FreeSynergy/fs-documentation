# KAddressBook - Structure and UI/UX

## Window structure

```
┌───────────────────────────────────────────────────────────────────┐
│ File Edit View AddressBook Tools Settings Help                    │
│ [🆕][✎][🗑]                    🔍 Search…                          │
├─────────────┬───────────────────────────┬─────────────────────────┤
│ Address book│ Contact list (table)      │ Detail view             │
│ tree        │ ☐ Name  E-mail  Tel       │ ┌─────────────────────┐ │
│ ● Personal  │ ☐ Berg, A.  a@…   +49…    │ │ [Photo] Andrea Berg │ │
│ ○ Work      │ ☐ Klein, B. b@…   +49…    │ │ ✉ a@…               │ │
│ ☁ CardDAV   │                           │ │ ☎ +49…              │ │
│ ☁ LDAP      │                           │ │ ★ Birthday          │ │
│             │                           │ └─────────────────────┘ │
└─────────────┴───────────────────────────┴─────────────────────────┘
```

- 3-column split; detail panel with a "Details" tab, newer versions with inline editing
- The quick-selection bar (bottom left) shows favourited contacts as buttons

## UI/UX

- Qt Widgets classic, follows the Breeze/Fusion design; system light/dark
- Columns freely selectable and sortable (click on the header)
- Font-size adjustment as in the rest of KDE

## Interactions

- **Drag & drop**: drag contacts between address-book folders (move/copy depending on permissions)
- **Right click**: context menu (edit, save as vCard, delete)
- **Double click**: detail editor
- **Animations**: practically none (desktop classic)

## Responsive design

Not responsive — a desktop window; at high DPI Qt fonts scale automatically.

## Accessibility

- Qt Accessibility: tables, forms and menus fully named; access keys (`Alt+F` …)
- Screen-reader-capable editors; detail-field labels are present
- Shortcuts in [shortcuts.md](shortcuts.md) are fully operable — mouse alternatives always available

## Editor structure

- Contact editor with section tabs; fields via a "+" menu grouped by category (phone types WORK/CELL, address types)
- Raw vCard view as a text field in "import contact/debug" (developer route)
