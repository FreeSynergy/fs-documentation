# OPNsense - Funktionen

## Übersicht

OPNsense deckt die klassische Router-/Firewall-Rolle vollständig ab: **Paketfilter (pf)** mit Regeln und Aliases, **NAT**, **VPN**, **Netzwerkdienste**, **Monitoring** und **Hochverfügbarkeit**. Fast jede Funktion ist ein MVC-Modul mit eigener UI-Seite *und* API-Controllern; Plugins erweitern das Muster.

---

## 1. Firewall-Regeln (pf)

- **Regel-Grids** je Interface und Floating („Quick“), mit Suche, Spaltenfilter, Drag-Reihenfolge
- **Feldumfang**: Quick/Action (block/reject/pass), Protokoll, Quelle/Ziel (Alias-Referenz), Port, Gateway, Log, Beschreibung
- **Aliases**: Hosts, Netzwerke, Portbereiche, GeoIP, externe Feed-Aliases (URL-Import mit Parser, versionabhängig)
- **Gruppen** (rule groups) und **Kategorien** für Alias-Aufräumaktionen
- **Apply** übernimmt Änderungen in den laufenden Regelsatz; „discard changes“ verwirft

## 2. NAT und Adressübersetzung

- **Port Forward** (DNAT) mit Regelverknüpfung und Redirect-Modi
- **Outbound** (Modus Hybrid/Automatic/Deaktiviert) für Source-NAT, **1:1** und **NPt** (IPv6-Adressübersetzung)
- **Virtual IPs** (CARP, Proxy ARP, IPalias) als Grundlage für Failover- und Forwarding-Konzepte

## 3. Interfaces und Routing

- **Zuweisung** (WAN/LAN/OPTx an physische/VLAN-/LAGG-Ports), Interface-Optionen (MTU, MAC, DHCPv4/v6, Traceroute)
- **VLANs, LAGGs, Bridges, GIF/GRE**-Tunnel im Menü *Interfaces ▸ Other Types*
- **Gateways, Gateway-Gruppen, Policy Routing, Static Routes, Multi-WAN**-Lastenausgleich (Menü *Routing*, versionabhängig)

## 4. VPN

- **IPsec**: Tunnel/Transport, IKEv1/v2, Phasen-Editor, Mobile Clients (EAP)
- **OpenVPN**: moderne Server-/Client-Implementierung (Clients, Servers, Export) und Legacy-Abschnitt (versionabhängig)
- **WireGuard** (Core seit 23.1): Instanzen, Peers, Live-Session-Status
- Plugin-VPNs: ZeroTier, Tailscale, Netbird u. a.

## 5. Dienste

- **DHCPv4/v6**: klassischer ISC-DHCP (Legacy) oder **Kea**-Plugin (Empfehlung in neuen Versionen)
- **DNS Filter (Unbound)**: Forwarding, Blocklists, Domain Overrides, Query Logs
- **Let's Encrypt** (Plugin) für UI-Zertifikate, **NUT** (USV), **Cron**, **Syslog**, **SNMP**
- **IPS/IDS**: Suricata oder Snort (Plugin) mit Ruleset-Management
- **Proxy (Legacy)**, Rspamd, Relayd/HAProxy-Alternativen als Plugins (versionabhängig)

## 6. Monitoring und Diagnose

- **Live-Ansicht** (Live View) mit Paket-/State-Diagrammen, **Insight/Analytics** (Netflow-basiert, versionabhängig)
- **Diagnostics**: Commands, Ping, Traceroute, DNS Lookup, SMART, Services, Edit File, Interface Statistics
- **States/Tabelle**, Log-Dateien (Firewall, System, Services) mit Filter-Grids
- **Interface-Statistiken** und Throughput-Diagramme in den Interface-Seiten
- **Netdata/Collectd/Telegraf**-Exporte über Plugins

## 7. Hochverfügbarkeit und Backup

- **CARP** mit Virtual IPs, Advertisements, Preconditions; **Config Sync** zwischen Geräten (XML-basiert)
- **Konfigurations-Historie**, Backup/Download/Restore, Factory Defaults
- **Monit**-Plugin für Prozess-/Service-Neustarts und Alerts

## 8. System und Sicherheit

- **Zertifikate/ACME**: eigene CA, CSR, importierte und ACME-Zertifikate (Trust-Manager)
- **Zwei-Faktor-Auth** (QR-TOTP), Sitzungs-Timeout, Login-Banner
- **Auth-Quellen**: lokal, LDAP, RADIUS; Gruppen mit feingranularen Rechten (ACL-System)
- **Firmware-Updates** (major/minor-Pfade), Repositories (Community/Business, versionabhängig)
- **Process-/Service-Neustarts** über Diagnostics ▸ Services und das Monit-Plugin

## 9. Was OPNsense NICHT kann

- **Keine Webhooks**: weder eingehend noch ausgehend (Alerts laufen über Mail/Plugin-Transporte)
- **Keine Container/Apps**: kein Docker-Katalog wie TrueNAS/Unraid — Erweiterungen sind OS-Pakete
- **Keine VM-Verwaltung** und kein Storage-Management (dafür Proxmox/TrueNAS)
- **Zustandsloser API-Fluss**: Regeländerung wirkt erst nach `apply`-Äquivalent — kein atomares Transaktions-Rollback
- **Kein eingebauter Zertifikats-Scan/Automatik** über ACME hinaus ( externe Tools nötig)
- **Legacy-Dienste sterben aus** (ISC-DHCP, Web Proxy): Funktionen wandern zu Plugins/Kea — Version beachten

## 10. Erweiterungen

- **os-*-Plugins** aus den offiziellen Repos (Acme-Client, CrowdSec, Rspamd, WireGuard-alt, Kea, Zabbix-Agent, REST-artige eigene Controller)
- **Eigene MVC-Plugins**: Modell (XML), Controller, View — API-Endpunkte entstehen automatisch
- **Business Edition (OPNBEcore)**: Zusatz-Automation für Support-/Update-Prozesse
- **Integrationen**: Terraform-Provider (community), Python-Beispiele (requests), Dashboard-Clients, threat-Feed-Skripte gegen die Alias-API

---

## Vergleich mit den Nachbarsystemen

| Funktion | OPNsense | Proxmox VE | TrueNAS |
|----------|----------|------------|---------|
| Kernaufgabe | Firewall/Router/VPN | Virtualisierung | Speicher/Freigaben |
| API | MVC-REST `/api/...`, Basic Auth | REST `/api2/json`, Tokens | JSON-RPC v2.0, Bearer |
| Konfig-Historie | XML + History | pmxcfs, Snapshots | Konfig-Backups |
| HA | CARP + Config Sync | Corosync/HA-Manager | nur Enterprise (versionabhängig) |
| Erweiterungen | os-Plugins | Pakete + API | Apps/Trains |

---

## Siehe auch

- [menu.md](menu.md) - Menüpfade und Grid-Aktionen
- [structure.md](structure.md) - UI-Aufbau und Apply-Flows
- [api.md](api.md) - REST-API und API-Key-Setup
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
