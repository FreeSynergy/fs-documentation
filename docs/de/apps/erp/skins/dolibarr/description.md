# Dolibarr - Beschreibung

## Was das Programm macht

Dolibarr deckt das Kaufmännische eines kleinen Unternehmens: wer (Dritte), was (Artikel), welche Papiere (Angebote bis Zahlung), welches Lager, welches Projekt. Auf jedem Webspace lauffähig, seit über 20 Jahren gepflegt.

## Vorteile

- **LAMP-Betrieb ohne Spezialwissen**, enorm stabil
- **modular**: was du nicht einschaltest, siehst du nicht
- API + Triggers reichen für Automationen (mit Maß)

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Odoo/ERPNext** | Suite-Tiefe (Fertigung, HR, Website); Dolibarr bewusst kleiner |
| **Lexware/wiso** | closed SaaS; Dolibarr quelloffen selbst gehostet |
| **CiviCRM** | NPO-Spezialist; Dolibarr hat Vereinsmodul + kommerzielle Kette |

## Technische Details

- **Stack**: PHP 8, MariaDB/MySQL; Mulitinstanzen-Setup möglich
- **Auth**: Session-Login; API: API-Key (`Authorization: Bearer <key>`) oder Session-Token
- **Deploy**: Shared Hosting, Docker-Images, Docker-Community-Builds
- **Lizenz**: GPL

## Für wen geeignet

- kleine Firmen/Vereine mit eigenem Hosting und Papierkram-Fokus
- FreeSynergy-Szenarien: leichter ERP-Counterpart für CRM-/Invoice-Skins
