# LaunchBoard - Description

## Overview

LaunchBoard is aimed at users and small teams who want to build an attractive homelab dashboard **without YAML and without source code**. The scope of delivery is identical whether the instance runs with the provider or in one's own Docker container: board editor, widget library, integration management and user management with single sign-on.

## What LaunchBoard does

LaunchBoard manages **boards** (user interfaces made of tiles) in a bundled database. In the **drag-and-drop editor**, layouts are created from app tiles, status displays, charts and text blocks; a widget library provides ready-made building blocks. **Integrations** store the URL and key of a service; widgets then display live values and trigger actions on supported services (restart a container, pause a download). Access works in three ways: local accounts, OAuth2/OIDC against an existing identity provider (Authentik, Keycloak, Entra ID, Google), or a protected cloud URL of the provider. Roles determine who may build boards and who may only view them. Operation, updates and, in the cloud variant, TLS are handled by the provider.

## Advantages

- **No configuration file chaos**: everything is done with the mouse; boards and widgets are stored in the database
- **Quick and attractive**: professional templates, themes and icon libraries out of the box
- **Single sign-on included**: OAuth2/OIDC is a core feature, not an add-on
- **Two operating options**: cloud subscription for minimal operation, container for data sovereignty
- **Team-ready**: roles, sharing and shared boards
- **Commercial support**: updates, support tickets, documented roadmap
- **Actions possible**: some integrations allow intervention in containers and media stacks

## Differentiation from other systems

### LaunchBoard vs. Homarr
- **Both** are configured with the mouse and store their data in a database
- **Homarr** is open source and free of charge, **LaunchBoard** is proprietary with a subscription model
- **Homarr** has a public tRPC reference, **LaunchBoard** has no freely viewable API documentation
- **LaunchBoard** excels in templates and SSO, **Homarr** in depth of integration in the homelab

### LaunchBoard vs. Heimdall
- **Heimdall** (Laravel, open source) relies on app tiles with optional statistics, **LaunchBoard** relies on a full widget editor
- **Heimdall** has no noteworthy rights management, **LaunchBoard** has roles and sharing
- **Heimdall** is free and self-hosted, **LaunchBoard** is paid, optionally as a cloud service

### LaunchBoard vs. Homer
- **Homer** is a static, YAML-configured page without login; **LaunchBoard** is an application with a database, editor and sign-in
- **Homer** is free and has no actions, **LaunchBoard** is interactive with integrations
- **Homer** suits minimal requirements, **LaunchBoard** is for convenience and team use

### LaunchBoard vs. Dashy
- **Dashy** is configured via `conf.yml` (optionally with a UI editor) and is open source, **LaunchBoard** is graphical only
- **Dashy** has a very extensive theme system and its own widget syntax, **LaunchBoard** has curated widgets and themes
- **Dashy** has no support, **LaunchBoard** has commercial support and licence terms per plan

## Technical details

- **Backend**: proprietary server application (not published in source code); bundled relational database in the container, managed by the provider in the cloud variant
- **Database**: present – boards, widgets, integrations, users and roles are persisted; the exact database system according to the provider's documentation in the customer portal (**not publicly documented**)
- **Frontend**: modern web client interface with drag-and-drop editor, responsive display, proprietary theme engine
- **Authentication**: local accounts with password, **OAuth2/OIDC** (Authentik, Keycloak, Entra ID, Google, Generic OIDC), optionally header authentication behind a reverse proxy; roles (Administrator, Editor, Viewer)
- **Hosting**: cloud subscription (subdomain of the provider, TLS and updates included) **or** own container (Docker/Compose, port via environment variable, HTTPS via reverse proxy); licence/subscription per instance

## Who is LaunchBoard suitable for?

- **Families and small teams** who need a maintained dashboard with SSO and separate rights
- **Users who do not want YAML** and who want to build boards with the mouse and use templates
- **Businesses that expect support** and accept a licence for it
- **Less suitable** for open-source environments, for environments without a database, and for anyone who wants to version their dashboard definition in Git (then use Homepage or Homer)
