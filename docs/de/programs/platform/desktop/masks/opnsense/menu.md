# OPNsense - Menüpunkte

## Übersicht

OPNsense führt über eine **Top-Menüleiste** (Dashboard-Symbol, Interfaces, Firewall, VPN, Services, System) und darunter eine linke Spalte mit Unterpunkten des gewählten Top-Menüs. Seit 22.7 heißen die Seiten „Pages“ mit **Grid-Tabellen** (Suche, Paginierung, `⋮`-Menüs) und Formulare mit **Save/Apply**-Trennung. Menüpunkte von Plugins tauchen in den passenden Top-Menüs auf. Die Punkt-Reihenfolge ist versionsabhängig.

## Hauptmenüs (Top-Leiste)

### 1. 🏠 Dashboard
- **Funktion**: Widget-Übersicht (System, Schnittstellen, Services, neuste Regeln u. a.)
- **Details**: Widgets per Widget-Menu (Zahnrad) an-/abschaltbar, Spaltenanzahl einstellbar

### 2. Interfaces
- **Funktion**: Physische/logische Netzseiten
- **Details**:
  - **Overview** (versionabhängig): Port-Status, MAC, Speed
  - **Assignments**: Interfaces an Ports/VLANs zuweisen
  - **Other Types**: VLANs, LAGGs, Bridges, GIFs, GRE
  - eigene Seiten je Interface (WAN, LAN, OPTx): IPv4/IPv6, DHCP-Client-Optionen, Traceroute-Gateway

### 3. Firewall
- **Funktion**: Paketfilter, NAT, Objekte
- **Details**:
  - **Rules**: Reiter Floating und je Interface; Add/Edit/Copy/Disable/Delete, Drag für Reihenfolge, „Apply Changes“
  - **NAT**: Port Forwarding, 1:1, Outbound, NPt (jeweils Grid + Dialog)
  - **Virtual IPs**: CARP, IP Alias, Proxy ARP
  - **Aliases / Groups / Categories**: Objekte verwalten, Feeds importieren, „Reset“/„Apply“ für Feeds
  - **Settings**: Firewall-Advanced (Defaults, Egress, FRAG-Optionen)
  - **Automation** (versionabhängig): Referenz-/Testoberfläche für die eigene Firewall-API

### 4. VPN
- **Funktion**: Tunnel und Peer-Verwaltung
- **Details**: IPsec (Tunnels, Mobile Clients), OpenVPN (Clients/Servers/Export, Legacy-Abschnitt), WireGuard (Instances, Local, Sessions, Live), Plugin-VPNs (ZeroTier, Tailscale …)

### 5. Services
- **Funktion**: Netzwerk- und Sicherheitsservices
- **Details**: DHCPv4/v6 (ISC oder Kea), DNS Filter (General, Advanced, Domain Overrides, Query Logs), Let's Encrypt, Proxy (Legacy), NUT, Rspamd, Suricata/Snort — Umfang plugin- und versionsabhängig

### 6. System
- **Funktion**: Gerätebasis, Rechte, Wartung
- **Details**:
  - **Access**: Users, Groups (Rechte/ACL), Password; API-Key-Erzeugung im Benutzerdialog
  - **Authentication**: Method (lokal/LDAP/RADIUS)
  - **Settings**: General, Logging, Notifications (Mail), Networking, Cron, Reboot, Firmware, Crash Dashboard, Tools (Config Restore)
  - **Trust**: Certificates, Authorities, Revocations (ACME-eingebunden)
  - **High Availability (CARP)**: Settings, Status, Virtual IP-Sync
  - **Diagnostics**: Commands, Ping, Traceroute, DNS Lookup, Smart, Services, Edit File, Interfaces (statistics), State Table, Reports (versionabhängig)

## Grid-Aktionen (Kontext)

- **Zeilen-Menü `⋮`**: Edit, Duplicate, Disable/Enable, Delete (je nach Seite)
- **Grid-Kopf**: Suche (`searchPhrase`), Spalten ein-/ausblenden, Seitenlänge, Sortierung
- **Dialog-Buttons**: Cancel / Save; bei Firewall-Seiten zusätzlich **Apply Changes** oben auf der Seite
- **Unsaved-Changes-Banner**: nach Edits der Hinweis, dass Änderungen erst nach Apply greifen

## Häufige Menüpfade (real)

- `Dashboard` → Widget-Zahnrad → Widgets ein-/ausblenden, Spalten anlegen
- `Interfaces ▸ Assignments` → WAN/LAN/OPTx an Ports oder VLANs zuweisen
- `Interfaces ▸ (WAN)` → IPv4/IPv6, DHCP-Client-Verhalten, Traceroute-Gateway
- `Firewall ▸ Rules: <Interface>` → Regel hinzufügen, verschieben, danach `Apply Changes`
- `Firewall ▸ NAT: Port Forward` → Weiterleitung mit „Add associated filter rule“
- `Firewall ▸ Aliases` → Alias anlegen, GeoIP-/URL-Feeds importieren
- `Firewall ▸ Virtual IPs` → CARP-Adressen mit Advertise-Intervallen
- `VPN ▸ WireGuard: Instances / Local / Sessions` → Tunnel und Peers prüfen
- `VPN ▸ OpenVPN: Clients / Servers / Export` → Profile erzeugen (versionabhängig)
- `Services: DHCPv4` oder `Services ▸ Kea` → Pools, Reservations (Provider versionabhängig)
- `Services ▸ Unbound DNS ▸ Query Log` → DNS-Verlauf als Grid
- `Services ▸ Let's Encrypt: Accounts / Certificates` → UI-Zertifikat automatisch erneuern
- `System ▸ Settings: General` → Hostname, DNS, TLS-Protokolle
- `System ▸ Access: Users` → Benutzerdialog → API-Key generieren
- `System ▸ Trust: Certificates / Authorities` → Zertifikatsverwaltung
- `System ▸ Firmware` → Versionszweig und Updates (versionabhängig)
- `System ▸ High Availability: Settings / Status` → CARP-Knoten, Config Sync
- `System ▸ Diagnostics: Commands / Services / States` → Wartung ohne SSH

## Benutzermenü oben rechts

- **Theme**: hell/dunkel umschalten (versionabhängig)
- **Abmelden**: Session beenden
- **Session-Info**: Anzeigename und Gruppe des angemeldeten Nutzers

## Kontext-Menüs zusätzlich

- **Dashboard-Widgets**: Zahnrad-Menü je Widget, Anordnung per Drag & Drop
- **Grid-Spaltenmenü**: Spalten ein-/ausblenden, Sortierung zurücksetzen
- **Plugin-Seiten**: eigene `⋮`- und Save/Apply-Muster nach demselben MVC-Schema

## Menüs nach Rolle

### Admin (Administratoren-Konto, volle Rechte)
- alle Menüs, System ▸ Access, Firmware, Diagnostics Commands

### Read-only-Benutzer
- Sichten ohne Save-Buttons (Gruppenrechte „GUI: system … read“), Diagnostics teils gesperrt

### Operators / technische Rollen (ACL)
- feingranular: z. B. Firewall-Regeln ja, System-Einstellungen nein — pro Ressourcen-ACL konfigurierbar

### API-Benutzer
- eigener Nutzer mit API-Key/Secret; sichtbare API-Endpunkte folgen denselben ACLs wie die GUI

## Shortcuts

Tastatursteuerung (Tabellen, Dialoge, Browser) ist in [shortcuts.md](shortcuts.md) beschrieben, inklusive der als nicht vorhanden markierten Kombinationen.
