# Coppermine latest — Theme „default“

Aus `layout.md` überführt (ADR 0012). Werte sind beschrieben, nicht kopiert (ADR 0013).

## Publikumsbereich (Standard-Theme)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Galerie-Titel  Menü: Startseiten | Alben | Suche | Login             │
├───────────────┬──────────────────────────────────────────────────────┤
│ Seitenblock   │ Kategorie-/Albenübersicht mit Miniaturen             │
│ (Blöcke)      │ ┌────┐┌────┐┌────┐┌────┐                             │
│ letzte Uploads│ └────┘└────┘└────┘└────┘                             │
│ Bestseller    │ Albenkopf: Titel, Beschreibung, Bildzähler, Sort.    │
└───────────────┴──────────────────────────────────────────────────────┘
   Bildseite: Bild mittig | Dateinfo | Bewertung | Kommentare | Navigation
```

- Admin-Oberfläche „cuPCP“ ist ein separates Maskensystem mit Tab-Reitern
- Seitenränder bestehen aus Blöcken, die pro Theme placiert werden
