# Homepage Dokumentation

## Übersicht

Homepage (Projekt `gethomepage/homepage`) ist ein statisches Dashboard für Homelabs: Dienste, Links und Live-Widgets werden aus YAML-Dateien unter `config/` gerendert. Die Anwendung läuft als Next.js-Container, bringt **keine Datenbank** mit und kennt **keine eigene Anmeldung** – Zugriffsschutz übernimmt der Reverse Proxy.

## Dateistruktur

- [menu.md](menu.md) - Bedien- und Konfigurationsbereiche (kein klassisches Anwendungsmenü)
- [features.md](features.md) - Widgets, Docker-/Kubernetes-Integration, Konfiguration
- [description.md](description.md) - Beschreibung und Abgrenzung zu Homer, Dashy und Homarr
- [structure.md](structure.md) - Seitenaufbau, Themes, Interaktionen, Performance
- [shortcuts.md](shortcuts.md) - Tastatursteuerung und klar als fehlend markierte Tasten
- [api.md](api.md) - interne `/api/...`-Proxy-Endpunkte und Widget-Datenquellen
- [gethomepage (Bibliothek)](../gethomepage/index.md) - Service-Client-Schicht hinter den Widgets
