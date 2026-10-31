# Google Kalender - Beschreibung

## Übersicht

Google Kalender ist der Kalender-Baustein von Google: ein Cloud-Kalender für Privatkonten und für Organisationen mit Google Workspace. Er ist als Web-Anwendung (calendar.google.com) und als App für Android und iOS verfügbar und deckt Termine, Serientermine, Aufgaben, Kalenderfreigaben, Ressourcenbuchung und Mehrpersonentermine ab. Der Zugang nach außen läuft über die Calendar REST API v3, CalDAV und ICS-Abonnements.

## Was Google Kalender macht

Nutzer legen einen oder mehrere Kalender an und tragen Termine mit Anfang, Ende, Ort, Beschreibung, Farbe und Erinnerung ein. Termine können mit Gästen geteilt werden; Google Kalender verschickt Einladungen per E-Mail und verwaltet die Antworten (Ja/Nein/Vielleicht). Wiederholungen, Ausnahmen, Zeitzonen und Arbeitszeiten werden automatisch berücksichtigt. Über die Freigabestufen sehen andere Personen nur belegte Zeiten, alle Details oder dürfen selbst Termine anlegen. Administratoren einer Workspace-Domäne setzen unternehmensweite Richtlinien (externe Freigabe erlauben oder sperren), verwalten Räume und Geräte als Ressourcenkalender und richten Teams-/Gruppenkalender ein. Die Web-Oberfläche zeigt Tag, Woche, Monat, Jahr und Agenda; Termine lassen sich per Drag & Drop verschieben und in der Länge ändern.

## Vorteile

- **Nahtlose E-Mail-Verzahnung**: Einladungen, Antworten und Meet-Links entstehen direkt aus Gmail und Kalender
- **Zero Administration im Privatbereich**: kein Server, keine Updates, keine Datenbank
- **Schnelle Eingabe**: "Schnell erstellen" verarbeitet natürlichsprachliche Terminangaben
- **Saubere Zeitzonenbehandlung**: Termine bleiben normiert, Anzeige je Zeitzone der Beteiligten, zweite Zeitzone einblendbar
- **Breite Client-Unterstützung**: Apple Kalender, Thunderbird, Outlook, Evolution, Fantastical, DAVx5 über API/CalDAV/ICS
- **Ausgereifte REST-API**: JSON, OAuth 2.0 mit feingliedrigen Scopes, Sync-Tokens, Push-Kanäle, Batches
- **Teamfunktionen**: Freigabestufen, Ressourcen, Arbeitsorte, Fokuszeit, Terminplan-Buchungsseiten
- **Barrierefreiheit und Themes**: helle/dunkle Oberfläche, Symbolsystem pro Kalender, Tastaturkürzel, Screenreader-Unterstützung

## Abgrenzung zu anderen Systemen

### Google Kalender vs. Outlook-Kalender (Microsoft 365 / Exchange)
- **Organisationstiefe**: Exchange/Outlook bietet Delegationsmodelle, öffentliche Ordner, freigegebene Postfächer und detaillierte Ressourcenverwaltung mit Kapazität und Genehmigungsregeln; Google Kalender hält Freigaben bewusst einfacher
- **Offline/Client**: Outlook (Desktop) arbeitet mit lokaler Cache-Datei und ist offline voll nutzbar; Google Kalender ist online-zentriert
- **Protokolle**: Exchange nutzt EWS/Graph und MAPI; Google nutzt Calendar API v3 und CalDAV
- **Administration**: Workspace-Admin Console vs. Microsoft 365 Admin Center/Exchange Online - beide proprietär, beide Cloud-only

### Google Kalender vs. Nextcloud Calendar
- **Hosting**: Nextcloud läuft auf eigenem Server (Self-Hosting), Google Kalender ausschließlich in der Google-Cloud
- **Protokoll**: Nextcloud Calendar ist ein CalDAV-Client auf einer Nextcloud-Instanz (Termine in der Instanz-Datenbank, Standard-Backend CalDAV/Sabre); Google Kalender ist ein geschlossener Dienst mit eigener REST-API
- **Datenschutz**: bei Nextcloud liegen Daten im eigenen Rechenzentrum; bei Google in der Google-Infrastruktur (mit AV-Vertrag für Workspace)
- **Komfort**: Google punktet bei Vorschlägen, Meet-Integration und Mobil-Apps; Nextcloud bei Kontrolle, Gruppenordnern und Kombination mit Dateien/Tasks

