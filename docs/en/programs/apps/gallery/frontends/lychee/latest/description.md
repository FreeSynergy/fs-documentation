# Lychee - Description

## What the program does

Lychee puts photos in albums on the web: upload, create albums, share links with or without a password. The focus is on a fast gallery and a tidy API rather than on AI features.

## Advantages

- **lightweight**: runs on small shared hosting/VPS, fast interface
- **clean REST API** with documented endpoints, good for frontend integration
- **shares with expiry and password** implemented in an everyday-usable way

## Differentiation

| System | Difference |
|--------|------------|
| **Piwigo** | Themes and permissions per category, huge plugin ecosystem; Lychee is more modern but narrower in function. |
| **PhotoPrism** | Index and AI search over existing folders; Lychee has no index pipeline. |
| **Immich** | Photo cloud with apps and AI; Lychee is deliberately a simple gallery. |

## Technical details

- **Backend**: PHP 8 / Laravel, MySQL, MariaDB or PostgreSQL
- **Frontend**: React (Lychee-front), deployed separately in v5
- **Images**: generated sizes (Thumb, Small, Medium, High), the original remains
- **Auth**: local, OAuth2/OIDC providers, API token per user
- **Deployment**: Docker Compose, bare metal with Composer
- **Licence**: MIT (v4/v5)

## Who it suits

- Small to medium galleries with a focus on sharing and speed
- FreeSynergy gallery frontends with an album / photo / share model
- Operators with no need for AI detection
