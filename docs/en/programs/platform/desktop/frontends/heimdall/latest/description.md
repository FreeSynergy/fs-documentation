# Heimdall - Description

## Overview

Heimdall (project `linuxserver/Heimdall`, heimdall.site) is an open-source dashboard that displays links to your own web applications as tiles and, if desired, enriches them with live values from the respective services. It sees itself as a lean start page, not as a portal platform.

## What Heimdall does

Heimdall provides a web interface with **panels**: a panel contains a group of app tiles, plus search, statistics and notice areas. Apps are links with title, URL, icon and colour. For many well-known self-built services there are **enhanced apps**: add-on packages that connect to the service and write figures such as blocked ad requests, running downloads or library sizes directly into the tile. Server tiles show CPU, memory, disk and network of the Heimdall machine.

The project deliberately emphasizes: no embedded frames, no applications within applications, no abstraction of third-party APIs.

## Advantages

- **Quick to get running**: start the container, create an admin account, enter apps
- **Clear tile look**: large, easy-to-read icons instead of small widgets
- **Enhanced apps**: live data from known services without custom code
- **Encrypted keys**: API keys of the enhanced apps are stored encrypted in the database
- **Laravel base**: familiar PHP structure, simple custom adjustments
- **Panel layout**: areas can be wrapped, moved and hidden
- **Lightweight**: one application, one database file, no build step

## Distinction from other systems

### Heimdall vs. Homarr
- **Heimdall** works with panels and tiles, **Homarr** with a free widget grid (resize, arbitrary positions)
- **Homarr** can start and stop containers, **Heimdall** displays data and links to it
- **Heimdall** configures runtime details in `.env`, **Homarr** entirely in the interface

### Heimdall vs. Homer
- **Homer** is a static page without a backend, **Heimdall** is a PHP application with a database and login
- **Homer** is described in `config.yml`, **Heimdall** is maintained via the interface
- **Homer** has no live values, **Heimdall** shows statistics via enhanced apps

### Heimdall vs. Dashy
- **Dashy** is controlled predominantly via `conf.yml`/`conf.json`, **Heimdall** via the interface
- **Dashy** offers mature theming, status checks and an optional REST API, **Heimdall** has neither of these in this form
- **Heimdall** is more manageable in its features, but very direct in operation

## Technical details

- **Backend**: PHP with Laravel; controllers, models and Blade templates
- **Database**: SQLite as default; MySQL/MariaDB and PostgreSQL possible via `.env`
- **Frontend**: Blade templates with jQuery (tile layout, drag & drop) and chart displays for statistics values
- **Authentication**: local accounts (standard installation one administrator account, newer versions with several users); sign-in can be disabled if needed; single sign-on only via a reverse proxy
- **Secrets**: credentials of the enhanced apps are stored encrypted with the Laravel `APP_KEY`
- **Hosting**: Docker image from LinuxServer.io (port 80/443, often 8080), also bare metal with PHP-FPM and web server; persistent volumes for database and uploaded icons

## Who is Heimdall suited for?

- **Users who want a tidy link start page** with some live tiles
- **PHP/Laravel users** who prefer customizations in the source code
- **Homelabs with known services** (media servers, download clients, ad filters) for which enhanced apps exist
- **Less suited** for detailed dashboards with many different widgets (then Homarr or Dashy) or for installation-free environments (then Homer)
