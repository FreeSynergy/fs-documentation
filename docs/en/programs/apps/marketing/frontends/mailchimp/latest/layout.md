# Mailchimp - Structure and UI/UX

## Layout

```
┌───────────────────────────────────────────────────────────────┐
│ Mailchimp   Search…                   [Create]  🐒 👤           │
├────────────┬──────────────────────────────────────────────────┤
│ Dashboard  │ Audience "Newsletter": 4,312 contacts            │
│ Campaigns  │  Segment "Donors" ▾  [Export] [Import]           │
│ Audience   │  Table: Email | Tags | Fields | Absence          │
│ Automations│ Journey builder: trigger → [mail] → [delay] →    │
│ Content    │           [condition] → [mail/tag]               │
│ Analytics  │  Reports with open/click curves                  │
└───────────────────────────────────────────────────────────────┘
```

- The contacts table is central; the journey builder is a horizontal flow

## UI/UX

- Friendly yellow-monkey branding; guided wizards ("start a campaign")
- Campaign editor: block palette + live preview (desktop/mobile)

## Interactions

- Tag/segment assignment inline; CSV import with column mapping
- Journey nodes by drag, conditions as decision diamonds

## Responsive design

- Desktop-centred; the mobile app is only reports/notifications

## Accessibility

- Standard web; the editor blocks are keyboard-operable

## Performance

- Large audiences (100k+) with a segment cache; API pagination is obligatory
