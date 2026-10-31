# KAddressBook - Menüpunkte

## Menüleiste (Einzelprogramm; in Kontact identisch als Modul)

| Menü | Einträge (Auswahl) |
|------|--------------------|
| **Datei** | Neu → Kontakt / Verteilerliste; Import/Export-Assistent; Drucken; Beenden |
| **Bearbeiten** | Kontakt bearbeiten, Kopieren/Ausschneiden/Einfügen, Kontakt löschen, Suchen/Ersetzen |
| **Ansicht** | Spalten ein/aus, Schnellauswahl-Leiste, Adressbuch-Browser ein/aus, Anzeigethema wählen |
| **Adressbuch** | Neues Adressbuch (Ordner/CardDAV/LDAP/…), Adressbuch-Eigenschaften, Alle als vCard speichern |
| **Werkzeuge** | Import/Export, Karten drucken (Visitenkarten-Layouts), Schnittstelle „Kontakte synchronisieren“ (Akonadi-Agentstatus) |
| **Einstellungen** | Akonadi-Ressourcen verwalten, Kurzbefehle, Configure KDE PIM |
| **Hilfe** | Handbuch, Info |

## Import-/Export-Assistent

| Format | Richtung |
|--------|----------|
| vCard (.vcf) | Import + Export (einzeln/Mehrfach) |
| LDIF / LDAP | Import + Export |
| CSV/LDIF (KABC-CSV) | Import |
| GMX/webdav-Export (veraltet) | Export |
| ABCZ, LDIF-Bord | je nach Version |

## Rechtsklick auf Kontakt

Bearbeiten · Kopieren · Löschen · Als vCard speichern · In Verteilerliste aufnehmen · Details anzeigen

## Adressbuch-Browser (links)

- Akonadi-Ordnerbaum: persönliche Ordner, CardDAV-/IMAP-/LDAP-Ressourcen
- Rechtsklick: Eigenschaften, Sync jetzt, offline-Verhalten

## Menüs nach Rolle

| Rolle | Wirkung |
|-------|---------|
| Lokaler Nutzer | alle Menüs |
| LDAP-Ordner (readonly) | Anlage-/Bearbeitungsmenüs ausgegraut |
| CardDAV-Share (read) | wie readonly |
