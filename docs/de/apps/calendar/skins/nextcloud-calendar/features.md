# Nextcloud Calendar - Funktionen

## Übersicht

Nextcloud Calendar deckt den klassischen Kalender-Alltag ab und ergänzt ihn um Groupware-Funktionen, die zum Nextcloud-Ökosystem passen: CalDAV-Sync, geteilte Kalender, Verfügbarkeits- und Terminumfragen, Räume und Ressourcen. Alles läuft auf dem eigenen Server.

---

## 1. Terminplanung

- **Ansichten**: Tag, Woche, Arbeitswoche, Monat, Agenda (Terminliste); Wochenanfang und Zeitzone pro Nutzer einstellbar
- **Termintypen**: Einzeltermine, ganztägige Termine, wiederkehrende Serien (RRULE: täglich/wöchentlich/monatlich/jährlich, Intervalle, bis/anzahl, Ausnahme eines Serientermins bearbeiten)
- **Erinnerungen**: Popup und/oder E-Mail, mehrere je Termin, Standardwerte in den Einstellungen
- **Verfügbarkeitsstatus**: Termin als „beschäftigt"/„frei" (busy/free), Free-Busy-Ansichten für eigene Kalender bei der Terminerstellung
- **Einladungen**: Teilnehmer per Nutzer-, Gruppen-, Kreis- (Circles) oder E-Mail-Suche; Organisator versendet ICS-Einladung, Annehmen/Ablehnen/vorläufig per E-Mail oder im Browser; Zu-/Absage-Status im Termin sichtbar
- **Anhänge**: Dateien aus dem Nextcloud-Speicher an Termine anhängen (Link, kein Duplikat)
- **Kommentare**: Diskussion zu einem Termin über die Nextcloud-Kommentarfunktion

## 2. Kalenderverwaltung

- **Eigene Kalender** mit Name, Farbe, Beschreibung; **Kalendergruppen** zum Bündeln
- **Import/Export**: ICS-Dateien importieren, jeden Kalender als `.ics` herunterladen, Einzelereignisse exportieren
- **Abos**: externe Kalender per URL abonnieren (ICS, `webcal://`, auch fremde CalDAV-Server mit Zugangsdaten); Aktualisierung über Server-Hintergrundjobs (Intervall von der Cron-Konfiguration abhängig)
- **Geburtstagskalender**: automatisch aus den Nextcloud-Kontakten (CardDAV)
- **Feiertagskalender**: länderabhängige Feiertage, ein-/ausblendbar
- **Ende-zu-Ende-verschlüsselte Kalender**: clientseitige Verschlüsselung optional; Unterstützung hängt vom Client ab (Web-Oberfläche ja, viele Dritt-Clients nein)

## 3. Teilen und Berechtigungen

- Freigabe an Benutzer, Gruppen und Kreise (Circles-App)
- Stufen: **nur Verfügbarkeiten anzeigen** → **kann anzeigen** → **kann bearbeiten** (CalDAV-ACL im Hintergrund)
- **Öffentliche Links**: Kalender als Abo-Link ohne Login, optional Passwort (abhängig von den DAV-Freigabeeinstellungen des Servers)
- Gruppenkalender: jede Nextcloud-Gruppe bekommt automatisch einen geteilten Kalender ihrer Mitglieder

## 4. Team- und Umfragefunktionen

- **„Zeiten finden" (Verfügbarkeitsumfragen)**: Zeitschlitze für Tage festlegen, Link auch an Externe teilen, Teilnehmende kreuzen freie Slots an, Überschneidungen werden gegenübergestellt, Termin aus dem Ergebnis anlegen
- **Talk-Termine (Terminumfragen/Buchung)**: Nextcloud Talk stellt Termin-Slots bereit, die aus der eigenen Kalender-Verfügbarkeit gebildet werden; Besucher wählen und buchen, die Bestätigung landet im eigenen Kalender
- **Talk-Verknüpfung im Termin**: Besprechung zu einem Talk-Unterhaltungskanal anlegen bzw. verlinken
- **Räume und Ressourcen**: mit der Ressourcen-App (Teil der Groupware) sind Konferenzräume und Geräte buchbar; Belegung wird im Termin-Editor angezeigt; Raum-Ressourcen werden als Teilnehmer eingeladen
- **Teamkalender**: Gruppenkalender als gemeinsamer Terminkalender für Abteilungen (Bearbeitungsrecht über Gruppenzugehörigkeit)

