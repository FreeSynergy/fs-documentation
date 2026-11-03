# OPNsense Dokumentation

## Übersicht

OPNsense ist eine Firewall- und Router-Distribution (FreeBSD-basiert, Deciso) mit vollständiger Web-UI: Interfaces, Firewall-Regeln (pf), NAT, VPN, Dienste und Plugins werden über Menüs konfiguriert, Änderungen mit „Apply“ aktiviert. Jede UI-Funktion folgt einem MVC-Muster und ist über die REST-API unter `/api/<modul>/<controller>/<methode>` mit API-Key (Basic Auth) ansprechbar.

## Dateistruktur

- [menu.md](menu.md) - Menüpfade (Firewall → Rules, VPN, Services, System …) nach Rolle
- [features.md](features.md) - Firewall, VPN, Dienste, HA, Monitoring, Plugins
- [description.md](description.md) - Beschreibung und Abgrenzung zu Proxmox, TrueNAS, pfsense
- [structure.md](structure.md) - Top-Menü, Grids, Dialoge, Apply-Flows
- [shortcuts.md](shortcuts.md) - Tastatursteuerung (und klar als fehlend markierte Shortcuts)
- [api.md](api.md) - MVC-REST-API, API-Key Basic Auth, `curl`-Beispiele
