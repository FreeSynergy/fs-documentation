# Pipedrive - Funktionen

## Übersicht

Pipedrive arbeitet mit fünf Kernobjekten — Leads, Persons, Organizations, Deals und Activities — die über Pipelines, Stages und Aktivitäten auf den Abschluss ausgerichtet werden. E-Mail-Sync, Sales Inbox, Produktliste und Workflows sind direkt angebaut; Erweiterungen kommen überwiegend aus dem Marketplace oder über die API.

---

## 1. Leads (Interessenten)

- **Lead-Erfassung**: Name, Quelle, Kontaktweg, Betragsschätzung
- **Lead-Box**: Sammeln und Qualifizieren vor der Pipeline
- **Qualifizierung**: Lead wird zu Deal mit Kontakte und Firma (ein Klick)
- **Verwerfen mit Grund**: verlorene Leads bleiben auswertbar
- **Import**: CSV-Import mit Feldzuordnung und Dublettenprüfung

## 2. Persons (Kontakte)

- **Kontaktdaten**: Name, Firma, Rollenbezeichnung, Telefon, E-Mail, Adresse
- **Beziehungen**: Kontakte an Organisationen und an mehrere Deals
- **Aktivitätsverlauf**: gesammelte E-Mails, Anrufe, Notizen je Kontakt
- **Felder**: eigene Felder über das Custom-Fields-Setup
- **Dubletten**: Warnung bei gleicher E-Mail-Adresse oder Telefonnummer

## 3. Organizations (Firmen)

- **Firmenstamm**: Name, Adresse, Branche, eigene Felder
- **Baumstruktur**: Eltern- und Tochterfirmen über ein Beziehungsfeld
- **Kontaktliste** und zugehörige Deals in der Detailansicht
- **Nutzung ohne Firmen**: kleinere Teams arbeiten nur mit Kontakten

## 4. Deals und Pipelines

- **Pipeline-Board**: Spalten je Stage, Kacheln je Deal, Spaltenreihenfolge per Drag & Drop
- **Mehrere Pipelines**: etwa "Neugeschäft" und "Bestandskunden", jeweils mit eigenen Stages
- **Deal-Felder**: Betrag, Währung, Abschlussdatum, Wahrscheinlichkeit, Quelle, Verantwortlicher
- **Abschlussbehandlung**: Verschieben in "Won" oder "Lost"; bei Verlust Grundabfrage
- **Listenansicht**: Tabelle mit Filtern, Sortierung und Spaltenauswahl
- **Prognose**: gewichtete Pipeline-Summe je Stage

## 5. Activities (Aktivitäten)

- **Typen**: Aufgabe, Anruf, Termin, E-Mail-Besprechung; eigene Typen anlegbar
- **Zeitplan**: Tages- und Wochenansicht mit fälligen Aktivitäten
- **Erinnerungen**: Benachrichtigung zum Zeitpunkt, auch per E-Mail
- **Mehrere Bearbeiter**: Aktivitäten mehreren Nutzern zuweisen
- **Aktivitäts-Speicherung**: erledigte Aktivitäten bleiben am Deal protokolliert

## 6. Produkte und Angebote

- **Produktliste**: Katalog mit Standardpreis und Währung
- **Deal-Produkte**: Produktzeilen mit Menge und Einzelpreis am Deal
- **Umsatz je Deal**: Summe der Produktzeilen oder Einzelfeld
- **Angebotsversand**: PDF- bzw. Angebotsfunktion als Zusatzfunktion (versionsabhängig)

## 7. E-Mail und Sales Inbox

- **Zweiseitiger Sync**: Gmail und Outlook (Add-in), IMAP/SMTP für andere Anbieter
- **Zuordnung**: E-Mails werden Kontakten und Deals automatisch zugeordnet
- **Sales Inbox**: gemeinsame Team-Adresse mit Bearbeiter-Zuweisung
- **E-Mail-Vorlagen**: persönliche und geteilte Vorlagen mit Platzhaltern
- **Nachverfolgung**: Lese- und Klick-Status bei versendeten E-Mails (versionsabhängig)

