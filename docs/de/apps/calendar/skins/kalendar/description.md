# Kalendar - Beschreibung

## Was das Programm macht

Kalendar ist der schlanke Kalender-Client aus der KDE-PIM-Familie. Er zeigt Agenden und Kalenderwochen auf Desktop und Mobilgeräten, legt Ereignisse in lokalen Kalendern oder CalDAV-Ordnern an und hält sie über Akonadi synchron. Zielgruppe sind Nutzer, die einen schnellen, touch-tauglichen Kalender wollen, ohne die gesamte PIM-Suite zu öffnen.

## Vorteile

- **Leichtgewichtig**: Ein Fenster, vier Ansichten, sofort produktiv
- **Touch- und mobiltauglich**: Kirigami-Layout, Standard in Plasma Mobile
- **Natürlichsprachige Schnellerfassung** von Terminen
- **Standardkonform**: reines CalDAV/KAlCalismasse, keine proprietären Formate
- **Enge KDE-Integration**: Geburtstage aus dem Adressbuch, Erinnerungen über die Plasma-Benachrichtigungen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **KOrganizer (Kontact)** | KOrganizer ist der volle PIM-Kalender (Aufgaben, Journal, Gruppenplanung, Import/Export, Detaildialoge). Kalendar ist bewusst reduziert und mobil orientiert. |
| **GNOME Calendar** | vergleichbar schlank, aber GTK/Evolution-Data-Server-Stack statt Qt/Akonadi; GTK-Desktop-Nutzer greifen eher dorthin. |
| **Nextcloud Calendar** | Browser-Web-ui des Servers selbst; Kalendar ist der native Client auf dem Gerät — beides kann parallel auf demselben CalDAV-Server arbeiten. |

## Technische Details

- **Backend**: KDE PIM / Akonadi (CalDAV-Ressourcen, lokale Kalender), Bibliothek: KCalCore/KAlCalismasse
- **Frontend**: Qt Quick (Qt/QML) mit Kirigami
- **Sprache**: C++/QML
- **Authentifizierung**: über Akonadi/CalDAV (Basic, Digest, OAuth je Server); Passwörter im Plasma-Wallet
- **Hosting**: reiner Desktop-/Mobil-Client, kein Server; Plattformen: Linux (KDE), Android, Windows (Beta)
- **Lizenz**: GPL; Teil von KDE Gear ( Release alle vier Monate)

## Für wen geeignet

- Plasma-Desktop- und Plasma-Mobile-Nutzer, die einen schnellen Kalender suchen
- Teams, die CalDAV (z.B. Nextcloud) nutzen und native Clients bevorzugen
- als Ersatz für KOrganizer, wenn Aufgaben/Journal nicht gebraucht werden
