# Axelor - Funktionen

## Hauptfunktionen

### ERP-Module
- Standard-Kette CRM→Angebot→Auftrag→Rechnung, Stock (Multi-Warehouse), MRP-Fertigung, Account (mehrere Journals), HR (Expense/Leave/Timesheet), Projekte

### Low-Code/BPM (Kern-Differenzierung)
- **App Builder**: Modelle + Views + Menüs ohne Deployment; **BPM-Designer** (BPEs, Aufgaben, Mail-Aktionen) mit Zuständigkeiten
- Action-Runner/Dashboards per Konfiguration

### Technik
- REST-Automatik pro Modell (`/ws/rest/partner`, `/ws/rest/saleOrder`…), JSON-Batch, Workflow-Trigger per API
- Berichte (Jasper-Reports), DMS/Document-Module

## Was Axelor NICHT kann

- **Community kleiner** als Odoo — Add-on-Markt begrenzt
- **UX gewöhnungsbedürftig** (Builder-Denken, Französisch-geprägte Historie)
- **GOBD/DE-Lokalisierung** nur teils (Community-Module prüfen)
- kein SaaS-Riesenbetrieb wie Odoo Online; Axelor Cloud kleiner

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST je Modell + BPM-Aktionen | offiziell |
| Java-Module im Kern erweiterbar | Entwicklerweg |
| Axelor Store | kommerzielle Zusatzmodule |
