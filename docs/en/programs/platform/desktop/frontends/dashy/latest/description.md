# Dashy - Description

## Overview

Dashy (project `Lissy93/dashy`, dashy.to) is an open-source, highly customizable start page tool for self-hosted services. The focus is on text-based configuration, from which a fast tile interface with status indicators, widgets and a theme-friendly design is created.

## What Dashy does

Dashy reads a configuration file (`conf.yml` or `conf.json` in the folder `user-data/`) and builds from it **sections** with **app tiles**: icon, title, description, target URL, opening mode, tags. On request, Dashy checks the reachability of each tile when the page loads (HTTP or ping) and colors it accordingly. Additionally, widgets (clock, weather, RSS, crypto prices, custom widgets) can be embedded. There are three views — normal, reduced and workspace — as well as themes, a search that filters instantly, and optionally several subpages.

The configuration can be changed by hand, via the interactive editor in the interface, or via the optional REST API.

## Advantages

- **Configuration as a file**: versionable, testable, compared in seconds
- **Interactive editor**: changes are still possible without a text editor
- **Status indicators**: green/red dots on all tiles, with custom check rules
- **Themes and custom CSS**: extensive bundled schemes, theme editor in the interface
- **Fast search**: instant filtering while typing, tags, URL aliases, web search with shortcut commands
- **Built-in authentication**: HTTP Basic, OIDC providers, local users with roles and optional two-factor option
- **Optional REST API**: read and write the configuration programmatically
- **Flexible hosting**: container, bare metal or purely static

## Distinction from other systems

### Dashy vs. Homarr
- **Dashy** describes the dashboard in a file, **Homarr** builds it via drag & drop in a database
- **Homarr** controls containers and media services, **Dashy** only checks reachability and displays values
- **Dashy** is highly customizable visually, **Homarr** follows a uniform look

### Dashy vs. Heimdall
- **Dashy** uses sections with many options per tile, **Heimdall** uses panels with tiles and enhanced apps
- **Dashy** has a documented REST API, **Heimdall** does not
- **Heimdall** is narrower in scope and therefore quicker to grasp

### Dashy vs. Homer
- **Both** are file-based, **Dashy** additionally has server functions: login, status checks, API, configuration write access
- **Homer** is much lighter and has no runtime logic at all
- **Dashy** can be hosted statically, but then loses status checks and the API

## Technical details

- **Backend**: optionally a Node server (Express) that handles status checks, authentication, configuration access and the API
- **Database**: none; state lives in `conf.yml`/`conf.json` and in local browser storage
- **Frontend**: Vue application (historically Vue 2, newer versions built with Vite), responsive display
- **Authentication**: HTTP Basic via the server, OIDC providers (Keycloak, Zitadel, among others), local users with hashed keys, roles (admin/user), optional two-factor authentication, minimum role per function
- **Hosting**: Docker image (LinuxServer.io or original), bare metal with Node, static on any web server/CDN (then without server functions)

## Who is Dashy suited for?

- **Admins who manage their start page as code** and still want an interface for follow-up changes
- **Users who want to see status indicators and widgets** on one page
- **Environments with logins**, such as family dashboards with different roles
- **Less suited** for plain link lists without further requirements (then Homer) or for teams that do not want to touch files (then Homarr)
