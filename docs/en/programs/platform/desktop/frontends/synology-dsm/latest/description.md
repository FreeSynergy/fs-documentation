# Synology DSM - Description

## Overview

DSM is not a dashboard in the sense of a link collection, but the **operating system of a Network Attached Storage device** with a graphical management interface in the browser. It brings storage, rights, backup, sharing and application logic; the browser portal is the workplace through which everything is controlled.

## What Synology DSM does

DSM manages disks, storage pools, volumes and shared folders and makes them available via SMB, NFS, AFP/WebDAV/FTP. The desktop portal shows a **desktop area with windows**, an app bar at the bottom edge, a **main menu** with all installed packages, desktop widgets for system status (CPU, memory, network, volume health – in current DSM versions deployed as "System Pulse"-style tiles) as well as a notification area. The **package centre** installs applications (Drive, Backup, Media Server, Surveillance Station, Docker containers via Container Manager). The **control panel** bundles users, groups, rights, services, security and task scheduling. The quick start guide leads through initial setup, shares and remote access (QuickConnect, reverse proxy, DDNS).

## Advantages

- **Mature and widely documented**: long-maintained interface, large community, official manuals
- **Package system**: storage, backup, media, virtualisation and monitoring applications installed with one click
- **Rights and services from one source**: users, groups, shares, logs, ACL, 2FA and IP blocking
- **Backup concept**: snapshot replication, Active Backup, hybrid backup, version control of shares
- **Own management API**: `SYNO.*` interface for automation, including `SYNO.FileStation.*` and `SYNO.Core.*`
- **Remote access included**: QuickConnect, reverse proxy wizard, VPN server
- **Close to hardware**: SMART checks, storage warnings, email/push notifications

## Differentiation from other systems

### Synology DSM vs. Homarr
- **DSM** is a complete NAS operating system, **Homarr** is a dashboard that only displays and operates
- **DSM** with its own rights management and packages, **Homarr** with board sharing and integrations
- **Both** are differently licensed, proprietary or open source: **DSM** proprietary, **Homarr** open source

### Synology DSM vs. Heimdall
- **Heimdall** collects tiles and statistics overlays, **DSM** provides the services itself
- **Heimdall** runs as a PHP application without system administration, **DSM** manages disks, shares and services
- **Heimdall** free, **DSM** only available on Synology hardware or licensed

### Synology DSM vs. Homer
- **Homer** is a static YAML page without sign-in and backend, **DSM** is a full system with accounts, logs and packages
- **Homer** shows links, **DSM** shows and controls storage, packages and tasks
- **Homer** can be hosted on any web server, **DSM** is tied to Synology devices

### Synology DSM vs. Dashy
- **Dashy** configures dashboards (`conf.yml`) and checks link status, **DSM** provides the monitored services itself
- **Dashy** with theme system and self-operation, **DSM** with control panel, maintenance and support
- **Dashy** can embed DSM as a tile via its API – the reverse is not intended

## Technical details

- **Backend**: proprietary DSM (Linux-based), web service `nginx`/own HTTP server with `entry.cgi` as API entry point
- **Database**: internal system database for accounts, packages and settings; not accessible to users as a classic database – packages use their own storage (e.g. MariaDB for web applications)
- **Frontend**: browser portal with window manager, app bar, main menu, desktop widgets; own clients for desktop and mobile
- **Authentication**: local accounts and groups, LDAP/AD domain, 2FA/OTP, trusted devices, session with timeout; ports **5000/5001** (HTTPS recommended), QuickConnect as relay service
- **Hosting**: on Synology hardware (DiskStation, RackStation); alternative platforms are not approved by the vendor; access via LAN, VPN or reverse proxy
- **Update model**: DSM updates via control panel/package centre, package lifecycle managed separately

## Who is Synology DSM suitable for?

- **Home and small office environments** that want central storage, shares and backup with little maintenance effort
- **Administrators who need rights, logs and log monitoring** and want to manage packages comfortably
- **Automators** who control jobs, shares and status from scripts via `entry.cgi`
- **Less suitable** as a pure overview dashboard (for that, Homarr/Homepage/Dashy) and for environments without Synology hardware
