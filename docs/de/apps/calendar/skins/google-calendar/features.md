# Google Kalender - Funktionen

## Übersicht

Google Kalender verwaltet Termine, wiederkehrende Serien, Aufgaben und Kalenderfreigaben in einer Cloud. Der Schwerpunkt liegt auf Mehrpersonenterminen: Einladungen mit Zu-/Absagen, Konferenzlinks, Anzeigen freier Zeiten und automatische Zeitzonen-Umrechnung. Für Organisationen kommen Teamkalender, Ressourcenkalender, Arbeitsort-Attribute und buchbare Terminpläne dazu.

---

## 1. Termine und Ereignisse

### Funktionen
- **Termin anlegen**: Titel, Ort, Anfang/Ende, ganztägig, Kalenderauswahl, Beschreibung (Rich Text), Farbe
- **Schnell erstellen**: natürlichsprachliche Eingabe wie "Zahnarzt am 12. Mai um 9 Uhr, alle 6 Monate"
- **Gäste einladen**: E-Mail-Adressen, Antwortstatus (Ja/Nein/Vielleicht/ausstehend), "Gäste können einladen/ändern/löschen", "Nur zeigen, wenn frei"
- **Konferenzlink**: Google Meet (bei Workspace auch Telefon-Brücken), Raum-/Ressourcenbuchung
- **Erinnerungen**: Pop-up und E-Mail, mehrere je Termin, Vorgabe pro Kalender
- **Sichtbarkeit und Verfügbarkeit**: öffentlich/privat/vertraulich, "frei" oder "belegt" (Transparenz)
- **Anhänge und Links**: Drive-Verknüpfungen, Links in der Beschreibung
- **Serientermine**: täglich, wöchentlich, monatlich, jährlich, benutzerdefiniert (z. B. "jeden 2. Dienstag"), Ausnahmen einzelner Termine, Änderung "nur diesen / alle nachfolgenden / alle"
- **Zeitumrechnung**: Termine werden in der viewing-Zeitzone angezeigt; zweite Zeitzone zusätzlich einblendbar
- **Aufgaben**: eigene Aufgabenliste mit Fälligkeit, Unteraufgaben und Wiederholung (Datenmodell der Tasks)
- **Zeitblöcke, Fokuszeit, Abwesenheit, Arbeitsort** als besondere Ereignistypen (Workspace)

### Was Google Kalender hier NICHT kann
- Keine genehmigungspflichtigen Freigabe-Workflows (ein Termin braucht keine mehrstufige Genehmigung)
- Keine Terminabhängigkeiten, Meilensteine oder Rückwärtsplanung (kein Projektplan)
- Keine Kapazitätsplanung pro Ressourcenmenge über die einfache Ressourcenbuchung hinaus
- Keine gemeinsame Live-Bearbeitung desselben Termins durch mehrere Personen (kein gleichzeitiges Editieren mit mehreren aktiven Nutzern)
- Keine verschachtelten, vererbten Berechtigungen pro Unterordner - Freigaben gelten pro Kalender

---

## 2. Kalender, Freigaben und Teams

### Funktionen
- **Mehrere Kalender** pro Konto, plus Unterkalender (eigene Farbe, eigene Freigabe)
- **Teamkalender** und Gruppenkalender (Google Gruppen als Kalender-ID)
- **Berechtigungsstufen**: nur freie/belegte Zeiten, alle Details, bearbeiten, verwalten
- **Domänenweite Vorgaben** durch Workspace-Administratoren (wer darf mit wem teilen, öffentliche Freigabe)
- **Abonnements**: öffentliche Kalender (Feiertage regional, Sport, Mondphasen), ICS-Abonnement-URL
- **Import/Export**: ICS-Datei importieren, jeden Kalender als ICS herunterladen; Google Takeout für den Vollexport
- **Ressourcenkalender**: Räume und Geräte mit Standort, Kapazität und Buchungsrichtlinie (Admin Console)
- **Wiederherstellen**: versehentliche Änderungen der letzten Zeiträume zurückholen

### Was Google Kalender hier NICHT kann
- Keine lokale/On-Premise-Kopie des Kalenders (kein Self-Hosting, keine eigene Datenbank)
- Keine mandantenweite Rechteverwaltung mit ROLEn-Vererbung über Organisationseinheiten (nur domänenweite Einstellungen plus Freigabe pro Kalender)
- Kein "Schreibzugriff auf einzelne Termine" - Rechte gelten immer für den ganzen Kalender
- Kein verschlüsseltes Ende-zu-Ende-Modell für Termine; Termine liegen in der Google-Cloud

---

## 3. Ansichten und Planungshilfen

### Funktionen
- **Ansichten**: Tag, Woche, Monat, Jahr, Zeitplan (Agenda), Angepasste Ansicht (mehrere Kalender nebeneinander)
- **Zeit finden / Frei-belegt-Ansicht**: freie Slots mehrerer Kalender vergleichen
- **Zeitzonenansicht für internationale Teams** (Uhrzeiten pro Beteiligter bei der Terminsuche)
- **Arbeitszeiten** als Rasterhintergrund, Wochenende ein-/ausblendbar
- **Terminpläne**: öffentliche Buchungsseite mit Slot-Definition, Pufferzeiten, Fragebogen (Nachfolger des Google-Buchungssystems)
- **Mini-Monat**, Farb- und Symbolsystem pro Kalender, Dichtesteuerung
- **Drucken** über die Druckvorlage des Browsers mit Kalenderoptionen

