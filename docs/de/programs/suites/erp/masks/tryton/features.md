# Tryton - Funktionen

## Hauptfunktionen

- **Modul-Cocktail**: Account (mehrstufige Pläne, Multi-Currency), Sale/Purchase (Freigabestufen), Stock (Locations, Moves, Lot/Serial), Production (BOM/Work), Project/Timesheet, CRM, Invoice Payment-Reconcile
- **Feldlogik**: „Fields prefill/onchange“, Zustandsfelder (state) mit Workflow-Buttons, Record Rules granular
- **Clients**: Desktop (GTK) + Web; Server multi-instanzig
- **Berichte**: Report-Engine (Py3o/ODT oder PDF), Reports an Dokumenten gebunden

## Was Tryton NICHT kann

- **kein Website-/Shop-/POS-Baukasten** (wie Odoo) — reines ERP
- **kein Drag&Drop-Kanban**, konservative UI
- **weniger fertige Integrationen** (Payment/Shipping) als Odoo — Selbstbau via Module/RPC
- DE-Lokalisierung (GOBD, DATEV) = Community-Arbeit

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| RPC (XML-RPC/JSON-RPC) | offiziell stabil |
| Modul-Ökosystem (Tryton Bugtracker/Community) | überschaubar, qualitativ |
| Tryton-Dev-Kit (Python) | eigene Module als Python-Pakete |
