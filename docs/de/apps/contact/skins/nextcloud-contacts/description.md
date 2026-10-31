# Nextcloud Contacts - Beschreibung

## Was das Programm macht

Nextcloud Contacts verwaltet persönliche und geteilte Adressbücher innerhalb einer Nextcloud-Instanz. Kontakte sind vCards in der Server-Datenbank, erreichbar über das Web-Frontend und jeden CardDAV-Client. Freigaben, Kreise und die Verknüpfung mit Mail/Talk/Calendar machen es zum Kontakt-Rückgrat der Suite.

## Vorteile

- **Ein Konto, alle Geräte**: CardDAV-Sync out of the box
- **DSGVO-freundlich**: Daten bleiben auf der eigenen Instanz
- **Suite-Integration**: Mail-Autocomplete, Talk-Chat-Buttons, Geburtstagskalender
- **Standardformate**: Import/Export reines vCard, keine Vendor-Lock-in

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **KAddressBook (KDE)** | Desktop-Programm mit Akonadi; Nextcloud Contacts ist der Server mit Web-ui. Beides kann an demselben CardDAV hängen. |
| **Monica** | Personal-CRM mit Aktivitäten und Beziehungen; Nextcloud Contacts speichert nur Kontaktdaten. |
| **GNOME Contacts** | lokaler GTK-Client auf Evolution-Data-Server; greift selbst auf CardDAV (auch auf Nextcloud) zu — Client vs. Server. |

## Technische Details

- **Backend**: PHP (Nextcloud-App `contacts`), vCard-Parser `sabre/vobject`
- **Datenbank**: Nextcloud-Haupt-DB (Tabellen `oc_cards`, `oc_cards_addressbook`)
- **Frontend**: Vue 3, Team-Dialog-Komponenten
- **Authentifizierung**: Nextcloud-Session/App-Passwörter; CardDAV Basic über TLS
- **Hosting**: auf jeder Nextcloud-Instanz (App aktivierbar)
- **Lizenz**: AGPL

## Für wen geeignet

- Nextcloud-Nutzer als zentraler Kontaktspeicher
- Familien/Teams mit CalDAV-/CardDAV-Clients auf allen Geräten
- FreeSynergy-Kontakt-Szenarien, die vCard-/CardDAV-Skins mit Freigaben abbilden wollen
