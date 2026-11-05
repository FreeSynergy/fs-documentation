# Mautic - Features

## Main features

- **Campaign canvas**: triggers (form, segment membership, event → decisions / waiting / actions (email, SMS*, tag, points, CRM webhook)
- **Static/dynamic segments** (rule builder), contact activity chronology (pages visited, mail interaction)
- Landing pages/forms/assets, an email builder with drag blocks, A/B campaigns
- Point leading (behaviour score) + leads/contact models with custom fields
- Webhooks + REST API → ideal in a FreeSynergy landscape (contact sync!)

## What Mautic does NOT do

- **Deliverability is your own build**: an SMTP/relay (Mailjet/Sendgrid) is needed — no built-in send service
- **Report depth < commercial suites** (funnel visuals are rudimentary)
- The UI slows down with >100k contacts without tuning
- SMS/telephone integrations = third-party plugins
- Updating large installations needs maintenance windows

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| REST API + webhooks | official |
| Plugin system (Composer) | Your own integration skins |
| WP/Joomla plugins, Zapier | Available |
