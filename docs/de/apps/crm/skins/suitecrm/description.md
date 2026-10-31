# SuiteCRM - Beschreibung

## Übersicht

SuiteCRM ist ein freies, webbasiertes CRM unter AGPL-3.0, das 2013 als Abspaltung der damals offenen SugarCRM-Suite (Stand SugarCRM 6.5) entstand. Gepflegt wird es von einer Community rund um den Anbieter SalesAgility. Die 7er-Linie (7.14.x als LTS) nutzt das klassische Sugar-Frontend, SuiteCRM 8 stellt eine Angular-Oberfläche vor die gleiche Modulschicht.

## Was SuiteCRM macht

SuiteCRM verwaltet Kundendaten und Vertriebsvorgänge in Modulen: **Leads** (unqualifizierte Interessenten), **Contacts** (Kontakte), **Accounts** (Firmen), **Opportunities** (Verkaufschancen/Deals) und **Activities** (Anrufe, Termine, Aufgaben). Dazu kommen Cases und Bugs für Support, Produkte, Angebote (Quotes), Kampagnen, Projekte und Berichte. Rechtestufen, Felder und Layouts werden ohne Programmierung angepasst; Erweiterungen kommen als Module über den Module Loader in die Instanz.

## Vorteile

- **Freie Lizenz**: AGPL-3.0, keine Lizenzkosten, keine bindende Nutzerzahl
- **Self-Hosted**: Daten bleiben auf eigener Infrastruktur (PHP, MySQL/MariaDB)
- **Breite Modulpalette**: Leads, Contacts, Accounts, Opportunities, Cases, Quotes, Projekte ab Werk
- **Anpassbar ohne Code**: Studio für Felder, Labels und Layouts; Workflow-Modul für Automatismen
- **API-Zugang**: REST-Schnittstelle (v8) und SOAP auf Modulbasis
- **Erweiterbar**: Module Loader, Logic Hooks, Connectoren, eigene Themes
- **Deutsche Oberfläche**: Sprachpakete inklusive

## Abgrenzung zu anderen Systemen

### SuiteCRM vs. SugarCRM
- **SugarCRM** ist die kommerzielle Weiterentwicklung mit Cloud-Angebot und neueren Funktionen
- **SuiteCRM** basiert auf der letzten offenen Sugar-Version und bleibt vollständig frei
- **SugarCRM** bietet mehr Komfort, **SuiteCRM** die freiere Lizenz und Selbstverwaltung

### SuiteCRM vs. EspoCRM
- **EspoCRM** ist schlanker, moderner und schneller, dafür funktional schmaler
- **SuiteCRM** deckt mehr Bereiche ab (Support, Kampagnen, Angebote, Projekte)
- **EspoCRM** ist leichter zu pflegen, **SuiteCRM** mächtiger, aber komplexer

### SuiteCRM vs. CiviCRM
- **CiviCRM** ist auf Vereine und Verbände (Constituent Management) zugeschnitten und hängt an einem CMS
- **SuiteCRM** ist ein eigenständiges Vertriebs-CRM mit Pipeline-Orientierung
- **CiviCRM** stark bei Spenden und Mitgliedschaften, **SuiteCRM** bei Leads und Deals

## Technische Details

- **Backend**: PHP in der SugarCRM-Architektur (Module, Vardefs, Logic Hooks); SuiteCRM 8 mit zusätzlichem Symfony-Layer vor der Legacy-Schicht
- **Database**: MySQL oder MariaDB
- **Frontend**: 7.x Template-Sätze (Handlebars) und JavaScript im Sugar-Layout; 8.x Angular-Shell mit eigenem Theme
- **Authentication**: lokale Konten mit Rollen und Teams, optional LDAP-/Active-Directory-Anbindung, Session-Cookie im Browser
- **Hosting**: Apache oder nginx mit PHP, Docker-Images von Community und SalesAgility, Scheduler über `cron.php`; Shared-Hosting ist möglich

## Für wen ist SuiteCRM geeignet?

- **Kleine und mittlere Unternehmen**, die ein vollständiges CRM ohne Lizenzkosten selbst betreiben
- **Vertriebs- und Supportteams**, die Leads, Deals und Fälle in einer Instanz bündeln
- **Administratoren mit PHP-/MySQL-Kenntnissen**, die Felder, Layouts und Workflows selbst pflegen
- **Weniger geeignet** für Teams, die eine moderne Oberfläche ohne Administrationsaufwand erwarten (dann EspoCRM oder eine SaaS-Lösung)
