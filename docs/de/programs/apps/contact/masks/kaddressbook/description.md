# KAddressBook - Beschreibung

## Was das Programm macht

KAddressBook verwaltet Kontakte auf dem KDE-Desktop. Es speichert sie in Akonadi-Ordnern oder synchronisiert sie mit CardDAV-, IMAP- und LDAP-Quellen, stellt Editoren, Import/Export und Drucklayouts bereit und versorgt KMail/Kontact mit Adressvorschlägen und Geburtstagen.

## Vorteile

- **Quellenoffen**: ein UI über lokale Ordner, CardDAV, LDAP und IMAP-Ordner
- **Formattreue**: sauberes vCard/LDIF ohne proprietäre Zusätze
- **Tiefe Desktop-Integration**: Autocomplete, Visitenkartendruck, Kalenderverknüpfung
- **Kontact-fähig**: als Modul derselbe Code wie das PIM-Suite-Kontaktwerkzeug

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Thunderbird (Kontakte)** | Thunderbird pflegt eine eigene mSQLite-Adressbuchdatei; KAddressBook geht über Akonadi-Ressourcen und kann dieselben CardDAV-Server wie Thunderbird nutzen. |
| **Nextcloud Contacts** | Server/Web-UI; KAddressBook ist der Desktop-Client darauf. |
| **Evolution** | GNOME-PIM-Suite mit eigenem Data-Server; vergleichbare Architektur (EDS ≈ Akonadi), anderes Toolkit. |

## Technische Details

- **Backend**: Akonadi (MySQL/SQLite je nach Setup), Bibliotheken `KPim::Akonadi`, `KABC` (vCard)
- **Frontend**: Qt Widgets, Teil von KDE Gear; Kontact-Modul oder Einzelprogramm
- **Sprache**: C++
- **Authentifizierung**: ressourcenabhängig (CardDAV Basic/App-Passwort, LDAP-Bind), Passwörter im KWallet
- **Plattformen**: Linux/BSD; Windows inoffiziell
- **Lizenz**: GPL

## Für wen geeignet

- KDE-/Kontact-Nutzer, die mehrere Kontaktquellen vereinheitlichen wollen
- Migrationen (GMX/LDAP/CSV → vCard/CardDAV)
- FreeSynergy-Skins, die Desktop-Kontaktmasken und vCard-Felder nachbilden
