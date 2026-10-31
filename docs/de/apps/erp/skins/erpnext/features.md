# ERPNext - Funktionen

## Hauptfunktionen

### Frappe-Doctypes
- Jede Entität = DocType (Schema + Rechte + UI automatisch): Customer, Sales Invoice, Stock Entry…; Custom Fields/Properties ohne Code
- **Client-/Server-Scripts**, Report Builder, Print Formats (Jinja), Benachrichtigungs-Events

### ERP-Decke
- Mehrfirmen-/Konsolidierungsbuchhaltung (IFRS-tauglich), Multi-Währung, Asset, Payroll (länderabhängig), Manufacturing (BOM, Work Orders), Quality, Subcontracting
- Webshop (Frappe-Website), POS, Portal für Kunden/Lieferanten

### Automatisierung
- **Webhooks** (DocType-Änderung → POST, Signing-Secret)
- Scheduler-/Realtime-Events (Socket-IO), Auto-Repeat für Dokumente, Workflow-Engine (Approval-Stufen)

## Was ERPNext NICHT kann

- **UI weniger poliert** als kommerzielle Suites (Lernkurve Frappe-Konzepte)
- **Lokalisierte Buchhaltung** (GOBD/DATEV, lokale Steuer) nur per Community-Addons — DE-Landbuch beachten
- **keine offizielle SaaS-Referenzgröße** wie Odoo Online (hosting: Eigenbau/Frappe Cloud)
- sehr große Transaktionsvolumina → MariaDB-Tuning nötig

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks | offiziell erstklassig |
| Apps im Frappe-Ökosystem | GitHub-Apps (z.B. DE-Buchhaltung) |
| Zapier/Make | Connectoren (Community) |
