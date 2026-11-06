# Redmine - Description

## Overview

Redmine is an open-source project management web application: multiple projects,
differentiated issue trackers, time tracking, wiki and forums — lean, proven and
extremely plugin-friendly.

## What Redmine does

Redmine manages **any number of (sub-)projects**, each with its own members, roles and
modules. Issues get **trackers** (e.g. bug, support, task), **status**, **priority**,
category, milestone, assignment and custom fields; status changes follow configurable
**workflows** per role and tracker. **Time entries** are booked per issue and activity
and evaluated via reports. Every project can activate a **wiki**, **forums (boards)**,
**documents**, **file attachments**, **news**, **roadmap** and **calendar**. Redmine has
been available since 2006 and is developed community-driven.

## Advantages

- **Lean and stable**: Rails core without ballast, proven over years
- **Plugin ecosystem**: hundreds of extensions (kanban boards, two-factor auth, themes, CRM ...)
- **Multilingual**: fully translated UI (German among others)
- **Granular workflows**: permissions per tracker, role, status transition and field
- **REST API** with XML and JSON plus Atom/ICS feeds
- **Version control**: integrated browsers for Git and Subversion, commit links to issues
- **Free and self-hosted**: full data sovereignty

## Differentiation from other systems

### Redmine vs. OpenProject
- **OpenProject** (from Redmine's ChiliProject line of origin) delivers a modern UI, Gantt and agile boards in the core; **Redmine** keeps the core small and gets features via plugins
- **OpenProject** needs PostgreSQL, **Redmine** also runs with MySQL/MariaDB
- **Redmine** is more plugin-oriented, **OpenProject** extends the core itself

### Redmine vs. Jira
- **Jira** is commercial with SaaS operation and a marketplace, **Redmine** self-hosted and free
- **Jira** comfortably offers JQL, boards and automation, **Redmine** solves the same via filters, plugins and manual work
- **Redmine** is more a ticket/issue system with project add-ons, **Jira** a product for agile software tracking

### Redmine vs. Trac
- **Trac** is aimed at one project (wiki + changesets), **Redmine** is multi-project from the ground up
- **Redmine** ships time tracking, workflows and a differentiated role model out of the box, **Trac** only basic tickets
- **Trac** is older and more minimalist, **Redmine** functionally much broader

## Technical details

- **Backend**: Ruby on Rails
- **Database**: MariaDB/MySQL or PostgreSQL recommended; SQLite only restricted/checked depending on version (version-dependent)
- **Frontend**: server-rendered HTML (ERB), jQuery; no single-page frontend
- **Authentication**: local accounts, LDAP; OpenID dropped from the core (Redmine 5.0+), alternatives via plugins (CAS, SAML, OAuth — version-dependent)
- **Hosting**: Ruby environment (Phusion Passenger, Puma), community Docker images; no official image

## Who Redmine suits

- **Technical teams and service providers** bundling issues, support and time tracking in one self-hosted application
- **Administrators with plugin needs** shaping Redmine into their own platform via extensions
- **Cost-conscious organisations** putting maturity and data sovereignty before modern comfort
- **Less suitable** for teams expecting modern scrum boards immediately without plugins