### Google Kalender vs. CalDAV-Selbstbau (Radicale, BAïkal, DAVx5)
- **Umfang**: Radicale/BAïkal sind reine CalDAV-/CardDAV-Server ohne eigene Kalender-Oberfläche; Google Kalender bringt Oberfläche, Mobile Apps und Vorschlagslogik mit
- **Rechte**: beim Selbstbau über Dateiberechtigungen bzw. kleine ACL-Tabellen geregelt, bei Google über Freigabestufen und Domänenrichtlinien
- **Automatisierung**: Selbstbau erlaubt direkten Datenzugriff (SQLite/PostgreSQL, Dateisystem), Google Kalender nur über API und Export

## Technische Details

- **Backend**: proprietärer Google-Dienst; Server-Code ist nicht offen. Programme der Google-Cloud-Infrastruktur, keine öffentlich dokumentierte Einzelkomponente
- **Datenbank**: Google-interne Speicherdienste; für Nutzer nicht einsehbar und nicht direkt abfragbar. Persistente Mitnahme nur als ICS-Datei oder über Google Takeout
- **Frontend**: Web-App (JavaScript-Einzelapplikation im Material-Design-Stil, Roboto-Schrift, Raster-Renderer für Tag/Woche/Monat) sowie native Apps für Android und iOS; das konkrete Framework der Web-App ist nicht öffentlich dokumentiert
- **Synchronisation**: Calendar REST API v3 (`https://www.googleapis.com/calendar/v3`), CalDAV für Kalender-Clients (für Workspace-Accounts administrativ zu aktivieren), ICS-Abonnement- und Embed-URLs
- **Authentifizierung**: Google-Konto mit Passwort und 2-Schritt-Bestätigung; OAuth 2.0 (Access-/Refresh-Token) für API-Zugriffe; Workspace-SSO (SAML/OIDC) und Geräteverwaltung über Admin Console; API-Schlüssel nur für öffentliche Kalender-Lesezugriffe
- **Berechtigungen**: Freigaben als ACL-Regeln pro Kalender (owner, writer, reader, free/busy reader); domänenweite Richtlinien der Admin Console
- **Client-seitige Erweiterungen**: Google Workspace Add-ons und Apps Script (`CalendarApp`)
- **Hosting**: ausschließlich Cloud/SaaS; kein Docker-Image, kein On-Premise-Betrieb. Kontomodelle: Privatkonto (kostenlos), Google Workspace Business/Enterprise (kostenpflichtig, mehr Admin- und Compliance-Funktionen)
- **Datenschutz-Hebel**: Datenexport (ICS/Takeout), Aufbewahrungs- und Löschfristen über Workspace-Admin, Verschlüsselung während Übertragung und in den Google-Rechenzentren; eine Ende-zu-Ende-Verschlüsselung für Kalenderinhalte ist nicht dokumentiert

## Für wen ist Google Kalender geeignet?

- **Privatnutzer im Google-Ökosystem**, die Gmail, Android und Kalender ohne Administration verbinden wollen
- **Kleine und mittlere Teams in Google Workspace**, die Teamkalender, Ressourcenräume und einfache Freigabestufen brauchen
- **Veranstalter mit externen Teilnehmern**, die buchbare Terminplan-Seiten oder öffentliche ICS-Kalender nutzen
- **Entwickler**, die Kalenderfunktionen per sauber dokumentierter REST-API anbinden möchten
- **Weniger geeignet** für Behörden und Firmen mit strikter Datenhoheits-Anforderung, für reine Offline-Arbeitsplätze, für organisationsweite Genehmigungsworkflows und für alle, die den Kalender auf eigener Hardware betreiben müssen (dann Nextcloud Calendar oder ein CalDAV-Server)
