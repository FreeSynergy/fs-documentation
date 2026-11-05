# gethomepage (Bibliothek) Dokumentation

## Übersicht

`gethomepage` bezeichnet die **API-Bibliotheksschicht** des Projekts `gethomepage/homepage`: die Service-Clients, Proxy-Handler, Konfigurationsleser und Hilfsfunktionen, die aus den YAML-Angaben der `services.yaml` tatsächliche HTTP-Aufrufe an Sonarr, Pi-hole, Proxmox, Docker oder Kubernetes machen. Die Bibliothek besitzt **keine eigene Oberfläche** – Bedienung und Konfiguration laufen über das Dashboard.

## Dateistruktur

- [menu.md](latest/menus.md) - Modul- und Paketverzeichnis der Bibliothek (kein UI-Menü)
- [features.md](latest/features.md) - Client-Funktionen, Handler-Typen, Validierung, Caching
- [description.md](latest/description.md) - Zweck und Abgrenzung zur Dashboard-Anwendung
- [structure.md](latest/layout.md) - Bibliotheksstruktur, Ebenen und Aufrufpfad
- [shortcuts.md](latest/shortcuts.md) - Build-, Dev- und CLI-Kommandos statt Tastenkürzel
- [api.md](latest/api.md) - Bibliotheks-API: Clients je Dienst, Methoden, Parameter

- [Homepage (Dashboard)](../homepage/index.md) - Anwendung, die diese Bibliothek verwendet
