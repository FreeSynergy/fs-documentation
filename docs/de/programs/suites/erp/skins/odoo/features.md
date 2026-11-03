# Odoo - Funktionen

## Hauptfunktionen

### Integrierte Suite
- CRM/Lead→Quotation→Auftrag→Rechnung→Zahlung durchgängig; Lager (Double-Entry-Flows, Barcodes), Fertigung (MRP/BOM), Projekte/Task, HR (Urlaub, Gehalt Enterprise), Website/Shop/POS
- Gemeinsame Modelle (`res.partner` für Kunden/Lieferanten/Kontakte) → saubere Datenrelationen

### Anpassbarkeit
- **Module als Python-Pakete**: Modelle (ORM), Views (XML), Rechte, Menüs; Vererbung von Bestehendem (`inherit_id`)
- **Studio** (Enterprise): Felder/Views/Automations ohne Code; Automationen (ir.ql-Trigger)
- Views-Typen: Kanban/List/Form/Kalender/Pivot/Graph, Dashboards

### Betrieb
- Multi-Company/Multi-Währung/Multi-Language, Portal-Zugang, E-Mail-Flows (Alias→Datensatz), qReport-PDF

## Was Odoo NICHT kann

- **Enterprise-Features kostenpflichtig** (Buchhaltung voll nur Ent, Studio, Mobile-Barcode)
- **ORM-API mächtig, aber kein sauberes öffentliches REST** (XML-RPC Standard; REST-Modul neu/Enterprise-abhängig — Stand prüfen)
- **Updates zwischen Großversionen** erfordern Migration (Custom-Code-Falle)
- **HOIA-/Konsolidierungstiefe** unter SAP/DATEV-Niveau (Add-ons nötig)
- Sehr generisches UI: Einarbeitung braucht Konfigurationsdisziplin

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| App-Store (40k+ Module) | teils kommerziell |
| XML-RPC/JSON-RPC + Webhooks (Ent) | offiziell |
| Payment/Versand-Shippers | offizielle Provider |
