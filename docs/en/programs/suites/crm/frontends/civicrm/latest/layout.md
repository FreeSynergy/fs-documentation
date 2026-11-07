# CiviCRM - Structure and UI/UX

## Page structure

```
┌────────────────────────────────────────────────────────────────┐
│ CMS bar (Drupal/WP/Joomla)                                     │
│ Contacts | Contributions | Events | Memberships | Administer   │
├──────────────────────────────┬─────────────────────────────────┤
│ Search results / Dashboard   │ Contact: Andrea Berg            │
│ 🔍 Find Contacts             │ [Actions ▾]                     │
│ ┌──────────────────────────┐ │ Tabs: Activities | Mailings |   │
│ │ ☐ Andrea Berg  ber…      │ │ Contributions | Events |        │
│ │ ☐ Beta GmbH              │ │ Memberships | Relationships |   │
│ └──────────────────────────┘ │ Tags | Custom                   │
│ Saved Searches               │ ── Tab content ──               │
│ Dashboard tiles              │ (tables + add actions)          │
└──────────────────────────────┴─────────────────────────────────┘
```

- The character is "CMS page with CRM content": forms, tables, tabs
- Public: event registration/donation forms as CMS pages (popup widget "Find Contributions" possible)

## UI/UX

- Functional backend style, not uniform (grown historically); the page theme follows the CMS
- Cividashboards + SearchKit admin pages are more modern than the legacy forms

## Interactions

- Mass actions via checkboxes + Actions button
- Inline pickers for relationships and tags (AJAX autocomplete)
- No live updates, reload-based

## Responsive design

- Admin pages partly responsive (core forms okay, report-style mass forms poor)
- Public forms (events/contributions) responsive thanks to templates

## Accessibility

- Follows CMS basics; forms labeled, but autocomplete widgets are weak
- Keyboard-accessible tables; Actions menus reachable via Tab

## Performance

- Large data sets (1M+ contacts) need DB index tuning and caching (Varmast); SearchKit uses SQL optimization
