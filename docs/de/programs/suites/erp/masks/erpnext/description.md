# ERPNext - Beschreibung

## Was das Programm macht

ERPNext liefert das komplette ERP (bis Buchabschluss) unter freier Lizenz und stellt die Technik als Framework bereit: DocTypes definieren Datenwelt, API/Webhooks inklusive. Wer Frappe versteht, bedient ERPNext mühelos.

## Vorteile

- **100 % FOSS, keine Feature-Walls** (im Gegensatz zu Odoo Enterprise)
- **beste API-Praxis** im ERP-Bereich (JSON-Rest, DocType-Schema maschinenlesbar)
- Frappe-Ökosystem auch für Nicht-ERP-Apps (Customer Portal, Helpdesk)

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Odoo** | breiterer Store/Komfort, aber Enterprise-Fenster; ERPNext kompromisslos offen |
| **Dolibarr** | einfacher (KMU-Rechnungslast); ERPNext volle Fertigung/HR |
| **SAP Business One** | proprietär/lizenziert; ERPNext gleichwertiger Kern, andere UX |

## Technische Details

- **Stack**: Python (Frappe), MariaDB, Redis, Node-Build-Assets; Socket-IO für Echtzeit
- **Modelle**: DocTypes (JSON-Schema + Controller-Klassen), Linked Documents, Name Series
- **Auth**: Session, **Token (`Authorization: token key:secret`)**, OAuth2/OIDC
- **Deploy**: Bench-CLI (eigene Server), Docker, Frappe Cloud
- **Lizenz**: GPLv3

## Für wen geeignet

- IT-affine KMU/Mittelständler mit Datenhoheits-Anspruch
- FreeSynergy-Szenarien: Referenz-ERP für API-Sync-Skins (Adressen/Aufträge ↔ CRM)
