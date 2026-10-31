# CiviCRM - Funktionen

## Hauptfunktionen

### Kontakte und Beziehungen
- Individuals, Organizations, Houses; Beziehungen (Mitglied von, Arbeitgeber von…)
- Groups (statisch/dynamisch durch Saved Searches), Tags, Custom Fields (eigene Entitäten)
- Deduplizierung (Unsupervised/Supervised Rules), Merge-Verlauf

### Spenden (CiviContribute)
- Beiträge, wiederkehrende Spenden, PCP-Spendenseiten, Zahlungsabwicklung über Prozessoren (Stripe, PayPal, GoCardless …)
- Buchungsnahe Belege: Finanz-Konten (Financial Types, Accounts), CSV-Export

### Veranstaltungen (CiviEvent)
- Event-Typen, Preise (Fee Levels), Kapazitäten, Warteliste, Online-Registrierung, Check-in (QR)

### Mitgliedschaften (CiviMember)
- Membership-Typen mit Laufzeiten/Roll-over, Statusregeln, automatische Verlängerung

### Kommunikation
- CiviMail (Bulk mit Tracking), Templates, Activities (Verlauf), Umfragen/Petitions (Campaigns)

### Fälle und Anträge
- Cases (Fall-Workflow mit Aktivitäten), Grants (Antragsverwaltung)

## Was CiviCRM NICHT kann

- **Kein Vertriebs-CRM** (keine Pipeline/Deals — EspoCRM/SuiteCRM Domäne; Erweiterungen rudimentär)
- **kein eigenes Login/ Rechteverwaltung** — hängt am CMS
- **Bulk-Mail ohne eigenes MTA-Setup** (SMTP/CiviMail-Massiverarbeitung konfigurieren nötig)
- **Reporting altbacken**: Standard-Reports schwach, Serious Dev/Semantic für bessere Auswertung (Extensions)
- **keine Mobile-App** (nur responsive Formularseiten, kein Agenten-App)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Extensions-Verzeichnis | CiviConnect/Download, `extmanage` |
| Payment | Payment Processor Framework |
| Zapier/make | offizieller Zapier-Connector + API v4 |
| Suche/Elastic | SearchKit/API4 + Extension (z.B. Search Kicker) |
| Backendsync | Drupal/Joomla/WordPress-User-Sync |
