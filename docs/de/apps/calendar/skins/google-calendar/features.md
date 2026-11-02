# Google Kalender – verifizierte Funktionen (Stand: 2.11.2026)

Grundlage: offizielle Hilfeseiten (support.google.com/calendar), offizielles Produktstück workspace.google.com/products/calendar, Calendar-REST-API-v3-Discovery (Revision 20261028) und das offizielle Google-Workspace-Updates-Blog.

## Kalender & Ansichten

- Mehrere Kalender pro Konto: eigener Standardkalender plus beliebig viele Sekundärkalender (Produktseite, „Get started“-Hilfe)
- Ansichten: **Tag, Woche, 4 Tage, Monat, Jahr, Zeitplan (Schedule)** (Hilfe „View your day, week, or month“)
- Farbmarkierung von Kalendern und Terminen; helles/dunkles/System-Design (Produktseite)
- Web-Oberfläche, Apps für **Android, iOS, Wear OS, Apple Watch** – automatische Synchronisation (Produktseite); **keine Desktop-App**, sondern Browser (Chrome, Firefox, Safari, Edge) (Hilfe „Get started“); Offline-Nutzung ist dokumentiert (Hilfeseite „Offline verwenden“, Umfang im Detail nicht geprüft)
- Suche über Freitext (API: `q` über Titel, Beschreibung, Ort, Teilnehmer u. a.)

## Termine

- Erstellen/Bearbeiten inkl. **Ganztags-, mehrsprachige beschreibbare Termine, Serientermine** (Wiederholungsmuster, API-Feld `recurrence`), Erinnerungen (Pop-up/E-Mail, API `EventReminder`)
- Gastauftritt: Einladungen mit Antwortstatus, Organizer/Rollenteilung; Gastsicherheit über `guestsCanInviteOthers`, `guestsCanModify`, `guestsCanSeeOtherGuests` (API-Feld `visibility`, `privateCopy`)
- **Dateianhänge an Termine** (Drive-Links/URLs; API `supportsAttachments`, `EventAttachment`; Produktseite)
- **Meet-Konferenzen** automatisch/per Klick (`conferenceData`, `hangoutLink`)
- **Fokuszeit**: Termin, der Chat-Benachrichtigungen stummschaltet und Besprechungen automatisch ablehnt (Hilfe 11190973; API `focusTimeProperties`)
- **Abwesenheit (Out of Office)** und **Arbeitsort/-zeiten** als Termin-Eigenschaften für Teams (API `outOfOfficeProperties`, `workingLocationProperties`; Produktseite)
- Geburtstagstermine als eigener Termintyp (API `birthdayProperties`)
- „Schnell hinzufügen“ per Freitext (API `events.quickAdd` mit `text`-Parameter)
- Termin verschieben zwischen Kalendern (API `events.move`)

## Zusammenarbeit & Freigaben

- Kalender freigeben mit Berechtigungsstufen: **nur Belegung sehen / Details sehen / Termine ändern / teilen verwalten** (Hilfe „Subscribe to someone else’s calendar“)
- Abonnieren fremder Kalender per E-Mail-Suche oder **URL (ICS-Abonnement öffentlicher Kalender)**; über **400 abonnierte Kalender** → Performance-Probleme (Hilfe 37100)
- „**Einen Termin finden**“ (Find a time): Vorschläge für freie Zeiten/Räume für Gruppen, Web + Android + iOS (Workspace-Updates-Blog 2016)
- Organisationskalender und **Räume/Ressourcen** in Google Workspace (FAQ Produktseite; Verwaltung ist Workspace-Admin-Funktion)
- Erinnerungen/Benachrichtigungen pro Kalender und pro Termin (E-Mail, App-Push; API-Kanäle für Drittanbieter)

## Buchung & Organisation

