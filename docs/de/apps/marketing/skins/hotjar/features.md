# Hotjar - Funktionen

## Hauptfunktionen

- **Heatmaps**: Klick/Move/Scroll auf echten Seiten (Delegierung für dynamische Inhalte), device-getrennt
- **Recordings**: DOM-basierte Replays (kein Video — Re-Konstruktion), Filter + „Rage Clicks/Dead Clicks“-Erkennung
- **Surveys/Feedback**: Fragetemplates, Targeting (URL/Verhalten), Antworten exportierbar (CSV)
- **Identify-API**: eigene User-IDs an Sessions binden (interne Testkonten markierbar)
- Masken (CSS-Selektor) für personenbezogene Felder; Consent-Kopplung

## Was Hotjar NICHT kann

- **keine Traffic-Kennzahlen** (dafür GA/Matomo/Plausible daneben stellen)
- **keine offene Heatmap-Rohdaten-API** (Ergebnisse nur UI/CSV-Umfang)
- Replays ohne Eingabefelder-Inhalte (Maskierung Default) — Debugging-Grenze
- Preis nach Pageviews (Skalierungskosten)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| GTM-Tag, Identify-API | offiziell |
| Zapier, GA-Kopplung | offiziell |
| Matomo (parallel) | komplementäres Muster |
