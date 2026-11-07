# Proxmox VE - Description

## Overview

Proxmox VE (PVE, Proxmox Server Solutions) is a free virtualisation platform: a Debian Linux system with its own web desktop for KVM/QEMU virtual machines, LXC containers, storage and network management. Subscriptions (enterprise repository, support) fund development; the software itself is GPL-licensed and fully usable.

## What Proxmox VE does

Proxmox VE manages virtual machines and containers on every **node** and combines several nodes into a **cluster** (Corosync, shared configuration store pmxcfs). The web UI shows a resource tree on the left (datacenter → nodes → VMs/CTs) and tabs per object on the right: summary, hardware, options, console, monitor, backup, snapshots. In addition there is storage connectivity (LVM-thin, ZFS, CIFS, iSCSI, Ceph), networking (bridges, bonds, VLAN, SDN), firewall per VM/node/cluster, backups (vzdump, Proxmox Backup Server), replication and HA. A complete REST API covers every UI action.

## Advantages

- **Two virtualisation types**: full virtualisation (KVM) and containers (LXC) in one interface
- **Built-in clustering**: Corosync, HA manager, live migration, replication without additional products
- **Complete REST API**: practically every UI action can be automated (ticket or API token)
- **Breadth of storage**: local (LVM-thin, ZFS), over the network (CIFS, iSCSI, NFS) up to Ceph
- **Debian base**: familiar package management, standard tools, no proprietary file system dogma
- **Proxmox Backup Server**: dedicated, deduplicating backup system from the same vendor
- **No lock-in**: open formats (QCOW2, RAW), API, CLI (`pvesh`)

## Differentiation from other systems

### Proxmox VE vs. Unraid
- **Proxmox** is virtualisation first, storage as a means; **Unraid** is storage first with VM add-on
- **Proxmox** is strong in clustering and API; **Unraid** is a single server with GraphQL addition (version-dependent)
- **Unraid** mixes disks of any size with parity; **Proxmox** requires RAID/LVM/ZFS under the VM disks

### Proxmox VE vs. TrueNAS
- **TrueNAS** is a storage appliance (ZFS, shares, apps) with VM functionality on top; **Proxmox** is a hypervisor with storage connectivity
- **TrueNAS** REST/JSON-RPC API covers the UI, but without cluster components; **Proxmox** has cluster API, HA, live migration
- Whoever primarily shares files chooses TrueNAS; whoever operates VM landscapes chooses Proxmox

### Proxmox VE vs. Homarr/Heimdall
- **Homarr/Heimdall** are dashboards without their own operating service; **Proxmox** is the operated system itself
- Homarr/Heimdall can only display Proxmox (via API), not perform actions with cluster semantics
- Typical combination: Proxmox runs the VMs, the dashboard collects the links

## Technical details

- **Backend**: Debian Linux; daemons `pvedaemon` (API/web), `pveproxy`, `pve-cluster` (pmxcfs), `pve-manager`; QEMU/KVM and LXC
- **Database**: no SQL database — configuration in the cluster file system **pmxcfs** (SQLite-backed, replicated across all nodes); status/RRD in databases under `/var/lib`
- **Frontend**: web UI as a JS app (historically Sencha ExtJS, parts rewritten), consoles via xterm.js/noVNC (version-dependent)
- **Authentication**: realms `pam` (system), `pve` (own user store), LDAP/LDAP2, AD, Keycloak/OIDC (version-dependent); API tokens, 2FA (TOTP/recovery), roles/ACL
- **Hosting**: bare-metal installer or Debian retrofit; web UI HTTPS port 8006; SPICE/xterm consoles; subscription or free repository

## Who is Proxmox VE suitable for?

- **Homelab and small server operators** who want to separate many VMs/containers cleanly
- **Administrators with cluster ambitions**: HA, live migration, Ceph, backups from one source
- **Automators**: REST API, `pvesh`, Terraform/Ansible integrations
- **Less suitable** for pure NAS storage landscapes (TrueNAS/Unraid are more direct there) and for users without basic Linux knowledge
