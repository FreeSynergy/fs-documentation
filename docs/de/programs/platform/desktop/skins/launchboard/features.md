# LaunchBoard - Funktionen

## Übersicht

LaunchBoard kombiniert vier Bausteine: **Boards** (Layouts), **Widgets** (Kacheln aus einer Bibliothek), **Integrationen** (Dienstzugang samt Schlüssel) und **Verwaltung** (Nutzer, Rollen, Single-Sign-On, Lizenzen). Alles wird zur Laufzeit über die Oberfläche geändert und in der mitgelieferten Datenbank gespeichert.

---

## 1. Boards und Layouts

- **Beliebig viele Boards** pro Instanz: „Homelab“, „Medien“, „Team“, „Mobil“
- **Drag-&-Drop-Raster** mit einstellbarer Spaltenzahl, Zeilenhöhen und Abständen
- **Kacheln verschieben und skalieren** über Greifpunkte, Einrasten am Raster, Ausrichtungshilfen
- **Getrennte layouts** für Desktop und Mobil (eigene Anordnung pro Endgerät)
- **Vorlagen**: fertige Boards (Medienserver, Netzwerk, Serverraum) als Startpunkt
- **Duplizieren, umbenennen, Archivieren, Löschen** sowie Startboard je Rolle einstellbar

## 2. Widget-Bibliothek

### Struktur-Widgets
- **App-Kachel**: Name, URL, Icon, Zielfenster, optionale Sekundärlinks
- **Linkliste, Textblock, Bild, Trenner, Einbettung (iframe)**
- **Ordner-/Tab-Widget** für mehrere Links in einer Kachel

### Status- und Mess-Widgets
- **Erreichbarkeits-Ampel** (HTTP-Status, Antwortzeit) mit Intervall
- **Container-Status** (laufend, gestoppt, gesund) über die Docker-Integration
- **Systemwerte** (CPU, RAM, Datenträger) für Host und Container
- **Diagramme** für Traffic und Auslastung, bezogen auf hinterlegte Integrationen

### Integrations-Widgets (Auszug)
- **Docker / Portainer**: Containerliste mit Aktionen (Stopp, Start, Neustart)
- **Medienstack**: Jellyfin/Plex/Emby (aktive Streams), Sonarr/Radarr/Prowlarr (Queue, offene Anfragen)
- **Downloads**: qBittorrent, SABnzbd, Transmission (Tempo, Warteschlange)
- **Netzwerk**: UniFi, OPNsense/pfSense (Clients, Throughput), Pi-hole/AdGuard (Blockstatistik)
- **Storage**: NFS/SMB-Freigaben, Belegung, SMART-Werte (je nach Anbieterintegration)
- **Kalender, RSS/Feed, Wetter, Notizen, Uhr** für Informationskacheln

### Eigene Inhalte
- **HTTP/JSON-Widget**: URL, Methode, Header, JSON-Pfad → Werte aus beliebiger Schnittstelle
- **Markdown-/Notizkachel** mit begrenzter Formatierung
- **Import/Export einer Widget-Definition** als JSON für Wiederholung und Austausch

## 3. Integrationen und Aktionen

- **Integration anlegen**: Typ wählen, interne/externe URL, Schlüssel oder Benutzername/Passwort
- **Verbindungstest** im Dialog mit Fehlerbeschreibung
- **Mehrere Instanzen** desselben Typs, Widgets wählen die gewünschte aus
- **Aktionen** aus der Kachel: Container-Neustart, Download pausieren, Anfrage freigeben (unterstützte Typen)
- **Schlüssel verschlüsselt** in der Datenbank abgelegt; Zugriff über den Server, nicht über den Browser
- **Zertifikate**: eigene Root-Zertifikate hinterlegen, um interne HTTPS-Dienste zu erreichen

## 4. Authentifizierung, Rollen und Freigaben

- **Lokale Konten** mit Passwort, Registrierung abschaltbar, Einladungsverfahren
- **OAuth2/OIDC**: Authentik, Keycloak, Entra ID, Google, Generic-OIDC (Issuer, Client-ID, Secret, Scopes)
- **Header-Authentifizierung** hinter vertrauenswürdigem Reverse Proxy (optional)
- **Rollen**: Administrator, Editor (darf Boards ändern), Betrachter (nur lesen)
- **Board-Freigaben**: öffentlich, nur eigene, auf Personen/Gruppen beschränkt
- **Sitzungseinstellungen**: Timeout, Mehrfachanmeldung, optionale Zwei-Faktor-Authentifizierung (Anbieterumfang je Tarif)

