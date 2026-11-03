# SuiteCRM - Menüpunkte

## Übersicht

SuiteCRM wird über eine waagerechte Hauptmenüleiste (7.x) bzw. eine Navigationsleiste mit Modulmenü (SuiteCRM 8) bedient. Zusätzlich gibt es ein Benutzer-Menü rechts oben und ein Admin-Menü, das nur Administratoren sehen. Welche Module sichtbar sind, hängt von Rolle, Team und Zugriffsrechten ab.

## Hauptmenüpunkte

### 1. Start (Home)
- **Funktion**: Startseite mit Dashlets und persönlichen Paneele
- **Details**:
  - Dashlets hinzufügen, verschieben, entfernen (Bearbeiten-Modus des Dashboards)

### 2. Aktivitäten (Activities)
- **Funktion**: Aufgaben, Anrufe und Termine verwalten
- **Details**:
  - Aufgaben (Tasks) mit Fälligkeit und Status
  - Anrufe (Calls) als Gesprächsnotiz
  - Termine (Meetings) mit Teilnehmern und Reminder

### 3. Leads
- **Funktion**: Interessenten erfassen, qualifizieren und konvertieren
- **Details**:
  - Liste mit Statusfiltern (New, Assigned, Converted)
  - Aktion "Konvertieren" (Assistent) erzeugt Kontakt, Firma, optional Opportunity

### 4. Opportunities (Verkaufschancen)
- **Funktion**: Deals mit Stage, Betrag und Abschlussdatum verfolgen
- **Details**:
  - Liste nach Sales Stage, Betreuer, abgeschlossen/offen filterbar
  - Detailbereich mit Subpanels: Beteiligte Kontakte, Produkte, Notizen, Aktivitäten

### 5. Kontakte und Firmen (Contacts, Accounts)
- **Funktion**: Stammdaten zu Personen und Organisationen
- **Details**:
  - Subpanels für Beziehungen (Firma, Opportunities, Cases, Aktivitäten)
  - Import, Export und Mass Actions

### 6. Support (Cases, Bugs)
- **Funktion**: Kundenanfragen und Fehler verfolgen
- **Details**:
  - Case-Status: New, Assigned, In Progress, Closed, Rejected

### 7. Kommunikation (Emails, Inbound Mail)
- **Funktion**: E-Mail-Ausgang, Archive und Postfachabfrage
- **Details**:
  - E-Mail-Verfassen im Modul "Emails" oder aus dem Datensatz
  - Eingehende Postfächer als Module (Konfiguration im Admin-Bereich)

### 8. Vertriebsergänzung (Products, Quotes, Campaigns, Projects)
- **Funktion**: Produktkatalog, Angebote, Kampagnen und Projekte
- **Details**:
  - Quotes mit Produktzeilen und PDF-Ausgabe
  - Kampagnen mit Zielgruppen (Target Lists) und ROI-Feldern

### 9. Berichte (Reports)
- **Funktion**: Abfragen über Modul- und Feldauswahl erstellen
- **Details**:
  - Berichtsbibliothek mit geteilten und privaten Berichten
  - Gruppen- und Kreuzberichte, CSV-Export

### 10. Benutzer-Menü (oben rechts)
- **Funktion**: eigenes Konto und Darstellung
- **Details**:
  - Mein Profil, Meine Einstellungen (Passwort, Sprache, Theme, Dashboard)
  - Abmelden

### 11. Admin-Menü (nur Administratoren)
- **Funktion**: Instanz verwalten
- **Details** (Auswahl):
  - **Studio**: Felder, Labels und Layouts anpassen
  - **Module Loader**: Erweiterungen installieren und entfernen
  - **Security Suite / Benutzer und Rollen**: Konten, Teams, Rechte
  - **Locale und Währung**: Übersetzungen, Formate, Zeitzone
  - **Scheduler**: geplante Jobs, Cron-Prüfung
  - **Workflow**: Automatisierungsregeln
  - **E-Mail-Einrichtung**: Outbound-Accounts, Inbound-Mail-Server
  - **Reparatur / Cache leeren**: Wartung nach Updates

## Kontext-Menüs

### Aktionenmenü in der Listenansicht
- Bearbeiten, Duplizieren, Löschen
- Mass Actions: Zuweisen, Markieren als Kampagnenziel, Export, Dublettenprüfung
- "Filter" und "Gespeicherte Filter" anwenden

### Detailansicht
- Bearbeiten, Duplizieren, Löschen, Verlauf ansehen
- Subpanel-Menü: Eintrag hinzufügen, bestehende Einträge verknüpfen, Beziehung trennen

### Dashboard
- Dashlet hinzufügen (Auswahlliste verfügbarer Dashlets)
- Dashlet konfigurieren, schließen, in der Reihenfolge ändern

### Rechtsklick
- **Nicht vorhanden**: SuiteCRM bietet keine Rechtsklick-Menüs; Aktionen liegen in Buttons und Dropdowns

## Menüs nach Benutzerrolle

### Administrator
- Volles Admin-Menü (Studio, Module Loader, Security Suite, Scheduler, E-Mail-Einrichtung, Reparatur)
- Alle Module mit Zugriffsrechten "Alle" (eigene, Team- und Fremd-Datensätze)
- Berichte anlegen und teilen, Rollen und Teams pflegen

### Bearbeiter (Standardanwender mit Rechten "Team"/"Eigene")
- Modulmenüs für Leads, Contacts, Accounts, Opportunities, Aktivitäten, Cases
- Eigene und Team-Datensätze bearbeiten, Fremd-Datensätze nur lesen (je nach Recht)
- Dashlets auf der eigenen Startseite, private gespeicherte Filter
- Kein Admin-Menü, kein Module Loader, kein Studio

### Leser (nur Ansichtsrechte)
- Listen und Detailansichten sichtbar, kein Bearbeiten-Schaltfläche
- Berichte ausführen, aber keine eigenen Berichte speichern
- Eigene Dashlets und persönliche Einstellungen weiterhin möglich

## Shortcuts

SuiteCRM veroeffentlicht keine eigene Shortcut-Liste. Die tatsächlich nutzbare Tastatursteuerung (Tab, Enter, Esc, Browser-Tasten) und die ausdrücklich als fehlend markierten Kurzzeichen stehen in [shortcuts.md](shortcuts.md).
