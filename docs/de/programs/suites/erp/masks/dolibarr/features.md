# Dolibarr - Funktionen

## Hauptfunktionen

### Kernprozesse KMU
- Dritte mit Kontakten, Kommerzielle Kette (Angebote→Bestellung→Lieferung→Rechnung→Zahlung), Artikel/Lager (mehrere Lagerplätze), Projekte mit Aufgaben/Zeiterfassung
- Vereinsmodul (Mitglieder/Beiträge) — NPO-geeignet wie kaum ein anderes ERP

### Technik
- PHP-Modulsysteem mit **Triggers/Hooks** (`modXxx` Klassen, z.B. `COMPANY_CREATED`), Extension-Markt (DoliaCloud/Dolistore)
- PDF-Modelle (ODT-basiert), E-Mail-Aktionen (fakturierte Rechnungen versenden), Import/Export-Assistenten
- **REST-API v3** + API-Key-Verwaltung; Webhooks über Modul „API REST hooks“

## Was Dolibarr NICHT kann

- **keine Fertigungssteuerung/MRP** (einfache Fertigung ja, kein Planning)
- **Buchhaltung = vereinfachtes Journal**; DATEV/GOBD-Export nur über Add-ons
- **keine echte Mandantenfähigkeit** pro Instanz (Multi-Company rudimentär)
- **UI funktional-altbacken** (Frames-Layout-Ära), keine Kanban-Ästhetik
- Hochperformante Multi-Tenancy: nein

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Dolistore-Module | kommerziell/frei |
| REST v3 + Webhooks-Modul | offiziell |
| Zahlungsdienstleister/PayPal | Module |
