# Outlook Kalender - Funktionen

## Übersicht

Der Outlook Kalender verwaltet Termine, Besprechungen, Aufgaben und Ressourcen in Exchange-Postfächern. Er ist mit E-Mail, Kontakten und Besprechungstools verknüpft, läuft in Web, Desktop und Mobil praktisch identisch und stellt alle Daten über Microsoft Graph programmatisch bereit. Der Austausch mit Fremdsystemen erfolgt über ICS-Dateien, Abonnements und den Google-Kalender-Abgleich.

---

## 1. Termine und Besprechungen

### Funktionen
- **Termine und Ereignisse**: mit Beginn/Ende, ganztägig, Zeitzone pro Termin
- **Besprechungen mit Teilnehmern**: erforderlich, optional, Ressourcen; Einladungen als Besprechungsanfragen
- **Antwortstatus**: Annehmen, Vorläufig annehmen, Ablehnen, Terminvorschlag senden; Nachverfolgung im Organizer-Kalender
- **Wiederholungen**: täglich, wöchentlich, monatlich, jährlich, benutzerdefiniert (Serien mit Ausnahmen)
- **Erinnerungen** (Popup/Benachrichtigung), **Kategorien/Farben**, **Anzeigen als** (Free/Busy, Abwesend, Abwesend mit Vertretung)
- **Anlagen** im Termin, Notizen, **Terminsache/Richtlinien** (vertraulich, privat)
- **Raum- und Equipmentbuchung** über Ressourcenpostfächer mit Autoverteilung und Buchungsrichtlinien
- **Arbeitszeiten** und Abwesenheitsstatus, Free/Busy-Anzeige für Kollegen

#### Was diese Funktion NICHT kann
- Keine doppelte Buchung in denselben Raum ohne Freigabe der Buchungsrichtlinie
- Keine Terminserien mit unbegrenzt vielen Ausnahmen: sehr lange Serien werden beim Export/Import in anderen Systemen häufig fehlerhaft dargestellt
- Keine direkte Bearbeitung in fremden Kalendern ohne die Freigabestufen Author/Editor/Owner

---

## 2. Planungsassistent und Zeitsuche

### Funktionen
- **Planungsassistent**: Wochenansicht mit Free/Busy-Zeilen aller Pflicht- und Optionalteilnehmer
- **Konfliktanzeige** und Vorschlag für die nächste freie Zeit
- **Ressourcensuche** (Verfügbarkeit von Räumen nach Kapazität/Ausstattung)
- **Arbeitszeitfenster** und Zeitzonen der Teilnehmer

