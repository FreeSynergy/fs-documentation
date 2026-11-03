# Request Tracker - Funktionen

## Hauptfunktionen

### Queues und Tickets
- Queues als Arbeitsbereiche mit eigenen Rechten, Templates, Autorespondern
- Ticketstatus new/open/stalled/resolved/rejected; Ticket-Merging (Parents/Kinder)
- Custom Fields (text, selection, stages…) je Queue, Ablage von Transaktionen

### Automatisierung mit Scrips
- pro Queue/Transaktion konfigurierbare „Condition → Action“-Scrips (Perl-One-Liner möglich)
- AutoReply/AutoCreate aus E-Mails, Escalation via Cron (`rt-crontool`)
- Benachrichtigungslogik vollständig Rechte-/Template-getrieben

### Suche und Berichte
- Query-Sprache (`Queue = "Hardware" AND Status = "open" AND Owner = "nobody"`)
- Saved Searches, Dashboards, Statistik-Reports; RT-Shipped „Charts“ (RT-IR)

### E-Mail-Workflow
- Ingest: alles an `queue-name@server` (und Aliase) wird Ticket/Antwort
- ausgehend je Transaktion, Threadhaltung über Ticket-IDs im Betreff

### REST und CLI
- REST 1.0 + JSON-RPC 2.0, CLI `rt` und `rt-mailgate`

## Was RT NICHT kann

- **kein modernes Web-Frontend** (Mason-Template-Klassik; neue MUI-Oberfläche in RT 5 nur Grundgerüst)
- **SLA/Fristen** nur über Zusatzmodule (`RT-Extension-SLA`)
- **kein Self-Service-Portal** im Zammad-Sinne (nur E-Mail + Weblogin)
- **kein Chat/Telefon-Kanal**
- **kein Asset-Modul** kernseitig (RT-IR für Inventar als Zusatz, nicht auf GLPI-Niveau)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Extensions (`RT::Extension::*`) | SLA, FullTextSearch, CommandByMail, Telegram, Agenda |
| SSO | LDAP, Shibboleth/OIDC (Plugin) |
| Volltextsuche | GSA (RT-Extension-GSA) oder PG-Trigger |
| Import | `rt-importer` (Outlook, RT2, OTRS) |
