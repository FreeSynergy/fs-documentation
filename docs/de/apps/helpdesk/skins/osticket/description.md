# osTicket - Beschreibung

## Was das Programm macht

osTicket wandelt eingehende E-Mails in Tickets um, weist sie Teams zu und begleitet sie bis zur Antwort. Es hält den Workflow minimal: Help Topics, Status, Prioritäten, SLA-Fristen — mehr nicht, und genau das ist die Stärke.

## Vorteile

- **läuft überall**: PHP/MySQL genügt, auch Shared Hosting
- **schnell gelernt**: Agenten brauchen keine Schulung
- **E-Mail-zentriert** ohne Webzwang: Kunden antworten schlicht per Mail
- **Vorhersagbar**: keine Feature-Inflation über Jahre

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Zammad** | moderne Maske, Suchindex, Kanäle, API-Reichtum — Zammad ist der „moderne“ Gegenentwurf |
| **Request Tracker** | mächtiger/regexp-lastiger, Perl, eher große Organisationen |
| **GLPI** | ITSM inkl. Assets; osTicket bleibt beim Support-Ticket |

## Technische Details

- **Backend**: PHP (8-kompatibel), MySQL/MariaDB
- **Frontend**: servergerenderte Templates (eigenes Theme-System), Agenten-/Portal-View
- **Authentifizierung**: lokal, optional LDAP
- **Hosting**: Apache/nginx + PHP, Cron für Fetch/SLA
- **Lizenz**: GPL (Community-Ausgabe)

## Für wen geeignet

- kleine Teams/Vereine mit einem Mail-Postfach als Support-Kanal
- Umgebungen ohne Platz für Elasticsearch & Co.
- FreeSynergy-Skins, die den schlichten Ticketstatus-Workflow (new/open/pending/closed) zeigen
