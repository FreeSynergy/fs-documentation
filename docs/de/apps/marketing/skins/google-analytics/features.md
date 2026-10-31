# Google Analytics - Funktionen

## Hauptfunktionen

- **Ereignis-Modell** (GA4): page_view, custom events mit Parametern; Web+App in einer Property
- **Auto-Messung** (Engagement, Conversions als Key Events), Trichter/Explorer-Reports
- **Zielgruppen** + Attribution (datengetriebene Modelle), Google-Ads-Sync
- **BigQuery-Export** (kostenlos bei Standard seit 2023/24-Status prüfen!) für Rohdaten-Analyse
- **Consent Mode v2**: datenschutzgesteuerte Messung (Einwilligungs-Signalübertragung)

## Was Google Analytics NICHT kann

- **DSGVO ist das Dauerthema**: Übermittlungs-Grundlagen dokumentieren (EU-US-DPF); manche DSKs negativ — Matomo/Plausible sind die „sicheren“ Wege
- keine Rohdaten-Hoheit (Export-Binärsprache BigQuery ja, aber Google-Cloud)
- **keine Self-Hosting-Option**
- Session-basierte Vergleichbarkeit begrenzt (sampling in großen Reports)
- keine E-Mail-Kontaktauflösung (Ads-Personalisierung ist anderes Produkt)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Data API v4 / Management API | offiziell |
| Tag Manager, Search Console, Ads | Google-Familie |
| Looker Studio | kostenlose Dashboards |
