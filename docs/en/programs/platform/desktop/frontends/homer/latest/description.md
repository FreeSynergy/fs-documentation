# Homer - Description

## Overview

Homer (project `bastien64/homer`, container image `b4bz/homer`) is a deliberately simple, static dashboard. A YAML file describes groups, tiles and links; a small single-page application reads this file in the browser and renders the start page.

## What Homer does

Homer shows a single page: a header with title, optional icon links, optionally a search field, and below that several columns with group headings and tiles. Each tile is a link to a service, visible via icon and name. The file `assets/config.yml` contains the complete description; it is loaded at runtime and can be switched via a query parameter. There is no user management, no live status values and no actions against services.

## Advantages

- **Tiny and fast**: static files, no database, no running application
- **Configuration as a text file**: versionable in Git, checked in seconds
- **No maintenance effort**: no migrations, no dependency updates during operation
- **Multiple instances possible**: different `config.yml` files for different teams or devices
- **Hostable anywhere**: nginx, Apache, object storage, GitHub Pages, even `file://`
- **Clean design**: light and dark scheme, custom CSS via CSS variables
- **Resource-friendly**: runs on a Raspberry Pi as well as on a CDN

## Distinction from other systems

### Homer vs. Homarr
- **Homer** is static, **Homarr** is an application with login, database and rights
- **Homer** is changed in the file, **Homarr** via drag & drop in the interface
- **Homarr** actively accesses Docker and services, **Homer** only links

### Homer vs. Heimdall
- **Heimdall** shows live values via enhanced apps, **Homer** remains with icon and name
- **Heimdall** maintains content via the interface in a database, **Homer** via the YAML file
- **Homer** has no login, **Heimdall** ships local accounts

### Homer vs. Dashy
- **Both** work with configuration files, **Dashy** additionally with a powerful interface and optional REST API
- **Dashy** offers status checks, widgets, themes and authentication, **Homer** none of these
- **Homer** is considerably smaller and faster, **Dashy** richer in features and heavier

## Technical details

- **Backend**: none. A Vue-based single-page application runs entirely in the browser
- **Database**: none; state exists only in the configuration file and in local browser storage (individual preferences)
- **Frontend**: HTML, CSS and JavaScript; the configuration is loaded as YAML at runtime
- **Authentication**: not available. Protection exclusively via reverse proxy (Basic auth, Authentik/Authelia), network segmentation or IP filter
- **Hosting**: nginx-based container image, any static web server, file hosting, CDN; updates by replacing the files

## Who is Homer suited for?

- **Users with a manageable list of services** who mainly need links
- **Admins who treat configuration as code**: Git, pull requests, CI/CD
- **Environments without maintenance windows** (off-grid, backup portal, emergency page)
- **Teams who want to show everyone the same start page** without managing accounts
- **Less suited** if live status, container actions or individual dashboards per person are expected
