# CiviCRM - Features

## Main features

### Contacts and relationships
- Individuals, Organizations, Households; relationships (member of, employer of…)
- Groups (static/dynamic via saved searches), tags, custom fields (own entities)
- Deduplication (unsupervised/supervised rules), merge history

### Donations (CiviContribute)
- Contributions, recurring donations, PCP donation pages, payment processing via processors (Stripe, PayPal, GoCardless …)
- Accounting-ready records: financial types and accounts, CSV export

### Events (CiviEvent)
- Event types, prices (fee levels), capacities, waiting list, online registration, check-in (QR)

### Memberships (CiviMember)
- Membership types with terms/roll-over, status rules, automatic renewal

### Communication
- CiviMail (bulk with tracking), templates, activities (history), surveys/petitions (campaigns)

### Cases and applications
- Cases (case workflow with activities), grants (application management)

## What CiviCRM CANNOT do

- **No sales CRM** (no pipeline/deals — EspoCRM/SuiteCRM territory; extensions are rudimentary)
- **No own login / permission management** — depends on the CMS
- **Bulk mail without its own MTA setup** (SMTP/CiviMail bulk processing must be configured)
- **Reporting dated**: standard reports are weak; Serious Dev/Semantic for better analysis (extensions)
- **No mobile app** (only responsive form pages, no agent app)

## Extensions and integrations

| Integration | Way |
|-------------|-----|
| Extensions directory | CiviConnect/Download, `extmanage` |
| Payment | Payment Processor Framework |
| Zapier/make | official Zapier connector + API v4 |
| Search/Elastic | SearchKit/API4 + extension (e.g. Search Kicker) |
| Backend sync | Drupal/Joomla/WordPress user sync |
