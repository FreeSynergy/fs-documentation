# Odoo - Beschreibung

## Was das Programm macht

Odoo verdrahtet Unternehmen in einer Suite: ein Lead wird zum Angebot, zur Lieferung, zur Rechnung — dieselbe Datenbank, dieselben Partner-Modelle. Der Open-Source-Core plus modulare Erweiterbarkeit macht es zum Baukasten-ERP.

## Vorteile

- **ein System statt Insellösungen** (CRM+ERP+Website aus einem Guss)
- **Community gratis & selbst hostbar**; Cloud/Odoo.sh für Komfort
- **ORM/Modulsystem** = Anpassungen first-class

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **ERPNext** | ähnlich offener Ansatz, Framework Frappe; Odoo größere Community/App-Store |
| **SAP** | Konzernprozesse/Zertifizierungen; Odoo KMU-flexibler |
| **Dolibarr** | schlanker (KMU-Rechnung/Lager); Odoo breiter/tiefer |

## Technische Details

- **Stack**: Python, PostgreSQL; Web-Frontend (Web Framework OWL), qWeb-Berichte
- **Modelle**: ORM mit Feldtypen, Compute/Onchange, rekursive Vererbung
- **Authentifizierung**: Session Login, portal; API: RPC-Token/OAuth2 (neuere APIs), 2FA
- **Deploy**: own Server, Docker, odoo.sh, Odoo Online (SaaS)
- **Lizenz**: LGPL (Community) + proprietäre Enterprise-Apps

## Für wen geeignet

- KMU/Mittelstand, die ERP+CRM+Web aus einer Hand und anpassbar wollen
- FreeSynergy-Skins: `res.partner`/`sale.order`-Muster als Referenz für Adress-/Auftragsmodelle ([modelle.md](../../../../data/modelle.md))