### Was Google Kalender hier NICHT kann
- Keine Gantt-/Kapazitätsdiagramme und keine Auslastungsberichte
- Keine Timer-/Zeiterfassung (keine Soll-Ist-Zeit, keine Integration in Arbeitszeitkonten ohne Fremdttool)
- Keine offline voll funktionsfähige Web-Ansicht (nur eingeschränkter Mobil-Cache)

---

## 4. Synchronisation und Zugriff von außen

### Funktionen
- **Calendar REST API v3** (JSON/HTTPS) für Kalender, Termine, ACL, Free/Busy und Push-Kanäle
- **CalDAV** für Kalender-Clients (in Workspace vom Administrator freizuschalten)
- **ICS-Abonnement-Links** für öffentliche Kalender, **Embed-URLs** für Websites
- **Mobile Apps** für Android und iOS mit Widgets, Benachrichtigungen und Material-Design-Oberfläche
- **Google Assistant / Nest**: Termine abfragen und anlegen
- **Synchronisation mit Gmail**: Einladungen, "In Kalender suchen", Meet-Erkennung

---

## Was Google Kalender NICHT kann (gesamt)

| Bereich | Grenze |
|---------|--------|
| Betrieb | Kein Self-Hosting, kein Container/Image, keine eigene Instanz - Google legt Server, Version und Datenhaltung fest |
| Datenhoheit | Kein direkter Datenbankzugriff; Export nur als ICS/Takeout, keine relationale Abfrage |
| Offline | Web-App ohne vollständige Offline-Bearbeitung; Mobil nur begrenzt gecacht |
| Berechtigungen | Recht immer pro Kalender, nicht pro Termin; keine Vererbung, keine Rechte-Ablaufdaten |
| Workflows | Keine Genehmigungsketten, keine Regeln/Automation im Kalender selbst (nur externe Automatisierung) |
| Aufgaben | Keine Abhängigkeiten, keine Projekt-/Team-Task-Boards in dem Sinne wie dedizierte Task-Tools |
| Berichte | Keine Auslastungs-/Überschneidungsberichte, keine Ressourcen-Kapazitätsplanung über simple Buchung hinaus |
| Client-Erweiterbarkeit | Kein eigenes Pluginsystem in der Oberfläche; Erweiterungen nur über Workspace Add-ons und Apps Script |
| Barrierefreiheit/Anpassung | Kein freies Theme-System, keine eigenen CSS-Vorgaben, kein White-Label |
| Terminpläne/API | Für Terminpläne (Buchungsseiten) existiert kein öffentlich dokumentierter Endpunkt der Calendar API v3 (nicht dokumentiert) |
| Historie | Keine vollständige Versionshistorie eines Termins (nur Seriennummer/Änderungszeitstempel in der API) |

---

## Erweiterungen, Plugins und Integrationen

### Google-eigene
- **Google Workspace Add-ons** (Karten-Oberflächen in Kalender, Gmail, Drive) über den Add-on-SDK-Mechanismus
- **Apps Script** mit dem Dienst `CalendarApp` (Kalender, Termine, Gäste per Skript lesen und schreiben)
- **Marketplace-Integrationen** (Workspace Marketplace) für Buchung, Ressourcen, Zeiterfassung
- **Gmail, Meet, Tasks, Drive, Forms** (Formulare in Terminplänen), **Google Chat** für Meet-Benachrichtigungen

### Gängige Drittanbieter-Anbindung (über API oder CalDAV/ICS)
- **Automatisierung**: Zapier, Make, IFTTT, Google Apps Script, n8n (Google-Calendar-Node)
- **Kalender-Clients**: Thunderbird (Provider für Google-Kalender), Apple Kalender, Apple Mail, Microsoft Outlook (Abonnement/Abruf), Evolution, Fantastical, eM Client, DAVx5 (Android, CalDAV)
- **Planungs- und Buchungs-Tools**: Calendly, YouCanBook.me, Excalibur, Reclaim, Motion, Notion Calendar
- **Task-Tools**: Todoist, Asana, TickTick (Terminspiegel in Google Kalender)
- **Hardware**: Android-Smartphones/Wear OS, Pixel Watch, Nest Hub, Chromecast mit Kalenderanzeige

### Eigenbau
- Client-Bibliotheken von Google für Python, Node.js, Java, PHP, Ruby, .NET, Go (siehe [api.md](api.md))
- CalDAV-Clients für klassische Kalenderprogramme

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für alle dokumentierten Tastenkürzel der Web-Ansicht.

---

## Empfehlung

- **Für Privatpersonen**: schnellste Terminverwaltung mit Gmail und Mobil-Synchronisation
- **Für Teams in Workspace**: starke Terminkoordination, Ressourcen, Teamkalender - dafür Administrationsrichtlinien beachten
- **Weniger geeignet**: wenn Datenhoheit, Self-Hosting, Freigabe-Workflows oder Offline-Fähigkeit Pflicht sind (dann Nextcloud Calendar, Radicale/BAïkal oder Groupware-Systeme prüfen)
