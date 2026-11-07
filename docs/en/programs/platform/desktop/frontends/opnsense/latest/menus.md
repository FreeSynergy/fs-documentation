# OPNsense - Menu items

## Overview

OPNsense works with a **top menu bar** (dashboard icon, Interfaces, Firewall, VPN, Services, System) and below it a left column with sub-items of the selected top menu. Since 22.7, the pages are called "Pages" with **grid tables** (search, pagination, `⋮` menus) and forms with a **Save/Apply** separation. Menu items from plugins appear in the matching top menus. The order of items depends on the version.

## Main menus (top bar)

### 1. 🏠 Dashboard
- **Function**: widget overview (system, interfaces, services, newest rules, among others)
- **Details**: widgets can be switched on/off via the widget menu (cog); number of columns adjustable

### 2. Interfaces
- **Function**: physical/logical network segments
- **Details**:
  - **Overview** (version-dependent): port status, MAC, speed
  - **Assignments**: assign interfaces to ports/VLANs
  - **Other Types**: VLANs, LAGGs, bridges, GIFs, GRE
  - own pages per interface (WAN, LAN, OPTx): IPv4/IPv6, DHCP client options, traceroute gateway

### 3. Firewall
- **Function**: packet filter, NAT, objects
- **Details**:
  - **Rules**: Floating tab and one per interface; Add/Edit/Copy/Disable/Delete, drag for order, "Apply Changes"
  - **NAT**: port forwarding, 1:1, outbound, NPt (each grid + dialogue)
  - **Virtual IPs**: CARP, IP alias, proxy ARP
  - **Aliases / Groups / Categories**: manage objects, import feeds, "Reset"/"Apply" for feeds
  - **Settings**: firewall advanced (defaults, egress, FRAG options)
  - **Automation** (version-dependent): reference/test interface for the firewall's own API

### 4. VPN
- **Function**: tunnel and peer management
- **Details**: IPsec (tunnels, mobile clients), OpenVPN (clients/servers/export, legacy section), WireGuard (instances, local, sessions, live), plugin VPNs (ZeroTier, Tailscale …)

### 5. Services
- **Function**: network and security services
- **Details**: DHCPv4/v6 (ISC or Kea), DNS filter (general, advanced, domain overrides, query logs), Let's Encrypt, proxy (legacy), NUT, Rspamd, Suricata/Snort – scope depends on plugins and version

### 6. System
- **Function**: device base, rights, maintenance
- **Details**:
  - **Access**: users, groups (rights/ACL), password; API key generation in the user dialogue
  - **Authentication**: method (local/LDAP/RADIUS)
  - **Settings**: general, logging, notifications (mail), networking, cron, reboot, firmware, crash dashboard, tools (config restore)
  - **Trust**: certificates, authorities, revocations (ACME-integrated)
  - **High Availability (CARP)**: settings, status, virtual IP sync
  - **Diagnostics**: commands, ping, traceroute, DNS lookup, SMART, services, edit file, interfaces (statistics), state table, reports (version-dependent)

## Grid actions (context)

- **Row menu `⋮`**: Edit, Duplicate, Disable/Enable, Delete (depending on the page)
- **Grid header**: search (`searchPhrase`), show/hide columns, page length, sorting
- **Dialogue buttons**: Cancel / Save; on firewall pages additionally **Apply Changes** at the top of the page
- **Unsaved changes banner**: after edits, a note that changes only take effect after Apply

## Common menu paths (real)

- `Dashboard` → widget cog → show/hide widgets, create columns
- `Interfaces ▸ Assignments` → assign WAN/LAN/OPTx to ports or VLANs
- `Interfaces ▸ (WAN)` → IPv4/IPv6, DHCP client behaviour, traceroute gateway
- `Firewall ▸ Rules: <Interface>` → add or move a rule, then `Apply Changes`
- `Firewall ▸ NAT: Port Forward` → forwarding with "Add associated filter rule"
- `Firewall ▸ Aliases` → create alias, import GeoIP/URL feeds
- `Firewall ▸ Virtual IPs` → CARP addresses with advertisement intervals
- `VPN ▸ WireGuard: Instances / Local / Sessions` → check tunnels and peers
- `VPN ▸ OpenVPN: Clients / Servers / Export` → generate profiles (version-dependent)
- `Services: DHCPv4` or `Services ▸ Kea` → pools, reservations (provider version-dependent)
- `Services ▸ Unbound DNS ▸ Query Log` → DNS history as a grid
- `Services ▸ Let's Encrypt: Accounts / Certificates` → automatically renew UI certificate
- `System ▸ Settings: General` → hostname, DNS, TLS protocols
- `System ▸ Access: Users` → user dialogue → generate API key
- `System ▸ Trust: Certificates / Authorities` → certificate management
- `System ▸ Firmware` → version branch and updates (version-dependent)
- `System ▸ High Availability: Settings / Status` → CARP nodes, config sync
- `System ▸ Diagnostics: Commands / Services / States` → maintenance without SSH

## User menu (top right)

- **Theme**: switch light/dark (version-dependent)
- **Sign out**: end session
- **Session info**: display name and group of the signed-in user

## Additional context menus

- **Dashboard widgets**: cog menu per widget, arrangement via drag and drop
- **Grid column menu**: show/hide columns, reset sorting
- **Plugin pages**: own `⋮` and Save/Apply patterns following the same MVC scheme

## Menus by role

### Admin (administrator account, full rights)
- all menus, System ▸ Access, Firmware, Diagnostics Commands

### Read-only user
- views without Save buttons (group rights "GUI: system … read"), Diagnostics partly blocked

### Operators / technical roles (ACL)
- fine-grained: e.g. firewall rules yes, system settings no – configurable per resource ACL

### API user
- own user with API key/secret; visible API endpoints follow the same ACLs as the GUI

## Shortcuts

Keyboard operation (tables, dialogues, browser) is described in [shortcuts.md](shortcuts.md), including the combinations marked as not available.
