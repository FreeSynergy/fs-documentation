# osTicket - Funktionen

## Hauptfunktionen

### Ticketentstehung
- E-Mail-Ingest per POP3/IMAP-Fetcher (Catch-All oder Antwort-Adresse)
- Web-Formulare (öffentliche Ticketformulare mit Captcha)
- API-Endpunkt (siehe api.md)
- Help Topics als Entry-Punkte, optional an Formulare gebunden

### Workflow
- Ticketstatus new → open → pending → closed mit konfigurierbaren Statusarten
- Filterregeln: eingehende Mails nach Muster/Domain/Empfänger klassifizieren (Topic, Group, Priority, Auto-Reply, Ticket-Nummer im Betreff erhalten)
- SLA-Pläne mit Fälligkeitsgrad je Priority, business hours
- Zuweisung an Agenten und Teams, Zusammenarbeit über geteilte Tickets

### Kunden und Wissen
- Kunden-/Organisationsprofile mit benutzerdefinierten Feldern (Formulare)
- Kundenportal mit eigener Ticketliste, FAQ (Knowledge Base), Artikel-Kategorien

### Betrieb
- Plain PHP + MySQL, Shared-Hosting-tauglich
- Backups per Datenbankdump + upload-Ordner

## Was osTicket NICHT kann

- **Keine Volltextsuche-Engine** (MySQL LIKE — langsam ab großer Historie)
- **Keine Echtzeit-Kollaboration** (kein WebSocket, kein Live-Feed)
- **Keine Kanäle wie Chat/Telegram/Telefon** out of the box (nur E-Mail/Web)
- **Keine mehrstufigen Workflows/BPM** und keine Business-Rules-Engine (nur einfache Filter)
- **Kein Asset-/ITSM-Modul** (GLPI-Domäne)
- **Kein modernes Theme-System**; Customizing = Templates forken
- **Keine offizielle Cloud** (nur Third-Party-Hostings)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| API v1 | API-Key, Tickets/ Benutzer erstellen/lesen |
| Cronjob | Fetching, SLA-Eskalation, Automations |
| LDAP | Login für Staff und Kunden (optional) |
| Plugins | offizielles Plugin-Ökosystem klein;Community-Patches existieren |
