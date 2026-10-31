# Tryton - Beschreibung

## Was das Programm macht

Tryton ist ERP für Menschen, die Ordnung lieben: kleine, saubere Module, durchdachte Zustandsmodelle, keine Feature-Masse. Der Desktop-Client wirkt wie eine Datenbank-IDE fürs Kaufmännische — schnell, konsistent, ehrlich.

## Vorteile

- **extrem stabil/langlebig**, Upgrade-Pfade diszipliniert
- **echte Open Source** (kein Open-Core)
- RPC-Schnittstelle geradlinig — Automatisierung ohne Marketing-API

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Odoo** | Suite+Web+Store; Tryton fokussiert und schmal |
| **GnuCash** | nur Buchhaltung Einzelplatz; Tryton Mehrbenutzer-ERP |
| **ERPNext** | Framework-Bärenumfang; Tryton Modulsparse |

## Technische Details

- **Stack**: Python (trytond), PostgreSQL; GTK-Clients; Web-UI integriert
- **Modell**: ORM mit `Model.<name>.execute` RPC-Methoden
- **Deploy**: Debian-Pakete, Docker, eigene Server
- **Lizenz**: GPL

## Für wen geeignet

- Genossenschaften/Büros mit IT-Kompetenz und Bestandsdenken
- FreeSynergy-Szenarien: stabiler Buchhaltungs-Backend-Skin (Journals/Reconcile)
