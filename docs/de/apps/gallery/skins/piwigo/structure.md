# Piwigo - Struktur und UI/UX

## Publikumsbereich

```
┌──────────────────────────────────────────────────────────────────────┐
│ Logo  Menü: Startseiten | Alben | Tags | Kalender | Suche | Login     │
├────────────────────────────┬─────────────────────────────────────────┤
│ Kategorie-Baum (Theme-abh.)│  Thumbnail-Raster, Seitennummerierung   │
│  ▸ Reisen                  │  ┌────┐┌────┐┌────┐┌────┐               │
│  ▸ Technik                 │  └────┘└────┘└────┘└────┘               │
│    ▸ Serverraum            │  Kopf: Albenname, Beschreibung, Zähler  │
└────────────────────────────┴─────────────────────────────────────────┘
        Bildseite: großes Bild | Metadata-Block | Kommentare | Aktionen
```

- Bildseite: Navigation zurück zur Kategorie, „Nächstes/Vorheriges“, Slideshow
- Admin-Bereich ist eine eigene Maske mit links gruppierten Modulen

## UI/UX

- Theme-abhängig, Standard-Theme „Bootstrap“ responsive
- Aktionen als Textlinks/Symbole unter dem Bild, Batch-Maske mit Checkboxen

## Interaktionen

- **Batch-Verwaltung**: Raster mit Auswahlkästchen → Aktionsleiste unten
- **Drag & Drop** in „AddPictures“ (Upload-Plugin) und beim Kategorien-Sortieren
- **Kommentarformulare** mit Vorschau, Moderationsstatus
- **Animationen**: Slideshow-Übergänge je Theme, sonst dezent

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Menü oben, Raster 4–6 Spalten |
| Tablet | Menü als Toggle, 3–4 Spalten |
| Mobil | einspaltiges Menü, 2 Spalten Raster, Bildseite gestapelt |

## Accessibility

- Skip-Link und semantische Überschriften im Standard-Theme
- Alternativtexte aus Bildtitel/Beschreibung, Tastaturnavigation in Slideshow
- Kontraste je Theme konfigurierbar (CSS-Variablen)

## Performance

- Generierte Vorschaugrößen, optionaler Cache und Plugin-Caching
- Große Galerien profitieren von `wait_for_images`-Cron und Datenbank-Indizes
