# Decidim - Funktionen

## Hauptfunktionen

### Prozessgerüst
- Prozesse mit **Phasen** (time-boxed), Komponenten als Bausteine: Proposals, Meetings, Budgets, Surveys, Accountabilities (Ergebnisberichte), Pages, Blog, Sortitions/Abstimmungen (Modul)
- Vorschläge: Kommentare, Supports (Kreuzzeichen), Themenzuordnung,Zusammenführen ähnlicher Vorschläge, Amending

### Verfassungs-/Beteiligungspflege
- Verifizierungssysteme (Login mit Bedingungen), Debatte-Regeln, Meldungs-Moderation, Transparenz-Berichte
- Meetings mit Hybrid-Unterstützung (Live streaming integration, Attendance reports)

### Betrieb
- Multi-Tenancy (Organisationen), Mehrsprachigkeit, Newsletter/E-Mail-Benachrichtigungen, Statistiken-Export

## Was Decidim NICHT kann

- **kein Liquid-Feedback** (delegative Abstimmungen: ❌ — dafür Liquid)
- **keine anonyme Abstimmung** (Verifizierung schlägt Anonymität; Wahlsysteme sind andere Tools)
- keine E-Voting-Zertifizierung (offizielle Wahlen brauchen andere Verfahren)
- Admin-Setup anspruchsvoll (Rails + Module, Wartung nicht trivial)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| GraphQL-API (voll) | offiziell — stark für Dashboards |
| Decidim-Modul-Ökosystem | Community-Module (z.B. Konsultationen, Volunteers) |
| Zensus-/Geo-APIs | Meeting-Karten mit Geodaten |