## 5. Design und Themes

- **Hell, dunkel und Systemeinstellung** pro Konto
- **Akzentfarbe, Kartenstil, Eckenradius, Blur, Deckkraft**
- **Hintergrundbilder** (Upload oder URL) pro Board
- **Icon-Bibliotheken** und eigener Icon-Upload
- **Custom-CSS-Feld** im Theme-Editor (Umfang/Verfügbarkeit je Lizenz **nicht öffentlich dokumentiert**)

## 6. Konfiguration und Betrieb

- **Ohne Config-Datei** für Inhalte; Boards, Widgets und Nutzer liegen in der Datenbank
- **Umgebungsvariablen für den Start** (Container-Variante): Port, Datenbankpfad, Sitzungs-/Verschlüsselungssecret, OIDC-Parameter, Lizenzschlüssel
- **Datenpersistenz**: Volume für Datenbank und Uploads sichern; Secret stabil halten, sonst sind gespeicherte Schlüssel unlesbar
- **Updates** über Container-Images oder automatisch bei der Cloud-Variante
- **Backups**: Datenbank-Export aus der Oberfläche plus Volume-Sicherung empfohlen

## 7. Was LaunchBoard NICHT kann

- **Keine Konfiguration als Datei**: Boards lassen sich nicht als YAML/JSON unter Versionskontrolle stellen (nur Widget-Export)
- **Kein offener Quellcode**: keine Nachbauten, kein Fork, keine eigenen Widget-Programmierungen im Produkt
- **Keine frei einsehbare API-Referenz**: Integrationen stützen sich auf die Kundenportal-Doku
- **Kein Monitoring-Ersatz**: Messwerte sind Momentaufnahmen, keine Langzeitkurven mit Alarmen (Monitoring-Paket bzw. Zusatzmodul je Tarif)
- **Kein Offline-Betrieb**: ohne Server und Anmeldung keine Anzeige
- **Kein Reverse-Proxy-Ersatz**: kein Routing, keine Zertifikatsverwaltung
- **Keine Mandantenfähigkeit**: Instanz = eine Gemeinschaft, kein Mehrkundenbetrieb
- **Kein freies Plugin-System**: neue Widget-Typen liefert der Anbieter

## 8. Erweiterungen und Integrationen

- **HTTP/JSON-Widget** als offizieller Weg zu eigenen Datenquellen
- **Webhooks** (Umfang je Tarif): Ereignisse aus dem Dashboard an externe Systeme melden; Details in [api.md](api.md)
- **OIDC als Brücke**: bestehende Identitäten aus Authentik/Keycloak/Entra ID ohne zweite Kontenlandschaft
- **REST-Schnittstelle** für Automatisierung (Boards, Widgets, Integrationen) – Schema in [api.md](api.md)
- **Support und Roadmap**: Funktionen werden über den Anbieter beigesteuert; Kunden können anfragen
- **Aufenthalt der Daten**: bei Cloud-Nutzung Speicherort und Auftragsverarbeitung vertraglich geregelt (Details im Kundenportal)

---

## Vergleich mit den anderen Dashboard-Typen

| Funktion | LaunchBoard | Homarr | Heimdall | Homer | Dashy |
|----------|-------------|--------|----------|-------|-------|
| Lizenz | proprietär, Abo | open source | open source | open source | open source |
| Konfiguration | Drag & Drop | Weboberfläche | Weboberfläche + `.env` | `config.yml` | `conf.yml` |
| Datenbank | ja | SQLite | ja | nein | optional |
| Rollen/Freigaben | ja (Admin/Editor/Betrachter) | ja | eingeschränkt | nein | ja |
| OAuth/OIDC | Kernfunktion | ja | nein | nein | eingeschränkt |
| Aktionen | teils | ja | eingeschränkt | nein | eingeschränkt |
| Support | kommerziell | Community | Community | Community | Community |

---

## Siehe auch

- [menu.md](menu.md) - Menüpunkte und Bedienebenen
- [structure.md](structure.md) - Editor-Oberfläche und Panels
- [api.md](api.md) - Schnittstellen, OIDC und Webhooks
- [../homarr/index.md](../homarr/index.md) - die quelloffene Alternative mit Mauskonfiguration
