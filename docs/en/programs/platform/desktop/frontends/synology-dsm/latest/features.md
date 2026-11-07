# Synology DSM - Features

## Overview

DSM is divided into four feature areas: **storage and data services**, **users and rights**, **packages and applications**, and **security, backup and monitoring**. The desktop portal is the common interface; every feature belongs to a package or to the control panel.

---

## 1. Storage and volumes

- **Storage pools** from HDD/SSD with RAID types (SHR, SHR-2, RAID 0/1/5/6/10)
- **Volumes** with file system Btrfs or ext4, pool expansion and cache acceleration (SSD cache)
- **Storage manager** as the central application: drive health, SMART tests, volume capacity, storage warnings
- **Btrfs functions**: data integrity checking, snapshot schedules, quotas, data optimisation
- **Drive hot-plug**, hybrid setup of volume and virtual storage (Virtual Machine Manager)
- **System Pulse / desktop widgets**: CPU, RAM, network, volume and temperature values directly on the desktop area

## 2. Shares and data services

- **Shared folders** with rights assignment, recycle bin, encrypted shares and data compression
- **Protocols**: SMB/CIFS, NFS, AFP, FTP/SFTP, WebDAV, iSCSI/LUN
- **File transfer** in the browser via **File Station**: preview, rename, copy/move, compress, upload and download with task list
- **Team folders and files with version control** (Synology Drive), share links with expiry and password
- **Media processing**: media indexing, transcoding, web access (Media Server, Video Station, Audio Station)
- **Universal Search** as indexed search across shares and package content

## 3. Users, groups and rights

- **Local accounts** with password policies, expiry, sign-in attempts and 2FA (TOTP)
- **Groups** with primary group, rights inheritance and quota
- **Domain connection**: LDAP and Windows AD, single sign-on for shares
- **Package rights**: per application a group/person may use or manage it
- **Guest account** and **application group** for service accounts
- **Protection of the admin account** (renaming, password history, mandatory 2FA) and **account protection** with IP block after failed sign-ins
- **Logs**: sign-in, share access, administration, connection (connection tool)

## 4. Packages and applications

- **Package centre**: catalogue, automatic updates, forced updates, manual installation of `.spk` packages, third-party package sources
- **Important packages**: Synology Drive Server, Snapshot Replication, Active Backup for Business, Universal Search, Media Server, Video/Audio Station, Mail Server/Plus, Chat, Directory Server, VPN Server, Web Station, Database Server, Virtual Machine Manager, Container Manager (Docker/OCI)
- **Package management**: start/stop, autostart, resource display, uninstallation with check for leftover data
- **Task scheduler**: schedules, Bash/PowerShell scripts, event-triggered tasks
- **Quick start (QuickStart)**: guided initial setup and short task instructions directly in the portal

## 5. Backup and restore

- **Snapshot Replication**: schedule-driven snapshots, replication to a second NAS, directory replication
- **Active Backup for Business**: backup of PCs, servers, VMs and mobile devices
- **Data backup** (formerly Hyper Backup): backup of shares and configuration to local targets, NFS, WebDAV, S3, Synology C2
- **Read-only versions** and encryption for backup targets
- **System configuration backup** via the control panel, restore after update

## 6. Network, remote access and services

- **Interface management** with link aggregation, VLAN, DNS, static routes
- **QuickConnect**: connected access without public addresses, with its own port management
- **Reverse proxy wizard**: forwarding rules, certificates (Let's Encrypt), HTTP/2
- **Firewall** per profile, geo-IP blocklists, auto-block, DoS protection
- **VPN server** (OpenVPN, WS, PPTP/L2TP), VPN client
- **DSM ports**: default **5000/5001**, further ports per package; switching and redirect in the control panel

## 7. Monitoring and notification

- **Resource monitor**: utilisation, processes, services, network, storage with history charts
- **Log centre**: event logs, Windows log consolidation, syslog reception
- **Notifications**: email, Synology notification (push), SMS (provider-dependent), notification bell in the portal
- **Storage warnings**: SMART, bad blocks, volume approaching capacity limit, RAID consistency
- **Privacy/security checks**: security advisor, security check, security guard (malware scan)

## 8. What DSM cannot do

- **No open operating system extension**: DSM officially runs only on Synology hardware; packages are signed
- **No public plugin system** for the desktop portal: custom interfaces are not intended
- **No freely accessible API design**: `SYNO.*` is documented in package developer manuals, but not promised as a stable, versioned product API
- **No monitoring stack such as Prometheus/Grafana**: histories are local and limited, alerting is basic
- **No multi-tenancy in the dashboard sense**: one system, one account landscape
- **No arbitrarily deep automation of the interface**: packages with their own logic (e.g. Drive, Surveillance) have their own, partly undocumented endpoints
- **No replacement for a dashboard portal**: links to third-party services are possible, but without a widget editor like Homarr or Dashy

## 9. Extensions and integrations

- **Package development**: `.spk` packages with their own web UI and own API (Synology developer manual)
- **Web Station** runs PHP/Node applications that can access DSM functions via `entry.cgi`
- **Container Manager** integrates Docker/OCI containers; ports appear in the portal under Windows/Ports
- **API calls from scripts**: Bash, PowerShell, Python, Go – details see [api.md](api.md)
- **Third-party integrations**: Home Assistant and monitoring scripts regularly use `SYNO.Core.System.Utilization`
- **Homepage/Dashy connection**: the Homepage library has its own DSM handler, see [../gethomepage/features.md](../../gethomepage/latest/features.md)

---

## Comparison with other systems

| Feature | Synology DSM | Homarr | Heimdall | Dashy |
|----------|--------------|--------|----------|-------|
| Purpose | NAS operating system | Dashboard | Dashboard | Dashboard |
| Own packages/apps | yes | no | no | no |
| Accounts and ACL | yes (system level) | board sharing | simple | roles |
| API | `entry.cgi`, `SYNO.*` | tRPC | Laravel endpoints | REST (optional) |
| Updates | vendor | container image | Composer/image | image |
| Cost | hardware + proprietary | free | free | free |

---

## See also

- [menu.md](menus.md) - Menu items by role
- [structure.md](layout.md) - Desktop portal, windows and widgets
- [api.md](api.md) - Authentication, session and endpoints
- [shortcuts.md](shortcuts.md) - Keyboard operation
