# Monica - Funktionen

## Hauptfunktionen

### Personen mit Geschichte
- Kontakte mit Stammdaten, benutzerdefinierten Feldern, Fotos, „wichtigen Infos“
- Beziehungen (Partner, Kind, Freund … mit gerichteten Typen), Gruppen/Labels
- Lebensereignisse (life events) und Meilensteine

### Aktivitäten und Journale
- Aktivitäten mit Typ, Datum, Beteiligten, Notiz; Timeline-Feed
- Journal-Bücher mit Einträgen, Stimmung, Ort
- Erinnerungen (reminders) z.B. „letzte Aktivität in 6 Monaten“

### Aufgaben, Geschenke, Schulden
- Aufgaben mit Fälligkeit je Kontakt oder global
- Geschenke (geplant/gekauft/erhalten) mit Ideenliste
- Schulden-Tracking zwischen Personen

### Datenhaltung
- vCard/CSV/Google-Import, JSON-/vCard-Export
- Öffentliche VCard-Seiten pro Kontakt (Link)
- Selbst gehostet oder Monica-CLOUD-Abonnement

## Was Monica NICHT kann

- **Kein Business-CRM** (keine Pipelines/Deals — SuiteCRM/pipedrive)
- **Kein Kalender-Sync** nach außen: eigene Erinnerungen, aber keine CalDAV-Schnittstelle (❌)
- **Keine E-Mail-Integration** (Posteingang/Mail-Sync)
- **Keine Mandantenfähigkeit über Kreise hinaus** (Kreise trennen, aber keine Rollen-Hierarchie)
- **Keine Mobile-App** (nur responsive Web-UI + Community-Apps)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Token | Einstellungen → API |
| Webhooks | pro Ereignis konfigurierbar (contact created, activity added …) |
| Importe | vCard, CSV, Google-Kontakte |
| Docker-/k8s-Deploy | offizielle Images |
| Community-Module | experimentelle Module (lebensereignisse, debt) |
