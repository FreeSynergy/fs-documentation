# Proxmox VE Dokumentation

## Übersicht

Proxmox VE ist eine quelloffene Virtualisierungsplattform auf Debian-Basis: KVM-/QEMU-Virtualmaschinen und LXC-Container werden über eine gemeinsame Web-UI (Port 8006, HTTPS) betrieben — optional als Cluster mit Ceph, Replikation und Hochverfügbarkeit. Die vollständige Funktionsmenge ist über die REST-API (`/api2/json`) mit Ticket- oder Token-Authentifizierung erreichbar.

## Dateistruktur

- [menu.md](menu.md) - Ressourcenbaum, Datacenter-/Node-/VM-Menüs nach Rolle
- [features.md](features.md) - VMs, Container, Storage, Netzwerk, Backup, Cluster
- [description.md](description.md) - Beschreibung und Abgrenzung zu Unraid, TrueNAS, Homarr
- [structure.md](structure.md) - Drei-Spalten-Layout, Baum, Reiter, Konsolen
- [shortcuts.md](shortcuts.md) - Tastatursteuerung (und klar als fehlend markierte Shortcuts)
- [api.md](api.md) - REST `/api2/json`, Ticket + CSRF, API-Tokens, `pvesh`, `proxmoxer`
