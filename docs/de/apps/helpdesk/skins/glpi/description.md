# GLPI - Beschreibung

## Was das Programm macht

GLPI verbindet Support-Tickets mit dem kompletten IT-Inventar: jedes Ticket kann an einen Rechner, einen Vertrag oder ein Netzwerkobjekt gebunden werden; Änderungen und Probleme werden als verknüpfte Objekte geführt. Dazu kommen Self-Service-Portal, Wissensdatenbank und Auto-Inventur.

## Vorteile

- **ein System für Helpdesk + Assets** — ersetzt zwei Tools
- **bewährt in Behörden/unis** (seit 2003, riesige Community, deutsch übersetzt)
- **Rules-Engine** für Zuweisungen, Statuswechsel, Benachrichtigungen
- **kostenlos** (GLPI-Network bietet kommerzielle Support-Versionen an)

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Zammad** | reiner, moderner Support-Cockpit ohne Assets — Zammad ist UX-getrieben, GLPI datenmodell-getrieben |
| **Request Tracker** | starker Ticket-Workflow, keine Assets |
| **Snipe-IT** | fokussiert Asset-Management ohne Helpdesk — GLPI kann beides |

## Technische Details

- **Backend**: PHP 8+, MySQL/MariaDB; Cron für SLA/Inventur-Queue
- **Frontend**: servergerendertes UI (Tabulator-Tabellen), Portal responsive
- **Authentifizierung**: intern, LDAP, CAS, OIDC-Plugins; API-Token
- **Hosting**: LAMP, Docker-Images (offiziell glpi/glpi), Hochverfügbarkeit über DB-Replikation
- **Lizenz**: GPL

## Für wen geeignet

- IT-Abteilungen, die Inventar und Tickets verzahnen müssen
- Öffentliche Verwaltung/Bildung mit SSO-Anforderungen
- FreeSynergy-Skins mit Asset+Ticket-Verknüpfung als Datenmodell-Vorlage