#### Was diese Funktion NICHT kann
- Keine echte Mehrsprachigkeits-/Präferenzoptimung („bevorzugt vormittags") wie in dedizierten Terminplanern
- Keine Teilnehmerauflösung über Mandantengrenzen ohne Organisationsbeziehung bzw. Gastfreigabe

---

## 3. Mehrere Kalender, Freigaben, Abonnements

### Funktionen
- **Mehrere Kalender pro Postfach** plus Kalendergruppen, Überlagerung im selben Kalenderblatt
- **Freigaben** mit abgestuften Rechten: nur Verfügbarkeit, Titel und Ort, Details, bearbeiten, Vollzugriff
- **Abonnement von Kalenderfeeds** (Feiertage, Sport, von Microsoft angebotene Feeds)
- **ICS-Import**: Kalenderdateien (`.ics`) in einen eigenen Kalender laden
- **Geburtstagskalender** aus Active-Directory-/Entra-Daten

---

## 4. ICS-Veröffentlichung und Export

### Funktionen
- **ICS als Datenaustauschformat** für Import und Weitergabe von Terminen
- **ICS-Download/Export** aus Clients (in der Weboberfläche als „Speichern unter" bzw. Download-Funktion vorhanden; Umfang ist versionsabhängig — genaue Limits: nicht dokumentiert)
- **Terminlinks** für einzelne Termine
- **Kalender-Abo-Links** bei freigegebenen Kalendern; externe Clients nutzen Exchange ActiveSync oder MAPI statt ICS-Abos
- **Wichtig**: Die frühere Funktion „Kalender im Web veröffentlichen" (öffentliche ICS-URL) wurde eingestellt; ein öffentliches ICS-Abo eines Outlook-Kalenders ist in aktuellen Versionen nicht vorgesehen (Stand: nicht dokumentiert, ob neu aufgelegt)

#### Was diese Funktion NICHT kann
- Kein CalDAV-Endpunkt (`/.well-known/caldav`) und kein CardDAV
- Keine öffentliche, anonym abonnierbare ICS-URL für Produktivkalender
- Keine fortlaufende Synchronisation bei importierten ICS-Dateien: ein Import ist eine einmalige Übernahme, kein Abo

---

## 5. Aufgaben, To Do und E-Mail-Verknüpfung

### Funktionen
- **To Do**: Aufgaben mit Fälligkeitsdatum, Flagge in der E-Mail, „Heute"-Liste, Synchronisation über Outlook Mobile und To Do
- **Verfolgte E-Mails** erscheinen im Kalender-/Aufgabenbereich
- **Vom Termin aus** E-Mail an Teilnehmer senden, Besprechungsprotokoll nachbereiten

---

## 6. Synchronisation und Clients

### Funktionen
- **Exchange Online** als eine Datenquelle für Web, Windows (neu und Classic), Mac, iOS, Android
- **Exchange ActiveSync (EAS)**, **MAPI over HTTP**, **Exchange Web Services** (veraltet), **Microsoft Graph**
- **Google-Kalender-Abgleich** (Bidirektional für Microsoft-365-Kalender, lizenzabhängig)
- **Offline-Caching** im Desktop-Client (Cache-Zeitraum administrativ einstellbar)
- **IMAP-Zugriff** auf Kalenderordner für ältere Drittanwendungen

---

## 7. Ansichten, Drucken, Benachrichtigungen

- Ansichten: Tag, Arbeitswoche, Woche, Monat, Terminübersicht (Agenda), Jahr
- Filter nach Kategorie, Besprechungstyp, Teilnahmestatus
- Druckdialog mit Layouts (Tag, Woche, Monat, Termindetail) und „Kalender drucken"-Assistent
- Push-/E-Mail-Benachrichtigungen, Erinnerungen, Besprechungsantworten
- Suchergebnisse mit Datumseingrenzung und Volltext

---

## Was Outlook Kalender NICHT kann

- **Nicht self-hostbar**: Es gibt keinen downloadbaren Kalender-Server für den eigenen Betrieb. Daten liegen in Exchange Online; lokal nur Exchange Server (On-Premises) als andere Produktlinie.
- **Kein CalDAV/CardDAV**: Third-Party-Clients (Thunderbird mit Ox, Evolution, Geary, CalDAV-Sync-Apps) können nicht direkt angebunden werden; Behelfe sind Google-Kalender-Abgleich oder Brückenwerkzeuge.
- **Kein offenes Abo-Format für Fremde**: keine dauerhafte öffentliche ICS-Feed-URL wie bei Google Kalender oder Nextcloud.
- **Keine echten Offline-Schreibrechte im Web**: Änderungen ohne Verbindung werden in der Weboberfläche nicht unbegrenzt nachgeführt (Desktop-Client mit OST-Cache ausnehmen).
- **Keine Kalender ohne Lizenzpflicht im Business-Kontext**: Funktionsumfang (Ressourcen, Planungsassistent mandantenübergreifend, Teams-Onlinebesprechungen) hängt am Microsoft-365-Plan.
- **Keine vollwertige Terminbuchung für Externe**: Kunden-Terminbuchung mit Selbstbedienung ist Microsoft Bookings (eigene Lizenz/Produkt), nicht der Kalender selbst.
- **Keine direkte ICS-API**: Export/Import sind UI-Aktionen; ein dokumentierter Graph-Endpunkt für „Kalender als ICS herunterladen" existiert nicht.
- **Keine echte Echtzeit-Kollaboration** an einem Termin: Bei paralleler Bearbeitung gewinnt die zuletzt gespeicherte Fassung; Konflikte werden nicht wie in Dokumenten-Editoren zusammengeführt.
- **Keine freie Datenhoheit**: Aufbewahrung, Löschfristen und Datenregion folgen den M365-Zusagen des Mandanten; eine eigene Datenbank ist nicht zugänglich.
- **Kein durchgängig identischer Funktionsstand** in allen Clients: Outlook im Web, neues Outlook, Outlook Classic und Mobile unterscheiden sich bei Import, Druck und Verwaltungsdetails.

---

## Erweiterungen, Add-ins und Integrationen

### Microsoft-eigene Integrationen
- **Microsoft Teams**: Onlinebesprechung am Termin, Teams-Besprechungskanal im Kalender
- **Microsoft Bookings**: öffentliche Terminbuchungsseite für Kunden (separates Produkt)
- **To Do / Planner / Lists**: Aufgabenbezug aus Terminen
- **Power Automate**: Trigger „Neuer Termin" / „Termin erstellt oder geändert" und Aktionen zum Anlegen von Terminen (Graph-basiert)
- **Microsoft Graph-Connectoren** in Power Apps und Logic Apps
- **Visio/Excel-Export** über eigene Skripte auf Graph-Daten

### Add-ins (Erweiterungen im Client)
- **FindTime** (Umfrage zur Terminfindung)
- **Zoom Workplace**: Onlinebesprechungsschaltfläche im Terminformular
- **Add-ins nach Office-JavaScript-API**: eigene Schaltflächen im Terminformular, Datenabgleich mit Fremdsystemen
- Verwaltet über den Add-in-Katalog bzw. vom Tenant-Administrator bereitgestellt

### Integrationen in Drittumgebung
- **Google Kalender**: bidirektionaler Abgleich für Microsoft-365-Kalender
- **Apple Kalender / iCloud**: Synchronisation über das Outlook-Mobile-Konto bzw. Exchange ActiveSync
- **ICS-Dateien**: Import in Outlook, Export aus Outlook, Konvertierung über iCalendar-Werkzeuge
- **Kalender-Skripte**: PowerShell mit Microsoft.Graph-Modul, Python/Node mit Graph-SDKs
- **Brückenwerkzeuge für CalDAV**: Drittanbieter (zum Beispiel Outlook CalDav Synchronizer für Outlook Classic und CalDAV-Server) — keine Microsoft-Funktion
- **CRM-/Helpdesk-Anbindung**: über Connectoren oder Graph (Beispiel: Termine zu Tickets, Kontakten oder Projekten verknüpfen)

### Entwicklung
- **Microsoft Graph API** (Kalender, Termine, Kalendergruppen, Freigaben, Zeitplan) — siehe [api.md](api.md)
- **Change Notifications (Webhooks)** für neue und geänderte Termine
- **Add-in-Entwicklung** mit dem Office-Add-in-Framework

---

## Shortcuts

siehe [shortcuts.md](shortcuts.md) für die dokumentierten Tasten und die als fehlend markierten Kombinationen.

---

## Empfehlung

- **Für Unternehmen mit Microsoft 365**: die natürliche Wahl, weil Ressourcen, Free/Busy und Compliance greifen
- **Für offene Landschaften (Linux, CalDAV, Self-Hosting)**: nur mit Abgleich oder Brücke sinnvoll, besser ein CalDAV-basiertes System
- **Für öffentliche Kalender (Verein, Campus, Events)**: ein CalDAV- oder ICS-Feed-orientiertes System verwenden
