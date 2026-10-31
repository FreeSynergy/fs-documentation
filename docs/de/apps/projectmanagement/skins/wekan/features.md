# Wekan - Funktionen

## Hauptfunktionen

### Kanban-Kern
- Boards mit **Swimlanen** (Wannen-Ebenen, z.B. pro Team/Monat), Listen, Karten, Labels, Checklisten, Fälligkeiten
- Karten-Custom-Fields, Vorlagen-Boards, Import aus Trello/CSV, JSON-Export

### Zusammenarbeit
- Organisationen und Teams, Beobachter-/Mitglied-/Admin-Rollen
- Aktivitäten-Feed, Kommentare, Anhänge (lokal/S3), Echtzeit-Sync (Meteor DDP)

### Integrationen
- **Invoke-Webhooks** (eingehend: POST → Karte anlegen/kommentieren) — ideal für Alerts
- **ausgehende Webhooks** pro Board (Karte verschoben, Kommentar…) → HTTP
- E-Mail-Benachrichtigungen (SMTP), ICal-Feed für Fälligkeiten

## Was Wekan NICHT kann

- **keine SaaS-Qualität** wie Trello (Mobil-Apps experimentell, Push rudimentär)
- **keine Automatisierungs-Engine** (Butler-Regeln: ❌ — nur Webhooks)
- **keine Berichte/Throughput-Charts** (nur Aktivitäten)
- **keine stabile offizielle API-Versionierung** (API stabil genutzt, aber dünn dokumentiert)
- Custom Fields ohne Berechtigungslogik

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API (persönlicher Token) | dokumentiert + Community |
| Invoke-/Outgoing-Webhooks | Board-Panel |
| LDAP/OAuth2/SAML | Admin-Panel |
| Storage | lokales Dateisystem/S3 |
