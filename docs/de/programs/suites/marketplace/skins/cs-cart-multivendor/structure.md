# CS-Cart Multi-Vendor - Struktur und UI/UX

## Layout

```
Frontend: Header (Suche/Kategorien) · Produktliste (Kacheln,
          „Verkauft von“-Label) · Warenkorb (Vendor-Split-Zeilen)
Vendor-Dashboard: Seitenmenü links (Produkte/Bestellungen/Finanzen),
          Produktformular mit Varianten-Matrix
Admin-Center: analog, plus Verkäufer-/Fee-Verwaltung,
          Bestellliste mit Vendor-Farbcodierung
```

## UI/UX

- klassische Shop-Konsistenz; Backend in Tab-/Formular-Form (v4-Look)
- Vendor-Kennzeichnung + getrennte Sendungen im Checkout sichtbar

## Interaktionen

- Produkt-Import (CSV), Massenänderungen (Select + Aktionen)
- Bestellstatus-Workflows (New→In process→Shipped… je Händler)

## Responsive Design

- Theme-System responsiv; Backend desktopzentriert

## Accessibility

- Theme-abhängig (Betreiber-Aufgabe); Backend Standard-Formulare

## Performance

- große Kataloge: Caching/DB-Optimierung; Add-on-Wahl beeinflusst Tempo stark
