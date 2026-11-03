# Mautic - Funktionen

## Hauptfunktionen

- **Kampagnen-Canvas**: Trigger (Formular, Segmentbeitritt, Ereignis→ Entscheidungen / Warten / Aktionen (E-Mail, SMS*, Tag, Punkte, CRM-Webhook)
- **Segmente statisch/dynamisch** (Regel-Builder), Kontakt-Aktivitätenchronik (besuchte Seiten, Mail-Interaktion)
- Landingpages/Formulare/Assets, E-Mail-Baukasten mit Drag-Blöcken, A/B-Kampagnen
- Point-Leading (Verhaltensscore) + Leads-/Kontaktmodelle mit Custom Fields
- Webhooks + REST-API → ideal in FreeSynergy-Landschaft (Kontakt-Sync!)

## Was Mautic NICHT kann

- **Zustellbarkeit selbst gebaut**: SMTP/Relay (Mailjet/Sendgrid) nötig — kein eingebauter Versand-Service
- **Berichtstiefe < kommerzielle Suiten** (Funnel-Visuals rudimentär)
- UI-Verlangsamung bei >100k Kontakten ohne Tuning
- SMS/Telefon-Integrationen = Drittanbieter-Plugins
- Updates großer Installationen brauchen Wartungsfenster

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks | offiziell |
| Plugin-System (Composer) | eigene Integrations-Skins |
| WP/Joomla-Plugins, Zapier | vorhanden |
