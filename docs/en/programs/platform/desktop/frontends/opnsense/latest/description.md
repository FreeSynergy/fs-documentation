# OPNsense - Description

## Overview

OPNsense (Deciso B.V., fork of pfSense since 2015) is an open-source firewall/router platform on FreeBSD with a web UI that covers the entire system – from interface assignment to IDS. The Community Edition is free; the Business Edition (OPNsense Plus/Hardened builds, support) requires a subscription.

## What OPNsense does

OPNsense turns an x86 system (or Deciso hardware) into a fully functional router/firewall: **pf rules** with aliases, GeoIP and groups, **NAT** (port forward, outbound, 1:1, NPt), **VPN** (IPsec, OpenVPN, WireGuard), **services** (DHCP, Unbound DNS filter, Let's Encrypt …), **monitoring** (live view, Insight analytics) and **high availability** via CARP. The configuration is stored as an XML file, edited via menus and applied to the running rule set with "Apply". An MVC framework provides an API controller for every interface.

## Advantages

- **Regular, fast releases** with visible changelog and security focus
- **Consistent web UI** (modern design since 22.7) with search grids for large rule sets
- **Complete MVC REST API**: UI and API use the same controllers
- **Plugin ecosystem** (os- packages): WireGuard (at times), Acme, CrowdSec, Rspamd, Zabbix and more
- **Configuration as XML**: built-in backup/rollback, can be versioned
- **Freely usable**, with commercial support/additional features available alongside

## Differentiation from other systems

### OPNsense vs. pfSense
- **OPNsense** has a modern UI cycle, MVC API and faster feature releases; **pfSense** (Netgate) maintains its own packages/paths and the Plus edition
- Rules/aliases are conceptually similar, API and menu structures differ significantly
- The decision usually comes down to community closeness versus vendor lock-in – compare details version-specifically before switching

### OPNsense vs. Proxmox VE / TrueNAS
- **OPNsense** is network security first – not a VM/storage platform; Proxmox virtualises, TrueNAS stores
- All three have web UI + API, but only OPNsense continuously changes the packet flow (firewall, NAT, IDS)
- Typical setup: OPNsense as edge device, Proxmox/TrueNAS behind it on the network

### OPNsense vs. Homarr/Heimdall
- **Homarr/Heimdall** only show status/links; **OPNsense** makes the actual forwarding decisions
- Dashboards can at most display OPNsense values (API read-only), but cannot replace security
- Sensible combination: OPNsense controls, dashboard visualises (e.g. WireGuard peers)

## Technical details

- **Backend**: FreeBSD; `configd` (configuration daemon) executes actions; Phalcon/MVC framework (PHP) for UI and API
- **Database**: no SQL database – configuration as **XML file** (`config.xml`, versioned backup/history mechanism), runtime status in files/procfs
- **Frontend**: web UI since 22.7 based on Vue/Ant Design components (with transitions from Bootstrap), grid tables with `searchPhrase` pagination
- **Authentication**: local users + group rights, 2FA (QR), LDAP/RADIUS; **API access via API key/secret as Basic Auth** per user
- **Hosting**: bare metal/VM (CARP cluster for HA); web UI on 443 (HTTP→HTTPS), console menu with shell access; updates via UI/CLI `opnsense-update`

## Who is OPNsense suitable for?

- **Home and SMB networks** that want to operate firewall, VPN and DNS filtering themselves
- **Automators** who handle rule/alias maintenance via API (CI, threat feed scripts)
- **Compliance-aware operators** who need configuration history and support options
- **Less suitable** as a replacement for storage/virtualisation platforms – for those, TrueNAS/Proxmox are partners, not competitors
