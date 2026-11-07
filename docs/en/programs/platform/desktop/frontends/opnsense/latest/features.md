# OPNsense - Features

## Overview

OPNsense fully covers the classic router/firewall role: **packet filter (pf)** with rules and aliases, **NAT**, **VPN**, **network services**, **monitoring** and **high availability**. Almost every function is an MVC module with its own UI page *and* API controllers; plugins extend the pattern.

---

## 1. Firewall rules (pf)

- **Rule grids** per interface and floating ("Quick"), with search, column filters, drag ordering
- **Field scope**: Quick/Action (block/reject/pass), protocol, source/destination (alias reference), port, gateway, log, description
- **Aliases**: hosts, networks, port ranges, GeoIP, external feed aliases (URL import with parser, version-dependent)
- **Groups** (rule groups) and **categories** for alias clean-up actions
- **Apply** takes changes into the running rule set; "discard changes" discards them

## 2. NAT and address translation

- **Port forward** (DNAT) with rule linkage and redirect modes
- **Outbound** (mode hybrid/automatic/disabled) for source NAT, **1:1** and **NPt** (IPv6 address translation)
- **Virtual IPs** (CARP, proxy ARP, IP alias) as the basis for failover and forwarding concepts

## 3. Interfaces and routing

- **Assignment** (WAN/LAN/OPTx to physical/VLAN/LAGG ports), interface options (MTU, MAC, DHCPv4/v6, traceroute)
- **VLANs, LAGGs, bridges, GIF/GRE** tunnels in the menu *Interfaces ▸ Other Types*
- **Gateways, gateway groups, policy routing, static routes, multi-WAN** load balancing (menu *Routing*, version-dependent)

## 4. VPN

- **IPsec**: tunnel/transport, IKEv1/v2, phase editor, mobile clients (EAP)
- **OpenVPN**: modern server/client implementation (clients, servers, export) and legacy section (version-dependent)
- **WireGuard** (core since 23.1): instances, peers, live session status
- Plugin VPNs: ZeroTier, Tailscale, Netbird among others

## 5. Services

- **DHCPv4/v6**: classic ISC DHCP (legacy) or **Kea** plugin (recommended in new versions)
- **DNS filter (Unbound)**: forwarding, blocklists, domain overrides, query logs
- **Let's Encrypt** (plugin) for UI certificates, **NUT** (UPS), **cron**, **syslog**, **SNMP**
- **IPS/IDS**: Suricata or Snort (plugin) with ruleset management
- **Proxy (legacy)**, Rspamd, Relayd/HAProxy alternatives as plugins (version-dependent)

## 6. Monitoring and diagnostics

- **Live view** with packet/state charts, **Insight/Analytics** (NetFlow-based, version-dependent)
- **Diagnostics**: commands, ping, traceroute, DNS lookup, SMART, services, edit file, interface statistics
- **States/table**, log files (firewall, system, services) with filter grids
- **Interface statistics** and throughput charts on the interface pages
- **Netdata/Collectd/Telegraf** exports via plugins

## 7. High availability and backup

- **CARP** with virtual IPs, advertisements, preconditions; **config sync** between devices (XML-based)
- **Configuration history**, backup/download/restore, factory defaults
- **Monit** plugin for process/service restarts and alerts

## 8. System and security

- **Certificates/ACME**: own CA, CSR, imported and ACME certificates (trust manager)
- **Two-factor authentication** (QR-TOTP), session timeout, login banner
- **Authentication sources**: local, LDAP, RADIUS; groups with fine-grained rights (ACL system)
- **Firmware updates** (major/minor paths), repositories (community/business, version-dependent)
- **Process/service restarts** via Diagnostics ▸ Services and the Monit plugin

## 9. What OPNsense cannot do

- **No webhooks**: neither incoming nor outgoing (alerts run via mail/plugin transports)
- **No containers/apps**: no Docker catalogue like TrueNAS/Unraid – extensions are OS packages
- **No VM management** and no storage management (for that, Proxmox/TrueNAS)
- **Stateless API flow**: a rule change only takes effect after the equivalent of `apply` – no atomic transaction rollback
- **No built-in certificate scanning/automation** beyond ACME (external tools required)
- **Legacy services are being phased out** (ISC DHCP, web proxy): functions move to plugins/Kea – mind the version

## 10. Extensions

- **os-*-plugins** from the official repositories (ACME client, CrowdSec, Rspamd, WireGuard-legacy, Kea, Zabbix agent, REST-like custom controllers)
- **Own MVC plugins**: model (XML), controller, view – API endpoints are created automatically
- **Business Edition (OPNBEcore)**: additional automation for support/update processes
- **Integrations**: Terraform provider (community), Python examples (requests), dashboard clients, threat feed scripts against the alias API

---

## Comparison with neighbouring systems

| Feature | OPNsense | Proxmox VE | TrueNAS |
|----------|----------|------------|---------|
| Core task | Firewall/router/VPN | Virtualisation | Storage/shares |
| API | MVC-REST `/api/...`, Basic Auth | REST `/api2/json`, tokens | JSON-RPC v2.0, Bearer |
| Configuration history | XML + history | pmxcfs, snapshots | configuration backups |
| HA | CARP + config sync | Corosync/HA manager | enterprise only (version-dependent) |
| Extensions | os plugins | packages + API | apps/trains |

---

## See also

- [menu.md](menus.md) - Menu paths and grid actions
- [structure.md](layout.md) - UI structure and apply flows
- [api.md](api.md) - REST API and API key setup
- [shortcuts.md](shortcuts.md) - Keyboard operation
