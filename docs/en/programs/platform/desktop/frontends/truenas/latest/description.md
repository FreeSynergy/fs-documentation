# TrueNAS - Description

## Overview

TrueNAS is the most widely used open-source storage platform worldwide (Community Edition free of charge, enterprise appliances with support). Its core is **ZFS management in a web interface**: pools, datasets, snapshots, replication and permissions. **TrueNAS CORE** runs on FreeBSD and is designed for storage; **TrueNAS SCALE** (current, versions named by year such as 24.10, 25.04) runs on Linux and brings Docker apps and KVM virtualisation.

## What TrueNAS does

The middleware (`middlewared`) connects web interface, CLI and API with the system: pools are created via a wizard, datasets are managed as a tree with properties (compression, quota, ACL, encryption). Shares (SMB, NFS, iSCSI, FTP, S3/bucket, WebShare depending on version) sit on datasets; periodic snapshots, replication tasks and cloud sync form data protection. The app catalogues install Docker containers, and from 24.10 also virtual machines. Rights come from local users/groups, ACLs and Active Directory/LDAP; API keys and 2FA belong to the sign-in layer.

## Advantages

- **ZFS first-class**: snapshots, replication, integrity checks, encryption from one source
- **Clear data hierarchy**: pools → datasets → shares, traceable and scriptable
- **Open source**: Community Edition complete, updates free of charge (enterprise optional)
- **Built-in data protection components**: snapshot tasks, replication, cloud sync, scrub, alerts
- **API + CLI with full coverage**: JSON-RPC v2.0, `midclaw call`, official Python client package
- **Apps and VMs** (SCALE): platform for the entire homelab/small server stack

## Differentiation from other systems

### TrueNAS vs. Unraid
- **TrueNAS** uses ZFS with fixed RAID topologies (RAIDZ etc.); **Unraid** mixes single disks with parity protection and is more flexible when expanding
- **TrueNAS** is open source with a complete API; **Unraid** is proprietary with a GraphQL addition (version-dependent)
- **Unraid** appears more mature in its app store (CA); **TrueNAS** excels in snapshots, replication and depth of ACLs

### TrueNAS vs. Proxmox VE
- **TrueNAS** is a storage appliance with VM/container extras; **Proxmox VE** is a hypervisor with storage connectivity
- **Proxmox** can do cluster, HA, live migration; **TrueNAS** is focused on one storage host (HA only in enterprise solutions)
- Common combination pattern: Proxmox VMs with TrueNAS iSCSI/NFS as storage

### TrueNAS vs. Synology DSM
- **DSM** is proprietary appliance software with its own package ecosystem and `SYNO.*` API; **TrueNAS** is open with a JSON-RPC API
- **DSM** shines with multimedia/mobile apps, **TrueNAS** with ZFS data protection and enterprise storage
- Both offer desktop-like web interfaces; TrueNAS remains storage-centred, DSM is broader in scope

## Technical details

- **Backend**: middleware process `middlewared` (Python); CORE on FreeBSD, SCALE on Debian Linux; ZFS in the kernel
- **Database**: middleware configuration in an SQLite file in the system pool; no external database required
- **Frontend**: Angular SPA with NG-ZORRO components, live status via WebSocket
- **Authentication**: local users (password/2FA), Active Directory, LDAP; API keys (user-specific), roles/privileges (version-dependent)
- **Hosting**: bare metal or VM; web UI port 80/443 (HTTP→HTTPS redirect), SSH/console menu; updates via UI/console menu

## Who is TrueNAS suitable for?

- **Storage-first environments**: data backup, media archives, virtualisation storage (NFS/iSCSI)
- **Administrators with data protection requirements**: snapshot plans, replication, scrub intervals
- **SCALE users** who want to run apps and a few VMs alongside the NAS
- **Less suitable** for large VM clusters (Proxmox) or for mixed-disk tinkerers without a ZFS plan (Unraid)