## 5. Synchronisation und Clients

- Voller **CalDAV-Server** (RFC 4791) mit Sync-Collection (inkrementeller Sync), Free-Busy-Report und Kalender-Reports
- Getestete Clients (CalDAV-standardkonform): Apple Kalender, Thunderbird, GNOME Evolution, Geary, mobile Apps; Android über DAVx⁵; iOS über das Kalender-Account-Setup
- Nextcloud-eigene mobile Apps greifen über dasselbe Konto auf Termine zu (Darstellung je App eingeschränkt)

---

## Was Nextcloud Calendar NICHT kann

- **Kein Microsoft-Exchange-Server**: kein MAPI/EAS/ActiveSync - Outlook kann nicht nativ verbinden, nur ICS-Import oder Drittanbieter-Brücken
- **Kein nativer Desktop-Client**: die Oberfläche ist eine Web-App; Offline-Arbeit und Desktop-Notifications nur über CalDAV-Clients
- **Keine eigene Videokonferenz**: zu Terminen lässt sich nur ein Talk-Raum (oder Link) verbinden; Zoom/Teams/Google Meet erfordern Community-Apps und sind nicht offiziell unterstützt
- **Kein Calendly-Ersatz mit Buchungsregeln**: Talk-Termine decken Slot-Buchung ab, aber ohne Zahlungsanbindung, Puffer-/Tagesregel-Feintuning im Kalender selbst (Details je Talk-Version (nicht dokumentiert))
- **Keine Freigabe-Workflows für Räume**: Raum Reservierungen laufen ohne dokumentierten Genehmigungsprozess
- **Keine Projektplanung**: kein Gantt, keine Abhängigkeiten, keine Ressourcenoptimierung
- **Keine Aufgabenverwaltung in der App**: Aufgaben (TODO/VTODO) verwaltet die separate Aufgaben-App (Tasks), der Kalender zeigt sie nicht vollwertig
- **Kein Admin-Zugriff auf fremde Kalender**: Administratoren sehen aus Datenschutzgründen keine Termine ihrer Nutzer
- **Keine offiziellen Push-Webhooks für Terminänderungen** (siehe [api.md](api.md))
- **Keine durchgehende Tastatursteuerung**: es gibt keine dokumentierten App-Shortcuts, Drag & Drop ist nicht tastaturbedienbar (siehe [shortcuts.md](shortcuts.md))

---

## Erweiterungen, Plugins und Integrationen

Nextcloud Calendar ist keine Insel, sondern Teil der Nextcloud-Apps; Funktionen wachsen durch Zusammenspiel:

| Ergänzung | Beitrag |
|-----------|---------|
| **Nextcloud Talk** | Terminumfragen/-buchung, Talk-Link und -Raum im Termin |
| **Circles** | persönliche Gruppen als Invite- und Freigabeziel |
| **Ressourcen (Räume/Ressourcen)** | buchbare Räume und Geräte mit Free-Busy |
| **Kontakte** | Geburtstagskalender aus CardDAV |
| **Aufgaben (Tasks)** | separate CalDAV-TODO-Verwaltung nebenan |
| **Mail** | ICS-Einladungen annehmen/ablehnen direkt im Postfach |
| **Kollaborations-Apps** | BigBlueButton/Zoom/Meet-Links in Terminen (Community-Apps) |
| **Volltextsuche & Activity** | Termine in der Instanz-Suche, Aktivitäten-Protokoll |
| **Dritt-Clients** | Thunderbird, Evolution, Apple Kalender, DAVx⁵ als „Plugins" im Alltag |
| **Webhooks (Community)** | generische Webhooks-App der Community, keine Kalender-spezifischen Events (nicht dokumentiert) |

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) - Nextcloud Calendar bringt keine dokumentierten eigenen Shortcuts mit; dort steht, welche Browser-Tasten stattdessen funktionieren.

---

## Empfehlung

- **Für Teams in Nextcloud-Umgebungen**: volle Funktionsbreite inklusive Teamkalendern und Umfragen
- **Für Einzelnutzer mit Wert auf Datenhoheit**: CalDAV + Abos + Geburtstags-/Feiertagskalender genügen meist
- **Für Exchange-zentrierte Firmen**: eher ungeeignet, da kein MAPI/ActiveSync
