# Piwigo - Description

## What the program does

Piwigo manages photos as a web-toolkit gallery: categories form the structure, roles decide visibility, themes determine the appearance. The images reside on the server and are brought in via sync or upload.

## Advantages

- **Very mature and stable**, in operation for over 15 years, large plugin catalogue
- **Fine-grained permissions** (groups × categories) — good for clubs and public authorities
- **Cheap to operate**: simple LAMP stack, suitable for shared hosting
- **Design freely adaptable** via themes and templates

## Differentiation

| System | Difference |
|--------|------------|
| **Immich / LibrePhotos** | A photo cloud with apps and AI, but without themes and a permission tree. |
| **PhotoPrism** | An index over folders with AI search, but no gallery permissions per folder. |
| **Coppermine** | A similar web toolkit, but an older codebase and a shrinking community. |

## Technical details

- **Backend**: PHP 8, MySQL/MariaDB, no mandatory framework (own core)
- **Images**: original + generated sizes (TH, CU, LI), watermark via cron
- **Frontend**: Smarty-like templates, themes with CSS overrides
- **Auth**: local, plugins for LDAP/OAuth2/social login
- **Deployment**: shared hosting, Docker, bare metal; upgrade via the admin interface
- **Licence**: GPLv2+

## Who it suits

- Clubs, schools and municipalities that need a curated public gallery
- FreeSynergy gallery frontends with a category / image / tag / group model
- Operators who want to steer design and permissions more strongly than the AI
