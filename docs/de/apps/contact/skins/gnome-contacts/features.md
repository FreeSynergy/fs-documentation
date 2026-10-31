# GNOME Contacts - Funktionen

## Hauptfunktionen

### Kontakte
- vCard-Felder: Name, Telefon, E-Mail, Adresse, Geburtstag/Jubiläum, Notiz, Website, Beziehungen (Eltern, Kinder, Partner, Geschwister)
- Fotos (Drag&Drop), Favoriten via „Stern“ nicht vorhanden — stattdessen „häufige Kontakte“-Sortierung
- Karten verknüpfen/splitten (`Link contacts`, `Unlink`)

### Quellen über Evolution Data Server (EDS)
- Lokale Adressbücher („Persönlich“)
- GNOME-Online-Konten: Google-Kontakte, CalDAV/CardDAV (Nextcloud, Fastmail …)
- LDAP-Adressbücher (readonly)
- Offline-Persist + Re-Sync durch EDS

### Wartung
- Duplikaterkennung und -zusammenführung
- vCard-Import/-Export (einzeln und Stapel)
- Drucken (Adresslisten)

## Was GNOME Contacts NICHT kann

- **Keine Verteilerlisten** als eigene Karten (Anlegen/Verwalten von Mailinglisten)
- **Keine Tags/Kategorien** (nur Feldtypen und Beziehungen)
- **Kein CRM** (keine Aktivitäten — Monica)
- **Keine eigene Server-Komponente/API** (EDS ist client-seitig; Freigaben laufen über CardDAV-Server)
- **Keine Feldvorlagen/benutzerdefinierte Felder**

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| GNOME Shell | Kontakte/Suchergebnis in der Übersicht |
| GNOME Online Accounts | Konto → EDS-Quelle automatisch |
| Geary/Evolution Mail | Autocomplete aus EDS |
| `abook`/`khal` | nutzen dieselben EDS-Kataloge |
