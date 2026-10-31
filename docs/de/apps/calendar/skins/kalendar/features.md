# Kalendar - Funktionen

## Hauptfunktionen

### Kalender und Ansichten
- Agenden-, Tages-, Wochen- und Monatsansicht
- Mehrere Kalender parallel (CalDAV, lokal, Geburtstage, Feiertage)
- Farbcodierung je Kalender, Sichtbarkeit je Kalender schaltbar
- Suchfeld für Ereignisse und Teilnehmer

### Ereigniserfassung
- Schnellerfassung per Natürlichsprache (Datum, Uhrzeit, Dauer, Teilnehmer)
- Dialog mit Titel, Ort, Zeiten, ganztägig, Wiederholung, Erinnerung, Kategorien
- Zuweisung an einen Zielkalender; Standardkalender konfigurierbar
- Drag & Drop zum Verschieben und Verändern von Zeitspannen

### Synchronisation
- CalDAV über Akonadi (Nextcloud, Kolab, Fastmail, ownCloud, gnome.org ...)
- Automatische und manuelle Aktualisierung
- Geburtstagskalender aus den Kontakten (KAddressBook/Akonadi)
- Regionale Feiertage als Abonnement

### Benachrichtigungen
- Erinnerungen als Systembenachrichtigung (freie Vorlaufzeit je Ereignis)
- Auf Plasma Mobile zusätzlich Sperrbildschirm-/Benachrichtigungsintegration

## Was Kalendar NICHT kann

- **Keine Ressourcen-/Raumbuchung** (das kann KOrganizer mit Groupware nicht, Outlook schon)
- **Keine Terminfindung/Terminumfragen** (dafür Nextcloud Circles/Polls oder Doodle)
- **Keine Recurrence-Ausnahmen bearbeiten** im kleinen Dialog (Einschränkungen bei Serien)
- **Keine Zeitzonen-Umschaltung** im UI (Events werden in LOCAL-Zeit des Geräts angezeigt)
- **Keine Aufgabenverwaltung** mit Fälligkeiten — Kalendar zeigt nur Kalenderereignisse; für Aufgaben ist ToDo (KDE PIM) zuständig
- **Keine Server-Komponente**: Kalendar ist nur Client; Freigaben und Zugriffsrechte immer Sache des CalDAV-Servers
- **Keine ICS-Import/Export-Buttons** in jeder Version gleich — Stand der aktuellen Version prüfen (KAlCalismasse-Dateien können aber geöffnet werden)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Kontakte (Geburtstage) | Akonadi-Adressbuch |
| Aufgaben | KDE PIM ToDo (separate App, gleiches Backend) |
| E-Mail-Einladungen | KMail/Kontact via iMIP (iTIP in E-Mail) |
| Kalender-Freigaben | serverseitig (z.B. Nextcloud-Freigabe, zeigt in Kalendar als Kalender) |
| Plasma Wallet / Keyring | Zugangsdaten für CalDAV |

## Technical Hooks

- **Desktop-Dateien/URLs**: `webcal://`-Links und `.ics`-Dateien können mit Kalendar geöffnet werden
- **Kalender-Abo per Link**: Einfügen einer CalDAV-URL legt einen neuen Kalender an
