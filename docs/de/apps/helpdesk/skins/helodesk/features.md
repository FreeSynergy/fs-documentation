# Helodesk - Funktionen

## Hauptfunktionen

### Kontaktcenter (Telefonie integriert)
- Web-Softphone mit Klick-wählen, Warm/Cold-Transfer, Konferenz, Aufzeichnung (plan-/rechtsabhängig)
- Warteschlangen mit Ansagen, IVR-Designer (Bäume, Skills, Zeiten), Callback-Termine
- Nummernverwaltung (DIDs), SIP-Trunk-Anbindung, Anrufanalyse je Agent/Queue

### Cases (Tickets)
- kanalübergreifende Cases: Anruf → Case mit Protokoll, E-Mail-Antwort, Chat, SMS
- SLA/Uhrzeiten, Eskalationsregeln, Zuweisung nach Skills/Runde
- benutzerdefinierte Felder und Formulare pro Case-Typ

### Kontakte und Knowledge
- Kontaktprofil mit allen Kanalkontakten (Telefon, Mail, Chat)
- Wissensartikel (intern + Kundenportal), Reply-Vorlagen

### Web-Widgets
- Chat-Widget, Callback-Button, Kontaktformulare (Embed-Skript auf eigener Website)

## Was Helodesk NICHT kann

- **kein Self-Hosting** (SaaS, Hosting in Frankreich/EU — Datenschutzvorteil, aber keine eigene Instanz)
- **kein eigenes Datenbanksystem/BI**; Reports auf mitgelieferte Maße begrenzt
- **API-Abdeckung lückenhaft**: Kontakte/Cases ja, Telefonie-Konfiguration nur teil automatisierbar
- **keine Marktplatz-Breite** wie Zendesk/Freshdesk (Integrationen über Connectoren/Zapier)
- **keine öffentliche Preisliste ohne Vertrieb** (Nummer/Tarif-Bündel)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks | Token-basiert (Administration → API) |
| CRM-Connectoren | HubSpot/Salesforce/Pipedrive-Connectoren, Zapier/Make |
| Website | Chat-/Callback-/Formular-Skripte |
| Browser-Erweiterung | Helodesk-Clipline-Connector (Kontext in Mail-/CRM-Oberflächen; Verfügbarkeit prüfen) |
