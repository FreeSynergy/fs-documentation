# Nextcloud Contacts - Structure and UI/UX

## Page structure

```
┌────────────────────────────────────────────────────────────────┐
│ Nextcloud bar (🔍 Search, 👤)                                    │
├──────────────────┬───────────────────────┬─────────────────────┤
│ Address books    │ Contact list          │ Detail/editing panel│
│ 📇 Personal       │ A ─ Andrea Berg       │ ✎ Andrea Berg       │
│ ★ Yellow (system)│ B ─ Ben Klein         │ 📧 andrea…           │
│ ○ Work (shared   │ B ─ Beta GmbH         │ ☎ +49…              │
│ + Address book   │ …                     │ ✚ Field             │
│ 🗑 Deleted        │ [☑ Selection] [Import]│ ♪ Birthday          │
└──────────────────┴───────────────────────┴─────────────────────┘
```

- Three-column master-detail layout; selection checkboxes for bulk actions (delete, download, add to book)
- Editing inline in the detail panel, "add field" menu grouped by vCard categories

## UI/UX

- Follows the Nextcloud design system (Team dialog), light/dark depending on the instance theme
- Initial avatars, photos, favourite star
- Real-time search over name, organisation, phone, e-mail

## Interactions

- **Drag & drop**: drop `.vcf` files straight into the list
- **Right click on a contact** (newer versions): context menu with download/delete
- **Animations**: panel transitions as cross-fades, list virtualisation without jumps

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Three columns |
| Tablet | List + expandable detail |
| Mobile | Single column, list → detail overlay |

## Accessibility

- DOM forms, keyboard tabbing is fine; screen-reader labels for field types are present
- Bulk-action tables with checkboxes — fully operable by keyboard
- Colour badges (shared) are additionally accompanied by text

## Performance

- With more than 10,000 contacts the initial load takes longer (sync status); versions with delta sync improve this noticeably
