# Request Tracker - Beschreibung

## Was das Programm macht

RT verwandelt jede E-Mail in ein Ticket und organisiert Arbeit über Queues, Rechte und Scrips. Der Kern ist kompromisslos protokollorientiert: Ticketzustand, Beteiligte und Historie werden als Transaktionen geführt; Automatisierung passiert als Perl-Skript an der Transaktion.

## Vorteile

- **Skaliert extrem**: seit 1996 in Betrieben mit > 1 Mio. Tickets im Feld
- **Alles scriptbar**: E-Mail-Adressen-Aliase, Scrips, REST/CLI — Automatisierung ohne Plugin-Zoo
- **Auditierbar**: jede Änderung ist Transaktion mit Autor, Zeit, Grunde

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Zammad** | gleiches Grundproblem, aber modernes UI + Elasticsearch; RT ist „unixiger“ |
| **osTicket** | einfacher, weniger Automatisierung |
| **GLPI** | Helpdesk + Assets; RT fokussiert Ticket-Workflow |

## Technische Details

- **Backend**: Perl (Mason-Web-Framework), MySQL/PostgreSQL/Oracle
- **Frontend**: serverseitig generiertes HTML, RT 5 mit neuerem MUI-Grundgerüst
- **Authentifizierung**: intern, LDAP, ExternalAuth (Shibboleth/OIDC-Module)
- **Hosting**: klassischer App-Server (Apache/mod_perl oder starman), Cron `rt-crontool`
- **Lizenz**: GPL (Community), Best Practical bietet GPL-konforme Support-Abos

## Für wen geeignet

- techniklastige Organisationen mit eigenem Ops-Team
- Migrationsfälle, in denen jede E-Mail-Adresse ein Workflow sein soll
- FreeSynergy-Skins, die „Ticket als Transaktionsprotokoll“ modellieren wollen
