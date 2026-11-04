# Monica - Features

## Main features

### People with a history
- Contacts with master data, custom fields, photos, "important information"
- Relationships (partner, child, friend … with directed types), groups/labels
- Life events and milestones

### Activities and journals
- Activities with type, date, participants, note; timeline feed
- Journal books with entries, mood, place
- Reminders, e.g. "last activity in 6 months"

### Tasks, gifts, debts
- Tasks with a due date per contact or globally
- Gifts (planned/bought/received) with an ideas list
- Debt tracking between people

### Data storage
- vCard/CSV/Google import, JSON/vCard export
- Public vCard pages per contact (link)
- Self-hosted or a Monica CLOUD subscription

## What Monica does NOT do

- **No business CRM** (no pipelines/deals — SuiteCRM/pipedrive)
- **No outward calendar sync**: its own reminders, but no CalDAV interface (❌)
- **No e-mail integration** (inbox/mail sync)
- **No multi-tenancy beyond circles** (circles separate, but no role hierarchy)
- **No mobile app** (responsive web UI + community apps only)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| REST API + token | Settings → API |
| Webhooks | Configurable per event (contact created, activity added …) |
| Imports | vCard, CSV, Google contacts |
| Docker/k8s deploy | Official images |
| Community modules | Experimental modules (life events, debt) |
