# CiviCRM - Description

## What the program does

CiviCRM manages the relationship with "members": who has donated, who is a member until when, who attended which event, who signed which petition. It runs as a module inside an existing CMS and shares users and permissions with that CMS's user accounts.

## Advantages

- **Built for non-profits**: donations/memberships/events are first-class objects, not retrofitted
- **Data sovereignty**: open source (AGPL), on your own server
- **CMS symbiosis**: form pages (event registration, donation forms) on your own website
- **API v4** modern and entity-driven — easy to automate

## Differentiation

| System | Difference |
|--------|-------------|
| **SuiteCRM/EspoCRM** | Sales CRMs with leads/pipeline/deals; CiviCRM has no sales pipeline |
| **Salesforce (Nonprofit Cloud)** | commercial, very large; CiviCRM is the open-source answer to the same problem |
| **Mailchimp** | only campaigns/audience segments; CiviCRM is database-first with mail as one channel |

## Technical details

- **Stack**: PHP, MySQL/MariaDB; runs in Drupal/Joomla/WordPress (own tables `civicrm_*`)
- **Frontend**: Angular/jQuery mishmash ("Cividashboards", SearchKit views), forms server-side
- **Authentication**: CMS login + Civi permissions; API with site_key/auth_key
- **Hosting**: suitable for shared hosting (mind cron/mailing), Docker images (Flow community)
- **License**: AGPL

## Suitable for

- Clubs, associations and NGOs with their own website and a donation focus
- FreeSynergy skins that model contact + contribution + event + membership (constituent model)
