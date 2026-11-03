# SuiteCRM - Funktionen

## Übersicht

SuiteCRM arbeitet modulbasiert: Jedes CRM-Objekt (Lead, Kontakt, Firma, Opportunity, Aktivität) besitzt eine Listen-, Detail- und Bearbeitungsansicht mit Beziehungen (Relationships) zu anderen Modulen. Dashlets, Filter und Berichte sitzen darüber; Anpassungen laufen über Studio, das Workflow-Modul und den Module Loader.

---

## 1. Leads (Interessenten)

- **Erfassung**: Formular mit Name, Firma, Branche, Quelle und Status
- **Statusverwaltung**: `New`, `Assigned`, `In Process`, `Converted`, `Recycled`, `Duplicate`
- **Konvertierung**: Lead wird zu Contact, Account und optional Opportunity
- **Dublettenprüfung**: Similar-Match-Regeln im Admin-Bereich, Warnung beim Speichern
- **Import**: CSV-Import mit Feldzuordnung und Dublettenbehandlung

## 2. Contacts und Accounts (Kontakte und Firmen)

- **Kontakte**: personengebundene Daten, Adressen, Telefon, E-Mail, Team-Zuordnung
- **Firmen (Accounts)**: Hierarchie über die Beziehung "Parent Account"
- **Subpanels**: Kontakte einer Firma, zugehörige Opportunities, Fälle, Aktivitäten
- **Feldverwaltung**: Pflichtfelder, Formate und Standardwerte über Studio
- **Mass Actions**: Dubletten zusammenführen, Felder überschreiben, exportieren

## 3. Opportunities (Verkaufschancen / Deals)

- **Pipeline-Werte**: Sales Stage, Amount, Expected Close Date, Wahrscheinlichkeit
- **Sales Stages**: Stufen wie Prospecting, Qualification, Proposal, Closed Won/Lost
- **Contact Roles**: Rollen der Beteiligten (Entscheider, Einkäufer, Nutzer)
- **Lost Reason**: Verlustgrund als Auswertungsfeld
- **Dashlets**: "Meine Opportunities", "Opportunities nach Sales Stage", Diagramm-Übersicht

## 4. Activities (Aktivitäten)

- **Calls**: Anrufhistorie mit Dauer und Notiztext
- **Meetings**: Termine mit Teilnehmern, Reminder und Dauer
- **Tasks**: Aufgaben mit Fälligkeit und Status (`Not Started`, `In Progress`, `Completed`)
- **Wiederkehrende Aktivitäten**: Serien mit Intervall
- **Kalenderartige Ansicht**: Terminübersicht im Meeting-Modul, Wochen- und Monatsbild

## 5. Cases und Bugs (Support)

- **Cases**: Vorgang mit Status, Priorität, Herkunft, Lösungsnotizen
- **Bugs**: Fehlerberichte mit Produkt- und Versionsbezug
- **Kundenportal**: Self-Service-Portal für Fälle und Wissensartikel (versionsabhängig)
- **Verlauf**: Zeitstempel- und Benutzerhistorie je Datensatz

## 6. E-Mail und Kommunikation

- **Outbound Accounts**: SMTP-Konten im Admin-Bereich, Versand aus der Anwendung
- **Inbound Mail**: Postfächer abfragen, E-Mails als Datensätze ablegen
- **E-Mail-Editor**: Verfassen im Detailview, Archive-Funktion für Postausgang

## 7. Produkte, Preise und Angebote

- **Products**: Produktkatalog mit Kategorien und Listenpreisen
- **Quotes**: Angebote mit Produktzeilen, Rabatten, Endbetrag
- **PDF-Ausgabe**: PDF-Template-Modul für Angebotsdruck (versionsabhängig)
- **Beziehungen**: Quote verknüpft mit Opportunity und Account

## 8. Kampagnen und Targets

- **Kampagnen**: Typ, Budget, Kosten, Status, zugeordnete Zielgruppen
- **Target Lists**: Empfängerlisten (Zielgruppen) mit Filtern
- **Marketing-E-Mails**: Massenversand über Outbound-Account
- **ROI-Auswertung**: Umsatz je Kampagne über verknüpfte Opportunities

## 9. Projekte und Aufgaben

