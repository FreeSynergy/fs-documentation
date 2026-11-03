# GLPI - Funktionen

## Hauptfunktionen

### Tickets (ITIL-Support)
- Ticketkategorien-Baum, Status inkl. „angenommen/verarbeitet/gelöst/geschlossen“
- SLA/OLA mit Geschäftszeiten, Eskalationsmatten, Vertragsbindung
- Verknüpfung von Tickets mit Assets, Problemen und Änderungen (Change-Management)
- Self-Service-Portal, Planning (Vor-Ort-Termine), Follow-up-Aufgaben

### IT-Asset-Verwaltung (ITAM)
- Inventarobjekte inkl. Historie, Statusketten (bestellt → geliefert → genutzt → entsorgt)
- Auto-Inventur über GLPI-Agent (ehem. FusionInventory)
- Software-Lizenzen, Verträge, Verbrauchsmaterial, Netzwerk-/Rack-Verwaltung

### Projekte und Werkzeuge
- Projekte mit Aufgaben/Gantt, Wissensdatenbank, Berichte/Statistiken (SVG-Reports)

### Automatisierung und Integration
- Business Rules (Ticketzuweisung nach Kriterien), Benachrichtigungs-Matritzen
- Cron-gesteuerte Aufgaben; REST-API; Webhooks über Plugin „glpi-webhooks“ (Community)
- SSO: LDAP, CAS, OIDC (Plugin), SMTP/VoIP-Header

## Was GLPI NICHT kann

- **Kein modernes Echtzeit-Frontend** (servergerendert, Reload statt Live)
- **Kein Kanalausbau wie Chat/Telegram** out of the box
- **Keine echte ITIL-Prozess-Engine** (Probleme/Änderungen als Datenmodell ohne Workflow-States beyond Grundstatus)
- **API nicht vollständig parity-fähig**: einige Aktionen (Massenbearbeitung) nur UI-seitig
- **Mobile Nutzung** nur via Responsive-Portal/GLPI-Agent-Apps

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Plugins (Marktplatz) | GLPI Agent, Fields, Webhooks, More reporting, Statistics |
| REST | `/apirest.php` |
| Monitoring | Anbindung via Plugins/Zabbix (Plugin „zabbix“) |
| LDAP/CAS/OIDC | native/Plugin |
