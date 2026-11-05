# GNOME Contacts - Beschreibung

## Was das Programm macht

GNOME Contacts ist der GNOME-eigene Kontaktmanager: eine schlanke GTK-Oberfläche auf den Evolution Data Server. Kontakte werden lokal und über Online-Konten (Google, CardDAV, LDAP) gepflegt und mit allen GNOME-Apps geteilt.

## Vorteile

- **Minimal und schnell**: ein Fenster, null Menüleiste, sofort nutzbar
- **EDS-Backend**: eine Quelle für GNOME-Shell-Suche, Mail-Clients, Kalender
- **Standardgeräte**: vCard-Im/Export, Online-Konten ohne Vendorbindung

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **KAddressBook** | KDE-Pendant mit Akonadi, breiteren Importformaten und Feldtyp-Vielfalt; GNOME Contacts ist radikaler reduziert. |
| **Evolution** | volle PIM-Suite (Mail/Kalender/Aufgaben) auf demselben EDS; Contacts = nur der Kontakt-Teil. |
| **Nextcloud Contacts** | Web-Server mit Freigaben; GNOME Contacts ist Desktop-Client und kann genau darauf zugreifen (Online-Account). |

## Technische Details

- **Backend**: Evolution Data Server (D-Bus-Dienste `evolution-source-registry`, -addressbook-registry)
- **Frontend**: GTK 4 / libadwaita, C/Vala
- **Datenhaltung**: EDS-Caches (`~/.local/share/evolution/addressbook/`), Synchron-Protokolle der Quellen
- **Authentifizierung**: Online-Accounts-Dialog (OAuth2 für Google; Basic für CardDAV), Passwörter im GNOME Keyring
- **Plattform**: Linux (GNOME), offizieller Build nur dort
- **Lizenz**: GPL

## Für wen geeignet

- GNOME-Nutzer mit Online-Konten oder Nextcloud/Fastmail-CardDAV
- Umgebungen, die eine einheitliche EDS-Kontaktbasis für mehrere Apps brauchen
- FreeSynergy-Skins, die reduzierte Kontaktmasken (Karte + Felder + Quellenwahl) nachbilden
