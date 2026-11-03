# Sharetribe - Struktur und UI/UX

## Marktplatz-Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Marktplatz „Nachbarschaft“   [Suchen…]  [+ Inserieren]  Konto    │
├──────────────────┬───────────────────────────────────────────────┤
│ Filter: Kategorie│  (Kartenansicht mit Listing-Pins)             │
│ Preis · Ort    │  oder Liste: Kacheln mit Bild/Preis/Bewertung  │
│ Zeitraum         │  Listing-Detail: Galerie · Preisstaffelung    │
│                  │   [Anfragen] Kalender-Belegung · Bewertungen   │
└──────────────────┴───────────────────────────────────────────────┘
```

- Inquiry/Buchung als mehrstufiger Flow (Datum wählen → Nachricht → Bestätigung)
- Chat + Transaktionsstatus zentral im Konto

## UI/UX

- helles Marktplatz-Template (default-templates), anpassbar (Branding)
- Vertrauenssignale: Verifizierungsbadge, Bewertungszähler, Antwortrate

## Interaktionen

- Karte ⇄ Liste synchron; Preisfilter mit Histogramm
- Anbieter-Dashboard: Listing-Editor, Kalender-Sperrungen, Auszahlungsstatus

## Responsive Design

- responsiv; Mobile-Suche ist Hauptkanal (Karte fokussiert)

## Accessibility

- Standard-Web; Template-Basis WCAG-orientiert

## Performance

- Suchindex (Elasticsearch-artig im SaaS) schnell; Karten-Kacheln clustern
