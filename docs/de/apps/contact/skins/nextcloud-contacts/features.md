# Nextcloud Contacts - Funktionen

## Hauptfunktionen

### Kontaktverwaltung
- vCard-3.0-Felder: Namen, Telefon, E-Mail, Adressen, Organisationen, Geburtstag/Jahrestag, Notizen, Social-Media, Fotos
- Favoriten, „Kürzlich im Kontakt“, Pools für wiederverwendete Felder (Key-Value)
- Duplikaterkennung beim Import, zusammenführbar

### Adressbücher und Kreise
- Mehrere CardDAV-Adressbücher je Nutzer
- Freigaben an Benutzer/Gruppen/Kreise mit drei Rechtestufen
- „Gelbes Systemadressbuch“ (alle Nextcloud-Benutzer als Kontakte) — adminsteuerbar
- Kreise (Teams): geteilte Kontakte, Runden-Geburtstagskalender

### Synchronisation
- CardDAV (RFC 6352) mit Thunderbird, iOS, Android (DAVx⁵), GNOME
- Voll-/Delta-Sync über Sync-Token/COLLECTION-REPORT

### Import/Export
- `.vcf`-Import (Mehrfachdateien), vCard-Export einzelner/aller Kontakte
- Zusammenführung importierter mit vorhandenen Kontakten

## Was Nextcloud Contacts NICHT kann

- **Kein CRM** (keine Aktivitäten-Historie, keine Aufgaben-Beziehung zu Personen — dafür Monica/OCS-CRM)
- **Keine Feldvorlagen/Gruppen-Felder** über die Standard-vCard hinaus
- **Keine LDAP-Replikation** der persönlichen Kontakte ( LDAP wird nur für Konten/ „gelbes Buch“ gelesen)
- **Keine E-Mail-Verfolgung** (Öffnung/Klicks) und keine Double-Opt-in-Features
- **Keine eigene REST-Verwaltungs-API** für Kontakte — Weg ist CardDAV bzw. OCS für Freigaben

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Talk | „Nachrichten“-Button, Statusanzeige |
| Mail | Autocomplete aus den Kontakten, Bilder |
| Calendar | Geburtstagskalender „Persönliche Geburtstage“ (aus Kontakten generiert) |
| Circles/Teams | geteilte Adressbücher, Team-Favoriten |
| DAVx⁵/Thunderbird | CardDAV mit Privatsphäre-/Sync-Filtern |
| OCC-CLI | `occ contacts:add`, `occ user:resetpassword` etc. (Admin-Ebene) |
