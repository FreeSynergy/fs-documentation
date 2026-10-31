# OPNsense - Beschreibung

## Übersicht

OPNsense (Deciso B.V., Fork von pfSense seit 2015) ist eine quelloffene Firewall-/Router-Plattform auf FreeBSD mit einer Web-UI, die das gesamte System abdeckt — von der Interface-Zuweisung bis zur IDS. Die Community Edition ist frei; die Business Edition (OPNSense Plus/Hardened-Builds, Support) kostet Abo.

## Was OPNsense macht

OPNsense macht aus einem x86-System (oder der Deciso-Hardware) einen voll funktionsfähigen Router/Firewall: **pf-Regeln** mit Aliases, GeoIP und Gruppen, **NAT** (Port Forward, Outbound, 1:1, NPt), **VPN** (IPsec, OpenVPN, WireGuard), **Dienste** (DHCP, Unbound DNS-Filter, Let's Encrypt …), **Monitoring** (Live-Ansicht, Insight-Analytics) und **Hochverfügbarkeit** über CARP. Die Konfiguration liegt als XML-Datei, wird über Menüs editiert und per „Apply“ in die laufende Regelmenge übernommen. Ein MVC-Framework stellt für jede Oberfläche einen API-Controller bereit.

## Vorteile

- **Regelmäßige, schnelle Releases** mit sichtbarem Changelog und Security-Fokus
- **Konsistente Web-UI** (seit 22.7 modernes Design) mit Such grids für große Regelwerke
- **Vollständige MVC-REST-API**: UI und API nutzen dieselben Controller
- **Plugin-Ökosystem** (os- Pakete): WireGuard (zeitweise), Acme, CrowdSec, Rspamd, Zabbix u. v. m.
- **Konfiguration als XML**: Backup/Rollback eingebaut, versionierbar
- **Frei nutzbar** mit kommerziellem Support/Zusatzfunktionen daneben

## Abgrenzung zu anderen Systemen

### OPNsense vs. pfsense
- **OPNsense** hat einen modernen UI-Zyklus, MVC-API und schnellere Feature-Releases; **pfsense** (Netgate) pflegt eigene Pakete/Pfade und die Plus-Ausgabe
- Regeln/Aliases sind konzeptionell ähnlich, API und Menüstrukturen unterscheiden sich deutlich
- Die Entscheidung fällt meist über Community-Nähe versus Anbieterbindung — Details vor einem Umstieg versionsbezogen vergleichen

### OPNsense vs. Proxmox VE / TrueNAS
- **OPNsense** ist Netzwerk-Sicherheit zuerst — keine VM-/Storage-Plattform; Proxmox virtualisiert, TrueNAS speichert
- Alle drei haben Web-UI + API, aber nur OPNsense verändert fortlaufend den Paketfluss (Firewall, NAT, IDS)
- Typisches Setup: OPNsense als Randgerät, Proxmox/TrueNAS dahinter am Netz

### OPNsense vs. Homarr/Heimdall
- **Homarr/Heimdall** zeigen nur Status/Links; **OPNsense** trifft die eigentlichen Durchleitungentscheidungen
- Dashboards können OPNsense-Werte allenfalls anzeigen (API read-only), aber keine Sicherheit ersetzen
- Sinnvolle Kombination: OPNsense regelt, Dashboard visualisiert (z. B. WireGuard-Peers)

## Technische Details

- **Backend**: FreeBSD; `configd` (Konfigurations-Daemon) führt Aktionen aus; Phalcon-/MVC-Framework (PHP) für UI und API
- **Database**: keine SQL-DB — Konfiguration als **XML-Datei** (`config.xml`, versionierter Backup-/History-Mechanismus), Laufzeitstatus in Dateien/Proc-FS
- **Frontend**: Web-UI seit 22.7 auf Vue/Ant-Design-Komponenten (mit Übergängen aus Bootstrap), Grid-Tabellen mit `searchPhrase`-Paginierung
- **Authentication**: lokale Nutzer + Gruppenrechte, 2FA (QR), LDAP/RADIUS; **API-Zugang über API-Key/Secret als Basic Auth** pro Benutzer
- **Hosting**: Bare-Metal/VM (CARP-Verbund für HA); Web-UI auf 443 (HTTP→HTTPS), Konsolenmenü mit Shell-Zugang; Updates über UI/CLI `opnsense-update`

## Für wen ist OPNsense geeignet?

- **Heim- und SMB-Netzwerke**, die Firewall, VPN und DNS-Filtering selbst betreiben wollen
- **Automatisierer**, die Regel-/Alias-Pflege per API (CI, Threat-Feed-Skripte) erledigen
- **Compliance-bewusste Betreiber** mit Bedarf an Konfig-Historie und Support-Optionen
- **Weniger geeignet** als Ersatz für Storage-/Virtualisierungsplattformen — dafür sind TrueNAS/Proxmox die Partner, nicht die Konkurrenz
