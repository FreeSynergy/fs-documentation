# KAddressBook - Funktionen

## Hauptfunktionen

### Kontakte und Ordner
- vCard 3.0/4.0 mit allen KDE-Feldtypen (Telefone, E-Mail, Adressen, Geburtstage, Organisationen, Bilder)
- Mehrere Adressbuch-Quellen parallel: lokale Ordner (Akonadi), CardDAV, IMAP, LDAP, Akonadi-Network-Contacts
- Verteilerlisten (als vCard-Gruppen), Schnellauswahl-Leiste, favorisierte Kontakte

### Bearbeitung
- Vollwertiger Detail-Editor mit Reitern (Allgemein, Adressen, Beziehungen, Notizen)
- Massenbearbeitung (Zuweisen von Kategorien/Löschmarken)
- Duplikatsprüfung über „Similarity“-Assistenten

### Ein- und Ausgabe
- Import-/Export-Assistent: vCard, LDIF, CSV/TSV, GMX, WebDAV
- Visitenkarten-/Label-Druck (Layouts, VCard-Renderer)
- QR-Visitenkarten (neuere Versionen, `kabc-export`-Helfer)

### Integration
- Geburtstags-/Jahreskalender im KDE-PIM-Kalender aus Kontakten
- Autocomplete in KMail/Kontact; Adressbuch-Fenster in KMail ist KAddressBook

## Was KAddressBook NICHT kann

- **Kein Server**: Kontakte liegen in Akonadi-Datenbanken bzw. Ressourcen — kein eigener Netzwerkendpunkt
- **Kein CRM** (keine Aktivitäten, keine Beziehungen über Personen hinaus — Monica)
- **Keine Web-/Mobil-Oberfläche** (nur Desktop; mobile KDE-Geräte über Plasma Mobile in Anfängen)
- **Keine Ende-zu-Ende-Verschlüsselung** der Ordner (nur Full-Disk/Ceph-Verschlüsselung des Betriebssystems)
- **Keine Team-Freigaben** — Freigaben müssen über CardDAV-Server erfolgen

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| CardDAV-Server (Nextcloud, Baïkal) | Akonadi-Ressource „CardDAV“ |
| LDAP/Active Directory | Akonadi-LDAP-Ressource |
| Google/Kalender-Sync | Akonadi Google-Ressource |
| KMail/Kontact | eingebettetes Modul |
| `kabc`/`akonadi-console` | CLI/Debug-Zugriff auf die Datenbank |