- **Projects und Project Tasks**: Meilensteine, Dauer, einfache Abhängigkeiten
- **Statusverfolgung**: Fortschritt je Aufgabe, Zuordnung zu Kontakten

## 10. Berichte, Filter und Dashlets

- **Report-Modul**: Modulauswahl, Feldfilter, Gruppenberichte, CSV-Export
- **Dashlets**: Paneele auf der Startseite (Meine Aufgaben, Meine Aktivitäten, Pipeline-Diagramm, aktuelle Cases)
- **Gespeicherte Filter**: eigene und geteilte Filter-Sets je Modul
- **Listenwerkzeuge**: Spaltenauswahl, Sortierung, Seitengröße, Volltextsuche

## 11. Automatisierung

- **Workflow-Modul**: Trigger (Datensatz erstellt/geändert), Bedingungen, Aktionen (Feld setzen, E-Mail senden, Aufgabe anlegen, Datensatz zuweisen)
- **Scheduler**: geplante Jobs über `cron.php` (Bereinigung, Kampagnenversand, Workflow-Lauf)
- **Team-Zuweisung**: Zuteilung über Teams und Rollen
- **Audit-Log**: Änderungshistorie je Feld (Standard-Feldverlauf)

## 12. Anpassung und Administration

- **Studio**: Felder anlegen, Labels ändern, Listen- und Detail-Layouts bearbeiten
- **Module Loader**: Erweiterungen als ZIP-Paket mit `manifest.php` installieren
- **Logic Hooks**: PHP-Code an Modellereignissen (`before_save`, `after_save`)
- **Security Suite**: Rollen, Teams und Rechte (View, Edit, Delete, Assign) je Modul
- **Locale und Währung**: Sprachpakete, Zeitzone, Währungsumrechnung
- **Reparaturfunktionen**: Cache leeren, Datenbank prüfen, Beziehungen neu aufbauen

---

## 13. Was SuiteCRM NICHT kann

- **Kein modernes Kanban-Pipeline-Board ab Werk**: Opportunities erscheinen als Liste, Filter und Diagramme; ein Board wie bei Pipedrive fehlt ohne Zusatzmodul
- **Kein E-Mail-Marketing mit Öffnungs- und Klicktracking**: dafür sind Zusatzmodule oder externe Dienste nötig
- **Keine eingebaute Telefonanlage oder CTI**: Anbindung nur über Connectoren oder Drittanbieter
- **Keine grafische Datenbankpflege**: Anpassungen laufen über Studio, Vardefs oder direkten Datenbankeingriff (auf eigenes Risiko)
- **Keine Mandantenfähigkeit**: eine Instanz bedient eine Organisation
- **Keine nativen Mobil-Apps**: Zugriff über den Browser
- **Kein zur Laufzeit konfigurierbares Plugin-System im SaaS-Sinn**: Module werden installiert und aktualisiert
- **Keine eingebaute Ratenbegrenzung** für die API (siehe [api.md](api.md))

---

## 14. Erweiterungen, Module und Connectoren

- **Module-Loader-Pakete**: zusätzliche Feldtypen, PDF-Werkzeuge, Kalender, Portale
- **Themes**: eigene Themes über Template- und CSS-Verzeichnisse
- **Self-Service-Portal**: Modul für externe Kunden mit eigenen Rollen
- **Standardwerkzeuge**: Import/Export, LDAP- und AD-Authentifizierung, Tagging, Audit-Log

---

## Vergleich mit verwandten Systemen

| Funktion | SuiteCRM | EspoCRM | SugarCRM |
|----------|----------|---------|----------|
| Lizenz | AGPL-3.0 | Open Source | kommerziell |
| Pipeline-Board | eingeschränkt (Sales Stages) | vorhanden | vorhanden |
| Support-Module | Cases, Bugs | eingeschränkt | Cases |
| API | REST v8, SOAP | REST | REST |
| Anpassung ohne Code | Studio | Layout-Editor | Studio |

---

## Shortcuts und API

Tastatursteuerung siehe [shortcuts.md](shortcuts.md), Schnittstellen siehe [api.md](api.md).

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [structure.md](structure.md) - Ansichten und UI-Details
- [description.md](description.md) - Abgrenzung und Technik