- **Reservierungsseiten / Terminpläne (Appointment schedules)**: eigene Buchungsseite mit Verfügbarkeitsfenstern, ohne Zusatz-Apps; **kostenlos für private Google-Konten** (FAQ Produktseite; Hilfe 10729749/11608416)
- Premium (bestimmte Google-One-/Workspace-Abos): **mehrere Reservierungsseiten, Stripe-Zahlungen, E-Mail-Erinnerungen, Verfügbarkeitsprüfung über mehrere Kalender** (Produktseite; Workspace-Admin-Schalter „Appointment schedules with payments“)
- **Tasks-Integration**: Aufgaben mit Datum/Uhrzeit erscheinen im Kalender (eigener Dienst Google Tasks) (Produktseite)
- Automatische Termine aus **Gmail** (Flüge, Hotels, Restaurants) (Produktseite)
- **„Ihre Zeit im Blick“ (Time Insights)**: Analyse des Meeting-Verhaltens, Workspace-Konten, administrativ abschaltbar (Hilfe 10738043)
- **Gemini-KI** (Premium-Abos): „Plane für mich“ in Gmail, „Zum Kalender hinzufügen“ aus E-Mails (Produktseite)
- **Migrationstools** u. a. aus Microsoft Exchange/Outlook und IBM Notes (Produktseite FAQ)

## Import, Export, Schnittstellen

- **ICS-Export** von Kalendern (nur Web, Rechte „Änderungen vornehmen & Freigabe verwalten“ erforderlich) (Hilfe 37111); **ICS-Import** in Google Kalender (Grundfunktion der Import-/Export-Hilfewelt; API-seitig `events.import`)
- **Calendar REST API v3** (alle Kalender-/Terminoperationen, Sync-Token, Batching, Push-Kanäle) und **Tasks API**; Apps-Script-Dienst `CalendarApp`; Workspace-Add-ons (siehe [api.md](api.md))

## Was Google Kalender NICHT bietet

- **Kein Self-Hosting**: weder Serversoftware noch lokale Variante; Daten liegen ausschließlich in Google-Rechenzentren
- **Kein Desktop-Programm** (nur Browser + mobile Apps) – ausdrücklich in der offiziellen Hilfe
- **Kein offizielles CalDAV/CardDAV** und kein Exchange ActiveSync mehr: Google Sync wurde 2024 eingestellt, CalDAV/CardDAV mit Passwort („weniger sichere Apps“) ab 2024/2025 deaktiviert; offizielle Doku nennt nur die REST-API. Drittanbieter-Endpunkte laufen inoffiziell über OAuth („weder von Google noch von DAVx⁵ offiziell unterstützt“)
- **Kein offenes Standardprotokoll** für Sync (eigene Sync-Token/Webhook-Kanäle statt RFC 4791 REPORT/Sync wie bei DAViCal)
- **Die „Ziele“-(Goals-)Funktion wurde eingestellt** (Abschaltung ab November 2022) – in älterer Literatur noch zu finden
- Aufgaben (Tasks) sind ein **separater, schlanker Dienst**, kein gleichwertiger Termintyp mit Teilnehmern/Serien im Kalenderdatensatz
- Reservierungsseiten sind **nicht per API verwaltbar** – im aktuellen Discovery v3 (Rev. 20261028) gibt es weder eine eigene Ressource noch einen `appointment`-`eventType`; reine UI-Funktion
- Workspace-Verwaltungsfeatures (Räume/Ressourcen, Richtlinien, Time Insights für die Org) gibt es **nicht für private Konten**
- Quoten & Schwellen (10.000/min/Projekt, 600/min/Nutzer, 1 Mio./Tag mit geplanter Bepreisung ab „später 2026“) – keine unbegrenzte Automatisierung
- Kein End-to-End-verschlüsselter Kalender; „Geheimadressen“-Freigaben ersetzen keine echte Verschlüsselung

## Nicht verifiziert

- Das Einstellungs-Feature „Zweite Zeitzone“ in der Web-Oberfläche war lange dokumentiert, der alte Hilfartikel ist umgezogen; Nachweis aus aktueller Primärquelle stand bei Redaktion nicht verfügbar → nicht als verifiziert gelistet
- Detailumfang der Offline-Nutzung (welche Operationen offline möglich sind)
- Ob die Workspace Events API inzwischen Kalender-Ressourcen subscriben lässt
