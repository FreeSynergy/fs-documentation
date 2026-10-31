# Pipedrive - Beschreibung

## Übersicht

Pipedrive ist ein proprietäres SaaS-CRM aus Estland (seit 2010), das bewusst schmal geschnitten ist: Es organisiert den Vertrieb um Pipeline, Deals und Aktivitäten und verzichtet auf die breiten Marketing- und Service-Funktionen großer Plattformen. Es gibt keine Selbst-Installation; genutzt wird der Dienst im Browser sowie mit offiziellen Mobil-Apps.

## Was Pipedrive macht

Pipedrive verwaltet **Leads** (neue Interessenten, die erst qualifiziert werden), **Persons** (Kontakte), **Organizations** (Firmen), **Deals** (Verkaufschancen in Pipelines mit Stages) und **Activities** (Anrufe, Termine, Aufgaben). Ein Deal trägt Betrag, Abschlussdatum, Wahrscheinlichkeit und beteiligte Kontakte; das Pipeline-Board zeigt den Bestand je Stage. Dazu kommen E-Mail-Synchronisation mit Gmail und Outlook, eine gemeinsame Sales Inbox, Produktliste mit Angebotszeilen, Berichtsbibliothek und regelbasierte Workflows.

## Vorteile

- **Pipeline zuerst**: Kanban-Board mit Stages, Drag & Drop und Abschlusswahrscheinlichkeit
- **Schnell erlernbar**: wenige Konzepte, kurze Einarbeitung für Vertriebsteams
- **E-Mail-Sync in beide Richtungen**: Verläufe landen automatisch am Deal oder Kontakt
- **Sales Inbox**: gemeinsame E-Mail-Adresse des Teams mit Zuordnung zu Datensätzen
- **Eingebaute Automatisierungen**: Workflows für Stage-Wechsel, Aufgaben und Feldwerte
- **Sauber dokumentierte REST-API** mit Personal Token und OAuth2
- **Berichte ab Werk**: Pipeline-Prognose, Aktivitätsberichte, Nutzerleistung

## Abgrenzung zu anderen Systemen

### Pipedrive vs. HubSpot
- **HubSpot** ist eine Plattform mit Marketing-, Content- und Service-Hubs, **Pipedrive** bleibt beim Vertrieb
- **HubSpot** hat umfangreiche Kontaktaufnahme- und Kampagnenwerkzeuge, **Pipedrive** nur ansatzweise E-Mail-Marketing
- **Pipedrive** ist in der Bedienung schlanker, **HubSpot** mächtiger, aber komplexer

### Pipedrive vs. Zoho CRM
- **Zoho CRM** deckt mit Modulen, Deluge-Skripten und Blueprints deutlich mehr Prozesstiefe ab
- **Pipedrive** ist enger auf Sales fokussiert und dadurch einfacher
- **Zoho CRM** ist günstiger im Paket mit weiterer Zoho-Suite, **Pipedrive** punktet bei Pipeline-Führung

### Pipedrive vs. SuiteCRM
- **SuiteCRM** ist Open Source und self-hosted, **Pipedrive** ausschließlich SaaS
- **SuiteCRM** bringt Support-Module und freie Feldmodellierung, **Pipedrive** keine Cases ohne Umweg
- **SuiteCRM** verlangt Administration, **Pipedrive** liefert Updates automatisch

## Technische Details

- **Backend**: geschlossene Serverlandschaft des Anbieters, erreichbar über die REST-API v1
- **Database**: Anbieter-seitig, keine eigene Datenbankwahl; Exporte als CSV über die Oberfläche
- **Frontend**: Browser-Anwendung (Single Page Application), offizielle Apps für iOS und Android
- **Authentication**: Konto mit Passwort, optional Zwei-Faktor-Sicherung; API-Personen-Token und OAuth2
- **Hosting**: ausschließlich Pipedrive-Cloud, kein Self-Hosting; Datenhaltung und Vertragsoptionen je nach Abschluss (versions- und vertragsabhängig)

## Für wen ist Pipedrive geeignet?

- **Kleine und mittlere Vertriebsteams**, die ihre Pipeline visuell führen wollen
- **Agenturen und Dienstleister**, die Deals, Kontakte und E-Mail-Verlauf an einem Ort brauchen
- **Teams ohne IT-Administration**, die ein sofort nutzbares SaaS ohne Projektphase suchen
- **Weniger geeignet** für Support-Tickets, aufwendige Marketing-Kampagnen oder Organisationen, die Daten selbst hosten müssen (dann SuiteCRM oder Zoho CRM)