## 8. Automatisierung

- **Workflows**: Auslöser (Deal angelegt, Stage gewechselt, Feld geändert) plus Aktionen
- **Aktionen**: Aufgabe anlegen, Feld setzen, E-Mail senden, Benachrichtigung, Lead zuweisen
- **Pipeline-Automation**: Stage-Regeln und Pflichtfelder je Stage
- **Bedingungen**: Filter je Workflow, etwa nur Deals über einem Betrag

## 9. Berichte und Prognosen

- **Berichtsbibliothek**: Pipeline-Berichte, Aktivitätsberichte, Nutzerleistung, Quellenanalyse
- **Eigene Berichte**: Achse, Metrik und Filter frei kombinieren
- **Prognose**: gewichtete Abschlüsse je Monat oder Quartal
- **Team-Leistung**: Aktivitäten und Abschlüsse je Nutzer und Team

## 10. Konfiguration und Rechte

- **Pipelines und Stages**: anlegen, umbenennen, Reihenfolge ändern
- **Custom Fields**: Text, Zahl, Datum, Auswahl, Kaskade, Datei (Feldtypen versionsabhängig)
- **Nutzer und Lizenzen**: Regular, Restricted und Admin; Lizenzzuweisung im Abrechnungs-Setup
- **Sichtbarkeitsgruppen**: wer welche Deals und Kontakte sieht
- **Import- und Feldeinstellungen**: Pflichtfelder, Standardwerte, Formate

## 11. Was Pipedrive NICHT kann

- **Kein Ticketsystem / Support-Cases**: keine Fallverwaltung mit SLA (Hilfsobjekte nur über Felder oder Zusatz-Apps)
- **Kein umfangreiches E-Mail-Marketing**: keine Landingpages, Formulare oder Segmentierungs-Engine wie bei HubSpot
- **Keine freie Feldmodellierung neuer Objekte**: eigene Module sind nicht anlegbar
- **Kein Self-Hosting**: Daten liegen ausschließlich beim Anbieter
- **Keine CalDAV- oder CardDAV-Schnittstelle**: Kalenderabgleich läuft über die Anbieter-Integrationen
- **Keine GraphQL-API** und keine offizielle Server-seitige Ereignis-API außer Webhooks
- **Keine mehrstufigen Freigabe-Workflows** (Genehmigungen) wie in Zoho CRM
- **Kein kostenloses Dauer-Abo**: Nutzung kostenpflichtig pro Nutzer und Monat

## 12. Erweiterungen, Marketplace und Integrationen

- **Marketplace**: fertige Integrationen (E-Mail, Telefonie, Formulare, Buchhaltung, Rechnungen)
- **Webhooks**: Ereignisse an eigene Systeme melden (siehe [api.md](api.md))
- **Formular-Einbettung**: Website-Formulare füllen Leads oder Kontakte
- **Zapier, Make und n8n**: vorgefertigte Verbindungen zu Fremd-Apps
- **Browser-Erweiterungen**: E-Mail-Anbindung für Gmail und Outlook
- **Mobil-Apps**: iOS und Android mit Pipeline, Aktivitäten und E-Mail-Funktionen

---

## Vergleich mit verwandten Systemen

| Funktion | Pipedrive | HubSpot | Zoho CRM |
|----------|-----------|---------|----------|
| Pipeline-Board | sehr ausgereift | vorhanden | vorhanden |
| Marketing-Hub | eingeschränkt | umfangreich | umfangreich |
| Support-Tickets | nicht vorhanden | vorhanden (Service Hub) | vorhanden |
| Eigene Objekte | nicht möglich | eingeschränkt (Custom Objects, planabhängig) | möglich |
| Skriptengine | keine | Workflow-Logik | Deluge |

---

## Siehe auch

- [menu.md](menu.md) - Navigation und Rollen
- [structure.md](structure.md) - Board, Deal-Detail, Themes
- [api.md](api.md) - REST-API, Token, Webhooks
