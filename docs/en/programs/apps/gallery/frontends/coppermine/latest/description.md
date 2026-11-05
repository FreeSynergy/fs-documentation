# Coppermine - Description

## What the program does

Coppermine presents photos in a web-toolkit gallery: categories and albums structure the collection, comments and ratings activate the community, roles govern who may see and upload what.

## Advantages

- **Proven feature set** of a community gallery (comments, ratings, albums)
- **Simple operation** on any PHP/MySQL system
- **Hooks** allow custom logic without forking the core

## Differentiation

| System | Difference |
|--------|------------|
| **Piwigo** | Actively developed, larger plugin landscape, webservice API; Coppermine has no API. |
| **Zenphoto** | A similar web toolkit, but with album inheritance and its own "zpCore" API. |
| **Lychee** | A modern surface with a REST API, but without community features. |

## Technical details

- **Backend**: PHP (current branches: PHP 8 compatible), MySQL/MariaDB
- **Images**: original + preview sizes generated in advance, watermark cron
- **Frontend**: theme system with templates, partly fixed layouts
- **Auth**: its own user tables, bridge integrations
- **Deployment**: shared hosting, Docker, bare metal
- **Licence**: GPLv3

## Who it suits

- Existing Coppermine installations that are to be recreated in FreeSynergy
- Operators running a community gallery without cloud conveniences
- As a comparison case in skin projects, because **no API** exists (to demonstrate the migration effort)
